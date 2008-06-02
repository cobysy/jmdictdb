#######################################################################
#  This file is part of JMdictDB. 
#  Copyright (c) 2006,2008 Stuart McGraw 
# 
#  JMdictDB is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published 
#  by the Free Software Foundation; either version 2 of the License, 
#  or (at your option) any later version.
# 
#  JMdictDB is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with JMdictDB; if not, write to the Free Software Foundation,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
#######################################################################

__version__ = ('$Revision$'[11:-2],
	       '$Date$'[7:-11]);

"""
Functions for generating XML descriptions of entries.

"""
from xml.sax.saxutils import escape as esc, quoteattr as esca
import jdb

global XKW, KW


def entr (entr, compat=None, genhists=False, genxrefs=True, wantlist=False):
	'''
	Generate an XML description of entry 'entr'.
	Parameters:
	  entr -- An entry object (such as return by entrList()).
	  compat -- If false, generate XML that completely 
		describes the entry using an enhanced version
		of the jmdict DTD.
		If "jmdict", generate XML that uses the standard
		JMdict DTD but looses information that is not
		representable with that DTD.
		If "jmnedict", generate XML that uses the standard
		JMnedict DTD but looses information that is not
		representable with that DTD.
	  genhists -- If true (and enhanced is also true), generate
		<hist> elements in the XML.  If false, don't. 
	  genxrefs -- If true generate <xref> elements.  If false
		don't.  In order to generate xrefs the 'entr' 
		object must have augmented xrefs.  If it doesn't
		a exception will be thrown.
	'''
	  #FIXME: Need to generate an kwid->xml-entity mapping
	  # idependent of the KW table.  See comments in jmxml.py
	  # but note the mapping used here needs to also support
	  # the enhanced DTD.
	global XKW, KW; XKW = KW = jdb.KW

	fmt= entrhdr (entr, compat)

	kanjs = getattr (entr, '_kanj', [])
	for k in kanjs: fmt.extend (kanj (k))

	rdngs = getattr (entr, '_rdng', [])
	for r in rdngs: fmt.extend (rdng (r, kanjs, compat))

	fmt.extend (info (entr, compat))

	senss = getattr (entr, '_sens', [])
	if compat == 'jmnedict':
	    for x in senss: fmt.extend (trans (x))
	else:
	    for x in senss: fmt.extend (sens (x, kanjs, rdngs, compat, entr.src, genxrefs))

	if not compat: fmt.extend (audio (entr))

	fmt.append ('</entry>')
	if wantlist: return fmt
	return '\n'.join (fmt)

def kanj (k):
	fmt = []
	fmt.append ('<k_ele>')
	fmt.append ('<keb>%s</keb>' % k.txt)
	fmt.extend (kwds (k, '_inf', 'KINF', 'ke_inf'))
	fmt.extend (freqs (k, '_freq', 'ke_pri'))
	fmt.append ('</k_ele>')
	return fmt

def rdng (r, k, compat):
	fmt = []
	fmt.append ('<r_ele>')
	fmt.append ('<reb>%s</reb>' % r.txt)
	fmt.extend (restrs (r, k))
	fmt.extend (kwds (r, '_inf', 'RINF', 're_inf'))
	fmt.extend (freqs (r, '_freq', 're_pri'))
	if not compat: fmt.extend (audio (r))
	fmt.append ('</r_ele>')
	return fmt

def restrs (r, kanj):
	fmt = []
	restr = getattr (r, '_restr', None)
	if restr: 
	    if len(restr) == len(kanj):
		fmt.append ('<re_nokanji/>')
	    else:
	        re = jdb.filt (kanj, ['kanj'], restr, ['kanj'])
	        fmt.extend (['<re_restr>' + x.txt + '</re_restr>' for x in re])
	return fmt

