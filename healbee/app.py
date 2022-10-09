import re
from click import prompt
from flask import Flask, render_template, request
import requests
import os
import cohere
co = cohere.Client('')
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    txt= request.args.get('msg')
    response = co.generate( 
    model='large', 
    prompt='HealBee is a Health Chatbot that talks about eating nutritious food and promoting a healthy lifestyle\nMe: Hi\nHealBee: Hi, I am Healbee\n--\nMe: What do you love?\nHealBee: I love nutritious food\n--\nMe: What are the tips for healthy eating?\nHealBee: Base your meals on higher fiber starchy carbohydrates and Eat lots of fruit and veg\n--\nMe: How can I reduce my fat\nHealBee: Cut down on saturated fat and sugar\n--\nMe:{}\nHealBee: '.format(txt), 
    max_tokens=100, 
    temperature=0.5, 
    k=0, 
    p=0.75, 
    frequency_penalty=0, 
    presence_penalty=0, 
    stop_sequences=["--"], 
    return_likelihoods='NONE') 
    answer = format(response.generations[0].text).strip("--")
    return answer



if __name__ == "__main__":
    app.run()