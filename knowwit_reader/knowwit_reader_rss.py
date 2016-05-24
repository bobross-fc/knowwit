#!/usr/bin/env python3

import feedparser
import json


def run(infile, outfile):
	urls = []
	with open(infile, 'rb') as file_reader:
		urls.append(file_rader.readline())

	for url in urls:
		try:
			site_rss = feedparser.parse(url)
		except Exception, e:
			print ('[!] {}'.format(e))
			raise
		else:
			print '{auth}: {link}'.format(auth=site_rss['']) #need to put in another loop and probably get a new function too	
		finally:
			pass




if __name__ == '__main__': 
	infile = src_sites.lst
	outfile = downloaded_sites.json
	run(infile, outfile)
