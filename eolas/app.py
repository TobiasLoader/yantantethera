from flask import Flask, render_template, request, session, jsonify
# from flask_session import Session
import random
# import os
from lenspy.main import *



app = Flask(__name__)
# 
# SESSION_TYPE = 'redis'
# app.config.from_object(__name__)
# Session(app)

singlequerypost = {'src':'article.svg','href':'article-id','title':'Better physics','desc':'Revolutionary discovery undermines modern physics','author':'Toby Loader','contributors':['Daisy Loader','Einstein']}

username = 'toby' # session['username'] from login
auth_client = None
localpaperstorage = {
	'James':[
		PubClass('James Research','Computer science problems',['toby','daisy'],'Lorem ipsum bla bla bla bla bla bla bla'),
		PubClass('Big Paper','Maths proof',['daisy'],'Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum'),
		PubClass('Friendly numbers','Fun maths problems',['rishin'],'Lorem ipsum bla bla bla bla bla bla bla'),
		PubClass('James Research','Computer science problems',['toby','daisy'],'Lorem ipsum bla bla bla bla bla bla bla')
	]}
profilehandles = []
profileids = []

def pubclasstodict(author,pub):
	return {'author':author,'title':pub.title,'desc':pub.desc,'contributors':pub.contributors,'data':pub.content}
	
def explorepapers():
	feed = []
	for handle, pubs in localpaperstorage.items():
		for pub in pubs:
			if random.random()>0.5:
				feed.append(pubclasstodict(handle,pub))
	return feed

def searchpapers(query):
	feed = []
	for handle, pubs in localpaperstorage.items():
		for pub in pubs:
			if query in pub.contributors:
				feed.append(pubclasstodict(handle,pub))
	return feed


@app.route('/')
def home():
	# session['username'] = 'toby'
	return render_template(
		'home.html',
		name=username,
		src="profile-pic",
		feed=explorepapers(),
	)

@app.route('/uploadpaper')
def uploadpaper():
	return render_template(
		'uploadpage.html',
		name=username,
	)

@app.route('/search')
def searchquery():
	search = request.args.get("term")
	pubfeed = searchpapers(search)
	# searchprofiles(search,10)
	return render_template(
		'search.html',
		search=search,
		name=username,
		src="profile-pic",
		feed=pubfeed,
	)

@app.route('/logindata', methods=['POST'])
def logindata():
	# print(request.json)
	auth_client, profilehandles, profileids = lOgin(request.json['handle'],request.json['private-address'])
	return jsonify(message='success')

@app.route('/login')
def login():
	return render_template(
		'login.html'
	)

@app.route('/profile')
def profile():
	handle = request.args.get("handle")
	singleprofile = {'src':'profile-pic.svg','name':handle,'id':profileids[profilehandles.index(handle)],'bio':'Philosifying Physics','publications':localpaperstorage[handle]}
	return render_template(
		'profile.html',
		name=username,
		profile=singleprofile
	)

@app.route('/pub')
def pub():
	author = request.args.get("author")
	title = request.args.get("title")
	allauthorspub = localpaperstorage[author]
	for mypub in allauthorspub:
		if mypub.title == title:
			return render_template(
				'publication.html',
				name=username,
				pub=pubclasstodict(author,mypub)
			)
	return render_template(
		'publication.html',
		name=username,
		pub={'author':'none','title':'none','desc':'none','contributors':[],'data':'none'}
	)


@app.route('/upload', methods=['POST'])
def upload():
	print(request.json)
	localpaperstorage[username].append(PubClass(request.json['title'],request.json['desc'],request.json['contributornames'],request.json['data']))
	return jsonify(message='success')