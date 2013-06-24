#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Goals:
classify voice command type 
classify syntax structure
extract query

(1)... T_KEY (QUERY)
(2)... VERB T_KEY PREP (QUERY)
(3)... VERB (QUERY) PREP T_KEY ...
(4)... I_KEY ...

L : (PREF) T_KEY QUERY
L : (PREF) VERB_PHRASE T_KEY PREP QUERY
L : (PERF) VERB_PHRASE QUERY PREP T_KEY (SUFF)
L : (PERF) I_KEY (SUFF)

VERB_PHRASE : VERB
VERB_PHRASE : VERB AUX

VERB:
search
look
pull
use
ask

AUX:
up

T_KEY:
google
search
open
computer
play

I_KEY:
news 
screenshot

PREP:
for
on


EX:
search seattle
google seattle
search google for seattle
do a google search on seattle # this works because we ignore all the in between stuff like 'search'
go ahead and google seattle
look up seattle on google
pull up search results for seattle
use google to search for seattle

get a youtube video of seattle
get a video on youtube of seattle

get the news
take a screenshot
news
screenshot

computer do you like sports
open facebook
play Justin Timberlake


RULES:
i_keys are overriden by t_keys at any point
once a t_key is set, all other t_keys are ignored. # there is a workaround for cases where latter t_keys are intended
once an action verb is set, all other action verbs are ignored

CORNER:
use youtube to search for seattle
'''

def main():
	t_keys = ['google', 'youtube', 'search', 'open', 'computer', 'play']
	i_keys = ['news','screenshot']
	action_verbs = ['search', 'look', 'pull', 'use']
	prepositions = ['for', 'on']
	aux = ['up']

	while 1:
		action_verb = "" 
		command_type = ""
		t_key = "" 
		i_key = ""

		line = raw_input("input line: ")
		words = line.split()

		for word in words:
			# set action verb if it comes before any other goalpost
			if word in action_verbs and action_verb == "" and t_key == "":
				action_verb = word 

			# set t_key if it comes before any other t_key
			if word in t_keys and t_key == "":
				t_key = word
				command_type = word

			# set i_key if it comes before any other key
			if word in i_keys and t_key == "" and i_key == "":
				i_key = word
				command_type = word

		print "ACTION VERB: " + action_verb
		print "COMMAND_TYPE: " + command_type

		#if command_type not in i_key: # then a query exists.



			




def get_query(words, syntax, command_type):
	if syntax == 1:
		query = "no query"

	elif syntax == 2:
		# (2)… A_VERB T_KEY PREP (QUERY)
		# find the command
		# find the preposition
		# get the query from the end

		command_index = words.index(command_type)
		preposition = command_index + 1
		query_list = words[preposition + 1:]
		query = ' '.join(query_list)

	#elif syntax == 3:


	elif syntax == 4:
		query_list = words[words.index(command_type) + 1:]
		query = ' '.join(query_list)

	elif syntax == 5:
		query = "no query"

	print "QUERY: " + query


if __name__ == "__main__":
	main()