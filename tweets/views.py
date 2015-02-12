from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.shortcuts import render_to_response
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import oauth2 as oauth
import json
import requests

# Create your views here.
def Home(request):
    ''' for entering twitter user details '''
    return  render(request, 'home.html')

def retrive_tweet(request):

	name = request.GET.get('name')
	count = request.GET.get('count')
	if not (name and count):
		return HttpResponse("Please provide name and count")
	CONSUMER_KEY = "your consumer kwy"
	CONSUMER_SECRET = "your consumer secret key"
	ACCESS_KEY = "your access key"
	ACCESS_SECRET = "your access secret"

	consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
	access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
	client = oauth.Client(consumer, access_token)


	timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+name+"&count="+count
	response, data = client.request(timeline_endpoint)

	tweets = json.loads(data)
	"""list comprehension"""
	if "errors" in tweets or tweets==[] or "error" in tweets:
		return HttpResponse("No tweets for user "+name )
	#print tweets
	tweets = [i.get('text') for i in tweets]
	#print ">>>>>>>>>"
	result = {"tweets": tweets}
	return HttpResponse(json.dumps(result))


def retrive_repos(request):
	print "working"
	name = request.GET.get('git_id')
	#if not name:
	#	return HttpResponse("Please provide a Github Username")
	API_TOKEN='your github apt token'
	GIT_API_URL='https://api.github.com'
	url='https://api.github.com/users/'+name+'/repos'
	url = '%s?access_token=%s' % \
	    (url,API_TOKEN)
	r = requests.get(url).json()
	repos = [data.get('full_name') for data in r]
	print repos
	result = {"repos":repos}
	return HttpResponse(json.dumps(result))
