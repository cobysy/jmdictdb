import sys, ply.yacc, re, unicodedata, pdb
from collections import defaultdict
import jdb, jellex, jelparse
from objects import *
import fmt, fmtjel

def main (args, opts):
	global KW, tokens

	cur = jdb.dbOpen ('jmdict')
	# Get local ref to the keyword tables...
	KW = jdb.KW

        lexer, tokens = jellex.create_lexer (debug=opts.debug>>8)
        parser = jelparse.create_parser (lexer, tokens, tabmodule='jelparse_tab')
	parser.debug = opts.debug

	if opts.seq:
	    seq = opts.seq
	      #FIXME: Corpid (used for xref resolution) is hardwired
	      # to 1 (jmdict) below.
	    srctxt, parsedtxt = _roundtrip (cur, lexer, parser, seq, 1)
	    if not srctxt:
		print "Entry %s not found" % seq
	    else:
		print srctxt
		print "----"
		print parsedtxt
	else:
	    _interactive (cur, lexer, parser)

def _roundtrip (cur, lexer, parser, seq, src):
    # Helper function useful for testing.  It will read an entry
    # identified by 'seq' and 'src' from the database opened on the
    # dpapi cursor object 'cur', convert that entry to a JEL text
    # string, parse the text to get a new entry object, and convert
    # that entry object top JEL text.  The text generated from the
    # the original object, and from the parser-generated object,
    # are returned and can be compared.  The should be identical.

	#pdb.set_trace()
	sql = "SELECT id FROM entr WHERE seq=%s AND src=%s"
	obj = jdb.entrList (cur, sql, [seq, src])
	if not obj: return None,None
	for s in obj[0]._sens:
	    jdb.augment_xrefs (cur, getattr (s, '_xref', []))
	jeltxt = _get_jel_text (obj[0])
	jellex.lexreset (lexer, jeltxt)
	result = parser.parse (jeltxt,lexer=lexer,tracking=True)
	resolv_xrefs (cur, result)
	jeltxt2 = _get_jel_text (result)
	return jeltxt, jeltxt2

def _get_jel_text (entr):

	'''Generate and return a JEL string from entry object
	'entr'.  The first line (text before the first "\n"
	character) is removed since it contains nformation
	that will vary between objects read from a database
	and created by parsing input text.'''

	jeltxt = fmtjel.entr (entr)
	return jeltxt.partition('\n')[2]

def _interactive (cur, lexer, parser):
	cnt = 0;  instr = ''
        while 1:
	    instr = _getinptext ()
	    if not instr: break
	    jellex.lexreset (lexer, instr)
	    try: 
		result = parser.parse(instr,lexer=lexer,debug=opts.debug)
	    except jelparse.ParseError, e: 
		if not e.loc: msg = e.args[0]
		else: msg = "%s\n%s" % (e.args[0], e.loc)
		print msg
		continue
	    try:
		jelparse.resolv_xrefs (cur, result)
	    except ValueError:
		print e
            s = fmtjel.entr (result)
            print s

def _getinptext ():
	instr = '';  cnt = 0;  prompt = 'test> '
	while cnt < 2:
            try: s = raw_input(prompt).decode('sjis')
            except EOFError: break
	    prompt = ''
            if s: cnt = 0
	    else: cnt += 1
	    if cnt < 1: instr += s + '\n'
	return instr.rstrip()


def _parse_cmdline ():
	from optparse import OptionParser 
	u = \
"""\n\tpython %prog [-d n][-q SEQ]
	
  This is a simple test/exerciser for the JEL parser.  It operates
  in two different modes depending on the presence or absense of 
  the --seq (-q) option.  

  When present it will read the entry with the given seq number
  from the jmdict corpus in the database, format it as a JEL text 
  string, and parse it.  It prints both the input text and the
  object generated from the parse in the same format, and both
  should be functionally identical.  (There may be non-significant
  differences such as tag order.)

  If the --seq (-q) option is not given, this program will read 
  text input interactively until a blank line is entered, feed the 
  text to the parser, and print the resulting object.  Note that
  because a database is not available in this mode, xrefs will not
  be resolved and thus not appear in the recreated output, even
  if present in the input.
Arguments: (None)
"""
	p = OptionParser (usage=u)
	p.add_option ("-q", "--seq", 
            type="int", dest="seq", default=None,
            help="Parse text generated by reading jmdict seq SEQ from" 
		" database rather than the default behavior of prompting" 
		" interactively for input text.")
	p.add_option ("-d", "--debug",
            type="int", dest="debug", default=0,
            help="Debug value to pass to parser:"
		" 2: Productions,"
		" 4: Shifts,"
		" 8: Reductions,"
		" 16: Actions,"
		" 32: States,"
		" 256: Lexer tokens")
	opts, args = p.parse_args ()
	#...arg defaults can be setup here...
	return args, opts

if __name__ == '__main__': 
	args, opts = _parse_cmdline ()
	main (args, opts)