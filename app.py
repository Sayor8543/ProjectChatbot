from email import message
from urllib import response
from flask import Flask, render_template,request,jsonify

from chat import get_response

import language_translate_helper

intial_language=""
app=Flask(__name__)

data_1=[{'name':'English'}, {'name':'Hindi'},{'name':'Marathi'}, {'name':'Gujarati'},
{'name':'Kannada'}, {'name':'Malayalam'},{'name':'Odia'}, {'name':'Punjabi'}, 
{'name':'Sindhi'}, {'name':'Tamil'},{'name':'Telugu'}, {'name':'Urdu'}]

@app.get("/")
def index_get():
    with open('language.txt', 'w') as f:
        f.write("English")
    return render_template("base.html",data=data_1)

@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    with open('language.txt', 'w') as f:
        f.write(select)
    data_2=language_translate_helper.drop_down_menu_list(data_1,select)
    return render_template("base.html",data=data_2)


@app.post("/predict")
def predict():
    text=request.get_json().get("message")
    with open('language.txt','r') as f:
        current_language=f.readline()
    
    text_2=language_translate_helper.user_message_language_changer(current_language,text)
    print(text_2)
    
    response= get_response(text_2)

    response_2=language_translate_helper.bot_message_language_changer(current_language,response)
    message={"answer":response_2}

    return jsonify(message)


if __name__ =="__main__" :
    app.run(debug=True)