def sens (s, kanj, rdng, compat, src, genxrefs=True):
	"""
	Format a sense.
	fmt -- A list to which formatted text lines will be appended.
	s -- The sense object to format.
	kanj -- The kanji object of the entry that 's' belongs to.
	rdng -- The reading object of the entry that 's' belongs to.
	compat -- See function entr().  We assume in sens() that if
	    compat is not None it is =='jmdict', that is, if it is 
	    'jmnedict', trans() would have been called rather than
	    sens().
	src -- If 'compat' is None, this should be the value of the
	    entry's .src attribute.  It is passed to the xref() func
	    which needs it when formatting enhanced xml xrefs.  If 
	    'compat' is not None, this parameter is ignored.
	genxrefs -- If false, do not attempt to format xrefs.  This
	    will prevent an exception if the entry has only ordinary
	    xrefs rather than augmented xrefs.
	"""
	fmt = []
	fmt.append ('<sense>')

	stagk = getattr (s, '_stagk', None)
	if stagk: 
	    sk = jdb.filt (kanj, ['kanj'], stagk, ['kanj'])
	    fmt.extend (['<stagk>' + x.txt + '</stagk>' for x in sk])

	stagr = getattr (s, '_stagr', None)
	if stagr: 
	    sr = jdb.filt (rdng, ['rdng'], stagr, ['rdng'])
	    fmt.extend (['<stagr>' + x.txt + '</stagr>' for x in sr])

	fmt.extend (kwds (s, '_pos', 'POS', 'pos'))

	xrfs = getattr (s, '_xref', None)
	if xrfs and genxrefs:
	    fmt.extend ([xref(x, (not compat) and src) for x in xrfs])

	fmt.extend (kwds (s, '_fld', 'FLD', 'field'))

	fmt.extend (kwds (s, '_misc', 'MISC', 'misc'))

	notes = getattr (s, 'notes', None)
	if notes: fmt.append ('<s_inf>%s</s_inf>' % esc (notes))

	lsource = getattr (s, '_lsrc')
	if lsource: 
	    for x in lsource: fmt.extend (lsrc (x))

	fmt.extend (kwds (s, '_dial', 'DIAL', 'dial'))

	for x in s._gloss: fmt.extend (gloss (x, compat))

	fmt.append ('</sense>')
	return fmt

def trans (s):
	"""Format a jmnedict trans element.
	s -- A sense object."""

	fmt = []
	nlist = getattr (s, '_pos', [])
	kwtab = getattr (XKW, 'POS')
	fmt.extend (['<name_type>&%s;</name_type>' % kwtab[x.kw].kw
		     for x in nlist if x.kw>=180 and x.kw<200])
	eng_id = KW.LANG['eng'].id
	for g in getattr (s, '_gloss', []):
	    lang = getattr (g, 'g_lang', eng_id)
	    lang_attr = (' xml:lang="%s"' % XKW.LANG[lang].kw) if lang != eng_id else ''
	    fmt.append ('<trans_det%s>%s</trans_det>' % (lang_attr, g.txt))
	if fmt: 
	    fmt.insert (0, '<trans>')
	    fmt.append ('</trans>')
	return fmt
	   
def gloss (g, compat=None):
	fmt = []
	attrs = []
	if g.lang != XKW.LANG['eng'].id:
	    attrs.append ('xml:lang="%s"' % XKW.LANG[g.lang].kw)
	  # If 'compat' is not None, we generate all glosses as "equ"
	  # glosses.  There is no way to regenerate the original gloss
	  # for non-"equ" glosses since the were parsed out of some 
	  # other gloss but we no longer have any information about 
	  # which one. 
	if not compat and g.ginf != XKW.GINF['equ'].id:
	    attrs.append ('g_type="%s"' % XKW.GINF[g.ginf].kw)
	attr = (' ' if attrs else '') + ' '.join (attrs)
	fmt.append ("<gloss%s>%s</gloss>" % (attr, esc(g.txt)))
	return fmt

def kwds (parent, attr, domain, elem_name):
	nlist = getattr (parent, attr, [])
	if not nlist: return nlist
	kwtab = getattr (XKW, domain)
	kwlist = ['<%s>&%s;</%s>' % (elem_name, kwtab[x.kw].kw, elem_name)
		  for x in nlist]
	return kwlist

def freqs (parent, attr, rk):
	kwds = getattr (parent, attr, [])
	if not kwds: return []
	tmp = [(XKW.FREQ[x.kw].kw, x.value) for x in kwds]
	tmp = jdb.rmdups (tmp)[0]
	tmp.sort()
	return [('<%s>%s%02d</%s>' if x[0]=='nf' else '<%s>%s%d</%s>') 
		  % (rk, x[0], x[1], rk) 
		for x in tmp]

