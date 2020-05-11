# -*- coding: utf-8 -*-
from Arowona_Website import app, mail
from Arowona_Website.form import ContactForm
from flask import render_template, flash, redirect
from flask_mail import Message


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route('/contact', methods=["GET","POST"])
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
def projects():
    
    
    return render_template( "projects.html", title="Projects")




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
    
