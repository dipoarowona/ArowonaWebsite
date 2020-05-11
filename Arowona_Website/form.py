# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,ValidationError, TextAreaField
from wtforms.validators import DataRequired, Email
import phonenumbers



class ContactForm(FlaskForm):
    
    first_name = StringField("First Name", validators=[DataRequired()])
    
    last_name =  StringField("Last Name", validators=[DataRequired()])
    
    email = StringField("Email", validators=[DataRequired(), Email()])
    
    phoneNumber = StringField("Phone Number", validators=[DataRequired()])
    
    message = TextAreaField("Message",validators=[DataRequired()])
    
    submit = SubmitField("Send")
    
    def validate_phoneNumber(form, phoneNumber):
        if len(phoneNumber.data) > 16:
            raise ValidationError('Invalid phone number.')
        try:
            input_number = phonenumbers.parse(phoneNumber.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
        except:
            input_number = phonenumbers.parse("+1"+phoneNumber.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')

