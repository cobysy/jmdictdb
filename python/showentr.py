# Simple command line tool to find and display entries
# in the JMdict database.

_VERSION_ = ("$Revision$"[11:-2], "$Date$"[7:-11])

import sys, os, re, locale
import jbdb, MySQLdb
from tables import *

class ParseError (RuntimeError): pass

global KW, Def_enc

def main (args, opts):
	global KW, Def_enc

	Def_enc = locale.getdefaultlocale()[1]
	# open the database...
	try: cursor = jbdb.dbOpen (user=opts.u, pw=opts.p, db=opts.d)
	except MySQLdb.OperationalError, e:
	    if e[0] == 1045: 
		print "Error, unable to connect to database, do you need -u or -p?\n", e[1];  
		sys.exit(1)
	    else: raise

	# Read in all the keyword tables...
	KW = jbdb.Kwds (cursor)
	mk_tmpsrch (cursor)

	print """
Type "help" for more info.
To exit type a return, or EOF (usually ^d on Unix, ^z on Windows)."""

	while True:
	    try: s = raw_input( "find> ").decode(Def_enc).strip()
	    except EOFError: break
	    if not s: break
	    if s[0] == "h" or s[0] == "H":
		help (); continue
	    try: rowcnt = search (cursor, s)
	    except ParseError, e: 
		print "Parse error, type \"h\" for help"; continue
	    if rowcnt == 0: print "Nothing found"
	    elif rowcnt == 1: 
		rs = get_found_list (cursor)
		entr = get_entry (cursor, rs[0][0])
		entr = display_entry (entr)
	    else:
		rs = get_found_list (cursor)
		choose_entry (cursor, rs)
	    
def search (cursor, s):
	Tbls = {'e':"entr",'k':"kanj",'r':"kana",'s':"sens",'g':"gloss",'q':"entr",None:"entr"}
	parsed = srch_parse (s)
	results = []
	for typ,tbl,val in parsed:
	    table = Tbls[tbl];  col = "txt"
	    if isinstance (val, (int,long)): col = "id"
	    if col=="txt" and table in ("entr","sens"):
		raise ParseError ("Parse error")
	    if typ is None: w = "%s.%s=%%s" % (table,col)
	    else: w = "%s.%s LIKE(%%s)" % (table,col)
	    if typ == '^': val = val + "%"
	    elif typ == '*': val = "%" + val + "%"
	    elif typ == '$': val = "%" + val
	    results.append ((table,w,(val,)))
	cursor.execute ("DELETE FROM _tmpsrch")
	sql, args = build_search_sql (results)
	cursor.execute ("INSERT INTO _tmpsrch(id) " + sql, args)
	return cursor.rowcount

def choose_entry (cursor, rs):
	display_list (rs)
	while True:
	    try: s = raw_input( "show> ").decode(Def_enc).strip()
	    except EOFError: break
	    if not s: break
	    elif s[0] == "h" or s[0] == "H": help ()
	    elif s[0] == "l" or s[0] == "L": display_list (rs)
	    else:
		try: numb = int (s)
		except ValueError: 
		    print "Not a number or command, type \"h\" for help"; continue
		if numb < 1 or numb > len(rs):
		    print "Number out of range 1-%d, type \"h\" for help" % len(rs); continue
		else: 
		    entr = get_entry (cursor, rs[numb-1][0])
		    display_entry (entr)

def display_list (rs):
	for n,(e,q,k,j,g) in enumerate (rs):
	    print "%3d.%6d%8d|%s|%s|%s" % (n+1,e,q,clip(k,10,u"\u3000"),
			clip(j,10,u"\u3000"),clip(g,18," "))

def clip (s, n, pad):
	if isinstance(pad, unicode): s = s.replace("; ", u"\uff1b")
	x = min (len (s), n)
	s = (pad * (n - x)) + s[:x]
	return s

