import re
from click import prompt
from flask import Flask, render_template, request
import requests
import os
import cohere
co = cohere.Client('')



app = Flask(__name__)



@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        txt = request.form['text']
        response = co.generate( 
        model='large', 
        prompt='This program will extract the ingredients from the Infomation given by the customer.\n--\nCustomer:What should I make I got tomatoes and some flour.\nBot:Tomatoes,Flour\n--\nCustomer:I have some potatoes\nBot: Potatoes\n\n--\nCustomer:{}\nBot:'.format(txt), 
        max_tokens=100, 
        temperature=0, 
        k=0, 
        p=1, 
        frequency_penalty=0, 
        presence_penalty=0, 
        stop_sequences=["--"], 
        return_likelihoods='NONE')
        foodingredients=format(response.generations[0].text).strip("--")
        apikey = ""
        webquery= ("https://api.spoonacular.com/recipes/findByIngredients?apiKey="+apikey+"&"+"ingredients="+foodingredients+"&number=1")  
        response1 = requests.get(webquery)
        respjson=  response1.json() 
        name = str(respjson[0]['title'])
        imgurl = str(respjson[0]['image'])
        recipeurl="https://www.google.com/search?q="+name+"  "+"recipe"

        

    return render_template('index.html', **locals())