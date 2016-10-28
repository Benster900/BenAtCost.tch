"""
Author: Ben Bornholm
Date: 6-2-15
Description: Webpage for kali linux docker image
"""

# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, redirect, request, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def home():
	return render_template('homepage.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')


# Run the app :)
if __name__ == "__main__":
	app.run(host='0.0.0.0')
