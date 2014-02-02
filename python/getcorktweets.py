from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key="xx"
consumer_secret="www"
access_token="aaa"
access_token_secret="bbbb"


class StdOutListener(StreamListener):

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


