from flask import Flask, render_template, request, session
# from flask_session import Session
import os

app = Flask(__name__)
# 
# SESSION_TYPE = 'redis'
# app.config.from_object(__name__)
# Session(app)

singlequerypost = {'src':'article.svg','href':'article-id','title':'Better physics','desc':'Revolutionary discovery undermines modern physics','author':{'name':'Toby Loader','href':'profile-id'},'contributors':[{'name':'Daisy Loader','href':'profile-id'},{'name':'Einstein','href':'profile-id'}]}

fromqueryposts = [singlequerypost,singlequerypost,singlequerypost,singlequerypost]

username = 'toby' # session['username'] from login

@app.route('/')
def home():
	# session['username'] = 'toby'
	return render_template(
		'home.html',
		name=username,
		src="profile-pic",
		feed=fromqueryposts,
	)

@app.route('/uploadpage')
def uploadpaper():
	return render_template(
		'uploadpage.html',
		name=username,
	)

@app.route('/search')
def searchquery():
	search = request.args.get("term")
	return render_template(
		'search.html',
		search=search,
		name=username,
		src="profile-pic",
		feed=fromqueryposts,
	)

@app.route('/login')
def login():
	return render_template(
		'login.html'
	)

@app.route('/profile')
def profile():
	handle = request.args.get("handle")
	singleprofile = {'src':'profile-pic.svg','name':handle,'bio':'Philosifying Physics','publications':[{'title':'Bla bla','href':'blabla'},{'title':'Bla bla 2','href':'blabla2'},{'title':'Bla bla 3','href':'blabla3'}]}
	return render_template(
		'profile.html',
		name=username,
		profile=singleprofile
	)

@app.route('/pub')
def pub():
	title = request.args.get("title")
	singlepub = {'author':'Toby','title':title,'desc':'Research into cool stuff I want to make public','contributors':['Yan','Tan','Tethera'],'data':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'}
	return render_template(
		'publication.html',
		name=username,
		pub=singlepub
	)