def get_found_list (cursor):
	sql = \
	    u"SELECT e.id,e.seq, " \
		u"(SELECT GROUP_CONCAT(k.txt ORDER BY ord SEPARATOR '; ') " \
		    u"FROM kana k WHERE k.entr=e.id) AS kana, " \
		u"(SELECT GROUP_CONCAT(j.txt ORDER BY ord SEPARATOR '; ') " \
		    u"FROM kanj j WHERE j.entr=e.id) AS kanj, " \
		u"(SELECT group_concat(g.txt ORDER BY s.ord,g.ord SEPARATOR '; ') " \
		    u"FROM sens s JOIN gloss g ON g.sens=s.id " \
		    u"WHERE s.entr=e.id) AS gloss " \
		u"FROM entr e JOIN _tmpsrch t ON e.id=t.id"
	cursor.execute (sql)
	rs = cursor.fetchall ()
	return rs

def display_entry (entr):

	  # Print basic entry information 

	print "\nseq: %s, lang=(%s), dial=(%s), id=%d\n" % (entr.seq, 
	    ",".join([KW.LANG[x.kw].descr for x in entr.lang]), 
	    ",".join([KW.DIAL[x.kw].descr for x in entr.dial]), entr.id)
	
	  # Print the entry's kanji text.
 
	klist = []
	for k in entr.kanj:
	    kwds = ";".join([KW.KINF[x.kw].kw for x in k.inf] \
		   + [KW.FREQ[x.kw].kw+str(x.value) for x in k.freq])
	    if kwds: klist.append (k.txt + "/" + kwds)
	    else: klist.append (k.txt)
	if klist: print "; ".join (klist)
	
	  # And the readings.  The "max(...) > 0" expression is 
	  # true if a restriction exists on any of the readings 
	  # in which case we call display_restr() instead of just 
	  # printing the readings.  We don't display r_inf or 
	  # r_rfreq for for simplicity -- method is same as for
	  # kanji.

	if max([len(r.restr) for r in entr.read]) > 0:
	    display_restr (entr.read, entr.kanj)
	else:
	    print ", ".join([x.txt for x in entr.read])

	  # Print the sense information.

	for n,s in enumerate (entr.sens):

	      # Part-of-speech, misc keywords, field...
	    pos = ";".join([KW.POS[p.kw].kw for p in s.pos])
	    if pos: pos = "[" + pos + "]"
	    misc = ";".join([KW.MISC[p.kw].kw for p in s.misc])
	    if misc: misc = "[" + misc + "]"
	    fld = ", ".join([KW.FLD[p.kw].descr for p in s.fld])

	      # Restrictions... 
	    if not s.stagr: sr = []
	    else: sr = filt ([x.kana for x in s.stagr], entr.read)
	    if not s.stagk: sk = []
	    else: sk = filt ([x.kanj for x in s.stagk], entr.kanj)
	    stag = ""
	    if sr or sk: 
		stag = " (%s only)" % ", ".join([x.txt for x in sk+sr])

	    print "\n  %d. %s%s%s(%d)" % (n+1, pos, misc, stag, s.id)
	    if fld: print "     Field(s): " + fld

	      # Now print the glosses...
	    for g in s.gloss:
		lang = KW.LANG[g.lang].kw
		if lang: lang += ": "
	        print "     %s%s" % (lang, g.txt)

	      # Print the number of xrefs than this sense references,
	      # and the numbers of other senses that reference this
	      # one.

	    if len(s.xref) > 0: print "     [%d xrefs from this sense.]" % len(s.xref)
	    if len(s.xrex) > 0: print "     [%d xrefs to this sense.]" % len(s.xrex)

def display_restr (rlist, klist):
	s = []
	for r in rlist:
	    valid = filt ([x.kanj for x in r.restr], klist)
	    if not valid: s.append (r.txt)
	    else: s.append (r.txt + u" (" + ", ".join([j.txt for j in valid]) + u")")
	print "; ".join(s)

