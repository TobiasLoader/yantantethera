from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/login')
def login():
	return render_template(
		'login.html'
	)

singlequerypost = {'src':'article.svg','href':'article-id','title':'Better physics','desc':'Revolutionary discovery undermines modern physics','author':{'name':'Toby Loader','href':'profile-id'},'contributors':[{'name':'Daisy Loader','href':'profile-id'},{'name':'Einstein','href':'profile-id'}]}

fromqueryposts = [singlequerypost,singlequerypost,singlequerypost,singlequerypost]

@app.route('/')
def home():
	return render_template(
		'home.html',
		name="toby",
		src="profile-pic",
		feed=fromqueryposts,
	)

@app.route('/upload-paper')
def uploadpaper():
	return render_template(
		'upload-paper.html',
	)

@app.route('/search')
def searchquery():
	search = request.args.get("term")
	return render_template(
		'search.html',
		search=search,
		name="toby",
		src="profile-pic",
		feed=fromqueryposts,
	)

