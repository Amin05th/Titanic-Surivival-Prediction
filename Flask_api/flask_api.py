#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd
from flask import Flask, jsonify
from werkzeug.serving import run_simple
import time


# In[53]:


app = Flask(__name__)
df = pd.read_csv("predictions.csv")
data = dict(zip(df["PassengerId"], df["Survived"]))


# In[54]:


@app.route("/")
def index():
    return jsonify(data)


# In[55]:


@app.route("/<id>")
def single_person(id):
    return jsonify({id: data[int(id)]})


# In[56]:


@app.errorhandler(500)
def keyerror(e):
    return jsonify(error=str(e)), {"Refresh": "5; url=/"}


# In[50]:


if __name__ == "__main__":
    run_simple("0.0.0.0",application=app, port=10000, threaded=True)

