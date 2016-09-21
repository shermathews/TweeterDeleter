import json
import oauth

tweets = requests.get("https://api.twitter.com/1.1/statuses/user_timeline.json")
