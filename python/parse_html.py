'''
parses the file generated by the tweet stream and outputs a csv file 
of the tweets for upload

'''

import json
import sys
import csv

def parseTwitter(file):
    if sys.argv[2] == 'media':
        domedia = True
    f = open(file, 'r')
    fo = open('tweets.html','w')
    fo.write('<html>\n')
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
                mu =  mu.replace(u'\\','')
                print mu
            except Exception, ex:
                pass
            if domedia and mu != '':
                da= '%s,%s,%s,%s,%s,"%s","%s"\n'%(c,id,na,lo, la, mu, t)
                fo.write(da)
	    fo.write("<img src='%s'></img></br>"%mu)


        except Exception,ex:
            pass # some unicode translation issues
    fo.write('</html>\n')
    fo.close()

if __name__ == "__main__":
    parseTwitter(sys.argv[1])