def get_entry (cursor, entrid):
	sql = "SELECT * FROM entr WHERE id=%s"
	e = load (Entr, cursor, sql, (entrid,))
	if len(e) < 1: return None
	e = e[0]; id = e.id
	e.lang = load (Lang, cursor, "select * from lang where entr=%s", (id,))
	e.dial = load (Dial, cursor, "select * from dial where entr=%s", (id,))
	e.read = load (Read, cursor, "select * from kana where entr=%s order by ord", (id,))
	e.kanj = load (Kanj, cursor, "select * from kanj where entr=%s order by ord", (id,))
	e.sens = load (Sens, cursor, "select * from sens where entr=%s order by ord", (id,))
	for s in e.sens:
	    s.gloss = load (Gloss, cursor, "select * from gloss where sens=%s order by ord", (s.id,))
	    s.pos = load (Pos, cursor, "select * from pos where sens=%s", (s.id,))
	    s.misc = load (Misc, cursor, "select * from misc where sens=%s", (s.id,))
	    s.fld = load (Fld, cursor, "select * from fld where sens=%s", (s.id,))
	    s.xref = load (Xref, cursor, "select * from xref where sens=%s", (s.id,))
	    s.xrex = load (Xref, cursor, "select * from xref where xref=%s", (s.id,))
	    s.stagr = load (Stagr, cursor, "select * from stagr where sens=%s", (s.id,))
	    s.stagk = load (Stagk, cursor, "select * from stagk where sens=%s", (s.id,))

	for j in e.kanj:
	    j.inf = load (Kinf, cursor, "select * from kinf where kanj=%s", (j.id,))
	    j.freq = load (Kfreq, cursor, "select * from kfreq where kanj=%s", (j.id,))
	for k in e.read:
	    k.inf = load (Kinf, cursor, "select * from rinf where kana=%s", (k.id,))
	    k.freq = load (Kfreq, cursor, "select * from rfreq where kana=%s", (k.id,))
	    k.restr = load (Restr, cursor, "select * from restr where kana=%s", (k.id,))
	return e

def build_search_sql (condlist):
	"""\
	Build a sql statement that will find the id numbers of
	all entries matching the conditions given in <condlist>.
	Note: This function does not provide for generating arbitrary 
	sql statements; it is only intented to support some limited 
	search capabilities.

	<condlist> is a list of 3-tuples.  Each 3-tuple specifies
	one condition:
	  0: Name of table, one of: "entr", "kana", "kanj", "sens", 
	    "gloss", "pos", "use".
	  1: Sql snippit that will be AND'd into the WHERE clause.
	    Field names must be qualified by table.  When looking 
	    for a value in a field.  A "?" may (and should) be used 
	    where possible to denote an exectime parameter.  The value
	    to be used when the sql is executed is is provided in
	    the 3rd member of the tuple (see #2 next).
	  2: A sequence of argument values for any exec-time parameters
	    ("?") used in the second value of the tuple (see #1 above).

	Example:
	    [("entr","entr.typ=1", ()),
	     ("gloss", "gloss.text LIKE ?", ("'%'+but+'%'",)),
	     ("pos","pos.kw IN (?,?,?)",(8,18,47))]

	  This will generate the SQL statement and arguments:
	    "SELECT entr.id FROM (((entr INNER JOIN sens ON sens.entr=entr.id) 
		INNER JOIN gloss ON gloss.sens=sens.id) 
		INNER JOIN pos ON pos.sens=sens.id) 
		WHERE entr.typ=1 AND (gloss.text=?) AND (pos IN (?,?,?))"
	    ('but',8,18,47)
	  which will find all entries that have a gloss containing the
	  substring "but" and a sense with a pos (part-of-speech) tagged
	  as a conjunction (pos.kw=8), a particle (18), or an irregular
	  verb (47)."""

	tables = []; wclauses = []; args =[]
	for tbl,cond,arg in condlist:
	    tables.append (tbl)
	    wclauses.append (cond)
	    args.extend (arg)
	t = "(%s INNER JOIN % s ON %s)"
	s = "entr "
	if "kana" in tables:  s = t % ( s, "kana",  "kana.entr=entr.id" )
	if "kanj" in tables:  s = t % ( s, "kanj",  "kanj.entr=entr.id" )
	if "sens" in tables \
		or "gloss" in tables \
		or "pos" in tables \
		or "misc" in tables:
			      s = t % ( s, "sens",  "sens.entr=entr.id" ) 
	if "gloss" in tables: s = t % ( s, "gloss", "gloss.sens=sens.id" ) 
	if "pos" in tables:   s = t % ( s, "pos",   "pos.sens=sens.id" ) 
	if "misc" in tables:  s = t % ( s, "misc",  "misc.sens=sens.id" ) 
	where = " AND ".join (wclauses)
	return "SELECT DISTINCT entr.id FROM %s WHERE %s" % (s, where), tuple(args)

