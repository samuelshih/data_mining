from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Twitter API
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"
consumer_key = "API_KEY"
consumer_secret = "API_SECRET"

# Listener that prints received tweets to stdout
class StdOutListener(StreamListener):

	def on_data(self, data):
		print data
		return True

	def on_error(self, status):
		print status

if __name__ == '__main__':
	# This handles Twitter auth and connection between Twitter streaming API
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)

	# line filter Twitter Streams to capture data by keywords
	stream.filter(track=['trump', 'bernie', 'rubio', 'bush', 'clinton', 'carson', 'cruz'])