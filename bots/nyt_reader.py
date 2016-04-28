#!/usr/bin/env python

import praw


def knowwit_post(txt, sub):
	try:
		praw_obj = praw.Reddit(user_agent='nyt_reader agent',
						   site_name='nyt_reader')
		praw_obj.login('nyt_reader', 'nyt_reader.nyt_reader')
		already_done = []

	except Exception as e:
		print(e)

if __name__ == '__main__':
	knowwit_post('Testing testing', 'nyt')



