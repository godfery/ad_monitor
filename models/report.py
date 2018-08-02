# coding:utf-8


try:
    from config.db import db
except ModuleNotFoundError as err:
    print("Module not found,manual load module")
    from flask import Flask
    import os
    # import sys
    app = Flask(__name__)
    app.root_path = os.path.join(os.path.dirname(__file__), '../')
    app.config['SECRET_KEY'] = '12345678'
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/report"
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UP'] = os.path.join(app.root_path, 'static/uploads')
    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy(app)
    # pass



class Monitor(db.Model):
    __tablename__ = 'monitor'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    uid = db.Column(db.String(64), nullable=False)  # 
    extra = db.Column(db.String(128), nullable=False)  # 
    add_time = db.Column(db.Integer, nullable=False)  # 注册时间 


if __name__ == '__main__':
    db.create_all()
