#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from doremi import query_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        data=[{'name':'서울'}, {'name':'강원'}, {'name':'경기'},
        {'name':'경남'}, {'name':'경북'}, {'name':'광주'},
        {'name':'대구'}, {'name':'대전'}, {'name':'부산'}, 
        {'name':'울산'}, {'name':'인천'}, {'name':'전남'},
        {'name':'전북'}, {'name':'제주'}, {'name':'충남'},
        {'name':'충북'}, {'name':'전국'}])

@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template(
        'result.html',
        data=data,
        error=error)


if __name__=='__main__':
    app.run(debug=True)