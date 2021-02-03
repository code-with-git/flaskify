from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'magnewskey'

@app.route('/')
def home():
    return "Hello, World!"