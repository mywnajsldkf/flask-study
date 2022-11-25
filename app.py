import os
from pydoc import plain
from models import Plan, db
from flask import Flask, redirect, render_template, request, url_for, jsonify
from datetime import date

app = Flask(__name__)
app.app_context().push()

# 현재있는 파일의 디렉토리 절대경로
basdir = os.path.abspath(os.path.dirname(__file__))
# basdir 경로안에 DB 파일 만들기
dbfile = os.path.join(basdir, 'db.sqlite')

# config.py 설정 파일
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 수정사항에 대한 TRACK
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SECRET_KEY
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/create', methods=['POST', 'GET'])
def create_plan():
    '''
    if request.method == 'POST': 
        plan = Plan(request.form['title'], request.form['description'], request.form['when'], request.form['who'], request.form['where'])
        db.session.add(plan)
        db.session.commit()
        return redirect(url_for('get_mypage'))
    return render_template("plan.html")
    '''

@app.route('/mypage')
def get_mypage():
    '''
    today_date = date.today().isoformat()

    plans = []
    completedPlan = Plan.query.filter(Plan.when < today_date).all()
    upcommingPlan = Plan.query.filter(Plan.when > today_date).all()

    plans.append(completedPlan)
    plans.append(upcommingPlan)

    return render_template('mypage.html', plans = plans)
    '''

def dict_helper(objlist):
    result2 = [item.obj_to_dict() for item in objlist]
    return result2

@app.get('/calender/data')
def get_calender_data():
    '''
    today_date = date.today().isoformat()

    plans = []
    completedPlan = Plan.query.filter(Plan.when < today_date).all()
    upcommingPlan = Plan.query.filter(Plan.when > today_date).all()

    completedPlan_dict = dict_helper(completedPlan)
    upcommingPlan_dict = dict_helper(upcommingPlan)
    plans.append(completedPlan_dict)
    plans.append(upcommingPlan_dict)

    return jsonify(plans=plans)
    '''

# DB 연결 부분
db.init_app(app)
db.app = app
db.create_all()

if __name__=='__main__':
    app.run()