'''
  File: forms.py
  Project: board
  
  Created Date: 2019-07-02 10:22:18
  Author: zhaopeng
  -----
  Copyright (c) 2019 zhaopeng. All rights reserved.
  -----
  HISTORY:
  Date      	By		Comments
  ----------	---		---------------------------------------------------------
'''

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class  HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(1,200)])
    submit = SubmitField()