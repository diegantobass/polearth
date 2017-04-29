#!/usr/bin/env python
#-*- coding: utf8 -*-

import sys
import os
import re
import csv
import xmltodict

folder = sys.argv[1]

for root, dirs, files in os.walk(folder):
	if len(files) > 1:
		output = csv.writer(open('output/' + root.split('/')[-1] + '.csv', 'w'))

	for filename in files :
		if filename != ".DS_Store":
			file = os.path.join(root, filename)
			print file
			xml = xmltodict.parse(open(file, 'r').read())
			date_parution = xml["PARUTION_JO_ASSOCIATION"]["@dateparution"].encode('utf8')
			annonces = xml["PARUTION_JO_ASSOCIATION"]["ANNONCE_REF"]
			
			for annonce_ref in annonces:
				if "@datedeclaration" in annonce_ref:
					date_declaration = annonce_ref["@datedeclaration"].encode('utf8')
				else:
					date_declaration = "parution"
				
				type_annonce = annonce_ref["TYPE"]["@code"].encode('utf8')

				if "LIEU_DECLARATION" in annonce_ref:
					lieu_declaration = annonce_ref["LIEU_DECLARATION"].encode('utf8')
				else:
					lieu_declaration = ""

				objet = ""
				if "OBJET" in annonce_ref:
					objet = annonce_ref["OBJET"]
				else:
					objet = ""
				if objet == None:
					objet = ""
				objet = objet.encode('utf-8')

				siege_social = ""
				if "SIEGE_SOCIAL" in annonce_ref:
					siege_social = annonce_ref["SIEGE_SOCIAL"]
				if siege_social == None:
					siege_social = ""
				siege_social = siege_social.encode('utf8')

				titre = ""
				if "TITRE" in annonce_ref:
					titre = annonce_ref["TITRE"]
				if titre == None:
					titre = ""
				titre = titre.encode('utf8')

				regex_code = re.compile(r'[0-9]{1,10}')
				if "THEMES" in annonce_ref:
					if annonce_ref["THEMES"] == None:
						themes = ""
					else:
						themes = str(annonce_ref["THEMES"])
				results = re.findall(regex_code, themes)
				themas = '|'.join(results).encode('utf8')

				smtp = ""
				http = ""
				if "INTERNET" in annonce_ref:
					if "@smtp" in annonce_ref["INTERNET"].keys():
						smtp = annonce_ref["INTERNET"]["@smtp"]
					else:
						smtp = ""
					if "@http" in annonce_ref["INTERNET"].keys():
						annonce_ref["INTERNET"]["@http"]
					else:
						http = ""
				if smtp == None:
					smtp = ""
				if http == None:
					http = ""
				smtp = smtp.encode('utf8')				
				http = http.encode('utf8')				

				row = [date_parution,
					date_declaration,
					type_annonce,
					lieu_declaration,
					titre,
					objet,
					siege_social,
					themas,
					smtp,
					http]

				output.writerow(row)
