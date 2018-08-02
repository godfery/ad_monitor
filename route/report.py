import datetime
from flask import render_template, redirect, url_for, request,flash,Response
from config.manager import app
# from models.models import db
from models.report import Monitor,db
from route.func import user_login_required
import time
from datetime import datetime
def dateformat(value,format="%Y-%m-%d"):
    return datetime.fromtimestamp(value).strftime(format)

app.jinja_env.filters['dateformat']=dateformat
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

# 文章列表
@app.route('/report/list/<int:page>/', methods=['GET'])
@user_login_required
def report_list(page):
    if page is None:
        page = 1
    
    page_data = Monitor.query.order_by(
        Monitor.add_time.desc()
    ).paginate(page=page, per_page=10)
    
    return render_template('report_list.html', title=u"模版列表", page_data=page_data)