def lsrc (x):
	fmt = [];  attrs = []
	if x.lang != XKW.LANG['eng'].id:
	    attrs.append ('xml:lang="%s"' % XKW.LANG[x.lang].kw)
	if x.part: attrs.append ('ls_type="part"')
	if x.wasei: attrs.append ('ls_wasei="y"')
	attr = (' ' if attrs else '') + ' '.join (attrs)
	if not x.txt: fmt.append ('<lsource%s/>' % attr)
	else: fmt.append ('<lsource%s>%s</lsource>' % (attr, esc(x.txt)))
	return fmt

def xref (xref, src):
	"""
	xref -- The xref object to be formatted.
	src -- Corpus id number of the entry that contains 'xref'.
	  If 'src' is true, enhanced XML will be generated.  If
	  not, legacy JMdict XML will be generated.

	"""
	try: targobj = xref.TARG
	except AttributeError:
	    raise AttributeError ("Expected 'TARG' attribute on xref")

	k = r = ''
	if getattr (xref, 'kanj', None):
	    k = targobj._kanj[xref.kanj-1].txt
	if getattr (xref, 'rdng', None):
	    r = targobj._rdng[xref.rdng-1].txt
	if k and r: target = k + u'\u30FB' + r  # \u30FB is mid-height dot.
	else: target = k or r
	if len(targobj._sens) != 1:
	    target += u'\u30FB%d' % xref.xsens

	tag = 'xref'; attrs = []
	if src:
	    attrs.append ('type="%s"' % XKW.XREF[xref.typ].kw)
	    attrs.append ('seq="%s"' % targobj.seq)
	    if targobj.src != src:
		attr.append ('corp="%s"' % jd.KW.SRC[targobj.src].kw)
	    if getattr (xref, 'notes', None): 
		attrs.append ('note="%s"' % esc(xref.notes))
	else:
	    if xref.typ == XKW.XREF['ant']: tag = 'ant'

	attr = (' ' if attrs else '') + ' '.join (attrs)
	return '<%s%s>%s</%s>' % (tag, attr, target, tag)

def info (entr, compat=None):
	fmt = [] 
	if not compat:
	    x = getattr (entr, 'srcnote', None)
	    if x: fmt.append ('<srcnote>%s</srcnote>' % esc(entr.srcnote))
	    x = getattr (entr, 'notes', None)
	    if x: fmt.append ('<notes>%s</notes>' % esc(entr.notes))
	for x in getattr (entr, '_hist', []):
	    fmt.extend (audit (x, compat))
	if fmt: 
	    fmt.insert (0, '<info>')
	    fmt.append ('</info>')
	return fmt

def audit (h, compat=None):
	fmt = []
	fmt.append ('<audit>')
	fmt.append ('<upd_date>%s</upd_date>' % h.dt.date().isoformat())
	if getattr (h, 'notes', None): fmt.append ('<upd_detl>%s</upd_detl>'   % esc(h.notes))
	if not compat:
	    if getattr (h, 'email', None): fmt.append ('<upd_email>%s</upd_email>' % esc(h.email))
	    if getattr (h, 'name', None):  fmt.append ('<upd_name>%s</upd_name>'   % esc(h.name))
	    if getattr (h, 'refs', None):  fmt.append ('<upd_refs>%s</upd_refs>'   % esc(h.refs))
	    if getattr (h, 'diff', None):  fmt.append ('<upd_diff>%s</upd_diff>'   % esc(h.diff))
	fmt.append ('</audit>')
	return fmt

def audio (entr_or_rdng):
	a = getattr (entr_or_rdng, '_snd', [])
	if not a: return []
	return ['<audio clipid="c%d"/>' % x.snd for x in a]

def entrhdr (entr, compat=None):
	global XKW
	if not compat:
	    id = getattr (entr, 'id', None)
	    idattr = (' id="%d"' % id) if id else ""
	    stat = getattr (entr, 'stat', None)
	    statattr = (' stat="%s"' % XKW.STAT[stat].kw) if stat else ""
	    apprattr = ' appr="n"' if entr.unap else ""
	    dfrm = getattr (entr, 'dfrm', None)
	    dfrmattr = (' dfrm="%d"' % entr.dfrm) if dfrm else ""
	    fmt = ["<entry%s%s%s%s>" % (idattr, statattr, apprattr, dfrmattr)]
	else: fmt = ['<entry>']
	seq = fmt.append ('<ent_seq>%d</ent_seq>' % entr.seq)
	src = jdb.KW.SRC[entr.src].kw
	if not compat: fmt.append ('<ent_corp>%s</ent_corp>' % src)
	return fmt

