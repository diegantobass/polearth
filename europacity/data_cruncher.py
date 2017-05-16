#!/usr/bin/env python
# -*- coding: utf8 -*-

import re
import csv
import sys
# import urllib2
# import urlparse
# import matplotlib
# import datetime as dt
from collections import defaultdict
from string import punctuation
from nltk.corpus import stopwords
from dateutil.parser import parse

# fichier input, stopwords et ponctuation
input_csv = csv.reader(open(sys.argv[1], 'r'))
headers = input_csv.next()
punctuation = punctuation.replace('#', '').replace("'", '').replace('@', '')
stops = stopwords.words('french') + [u'à', u'les', u'la', u'le', u'a', u'un', u'des']

# variables
account_count = defaultdict(int)
hashtags_count = defaultdict(int)
keywords_count = defaultdict(int)
domains_count = defaultdict(int)
dates_count = defaultdict(int)
retweets_count = defaultdict(int)
retweets_network = defaultdict(list)
mentions_count = defaultdict(int)
mentions_network = defaultdict(list)

# outputs
output_csv = csv.writer(open('output_csv.csv', 'w'))
account_out = csv.writer(open('accounts.csv', 'w'))
hashtags_out = csv.writer(open('hashtags.csv', 'w'))
keywords_out = csv.writer(open('keywords.csv', 'w'))
domains_out = csv.writer(open('domains.csv', 'w'))
dates_out = csv.writer(open('dates.csv', 'w'))
network_out = csv.writer(open('retweets.csv', 'w'))
mentions_out = csv.writer(open('mentions.csv', 'w'))

# dates évènements clés
events = ['08/11/2016', '21/05/2017']
events = sorted([parse(x, dayfirst=True) for x in events])

count_line = 0
for line in input_csv:
	link, account, date, lang, geo, tweet = line
	tweet_id = link.split('/')[-1]

	# texte du tweet sans ponctuation et sans urls et texte sous forme de liste de tokens
	tweet_text = ' '.join([x for x in tweet.split() if not re.match(r'(https?://\S+)', x)])
	tweet_text = ''.join([x for x in tweet_text if x not in punctuation]).replace('…', '')
	tweet_tokens = tweet_text.split()

	# date du tweet
	date = date.split('T')[0]
	dates_count[date] += 1
	date = parse(date, dayfirst=True)

	# set the keyword filter and date intervals filter here
	if "#europacity" in tweet_text.lower() and date < events[0]:

	# fréquence de tweet des comptes
		account_count[account] += 1
		
	# hashtags utilisés dans le tweet	
		hashtags = [x for x in tweet_text.split() if x.startswith('#')]
		for tag in hashtags:
			hashtags_count[tag.lower()] += 1

	# mots-pleins contenus dans le tweet (pas les hashtags)
		keywords = [x for x in tweet_text.split() if not x.startswith('#') and not x.startswith('@') and x not in stops]
		for keyword in keywords:
			keywords_count[keyword.lower()] += 1

	# urls valides présentes dans le tweet
		urls = re.findall(r'(https?://\S+)', tweet)
		urls_resolved = urls
		# urls_resolved = []
		# domains = []
		# for url in urls:
		# 	try: 
		# 		resolved = urllib2.urlopen(url).geturl()
		# 		domain = urlparse.urlparse(resolved).netloc
		# 		domains.append(domain)
		# 		urls_resolved.append(resolved)
		# 		domains_count[domain] += 1
		# 	except:
		# 		pass

	# reseau de retweets
		retweet_from_account = ""
		if tweet.startswith('RT'):
			if len(tweet_tokens) > 1 and tweet_tokens[1].startswith('@'):
				retweet_from_account = tweet_tokens[1][1:]
				retweets_count[account] += 1
				retweets_network[account].append(retweet_from_account)

	# réseau de mentions
		mentions = []
		for token in tweet_tokens:
			if token.startswith('@'):
				mentions.append(token[1:])
				mentions_count[account] += 1
				mentions_network[account].append(token[1:])

		# line_plus = line + [tweet_text, '|'.join(hashtags), '|'.join(keywords), '|'.join(domains), retweet_from_account, '|'.join(mentions)]
		line_plus = line + [tweet_text, '|'.join(hashtags), '|'.join(keywords), retweet_from_account, '|'.join(mentions)]
		output_csv.writerow(line_plus)

	# std_out infos 
		count_line += 1
		print count_line, "OK n°", tweet_id

####

# fréquence des comptes
for account in account_count:
	line = [account, account_count[account]]
	account_out.writerow(line)

# fréquence des hashtags
for hashtag in hashtags_count:
	line = [hashtag, hashtags_count[hashtag]]
	hashtags_out.writerow(line)

# fréquence des keywords
for keyword in keywords_count:
	line = [keyword, keywords_count[keyword]]
	keywords_out.writerow(line)

# fréquence des domains
for domain in domains_count:
	line = [domain, domains_count[domain]]
	domains_out.writerow(line)

# fréquence des dates
for date in dates_count:
	line = [date, dates_count[date]]
	dates_out.writerow(line)

# reseau de RT
for node in retweets_network:
	line = [node, '|'.join(retweets_network[node])]
	network_out.writerow(line)

# reseau de mentions
for node in mentions_network:
	line = [node, '|'.join(mentions_network[node])]
	mentions_out.writerow(line)


















