# -*- coding: utf-8 -*-
from Arowona_Website import app, mail
from Arowona_Website.form import ContactForm
from flask import render_template, flash, redirect
from flask_mail import Message


@app.route("/home")
@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/about")
@app.route("/about/")
def about():
    return render_template("about.html", title="About")

@app.route('/contact', methods=["GET","POST"])
@app.route('/contact/', methods=["GET","POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        fname = form.first_name.data
        lname = form.last_name.data
        email = form.email.data
        phone_number =form.phoneNumber.data
        message = form.message.data
        send_message(fname,lname,email,phone_number,message)
        flash("Your Message Has Been Sent!", "success")
        return redirect('contact')
    return render_template( "contact.html", title="Contact", form=form)

@app.route("/projects")
@app.route("/projects/")
def projects():
    
    
    return render_template( "projects.html", title="Projects")


@app.errorhandler(404)
def error_404(e):
    return render_template("404.html"), 404

@app.errorhandler(403)
def error_403(e):
    return render_template("403.html"), 403
@app.errorhandler(500)
def error_500(e):
    return render_template("500.html"), 500





def send_message(fname,lname,email,phone_number,message):
    
    msg = Message("Arowona.com Inquiry",
                  sender="noreplyarowona@gmail.com", 
                  recipients=["abdulsalam.arowona@gmail.com"])
    msg.body = f'''NAME: {fname} {lname}
EMAIL: {email}
PHONE NUMBER: {phone_number}

MESSAGE:
    
{message}
    '''
    
    msg_user = Message("Arowona.com Inquiry Confirmation",
                  sender="noreplyarowona@gmail.com", 
                  recipients= [email])
    msg_user.body = f'''Your inquiry has been sent!

Review of Inquiry:
    
NAME: {fname} {lname}
EMAIL: {email}
PHONE NUMBER: {phone_number}

MESSAGE:
    
{message}
    '''
    
    mail.send(msg)
    mail.send(msg_user)
    
    
    
