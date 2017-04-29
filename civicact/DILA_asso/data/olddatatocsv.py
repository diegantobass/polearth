#!/usr/bin/env python
#-*- coding: utf8 -*-

import sys
import os
import re
import csv
import codecs
import xmltodict

folder = sys.argv[1]

def walk_files_folder(folder):
	filenames = []
	for root, dirs, files in os.walk(folder):
		for filename in files :
			if filename != ".DS_Store":
				filenames.append(os.path.join(root, filename))
	return filenames

def encode(champs):
	check = ""
	if champs == None:
		check = ""
	else:
		check = champs
	return check.encode('utf8')


for root, dirs, files in os.walk(folder):

	if "stock_assoc" in root.split('/')[-1]:
		output = csv.writer(open('output/' + root.split('/')[-1] + '.csv', 'w'))

	if len(files) > 1:
		for file in files:#walk_files_folder(folder):
			if ".DS_Store" not in file:
				annonce_ref = xmltodict.parse(codecs.open(os.path.join(root, file), 'r', encoding='ISO-8859-1').read())["ANNONCE_REF"]

				num_annonce = encode(annonce_ref["@numannonce"])
				date_declaration = encode(annonce_ref["@datedeclaration"])
				dept = encode(annonce_ref["@dept"])
				cp = encode(annonce_ref["@cp"])
				type_annonce = encode(annonce_ref["TYPE"]["@code"])
				lieu_declaration = encode(annonce_ref["LIEU_DECLARATION"])
				ancien_titre = encode(annonce_ref["ANCIEN_TITRE"])
				nouveau_titre = encode(annonce_ref["NOUVEAU_TITRE"])
				additif_objet = encode(annonce_ref["ADDITIF_OBJET"])
				nouvel_objet = encode(annonce_ref["NOUVEL_OBJET"])
				objet = encode(annonce_ref["OBJET"])
				titre = annonce_ref["TITRE"].encode('utf8')
				siege_social = encode(annonce_ref["SIEGE_SOCIAL"])
				if "INTERNET" in annonce_ref:
					smtp = encode(annonce_ref["INTERNET"]["@smtp"])
					http = encode(annonce_ref["INTERNET"]["@http"])
				else:
					smtp = ""
					http = ""
				date_parution = encode(annonce_ref["PARUTION_JO_ASSOCIATION"]["@dateparution"])

				regex_code = re.compile(r'[0-9]{1,10}')
				if "THEMES" in annonce_ref:
					if annonce_ref["THEMES"] == None:
						themes = ""
					else:
						themes = str(annonce_ref["THEMES"])
				results = re.findall(regex_code, themes)
				themas = '|'.join(results).encode('utf8')

				row = [date_parution,
					date_declaration,
					type_annonce,
					lieu_declaration,
					titre,
					objet,
					siege_social,
					themas,
					smtp,
					http,
					nouvel_objet,
					additif_objet,
					ancien_titre,
					cp,
					dept]

				output.writerow(row)