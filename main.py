# -*- coding: utf-8 -*-
# Access level	 Read-only 
# About the application permission model
# Consumer key	7ZIEgmML9y8PdEhvaE0Gaw
# Consumer secret	swH5zPJBqXPYsm9dd0j2Gu0cTSxrt6eD9ADgiXNMfM
# Request token URL	https://api.twitter.com/oauth/request_token
# Authorize URL	https://api.twitter.com/oauth/authorize
# Access token URL	https://api.twitter.com/oauth/access_token
# Callback URL	None

# Access token	583539640-qDSUScVcaOU9FXRnbNN1IQUhkvfgNyoAZ83ATxZV
# Access token secret	DzzrtQAItoMqcJyVmzN7P1aRPiNzl3o1KOA2g0MENlo
# Access level	Read-only
import twitter

api = twitter.Api(consumer_key='7ZIEgmML9y8PdEhvaE0Gaw',
consumer_secret='swH5zPJBqXPYsm9dd0j2Gu0cTSxrt6eD9ADgiXNMfM', access_token_key='583539640-qDSUScVcaOU9FXRnbNN1IQUhkvfgNyoAZ83ATxZV', access_token_secret='DzzrtQAItoMqcJyVmzN7P1aRPiNzl3o1KOA2g0MENlo')
statuses = api.GetUserTimeline(raw_input("Podaj nazwe uzytkownika: "))
i = 0
while i<5:
	print " --------------------------"
	print statuses[i].text,"#", statuses[i].created_at
	print " --------------------------"
	i+=1