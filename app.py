# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
      'user': "root",
      'password': "Abcde5Fghij1Klmno1Pqrst",
      'host': "sample-db-1.caruzcbh5rmg.ap-northeast-1.rds.amazonaws.com",
      'db_name': "test"
  })

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Test_sample1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    value1 = db.Column(db.Integer)
    valu2 = db.Column(db.Integer)


@app.route('/')
def get_sample():
    data = Test_sample1.query.filter_by(id=1).first()
    return render_template('sample1.html', name=data.name)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