def sndvols (vols):
	if not vols: return []
	fmt = []
	for v in vols:
	    idstr = ' id="v%s"' % str (v.id)
	    fmt.append ('<avol%s>' % idstr)
	    if getattr (v, 'loc',   None) is not None: fmt.append ('<av_loc>%s</av_loc>'     % v.loc)
	    if getattr (v, 'type',  None) is not None: fmt.append ('<av_type>%s</av_type>'   % v.type)
	    if getattr (v, 'title', None) is not None: fmt.append ('<av_title>%s</av_title>' % v.title)
	    if getattr (v, 'idstr', None) is not None: fmt.append ('<av_idstr>%s</av_idstr>' % v.idstr)
	    if getattr (v, 'corp',  None) is not None: fmt.append ('<av_corpus>%s</av_corpus>' % v.corp)
	    if getattr (v, 'notes', None) is not None: fmt.append ('<av_notes>%s</av_notes>' % v.notes)
	    fmt.append ('</avol>')
	return fmt

def sndsels (sels):
	if not sels: return []
	fmt = []
	for s in sels:
	    idstr = ' id="s%s"' % str (s.id)
	    volstr = ' vol="v%s"' % str (s.vol)
	    fmt.append ('<asel%s%s>' % (idstr, volstr))
	    if getattr (s, 'loc',   None) is not None: fmt.append ('<as_loc>%s</as_loc>'     % s.loc)
	    if getattr (s, 'type',  None) is not None: fmt.append ('<as_type>%s</as_type>'   % s.type)
	    if getattr (s, 'title', None) is not None: fmt.append ('<as_title>%s</as_title>' % s.title)
	    if getattr (s, 'notes', None) is not None: fmt.append ('<as_notes>%s</as_notes>' % s.notes)
	    fmt.append ('</asel>')
	return fmt

def sndclips (clips):
	if not clips: return []
	fmt = []
	for c in clips:
	    idstr = ' id="c%s"' % str (c.id)
	    selstr = ' sel="s%s"' % str (c.file)
	    fmt.append ('<aclip%s%s>' % (idstr,selstr))
	    if getattr (c, 'strt',  None) is not None: fmt.append ('<ac_strt>%s</ac_strt>'   % c.strt)
	    if getattr (c, 'leng',  None) is not None: fmt.append ('<ac_leng>%s</ac_leng>'   % c.leng)
	    if getattr (c, 'trns',  None) is not None: fmt.append ('<ac_trns>%s</ac_trns>'   % c.trns)
	    if getattr (c, 'notes', None) is not None: fmt.append ('<ac_notes>%s</ac_notes>' % c.notes)
	    fmt.append ('</aclip>')
	return fmt

def corpus (corpuses):
	KW = jdb.KW;  fmt = []
	for c in corpuses:
	    kwo = KW.SRC[c]
	    fmt.append ('<corpus id="%d">' % kwo.id)
	    fmt.append ('<name>%s</name>' % kwo.kw)
	    if getattr (kwo, 'descr', None): fmt.append ('<descr>%s</descr>' % esc(KW.SRC[c].descr))
	    if getattr (kwo, 'dt',    None): fmt.append ('<dt>%s</dt>'       % KW.SRC[c].dt)
	    if getattr (kwo, 'notes', None): fmt.append ('<notes>%s</notes>' % esc(KW.SRC[c].notes))
	    if getattr (kwo, 'seq',   None): fmt.append ('<seqname>%s</seqname>' % esc(KW.SRC[c].seq))
	    fmt.append ('</corpus>')
	return fmt

def _main (args, opts):
	cur = jdb.dbOpen ('jmdict')
	while True:
	    try: id = raw_input ("Id number? ")
	    except EOFError: id = None
	    if not id: break
	    e, raw = jdb.entrList (cur, [int(id)], ret_tuple=True)
	    jdb.augment_xrefs (cur, raw['xref'])
	    if not e:
		print "Entry id %d not found" % id
	    else:
		txt = entr (e[0], compat=None)
		print txt

if __name__ == '__main__':
	_main (None, None)
