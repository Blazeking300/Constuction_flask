from flask import Flask, render_template, request, redirect, url_for, flash
import os
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/service")
def service():
    return render_template('service.html')

@app.route("/service-item")
def service_item():
    return render_template('service-item.html')

@app.route("/project")
def project():
    return render_template('project.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/post")
def post():
    return render_template('single-post.html')

if __name__ == '__main__':
    app.run(debug=True)
