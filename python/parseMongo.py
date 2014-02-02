from pymongo import MongoClient
client = MongoClient("mongodb://hackathon:hackathon@ds027699.mongolab.com:27699/hackathon")
db = client.hackathon
col = db.tweets

import datetime
'''
post = {"author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()}
'''


import json
import sys
import csv

def parseTwitter(file):
    tweets = db.tweets
    if sys.argv[2] == 'media':
        domedia = True
    f = open(file, 'r')
    fo = open('tweets.csv','w')
    fo.write('created,id,name,longitude,latitude,media,text\n')
    for l in f:
        #l = u' '.join(l).encode('utf-8').strip()
        try:

            data = json.loads(l)
            c =  data["created_at"].replace('"','')
            id = data['id']
            t =  data["text"]
            lo =  data["coordinates"]['coordinates'][0]
            la =  data["coordinates"]['coordinates'][1]
            na =  data['user']['name']
            sn =  data['user']['screen_name']
            mu = ''
            try:
                mu =  data['entities']['media'][0]['media_url']
            except Exception, ex:
                pass
            #if domedia and mu != '':
            da= '%s,%s,%s,%s,%s,"%s","%s"\n'%(c,id,na,lo, la, mu, t)
            tweet = {"text": t,
                "tweet_id": id,
                "name": na,
                "longitude": lo,
                "latitude": la,
                "media_url": mu}
            tweet_id = tweets.insert(tweet)
            #fo.write(post)



        except Exception,ex:
            print ex
            pass # some unicode translation issues
    fo.close()

if __name__ == "__main__":
    parseTwitter(sys.argv[1])


