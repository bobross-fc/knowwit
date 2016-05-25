#!/usr/bin/env python3

from collections import namedtuple
import feedparser
import json
from src import utils


def file_contents_iter(filename):
	""" reads the contents of filename and returns a generator of its contents """
	with open(infile, 'rb') as f_reader:
		for line in f_reader.readlines():
			line = utils.to_str(line.strip())  # strip off any whitespace and convert to unicode str
			yield line


def get_site_rss(url):
	""" uses feedparser to download the contents at url and returns feedparser dict object """
	try:
		ret_dict = feedparser.parse(url)
	except Exception as e:
		raise e
	else:
		return ret_dict


def run(infile, outfile):
	rss_tuple = namedtuple('rss_tuple', 'domain link author')  # container for rss data
	
	urls = list(file_contents_iter(infile))
	
	out_rss_list = []  # will be list of rss_tuples 
	for url in urls:
		rss_data = get_site_rss(url)

		for rss_entry in rss_data.entries:
			if 'link' in rss_entry:
				link = rss_entry['link']
			else:
				link = ''

			if 'author' in rss_entry:
				author = rss_entry['author']
			else:
				author = ''

			rss_tup = rss_tuple(domain=url, link=link, author=author)
			out_rss_list.append(rss_tup)

	for rss_tup in out_rss_list:
		print ('''\
		       Author: {auth}
		       Domain: {url_d}
		       Link: {url_l}
		       \n'''.format(auth=rss_tup.author, url_d=rss_tup.domain, url_l=rss_tup.link))

if __name__ == '__main__': 
	infile = './src_sites.lst'
	outfile = './downloaded_sites.json'
	run(infile, outfile)
