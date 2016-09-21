import json
import oauth2
from oauth_request import OauthRequest

try:
	token = sys.argv[1]
	secret = sys.argv[2]
	
except ValueError:
	print("Invalid arguments. Expected token and secret.")
	
request = OauthRequest(secret, token)

tweets = tweetRequest.getTweets()
for tweet in tweets:
	tweetRequest.delete(tweet)
	

	