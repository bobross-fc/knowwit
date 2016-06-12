#!/usr/bin/env python3

from collections import namedtuple
import configparser
import json
import praw
from src import utils

KNOWWIT_USER = 'mail_carrier'
KNOWWIT_USER_AGENT = 'special delivery'

class KnowwitConnection(object):
	"""docstring for KnowwitConnection"""
	def __init__(self, knowwit_user, knowwit_user_agent):
		super(KnowwitConnection, self).__init__()
		self.knowwit_user = knowwit_user
		self.knowwit_user_agent = knowwit_user_agent

		self._knowwit_inst = praw.Reddit(user_agent=self.knowwit_user_agent, site_name=self.knowwit_user)


def run(to_read_filename, knowwit_user=KNOWWIT_USER, knowwit_user_agent=KNOWWIT_USER_AGENT):
	knowwit_connection = praw.Reddit(user_agent=knowwit_user_agent, site_name=knowwit_user)
	knowwit_connection.login('happy_trees', 'Happy.Trees.420')
	knowwit_connection.send_message('mail_carrier', 'Here come dat boi', 'oh shit wuddup')
	


if __name__ == '__main__':
	run(to_read_filename='./downloaded_sites.json', knowwit_user='happy_trees', knowwit_user_agent='Happy Trees Mail Reader' )