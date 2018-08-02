import datetime
from flask import render_template, redirect, url_for, request,flash,Response
from config.manager import app
# from models.models import db
from models.report import Monitor,db
import time

@app.route('/report',methods=['GET','POST'])
def report():
    # print(request.values)
    print(request.values)
    param =""
    for i in request.values:
        param += i + "="+request.values.get(i) + "&"
    print(param)
    temp = Monitor(
            uid=request.values.get('uid'),
            extra=param,
            add_time=int(time.time())
        )
    db.session.add(temp)
    db.session.commit()

    return Response('success')