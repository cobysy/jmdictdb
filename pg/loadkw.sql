\set ON_ERROR_STOP 1
\copy kwdial from '../pg/data/kwdial.csv' CSV delimiter E'\t'
\copy kwfreq from '../pg/data/kwfreq.csv' CSV delimiter E'\t'
\copy kwfld  from '../pg/data/kwfld.csv'  CSV delimiter E'\t'
\copy kwginf from '../pg/data/kwginf.csv' CSV delimiter E'\t'
\copy kwkinf from '../pg/data/kwkinf.csv' CSV delimiter E'\t'
\copy kwlang from '../pg/data/kwlang.csv' CSV delimiter E'\t'
\copy kwmisc from '../pg/data/kwmisc.csv' CSV delimiter E'\t'
\copy kwpos  from '../pg/data/kwpos.csv'  CSV delimiter E'\t'
\copy kwrinf from '../pg/data/kwrinf.csv' CSV delimiter E'\t'
\copy kwsrc  from '../pg/data/kwsrc.csv'  CSV delimiter E'\t'
\copy kwstat from '../pg/data/kwstat.csv' CSV delimiter E'\t'
\copy kwxref from '../pg/data/kwxref.csv' CSV delimiter E'\t'
