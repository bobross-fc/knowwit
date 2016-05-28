#!/usr/bin/env python3

from collections import namedtuple
import configparser
import json
import praw
from src import utils

praw_tuple = namedtuple('praw_tuple', 'username password user_agent')  # container for praw login data


def get_praw_config(config_filename):
	try:
		config = configparser.ConfigParser()
		config.read(config_filename)
		if 'credentials' in config:
			config_creds = config['credentials']  # just saving typing by creating config_creds
		else:
			raise Exception('Now \'credentials\' section found in {}'.format(config_filename))

		if 'username' in config_creds:
			username = config_creds['username']
		else:
			raise Exception('Config missing needed option: {}'.format('username'))
		
		if 'password' in config_creds:
			password = config_creds['password']
		else:
			raise Exception('Config missing needed option: {}'.format('password'))
		

		if 'user_agent' in config_creds:
			user_agent = config_creds['user_agent']
		else:
			raise Exception('Config missing needed option: {}'.format('user_agent'))
	except Exception as e:
		raise e
	else:
		ret_praw_tup = praw_tuple(username=username, password=password, user_agent=user_agent)
		return ret_praw_tup


def run(to_read_filename, knowwit_conf_filename, nicknames_filename):
	mail_carrier_praw = get_praw_config(knowwit_conf_filename)
	print ('Received {} {} {}'.format(mail_carrier_praw.username, mail_carrier_praw.password, mail_carrier_praw.user_agent))


if __name__ == '__main__':
	run(to_read_filename='./downloaded_sites.json', nicknames_filename='./nicknames.json', knowwit_conf_filename='./mail_carrier.conf')