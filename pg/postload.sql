-- 
--    psql -f postload.sql [-d jmdict] [-U username]
--
-- You may need to use additional arguments such
-- as '-U username' depending on exiting defaults.

\set ON_ERROR_STOP 1
\i syncseq.sql
vacuum analyze