def srch_parse (txt):
		  #   123          4         56       7      89           0  1
	regex = ur"\s*((([ekrsgq])?([0-9]+))|(([*^$])?([krg])(([^'\s]\S*)|(\'([^']*?)\'))))"
                  #   123        3 3      32 23     3 3     334         4 4  5      5  4321
	reob = re.compile (regex, re.I|re.U)
	start = 0;  results = []
	while start < len(txt):
	    m = reob.match (txt.strip(), start)
	    if not m: raise ParseError ("Parse error")
	    start = m.span()[1]
	    if m.group(4): results.append ((None,m.group(3),int(m.group(4))))
	    else: 
		if m.group(8): results.append ((m.group(6),m.group(7),m.group(8)))
		else: results.append ((m.group(6),m.group(7),m.group(11)))
	return results

def load (cls, cursor, sql, sqlargs):
	cursor.execute (sql, sqlargs)
	rs = cursor.fetchall ()
	return [cls (x) for x in rs]

def filt (exclude, xlist):
	# returns a list containing those items of <xlist>
	# that do not have an id number that is in the list
	# of numbers in <exclude>.
	return [x for x in xlist if x.id not in exclude]

def mk_tmpsrch (cursor):
	cursor.execute ("DROP TABLE IF EXISTS _tmpsrch;")
	cursor.execute (
	    "CREATE TABLE _tmpsrch (" \
		"id INT UNSIGNED NOT NULL PRIMARY KEY, " \
		"ord INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE);")


# Following stuff is boilerplate code...
#---------------------------------------------------------------------

from optparse import OptionParser

def parse_cmdline ():
	u = \
"""\n\t%prog [-d database][-u user][-p passwd] 

  %prog is a simple-minded program to illustrate extracting
  and displaying data from the jb database.  Options can be
  used to give information necessary for connecting to the
  database.  The program runs in a loop, prompting for an
  entry id or sequence number number, and displaying that
  entry.

  To exit, type a returnm or enter ^Z on MS Windows or ^D
  on Unix. 

arguments:  None"""

	v = sys.argv[0][max (0,sys.argv[0].rfind('\\')+1):] \
	        + " Rev %s (%s)" % _VERSION_
	p = OptionParser (usage=u, version=v)
	p.add_option ("-d", "--database",
             type="str", dest="d", default="jb",
             help="Name of the database to load.  Default is \"jb\".")
	p.add_option ("-u", "--user",
             type="str", dest="u", default="root", 
             help="Connect to Mysql with this username.  " \
                      "Deafult is \"root\"")
	p.add_option ("-p", "--passwd",
             type="str", dest="p", default="",
             help="Connect to Mysql with this password.")
	p.add_option ("-D", "--debug",
             action="store_true", dest="D", 
             help="Startup in Python pdb debugger.")
	opts, args = p.parse_args ()
	if len(args) > 0: p.error("Error, no arguments expected.  " 
				"Use --help for more info")
	return args, opts

def exceptionHandler (type, value, tb):
	if not (sys.stderr.isatty() and sys.stdin.isatty()) or type==SyntaxError: 
	    sys.__excepthook__(type, value, tb)
	else: # Not in interactive mode, print the exception...
	    import traceback, pdb
	    traceback.print_exception(type, value, tb)
	    print;  pdb.pm()

if __name__ == '__main__': 
	args, opts = parse_cmdline ()
	if (opts.D):
	    import pdb, traceback
	    sys.excepthook = exceptionHandler
	    pdb.set_trace ()
	main (args, opts)


