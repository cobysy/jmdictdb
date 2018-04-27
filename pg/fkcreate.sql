 -- This file was auto-generated at 2018-04-26 17:55:29.436646-06, dbver 20c2fe.

 ALTER TABLE public.kwxref ADD CONSTRAINT kwxref_kw_key UNIQUE (kw);
 ALTER TABLE public.kwstat ADD CONSTRAINT kwstat_kw_key UNIQUE (kw);
 ALTER TABLE public.kwsrct ADD CONSTRAINT kwsrct_kw_key UNIQUE (kw);
 ALTER TABLE public.kwsrc ADD CONSTRAINT kwsrc_kw_key UNIQUE (kw);
 ALTER TABLE public.kwrinf ADD CONSTRAINT kwrinf_kw_key UNIQUE (kw);
 ALTER TABLE public.kwpos ADD CONSTRAINT kwpos_kw_key UNIQUE (kw);
 ALTER TABLE public.kwlang ADD CONSTRAINT kwlang_kw_key UNIQUE (kw);
 ALTER TABLE public.kwgrp ADD CONSTRAINT kwgrp_kw_key UNIQUE (kw);
 ALTER TABLE public.kwginf ADD CONSTRAINT kwginf_kw_key UNIQUE (kw);
 ALTER TABLE public.kwfreq ADD CONSTRAINT kwfreq_kw_key UNIQUE (kw);
 ALTER TABLE public.kwfld ADD CONSTRAINT kwfld_kw_key UNIQUE (kw);
 ALTER TABLE public.kwdial ADD CONSTRAINT kwdial_kw_key UNIQUE (kw);
 ALTER TABLE public.kwcinf ADD CONSTRAINT kwcinf_kw_key UNIQUE (kw);
 ALTER TABLE public.freq ADD CONSTRAINT freq_entr_rdng_kanj_kw_key UNIQUE (entr, rdng, kanj, kw);
 ALTER TABLE public.conj ADD CONSTRAINT conj_name_key UNIQUE (name);
 ALTER TABLE public.xresolv ADD CONSTRAINT xresolv_pkey PRIMARY KEY (entr, sens, typ, ord);
 ALTER TABLE public.xref ADD CONSTRAINT xref_pkey PRIMARY KEY (entr, sens, xref, xentr, xsens);
 ALTER TABLE public.stagr ADD CONSTRAINT stagr_pkey PRIMARY KEY (entr, sens, rdng);
 ALTER TABLE public.stagk ADD CONSTRAINT stagk_pkey PRIMARY KEY (entr, sens, kanj);
 ALTER TABLE public.sndvol ADD CONSTRAINT sndvol_pkey PRIMARY KEY (id);
 ALTER TABLE public.sndfile ADD CONSTRAINT sndfile_pkey PRIMARY KEY (id);
 ALTER TABLE public.snd ADD CONSTRAINT snd_pkey PRIMARY KEY (id);
 ALTER TABLE public.sens ADD CONSTRAINT sens_pkey PRIMARY KEY (entr, sens);
 ALTER TABLE public.rinf ADD CONSTRAINT rinf_pkey PRIMARY KEY (entr, rdng, kw);
 ALTER TABLE public.restr ADD CONSTRAINT restr_pkey PRIMARY KEY (entr, rdng, kanj);
 ALTER TABLE public.rdngsnd ADD CONSTRAINT rdngsnd_pkey PRIMARY KEY (entr, rdng, snd);
 ALTER TABLE public.rdng ADD CONSTRAINT rdng_pkey PRIMARY KEY (entr, rdng);
 ALTER TABLE public.rad ADD CONSTRAINT rad_pkey PRIMARY KEY (num, var);
 ALTER TABLE public.pos ADD CONSTRAINT pos_pkey PRIMARY KEY (entr, sens, kw);
 ALTER TABLE public.misc ADD CONSTRAINT misc_pkey PRIMARY KEY (entr, sens, kw);
 ALTER TABLE public.lsrc ADD CONSTRAINT lsrc_pkey PRIMARY KEY (entr, sens, lang, txt);
 ALTER TABLE public.kwxref ADD CONSTRAINT kwxref_pkey PRIMARY KEY (id);
 ALTER TABLE public.kwstat ADD CONSTRAINT kwstat_pkey PRIMARY KEY (id);
 ALTER TABLE public.kwsrct ADD CONSTRAINT kwsrct_pkey PRIMARY KEY (id);
 ALTER TABLE public.kwsrc ADD CONSTRAINT kwsrc_pkey PRIMARY KEY (id);
 ALTER TABLE public.kwrinf ADD CONSTRAINT kwrinf_pkey PRIMARY KEY (id);
 ALTER TABLE public.kwpos ADD CONSTRAINT kwpos_pkey PRIMARY KEY (id);
 ALTER TABLE public.kwmisc ADD CONSTRAINT kwmisc_pkey PRIMARY KEY (id);
 ALTER TABLE public.kwlang ADD CONSTRAINT kwlang_pkey PRIMARY KEY (id);
 ALTER TABLE public.kwkinf ADD CONSTRAINT kwkinf_pkey PRIMARY KEY (id);
 ALTER TABLE public.kwgrp ADD CONSTRAINT kwgrp_pkey PRIMARY KEY (id);
 ALTER TABLE public.kwginf ADD CONSTRAINT kwginf_pkey PRIMARY KEY (id);
 ALTER TABLE public.kwfreq ADD CONSTRAINT kwfreq_pkey PRIMARY KEY (id);
 ALTER TABLE public.kwfld ADD CONSTRAINT kwfld_pkey PRIMARY KEY (id);
 ALTER TABLE public.kwdial ADD CONSTRAINT kwdial_pkey PRIMARY KEY (id);
 ALTER TABLE public.kwcinf ADD CONSTRAINT kwcinf_pkey PRIMARY KEY (id);
 ALTER TABLE public.kresolv ADD CONSTRAINT kresolv_pkey PRIMARY KEY (entr, kw, value);
 ALTER TABLE public.kinf ADD CONSTRAINT kinf_pkey PRIMARY KEY (entr, kanj, kw);
 ALTER TABLE public.kanj ADD CONSTRAINT kanj_pkey PRIMARY KEY (entr, kanj);
 ALTER TABLE public.hist ADD CONSTRAINT hist_pkey PRIMARY KEY (entr, hist);
 ALTER TABLE public.grp ADD CONSTRAINT grp_pkey PRIMARY KEY (entr, kw);
 ALTER TABLE public.gloss ADD CONSTRAINT gloss_pkey PRIMARY KEY (entr, sens, gloss);
 ALTER TABLE public.fld ADD CONSTRAINT fld_pkey PRIMARY KEY (entr, sens, kw);
 ALTER TABLE public.entrsnd ADD CONSTRAINT entrsnd_pkey PRIMARY KEY (entr, snd);
 ALTER TABLE public.entr ADD CONSTRAINT entr_pkey PRIMARY KEY (id);
 ALTER TABLE public.dial ADD CONSTRAINT dial_pkey PRIMARY KEY (entr, sens, kw);
 ALTER TABLE public.db ADD CONSTRAINT db_pkey PRIMARY KEY (id);
 ALTER TABLE public.conotes ADD CONSTRAINT conotes_pkey PRIMARY KEY (id);
 ALTER TABLE public.conjo_notes ADD CONSTRAINT conjo_notes_pkey PRIMARY KEY (pos, conj, neg, fml, onum, note);
 ALTER TABLE public.conjo ADD CONSTRAINT conjo_pkey PRIMARY KEY (pos, conj, neg, fml, onum);
 ALTER TABLE public.conj ADD CONSTRAINT conj_pkey PRIMARY KEY (id);
 ALTER TABLE public.cinf ADD CONSTRAINT cinf_pkey PRIMARY KEY (entr, kw, value, mctype);
 ALTER TABLE public.chr ADD CONSTRAINT chr_pkey PRIMARY KEY (entr);
 ALTER TABLE public.xresolv ADD CONSTRAINT xresolv_check CHECK (((rtxt IS NOT NULL) OR (ktxt IS NOT NULL)));
 ALTER TABLE public.xref ADD CONSTRAINT xref_xref_check CHECK ((xref > 0));
 ALTER TABLE public.xref ADD CONSTRAINT xref_check1 CHECK (((kanj IS NOT NULL) OR (rdng IS NOT NULL)));
 ALTER TABLE public.xref ADD CONSTRAINT xref_check CHECK ((xentr <> entr));
 ALTER TABLE public.sens ADD CONSTRAINT sens_sens_check CHECK ((sens > 0));
 ALTER TABLE public.rdng ADD CONSTRAINT rdng_rdng_check CHECK ((rdng > 0));
 ALTER TABLE public.rad ADD CONSTRAINT rad_loc_check CHECK (((loc IS NULL) OR (loc = ANY (ARRAY['O'::bpchar, 'T'::bpchar, 'B'::bpchar, 'R'::bpchar, 'L'::bpchar, 'E'::bpchar, 'V'::bpchar]))));
 ALTER TABLE public.kanj ADD CONSTRAINT kanj_kanj_check CHECK ((kanj > 0));
 ALTER TABLE public.hist ADD CONSTRAINT hist_hist_check CHECK ((hist > 0));
 ALTER TABLE public.gloss ADD CONSTRAINT gloss_gloss_check CHECK ((gloss > 0));
 ALTER TABLE public.freq ADD CONSTRAINT freq_check CHECK (((rdng IS NOT NULL) OR (kanj IS NOT NULL)));
 ALTER TABLE public.entr ADD CONSTRAINT entr_seq_check CHECK ((seq > 0));
 ALTER TABLE public.xresolv ADD CONSTRAINT xresolv_typ_fkey FOREIGN KEY (typ) REFERENCES kwxref(id);
 ALTER TABLE public.xresolv ADD CONSTRAINT xresolv_entr_fkey FOREIGN KEY (entr, sens) REFERENCES sens(entr, sens) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.xref ADD CONSTRAINT xref_xentr_fkey FOREIGN KEY (xentr, xsens) REFERENCES sens(entr, sens) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.xref ADD CONSTRAINT xref_typ_fkey FOREIGN KEY (typ) REFERENCES kwxref(id);
 ALTER TABLE public.xref ADD CONSTRAINT xref_rdng_fkey FOREIGN KEY (xentr, rdng) REFERENCES rdng(entr, rdng) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.xref ADD CONSTRAINT xref_kanj_fkey FOREIGN KEY (xentr, kanj) REFERENCES kanj(entr, kanj) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.xref ADD CONSTRAINT xref_entr_fkey FOREIGN KEY (entr, sens) REFERENCES sens(entr, sens) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.stagr ADD CONSTRAINT stagr_entr_fkey1 FOREIGN KEY (entr, rdng) REFERENCES rdng(entr, rdng) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.stagr ADD CONSTRAINT stagr_entr_fkey FOREIGN KEY (entr, sens) REFERENCES sens(entr, sens) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.stagk ADD CONSTRAINT stagk_entr_fkey1 FOREIGN KEY (entr, kanj) REFERENCES kanj(entr, kanj) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.stagk ADD CONSTRAINT stagk_entr_fkey FOREIGN KEY (entr, sens) REFERENCES sens(entr, sens) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.sndvol ADD CONSTRAINT sndvol_corp_fkey FOREIGN KEY (corp) REFERENCES kwsrc(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.sndfile ADD CONSTRAINT sndfile_vol_fkey FOREIGN KEY (vol) REFERENCES sndvol(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.snd ADD CONSTRAINT snd_file_fkey FOREIGN KEY (file) REFERENCES sndfile(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.sens ADD CONSTRAINT sens_entr_fkey FOREIGN KEY (entr) REFERENCES entr(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.rinf ADD CONSTRAINT rinf_kw_fkey FOREIGN KEY (kw) REFERENCES kwrinf(id);
 ALTER TABLE public.rinf ADD CONSTRAINT rinf_entr_fkey FOREIGN KEY (entr, rdng) REFERENCES rdng(entr, rdng) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.restr ADD CONSTRAINT restr_entr_fkey1 FOREIGN KEY (entr, kanj) REFERENCES kanj(entr, kanj) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.restr ADD CONSTRAINT restr_entr_fkey FOREIGN KEY (entr, rdng) REFERENCES rdng(entr, rdng) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.rdngsnd ADD CONSTRAINT rdngsnd_snd_fkey FOREIGN KEY (snd) REFERENCES snd(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.rdngsnd ADD CONSTRAINT rdngsnd_entr_fkey FOREIGN KEY (entr, rdng) REFERENCES rdng(entr, rdng) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.rdng ADD CONSTRAINT rdng_entr_fkey FOREIGN KEY (entr) REFERENCES entr(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.pos ADD CONSTRAINT pos_kw_fkey FOREIGN KEY (kw) REFERENCES kwpos(id);
 ALTER TABLE public.pos ADD CONSTRAINT pos_entr_fkey FOREIGN KEY (entr, sens) REFERENCES sens(entr, sens) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.misc ADD CONSTRAINT misc_kw_fkey FOREIGN KEY (kw) REFERENCES kwmisc(id);
 ALTER TABLE public.misc ADD CONSTRAINT misc_entr_fkey FOREIGN KEY (entr, sens) REFERENCES sens(entr, sens) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.lsrc ADD CONSTRAINT lsrc_lang_fkey FOREIGN KEY (lang) REFERENCES kwlang(id);
 ALTER TABLE public.lsrc ADD CONSTRAINT lsrc_entr_fkey FOREIGN KEY (entr, sens) REFERENCES sens(entr, sens) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.kwsrc ADD CONSTRAINT kwsrc_srct_fkey FOREIGN KEY (srct) REFERENCES kwsrct(id);
 ALTER TABLE public.kresolv ADD CONSTRAINT kresolv_entr_fkey FOREIGN KEY (entr) REFERENCES entr(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.kinf ADD CONSTRAINT kinf_kw_fkey FOREIGN KEY (kw) REFERENCES kwkinf(id);
 ALTER TABLE public.kinf ADD CONSTRAINT kinf_entr_fkey FOREIGN KEY (entr, kanj) REFERENCES kanj(entr, kanj) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.kanj ADD CONSTRAINT kanj_entr_fkey FOREIGN KEY (entr) REFERENCES entr(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.hist ADD CONSTRAINT hist_stat_fkey FOREIGN KEY (stat) REFERENCES kwstat(id);
 ALTER TABLE public.hist ADD CONSTRAINT hist_entr_fkey FOREIGN KEY (entr) REFERENCES entr(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.grp ADD CONSTRAINT grp_kw_fkey FOREIGN KEY (kw) REFERENCES kwgrp(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.grp ADD CONSTRAINT grp_entr_fkey FOREIGN KEY (entr) REFERENCES entr(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.gloss ADD CONSTRAINT gloss_lang_fkey FOREIGN KEY (lang) REFERENCES kwlang(id);
 ALTER TABLE public.gloss ADD CONSTRAINT gloss_entr_fkey FOREIGN KEY (entr, sens) REFERENCES sens(entr, sens) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.freq ADD CONSTRAINT freq_kw_fkey FOREIGN KEY (kw) REFERENCES kwfreq(id);
 ALTER TABLE public.freq ADD CONSTRAINT freq_entr_fkey1 FOREIGN KEY (entr, kanj) REFERENCES kanj(entr, kanj) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.freq ADD CONSTRAINT freq_entr_fkey FOREIGN KEY (entr, rdng) REFERENCES rdng(entr, rdng) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.fld ADD CONSTRAINT fld_kw_fkey FOREIGN KEY (kw) REFERENCES kwfld(id);
 ALTER TABLE public.fld ADD CONSTRAINT fld_entr_fkey FOREIGN KEY (entr, sens) REFERENCES sens(entr, sens) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.entrsnd ADD CONSTRAINT entrsnd_snd_fkey FOREIGN KEY (snd) REFERENCES snd(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.entrsnd ADD CONSTRAINT entrsnd_entr_fkey FOREIGN KEY (entr) REFERENCES entr(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.entr ADD CONSTRAINT entr_stat_fkey FOREIGN KEY (stat) REFERENCES kwstat(id);
 ALTER TABLE public.entr ADD CONSTRAINT entr_src_fkey FOREIGN KEY (src) REFERENCES kwsrc(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.entr ADD CONSTRAINT entr_dfrm_fkey FOREIGN KEY (dfrm) REFERENCES entr(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.dial ADD CONSTRAINT dial_kw_fkey FOREIGN KEY (kw) REFERENCES kwdial(id);
 ALTER TABLE public.dial ADD CONSTRAINT dial_entr_fkey FOREIGN KEY (entr, sens) REFERENCES sens(entr, sens) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.conjo_notes ADD CONSTRAINT conjo_notes_pos_fkey FOREIGN KEY (pos, conj, neg, fml, onum) REFERENCES conjo(pos, conj, neg, fml, onum) ON UPDATE CASCADE;
 ALTER TABLE public.conjo_notes ADD CONSTRAINT conjo_notes_note_fkey FOREIGN KEY (note) REFERENCES conotes(id) ON UPDATE CASCADE;
 ALTER TABLE public.conjo ADD CONSTRAINT conjo_pos_fkey FOREIGN KEY (pos) REFERENCES kwpos(id) ON UPDATE CASCADE;
 ALTER TABLE public.conjo ADD CONSTRAINT conjo_pos2_fkey FOREIGN KEY (pos2) REFERENCES kwpos(id) ON UPDATE CASCADE;
 ALTER TABLE public.conjo ADD CONSTRAINT conjo_conj_fkey FOREIGN KEY (conj) REFERENCES conj(id) ON UPDATE CASCADE;
 ALTER TABLE public.cinf ADD CONSTRAINT cinf_kw_fkey FOREIGN KEY (kw) REFERENCES kwcinf(id) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.cinf ADD CONSTRAINT cinf_entr_fkey FOREIGN KEY (entr) REFERENCES chr(entr) ON UPDATE CASCADE ON DELETE CASCADE;
 ALTER TABLE public.chr ADD CONSTRAINT chr_entr_fkey FOREIGN KEY (entr) REFERENCES entr(id) ON UPDATE CASCADE ON DELETE CASCADE;

 CREATE UNIQUE INDEX chr_chr_idx ON chr USING btree (chr);
 CREATE INDEX cinf_kw ON cinf USING btree (kw);
 CREATE INDEX cinf_val ON cinf USING btree (value);
 CREATE UNIQUE INDEX conj_name_key ON conj USING btree (name);
 CREATE INDEX entr_dfrm_idx ON entr USING btree (dfrm) WHERE (dfrm IS NOT NULL);
 CREATE INDEX entr_seq_idx ON entr USING btree (seq);
 CREATE INDEX entr_stat_idx ON entr USING btree (stat) WHERE (stat <> 2);
 CREATE INDEX entr_unap_idx ON entr USING btree (unap) WHERE unap;
 CREATE INDEX entrsnd_snd_idx ON entrsnd USING btree (snd);
 CREATE UNIQUE INDEX freq_entr_coalesce_coalesce1_kw_idx ON freq USING btree (entr, COALESCE((rdng)::integer, 999), COALESCE((kanj)::integer, 999), kw);
 CREATE UNIQUE INDEX freq_entr_rdng_kanj_kw_key ON freq USING btree (entr, rdng, kanj, kw);
 CREATE UNIQUE INDEX gloss_entr_sens_lang_txt_idx ON gloss USING btree (entr, sens, lang, txt);
 CREATE INDEX gloss_lower_idx ON gloss USING btree (lower((txt)::text) varchar_pattern_ops);
 CREATE INDEX gloss_lower_idx1 ON gloss USING btree (lower((txt)::text));
 CREATE INDEX gloss_txt_idx ON gloss USING btree (txt);
 CREATE INDEX grp_kw ON grp USING btree (kw);
 CREATE INDEX hist_dt_idx ON hist USING btree (dt);
 CREATE INDEX hist_email_idx ON hist USING btree (email);
 CREATE INDEX hist_userid_idx ON hist USING btree (userid);
 CREATE UNIQUE INDEX kanj_entr_txt_idx ON kanj USING btree (entr, txt);
 CREATE INDEX kanj_txt_idx ON kanj USING btree (txt);
 CREATE INDEX kanj_txt_idx1 ON kanj USING btree (txt varchar_pattern_ops);
 CREATE UNIQUE INDEX kwcinf_kw_key ON kwcinf USING btree (kw);
 CREATE UNIQUE INDEX kwdial_kw_key ON kwdial USING btree (kw);
 CREATE UNIQUE INDEX kwfld_kw_key ON kwfld USING btree (kw);
 CREATE UNIQUE INDEX kwfreq_kw_key ON kwfreq USING btree (kw);
 CREATE UNIQUE INDEX kwginf_kw_key ON kwginf USING btree (kw);
 CREATE UNIQUE INDEX kwgrp_kw_key ON kwgrp USING btree (kw);
 CREATE UNIQUE INDEX kwlang_kw_key ON kwlang USING btree (kw);
 CREATE UNIQUE INDEX kwpos_kw_key ON kwpos USING btree (kw);
 CREATE UNIQUE INDEX kwrinf_kw_key ON kwrinf USING btree (kw);
 CREATE UNIQUE INDEX kwsrc_kw_key ON kwsrc USING btree (kw);
 CREATE UNIQUE INDEX kwsrct_kw_key ON kwsrct USING btree (kw);
 CREATE UNIQUE INDEX kwstat_kw_key ON kwstat USING btree (kw);
 CREATE UNIQUE INDEX kwxref_kw_key ON kwxref USING btree (kw);
 CREATE UNIQUE INDEX rdng_entr_txt_idx ON rdng USING btree (entr, txt);
 CREATE INDEX rdng_txt_idx ON rdng USING btree (txt);
 CREATE INDEX rdng_txt_idx1 ON rdng USING btree (txt varchar_pattern_ops);
 CREATE INDEX rdngsnd_snd ON rdngsnd USING btree (snd);
 CREATE INDEX sndfile_vol_idx ON sndfile USING btree (vol);
 CREATE INDEX xref_xentr_xsens_idx ON xref USING btree (xentr, xsens);
 CREATE INDEX xresolv_kanj ON xresolv USING btree (ktxt);
 CREATE INDEX xresolv_rdng ON xresolv USING btree (rtxt);

