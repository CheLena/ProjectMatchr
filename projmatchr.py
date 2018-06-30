#import os
#import request
import nltk
import numpy as np
import pandas as pd
import re
import io
import pickle
import gensim
import difflib

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
from difflib import SequenceMatcher as sm
from gensim import corpora
from gensim import models
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import psycopg2
from collections import Counter
from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)


# create a database and query from it
dbname = 'projects_db'
username = 'sugac_000'
pswd = 'Br@sw3ll'
engine = create_engine('postgresql://%s:%s@localhost/%s'%(username,pswd,dbname))
if not database_exists(engine.url):
    create_database(engine.url)

proj_data = pd.read_csv('Project_Title_Data.csv', encoding='latin-1')
proj_data.to_sql('projects_table', engine, if_exists='replace')

con = None
con = psycopg2.connect(database = dbname, user = username, host='localhost',password=pswd)
cur = con.cursor()


@app.route('/')
def home():
    return render_template('input_page.html')
        #'home_page_v2.html',
        #action=[{'name':'Classify'},{'name':'Collect'},{'name':'Find'},
        #       {'name':'Map'},{'name':'Optimize'}, {'name':'Predict'}, {'name':'Recommend'}],
        #topic=[{'name':'Data science'},{'name':'ECommerce'},{'name':'Food/drink'},
        #       {'name':'Housing'},{'name':'Neighborhood'},{'name':'Social media'},{'name':'Sports'},
        #       {'name':'Travel'},{'name':'Other'}])

@app.route("/results" , methods=['GET', 'POST'])
#def query_projects(a, t):
#    cur.execute("SELECT project FROM projects_table WHERE project_action = %s OR project_topic = %s ORDER BY sm_score DESC LIMIT 5",
#       (a+'%', t+'%'))
#    return cur.fetchall()


def results():
#  title_list = []
#  fig_list = []
#  sm_list = []
#  url_list = []

  if request.method == 'POST':
    action = request.form.get("action")
    topic  = request.form.get("topic")

 # query_projects = sql_query(action, topic)

  sql_query = ("""SELECT * FROM projects_table 
    WHERE ((project_topic IN ('%s')) AND (project_action IN ('%s'))) LIMIT 5;""" %(topic, action))
    #ORDER BY sm_score DESC LIMIT 5;""")
  titleSelect = pd.read_sql_query(sql_query,con).drop('index',axis=1)
  title_list= titleSelect['project']
  fig_list = 'static/images/'+titleSelect['image_ext']+'.jpg'
  #sm_list = titleSelect['sm_score']
  url_list = titleSelect['url']

  return render_template('results.html', titleSelect = titleSelect, title=title_list, fig = fig_list, site=url_list)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/slides')
def slides():
    return render_template('slides.html')

if __name__ == '__main__':
	app.run(debug=True)
