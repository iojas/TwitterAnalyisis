import sys
import re
import simplejson as json
import operator

def reads(filename):
# reads from a file created using twitterstream.py  
  f = open(filename)
  
  places =[]
  Ucountries={}
  Ucountries2={}
  hasht=[]
  hashtd={}
  hashList=[]
  lang={}
  langs=[]
  sortedlang=[]
  sortedWords=[]
  words={}
  
  for line in f:
    tweet = json.loads(line)
###########Creates an Array for Hashtags#############   
    if 'text' in tweet:
	      if tweet['lang']=='en':
	           text = tweet['text'].lower()
      	           if (tweet['entities']['hashtags']!=None):
		            hasht.append(tweet['entities']['hashtags'])

###########Creates an Array for Places#############    
    if 'place' in tweet:
	places.append(tweet['place'])

###########Creates an Array for Languages#############    
    if 'lang' in tweet:
	langs.append(tweet['lang'])
 
#########################################################################
# Here, We go through an array named langs and add each language to a dictionary named lang. If it is already present we increament the count.  
  for i in langs:
	if (lang.has_key(i)==False):
		lang[i]=1
	else:
		lang[i]=lang[i]+1
  sortedlang = sorted(lang.items(),key=operator.itemgetter(1))
  print "***************Languages***************"
# Print Languages  
  for i in range(len(sortedlang)):
	print sortedlang[i] 
  
  
#########################################################################
  for i in hasht:
	if(i):
		
		for j in range(len(i)):
			
			if (hashtd.has_key(i[j]['text'])==False):
				hashtd[i[j]['text']]=1
			else:
				hashtd[i[j]['text']]=hashtd[i[j]['text']]+1
		
  hashList=sorted(hashtd.items(),key=operator.itemgetter(1),reverse=True)	
  print "***************HashTags***************"
  for i in range(10):
	print hashList[i]		
   
#########################################################################  
  for i in range(len(places)):
	if(places[i]!=None):
		cc= places[i]['country_code']
		
		if (Ucountries.has_key(cc)==False):
			Ucountries[cc]=1
		else:
			Ucountries[cc]=Ucountries[cc]+1
  
  

  locList = sorted(Ucountries.items(),key=operator.itemgetter(1))
  print "***************Countries***************"
  for i in range(len(locList)):
	print locList[i]

#########################################################################		
 		
def main():
  if len(sys.argv)!= 2:
    print 'Please enter filename followed by program name'
    sys.exit(1)
  filename= sys.argv[1]
 # print filename
  reads(filename)  

if __name__ =='__main__':
  main()
