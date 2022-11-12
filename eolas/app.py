from flask import Flask

app = Flask(__name__)

from flask import render_template

@app.route('/')
def home():
	return render_template(
		'home.html',
		title="Eolas",
		description="Social research network"
	)