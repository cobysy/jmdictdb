
# jelparse_tab.py
# This file is automatically generated. Do not edit.

_lr_method = 'LALR'

_lr_signature = '\xf6Y&\x16\xe0\x1b\xfc\xa8\x10\xb8\xa0\x8f\xe7\xf4N)'

_lr_action_items = {'RTEXT':([0,2,13,15,16,18,33,35,58,61,66,],[1,1,24,1,1,1,24,52,52,52,78,]),'NL':([0,1,3,6,7,8,9,10,11,12,14,15,19,20,27,28,32,34,],[2,-14,-7,-13,15,-5,-9,17,-11,-8,-24,26,-12,-25,37,-6,-10,-26,]),'SEMI':([1,3,6,7,8,9,10,11,12,14,19,20,27,28,32,34,39,40,42,44,45,47,48,49,50,52,53,55,56,59,64,65,67,68,69,70,73,78,80,],[-14,-7,-13,16,-5,-9,18,-11,-8,-24,-12,-25,18,-6,-10,-26,-18,-20,57,58,-42,-45,-51,-48,-40,-49,-46,-21,-22,-43,-53,-52,-47,-23,-19,-41,-44,-50,-54,]),'TEXT':([13,33,35,48,62,63,81,],[23,23,46,64,74,77,74,]),'COLON':([46,77,],[62,81,]),'BRKTR':([21,22,23,24,25,43,44,45,46,47,48,49,50,51,52,53,59,62,64,65,67,70,71,72,73,74,75,76,78,80,82,83,],[-27,34,-31,-30,-29,-28,-37,-42,-32,-45,-51,-48,-40,-33,-49,-46,-43,-34,-53,-52,-47,-41,80,-55,-44,-38,-39,-35,-50,-54,-56,-36,]),'NUMBER':([35,58,60,79,],[48,48,72,82,]),'GTEXT':([14,20,31,34,41,57,],[-24,-25,40,-26,56,40,]),'KTEXT':([0,2,13,15,16,18,33,35,58,61,],[6,6,25,6,6,6,25,49,49,49,]),'COMMA':([21,22,23,24,25,43,44,45,46,47,48,49,50,51,52,53,59,62,64,65,67,70,71,72,73,74,75,76,78,80,82,83,],[-27,33,-31,-30,-29,-28,-37,-42,-32,-45,-51,-48,-40,-33,-49,-46,-43,-34,-53,-52,-47,-41,79,-55,-44,-38,-39,-35,-50,-54,-56,-36,]),'EQL':([23,],[35,]),'SLASH':([46,],[63,]),'QTEXT':([35,62,81,],[51,75,75,]),'HASH':([48,],[65,]),'SNUM':([14,17,20,26,29,30,34,36,37,38,39,40,42,54,55,56,68,69,],[-24,31,-25,31,31,-15,-26,31,31,-16,-18,-20,-17,31,-21,-22,-23,-19,]),'BRKTL':([1,3,6,11,12,14,19,20,31,34,40,41,45,48,49,52,53,55,56,57,64,65,68,78,],[-14,13,-13,13,13,-24,13,-25,13,-26,13,13,60,-51,-48,-49,60,13,13,13,-53,-52,13,-50,]),'DOT':([45,48,49,64,65,],[61,-51,66,-53,-52,]),'$end':([4,5,14,20,29,30,34,36,38,39,40,42,54,55,56,68,69,],[-1,0,-24,-25,-3,-15,-26,-4,-16,-18,-20,-17,-2,-21,-22,-23,-19,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _lr_action.has_key(_x):  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'rdngitem':([2,15,18,],[9,9,32,]),'gloss':([31,57,],[39,69,]),'xrefnum':([35,58,],[45,45,]),'slist':([45,53,],[59,67,]),'entr':([0,],[5,]),'sense':([17,26,29,36,37,54,],[30,30,38,38,30,38,]),'tagitem':([13,33,],[21,43,]),'xref':([35,58,],[50,70,]),'rdngsect':([2,15,],[10,27,]),'jtext':([35,58,61,],[53,53,53,]),'preentr':([0,],[4,]),'taglist':([3,11,12,19,31,40,41,55,56,57,68,],[14,14,20,20,14,14,20,20,14,14,20,]),'senses':([17,26,37,],[29,36,54,]),'tags':([13,],[22,]),'jitem':([35,58,61,],[47,47,73,]),'taglists':([3,11,31,40,56,57,],[12,19,41,55,68,41,]),'glosses':([31,],[42,]),'snums':([60,],[71,]),'krtext':([0,2,15,16,18,],[3,11,11,3,11,]),'xrefs':([35,],[44,]),'kanjsect':([0,],[7,]),'atext':([62,81,],[76,83,]),'kanjitem':([0,16,],[8,28,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _lr_goto.has_key(_x): _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S'",1,None,None,None),
  ('entr',1,'p_entr_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',40),
  ('preentr',5,'p_preentr_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',76),
  ('preentr',4,'p_preentr_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',80),
  ('preentr',4,'p_preentr_3','C:\\Temp\\jb\\python\\lib\\jelparse.py',84),
  ('kanjsect',1,'p_kanjsect_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',88),
  ('kanjsect',3,'p_kanjsect_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',92),
  ('kanjitem',1,'p_kanjitem_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',96),
  ('kanjitem',2,'p_kanjitem_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',100),
  ('rdngsect',1,'p_rdngsect_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',107),
  ('rdngsect',3,'p_rdngsect_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',111),
  ('rdngitem',1,'p_rdngitem_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',115),
  ('rdngitem',2,'p_rdngitem_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',119),
  ('krtext',1,'p_krtext_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',126),
  ('krtext',1,'p_krtext_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',130),
  ('senses',1,'p_senses_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',134),
  ('senses',2,'p_senses_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',138),
  ('sense',2,'p_sense_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',142),
  ('glosses',1,'p_glosses_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',149),
  ('glosses',3,'p_glosses_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',153),
  ('gloss',1,'p_gloss_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',157),
  ('gloss',2,'p_gloss_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',161),
  ('gloss',2,'p_gloss_3','C:\\Temp\\jb\\python\\lib\\jelparse.py',165),
  ('gloss',3,'p_gloss_4','C:\\Temp\\jb\\python\\lib\\jelparse.py',169),
  ('taglists',1,'p_taglists_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',173),
  ('taglists',2,'p_taglists_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',177),
  ('taglist',3,'p_taglist_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',182),
  ('tags',1,'p_tags_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',186),
  ('tags',3,'p_tags_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',190),
  ('tagitem',1,'p_tagitem_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',195),
  ('tagitem',1,'p_tagitem_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',199),
  ('tagitem',1,'p_tagitem_3','C:\\Temp\\jb\\python\\lib\\jelparse.py',203),
  ('tagitem',3,'p_tagitem_4','C:\\Temp\\jb\\python\\lib\\jelparse.py',212),
  ('tagitem',3,'p_tagitem_5','C:\\Temp\\jb\\python\\lib\\jelparse.py',229),
  ('tagitem',4,'p_tagitem_6','C:\\Temp\\jb\\python\\lib\\jelparse.py',236),
  ('tagitem',5,'p_tagitem_7','C:\\Temp\\jb\\python\\lib\\jelparse.py',244),
  ('tagitem',7,'p_tagitem_8','C:\\Temp\\jb\\python\\lib\\jelparse.py',258),
  ('tagitem',3,'p_tagitem_9','C:\\Temp\\jb\\python\\lib\\jelparse.py',269),
  ('atext',1,'p_atext_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',290),
  ('atext',1,'p_atext_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',294),
  ('xrefs',1,'p_xrefs_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',298),
  ('xrefs',3,'p_xrefs_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',302),
  ('xref',1,'p_xref_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',307),
  ('xref',2,'p_xref_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',311),
  ('xref',3,'p_xref_3','C:\\Temp\\jb\\python\\lib\\jelparse.py',315),
  ('xref',1,'p_xref_4','C:\\Temp\\jb\\python\\lib\\jelparse.py',319),
  ('jitem',1,'p_jitem_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',323),
  ('jitem',2,'p_jitem_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',327),
  ('jtext',1,'p_jtext_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',332),
  ('jtext',1,'p_jtext_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',336),
  ('jtext',3,'p_jtext_3','C:\\Temp\\jb\\python\\lib\\jelparse.py',340),
  ('xrefnum',1,'p_xrefnum_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',344),
  ('xrefnum',2,'p_xrefnum_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',348),
  ('xrefnum',2,'p_xrefnum_3','C:\\Temp\\jb\\python\\lib\\jelparse.py',352),
  ('slist',3,'p_slist_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',356),
  ('snums',1,'p_snums_1','C:\\Temp\\jb\\python\\lib\\jelparse.py',360),
  ('snums',3,'p_snums_2','C:\\Temp\\jb\\python\\lib\\jelparse.py',367),
]
