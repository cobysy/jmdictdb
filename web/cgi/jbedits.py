#!/usr/bin/env python3
#######################################################################
#  This file is part of JMdictDB.
#  Copyright (c) 2010 Stuart McGraw
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
#  51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
#######################################################################

__version__ = ('$Revision$'[11:-2],
               '$Date$'[7:-11])

import sys, cgi, re, os
sys.path.extend (['../lib','../../python/lib','../python/lib'])
import logger; from logger import L; logger.enable()
import jdb, jmcgi

Enc = 'utf-8'

def main (args, opts):
        jdb.reset_encoding (sys.stdout, 'utf-8')
        errs = []
        try: form, svc, dbg, cur, sid, sess, parms, cfg = jmcgi.parseform()
        except Exception as e: jmcgi.err_page ([str(e)])

          # The filesystem path of the directory containing editdata files.
        filesdir = cfg['web']['EDITDATA_DIR']
          # The URL for the directory containing editdata files.
        httpdir  = cfg['web']['EDITDATA_URL']

        fv = lambda x:(form.getfirst(x) or '').decode(Enc)
        is_editor = jmcgi.is_editor (sess)

        allfiles = sorted (os.listdir (filesdir))
        editfiles = [x for x in allfiles if re.search (r'[0-9]{5}\.dat$', x) ]
        logfiles = [x for x in allfiles if re.search (r'((ok)|(bad))\.log$', x) ]

        jmcgi.jinja_page ('jbedits.jinja', parms=parms,
                         filesdir=filesdir, httpdir=httpdir,
                         editfiles=editfiles, logfiles=logfiles,
                         svc=svc, dbg=dbg, sid=sid, session=sess, cfg=cfg,
                         this_page='jbedits.py')

if __name__ == '__main__':
        args, opts = jmcgi.args()
        main (args, opts)
