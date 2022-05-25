from flask import Flask, render_template, url_for
app = Flask(__name__)
print(__name__)



@app.route('/')
def my_home():
	return render_template('index.html')

# HOME

@app.route('/index.html')
def home_refresh():
	return render_template('index.html')

# ABOUT

@app.route('/about.html')
def about():
	return render_template('about.html')

# WORKS

@app.route('/works.html')
def work():
	return render_template('works.html')

# CONTACT

@app.route('/contact.html')
def contact():
	return render_template('contact.html')

# COMPONENTS

@app.route('/components.html')
def components():
	return render_template('components.html')

# FAVICON

@app.route('/favicon.ico')
def favicon():
	return 
