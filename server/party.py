import random
import re
import asyncio
from enum import Enum

from server import database
from server.constants import TargetType
from server.exceptions import ClientError, ServerError, ArgumentError

class Party:
	def __init__(self, server, name, leader, party_id, locked=True):
		self.server = server
		self.name = name
		self.leader = leader
		self.users = set()
		self.id = party_id
		self.invite_list = {}
		self.lock = locked
		self.users.add(leader)
		self.notepad = ''
		self.votes = set()
		self.voters = []
		self.playerid = []
		
	def add_user(self, client):
		self.users.add(client)

	def mg_roles(self, roles):
		players = len(self.users)
		players = players - 1
		userrange = range(players)
		index = 0
		self.playerid = []
		for user in self.users:
			if user != self.leader:
				self.playerid.append(index)
				self.playerid[index] = user
				index += 1
		keymaster = self.playerid[random.choice(userrange)]
		keymaster.partyrole = 'Keymaster'
		keymaster.votepower = 0
		loop = True
		while loop:
			sage = self.playerid[random.choice(userrange)]
			if sage.partyrole == '':
				sage.partyrole = 'Sage'
				sage.votepower = 0
				break
		while loop:
			sac = self.playerid[random.choice(userrange)]
			if sac.partyrole == '':
				sac.partyrole = 'Sacrifice'
				sac.votepower = 1
				break
		index = 0
		customroles = len(roles)
		freeplayers = players - 3
		if customroles >= freeplayers:
			raise ArgumentError('Not enough players to hand out roles!')
		while index < customroles:
			if customroles == 0:
				break
			role = self.playerid[random.choice(userrange)]
			if role.partyrole == '':
				role.partyrole = roles[index]
				role.votepower = 0
				index += 1
		for user in self.users:
			if user != self.leader and user.partyrole == '':
				user.partyrole = 'Commoner'
				user.votepower = 0
		self.playerid = []
		msg = 'All roles handed out!'
		return msg

class Vote:
    def __init__(self, name):
        self.name = name
        self.number = 0
        self.voters = set()