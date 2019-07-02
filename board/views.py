'''
  File: views.py
  Project: board
  
  Created Date: 2019-07-02 10:22:34
  Author: zhaopeng
  -----
  Copyright (c) 2019 zhaopeng. All rights reserved.
  -----
  HISTORY:
  Date      	By		Comments
  ----------	---		---------------------------------------------------------
'''

from flask import flash, redirect, url_for, render_template

from board import app, db
from board.models import Message
from board.forms import HelloForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)