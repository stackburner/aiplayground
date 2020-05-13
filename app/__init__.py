from flask import Flask, jsonify, render_template, request
from wtforms import Form, TextAreaField, validators
import pickle
import sqlite3
import os
import numpy as np
from vectorizer import vect
import datetime
import psutil

app = Flask(__name__)
cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'classifier.pkl'), 'rb'))
db = os.path.join(cur_dir, 'moods.sqlite')
domain = 'aiplayground'

def classify(document):
    label = {0: 'negative', 1: 'positive'}
    X = vect.transform([document])
    y = clf.predict(X)[0]
    proba = np.max(clf.predict_proba(X))
    return label[y], proba

def train(document, y):
    X = vect.transform([document])
    clf.partial_fit(X, [y])

def sqlite_entry(path, document, y):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("INSERT INTO moods_db (mood, sentiment, date) VALUES (?, ?, DATETIME('now'))", (document, y))
    conn.commit()
    conn.close()

class ReviewForm(Form):
    mood = TextAreaField('', [validators.DataRequired(), validators.length(min=15, max=500)])

@app.route('/')
def index():
    form = ReviewForm(request.form)
    return render_template('index.html', domain=domain, form=form, system_info_text=get_system_info())

@app.route('/results', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    if request.method == 'POST' and form.validate():
        review = request.form['mood']
        y, proba = classify(review)
        return render_template('results.html', domain=domain, content=review, prediction=y, probability=round(proba*100, 4), system_info_text=get_system_info())
    return render_template('index.html', domain=domain, form=form, system_info_text=get_system_info())

@app.route('/thanks', methods=['POST'])
def feedback():
    feedback = request.form['feedback_button']
    mood = request.form['mood']
    prediction = request.form['prediction']
    inv_label = {'negative': 0, 'positive': 1}
    y = inv_label[prediction]
    if feedback == 'Incorrect':
        y = int(not(y))
    #train(mood, y)
    sqlite_entry(db, mood, y)
    return render_template('thanks.html', domain=domain, system_info_text=get_system_info())

@app.route('/sys_info.json')
def system_info():
    return get_system_info()
    
def get_system_info():
	return 'System Information: [CPU: {0}%] [Memory: {1}%]'.format(str(psutil.cpu_percent()), str(psutil.virtual_memory()[2]))

if __name__ == '__main__':
    app.run(debug=True)