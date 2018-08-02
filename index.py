# coding:utf-8
import datetime, os, uuid
from flask import render_template, redirect, url_for, flash, session, Response, request,Flask
from config.manager import app
import route.index 
import route.route
import route.template
import route.report


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
