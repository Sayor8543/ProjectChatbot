from googletrans import Translator

translator = Translator()


def en_to_hi (string):
    out=translator.translate(string, dest='hi',src='en')
    return (out.text)

def hi_to_en (string):
    out=translator.translate(string, dest='en',src='hi')
    return (out.text)

def en_to_bn (string):
    out=translator.translate(string, dest='bn',src='en')
    return (out.text)

def bn_to_en (string):
    out=translator.translate(string, dest='en',src='bn')
    return (out.text)

def en_to_gu (string):
    out=translator.translate(string, dest='gu',src='en')
    return (out.text)

def gu_to_en (string):
    out=translator.translate(string, dest='en',src='gu')
    return (out.text)

def en_to_kn (string):
    out=translator.translate(string, dest='kn',src='en')
    return (out.text)

def kn_to_en (string):
    out=translator.translate(string, dest='en',src='kn')
    return (out.text)

def en_to_ml (string):
    out=translator.translate(string, dest='ml',src='en')
    return (out.text)

def ml_to_en (string):
    out=translator.translate(string, dest='en',src='ml')
    return (out.text)

def en_to_mr (string):
    out=translator.translate(string, dest='mr',src='en')
    return (out.text)

def mr_to_en (string):
    out=translator.translate(string, dest='en',src='mr')
    return (out.text)

def en_to_or (string):
    out=translator.translate(string, dest='or',src='en')
    return (out.text)

def or_to_en (string):
    out=translator.translate(string, dest='en',src='or')
    return (out.text)

def en_to_pa (string):
    out=translator.translate(string, dest='pa',src='en')
    return (out.text)

def pa_to_en (string):
    out=translator.translate(string, dest='en',src='pa')
    return (out.text)

def en_to_sd (string):
    out=translator.translate(string, dest='sd',src='en')
    return (out.text)

def sd_to_en (string):
    out=translator.translate(string, dest='en',src='sd')
    return (out.text)

def en_to_ta (string):
    out=translator.translate(string, dest='ta',src='en')
    return (out.text)

def ta_to_en (string):
    out=translator.translate(string, dest='en',src='ta')
    return (out.text)


def en_to_te (string):
    out=translator.translate(string, dest='te',src='en')
    return (out.text)

def te_to_en (string):
    out=translator.translate(string, dest='en',src='te')
    return (out.text)


def en_to_ur (string):
    out=translator.translate(string, dest='ur',src='en')
    return (out.text)

def ur_to_en (string):
    out=translator.translate(string, dest='en',src='ur')
    return (out.text)

# result = translator.translate('Mikä on nimesi', src='fi', dest='fr')

# print(result.src)
# print(result.dest)
# print(result.text)


data_1=[{'name':'English'}, {'name':'Hindi'},{'name':'Marathi'}, {'name':'Gujarati'},
{'name':'Kannada'}, {'name':'Malayalam'},{'name':'Odia'}, {'name':'Punjabi'},
{'name':'Sindhi'}, {'name':'Tamil'},{'name':'Telugu'}, {'name':'Urdu'}]


selected='Sindhi'



def drop_down_menu_list(data_list,selected_language):
    for index,element in enumerate(data_list):
        if element=={'name':selected_language}:
            data_list.pop(index)

    data_list.insert(0,{'name':selected_language})
    return data_list

data_1=[{'name':'English'}, {'name':'Hindi'},{'name':'Marathi'}, {'name':'Gujarati'},
{'name':'Kannada'}, {'name':'Malayalam'},{'name':'Odia'}, {'name':'Punjabi'},
{'name':'Sindhi'}, {'name':'Tamil'},{'name':'Telugu'}, {'name':'Urdu'}]

def bot_message_language_changer(current_language,bot_message):
    if current_language=="English" :
        return bot_message
    elif current_language=="Hindi" :
        return (en_to_hi(bot_message))
    elif current_language=="Gujarati" :
        return (en_to_gu(bot_message))
    elif current_language=="Marathi" :
        return (en_to_mr(bot_message))
    elif current_language=="Kannada" :
        return (en_to_kn(bot_message))
    elif current_language=="Malayalam":
        return (en_to_ml(bot_message))
    elif current_language=="Odia" :
        return (en_to_or(bot_message))
    elif current_language=="Punjabi" :
        return (en_to_pa(bot_message))
    elif current_language=="Sindhi" :
        return (en_to_sd(bot_message))
    elif current_language=="Tamil" :
        return (en_to_ta(bot_message))
    elif current_language=="Telugu" :
        return (en_to_te(bot_message))  
    elif current_language=="Urdu" :
        return (en_to_ur(bot_message))


def user_message_language_changer(current_language,user_text):
    if current_language=="English" :
        return user_text
    elif current_language=="Hindi" :
        return (hi_to_en(user_text))
    elif current_language=="Gujarati" :
        return (gu_to_en(user_text))
    elif current_language=="Marathi" :
        return (mr_to_en(user_text))
    elif current_language=="Kannada" :
        return (kn_to_en(user_text))
    elif current_language=="Malayalam":
        return (ml_to_en(user_text))
    elif current_language=="Odia" :
        return (or_to_en(user_text))
    elif current_language=="Punjabi" :
        return (pa_to_en(user_text))
    elif current_language=="Sindhi" :
        return (sd_to_en(user_text))
    elif current_language=="Tamil" :
        return (ta_to_en(user_text))
    elif current_language=="Telugu" :
        return (te_to_en(user_text))
    elif current_language=="Urdu" :
        return (ur_to_en(user_text))
