from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="rVHvS0LLSfQ5vKQd6qIRA"
consumer_secret="E56YPYHvkBaP2TTuXq61GDawV63uaSuVP1QcLc2VY"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="2988701-xUucsTgBpk2OfaQGQjl4kwuhlWwJ8KAaSFcigYdtho"
access_token_secret="fZYwywfRqDoXGXTZKm3MJkXOG2RMYULsCZs2xW8n7r8"


class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        f = open('corkData.json', 'a')
        f.write(data)
	f.close()
	
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter( locations=[-9.56,51.49,-8.05,52.27])


