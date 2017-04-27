#!/usr/bin/env python
# -*- coding: utf8 -*-

import re
import csv
import urllib2
import urlparse
import matplotlib
import datetime as dt
from collections import defaultdict
from string import punctuation
from nltk.corpus import stopwords

europa_csv = csv.reader(open('jeudi.csv', 'r'))
headers = europa_csv.next()
punctuation = punctuation.replace('#', '').replace("'", '').replace('@', '')
stops = stopwords.words('french') + [u'à', u'les', u'la', u'le', u'a', u'un', u'des']

# urls = []
# other_hashtags = defaultdict(int)
# keywords = defaultdict(int)
# network = defaultdict(list)
# network = csv.writer(open('network.csv', 'w'))
# count_RT = 0
datecount = defaultdict(int)

for line in europa_csv:
	link = line[0]
	account = line[1]
	date = line[2]
	lang = line[3]
	geo = line[4]
	tweet = line[5]

### Hashtags

# 	tweet = ' '.join([x for x in tweet.split() if not re.match(r'(https?://\S+)', x)])
# 	tweet = ''.join([x for x in tweet if x not in punctuation])
# 	hashtags = [x for x in tweet.split() if not x.startswith('#') and not x.startswith('@') and x not in stops]

# 	for tag in hashtags:
# 		# other_hashtags[tag.replace('…', '').lower()] += 1
# 		keywords[tag.replace('…', '').lower()] += 1

# for tag in keywords:
# 	print keywords[tag], '\t', tag

### URLS

	# urls_found = re.findall(r'(https?://\S+)', tweet)
	# urls = []
	# for url in urls_found:
	# 	try: 
	# 		expanded = urllib2.urlopen(url)
	# 		url = urlparse.urlparse(expanded.geturl()).netloc
	# 		print url
	# 	except:
	# 		print "broken"

### RT

	# if tweet.startswith('RT'):
	# 	print tweet
# 		tweet = ''.join([x for x in tweet if x not in punctuation])
# 		tweet_split = tweet.split()
# 		if tweet_split[1].startswith('@'):
# 			count_RT += 1
# 			network[line[1].lower()].append(tweet_split[1][1:].lower())

# print count_RT
# for count in network:
# 	line = [count, '|'.join(network[count])]
# 	output.writerow(line)

### Dates

# 	date = date.split('T')[0]
# 	datecount[date] += 1

# for date in datecount:
# 	print date, datecount[date]



















