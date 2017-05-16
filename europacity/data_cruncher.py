#!/usr/bin/env python
# -*- coding: utf8 -*-

import re
import csv
import sys
import urllib2
import urlparse
from collections import defaultdict
from string import punctuation
from nltk.corpus import stopwords
from dateutil.parser import parse

def dicoToFile(dico, name):
	file = csv.writer(open(name + '.csv', 'w'))
	for key in dico:
		line = [key, dico[key]]
		file.writerow(line)

def networkToFile(network, name):
	file = csv.writer(open(name + '.csv', 'w'))
	for node in network:	
		line = [node, '|'.join(network[node])]
		file.writerow(line)

def crunchTweet(link, account, date, lang, geo, tweet, do_urls=False):
	tweet_id = link.split('/')[-1]
	
	# texte du tweet sans ponctuation et sans urls et texte sous forme de liste de tokens
	tweet_text = ' '.join([x for x in tweet.split() if not re.match(r'(https?://\S+)', x)])
	tweet_text = ''.join([x for x in tweet_text if x not in punctuation]).replace('…', '')
	tweet_tokens = tweet_text.split()
	
	# dates
	date = date.split('T')[0]
	dates_count[date] += 1
	
	# fréquence de tweet des comptes
	accounts_count[account] += 1
	
	# hashtags utilisés dans le tweet	
	hashtags = [x for x in tweet_text.split() if x.startswith('#')]
	for tag in hashtags:
		hashtags_count[tag.lower()] += 1
	
	# mots-pleins contenus dans le tweet (pas les hashtags)
	keywords = [x for x in tweet_text.split() if not x.startswith('#') and not x.startswith('@') and x not in stops]
	for keyword in keywords:
		keywords_count[keyword.lower()] += 1
	
	# urls valides présentes dans le tweet
	domains = []
	if do_urls :
		urls = re.findall(r'(https?://\S+)', tweet)
		urls_resolved = urls
		urls_resolved = []
		domains = []
		for url in urls:
			try: 
				resolved = urllib2.urlopen(url).geturl()
				domain = urlparse.urlparse(resolved).netloc
				domains.append(domain)
				urls_resolved.append(resolved)
				domains_count[domain] += 1
			except:
				pass
	
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

	if do_urls :
		line_plus = line + [tweet_text, '|'.join(hashtags), '|'.join(keywords), '|'.join(domains), retweet_from_account, '|'.join(mentions)]
	else :
		line_plus = line + [tweet_text, '|'.join(hashtags), '|'.join(keywords), retweet_from_account, '|'.join(mentions)]

	# std_out infos 
	print "OK n°", tweet_id
	return line_plus

###############################################

if __name__ == "__main__":

	# fichier input, stopwords et ponctuation
	input_csv = csv.reader(open(sys.argv[1], 'r'))
	headers = input_csv.next()
	punctuation = punctuation.replace('#', '').replace("'", '').replace('@', '')
	stops = stopwords.words('french') + [u'à', u'les', u'la', u'le', u'a', u'un', u'des']
	output_csv = csv.writer(open('output.csv', 'w'))

	# counters
	accounts_count = defaultdict(int)
	hashtags_count = defaultdict(int)
	keywords_count = defaultdict(int)
	domains_count = defaultdict(int)
	dates_count = defaultdict(int)
	retweets_count = defaultdict(int)
	mentions_count = defaultdict(int)

	# networkers
	retweets_network = defaultdict(list)
	mentions_network = defaultdict(list)

	for line in input_csv:
		link, account, date, lang, geo, tweet = line

		# set the keyword filter and date intervals filter here
		if "#europacity" in tweet.lower() and parse(date, dayfirst=True) < parse('08/11/2016', dayfirst=True):
			new_line = crunchTweet(link, account, date, lang, geo, tweet, do_urls=True)
			output_csv.writerow(new_line)

	dicoToFile(accounts_count, "accounts")
	dicoToFile(hashtags_count, "hashtags")
	dicoToFile(keywords_count, "keywords")
	dicoToFile(domains_count, "domains")
	dicoToFile(dates_count, "dates")

	networkToFile(retweets_network, "retweets_network")
	networkToFile(mentions_network, "mentions_network")



















