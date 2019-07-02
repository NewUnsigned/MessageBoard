"""
  File: models.py
  Project: board
  
  Created Date: 2019-07-02 10:22:25
  Author: zhaopeng
  -----
  Copyright (c) 2019 zhaopeng. All rights reserved.
  -----
  HISTORY:
  Date      	By		Comments
  ----------	---		---------------------------------------------------------
"""

from datetime import datetime
from board import db
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
