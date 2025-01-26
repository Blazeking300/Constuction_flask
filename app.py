from flask import Flask, render_template, request, redirect, url_for, flash
import os

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

@app.route("/admin")
def adminlogin():
    return render_template('login.html')


@app.route("/admin-login-post", methods=['GET','POST'])
def admin_login_post():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']

        # return f"The password is {password == '12345678'}"

        if name == 'admin' and password == '12345678':
            return render_template('admin.html')
    return redirect("/")

    
if __name__ == '__main__':
    app.run(debug=True)
