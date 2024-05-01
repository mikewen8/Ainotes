import pathlib
import textwrap
import pull 

import google.generativeai as genai
genai.configure(api_key="AIzaSyCUXEfHA5OvN6Y41kEVaOVHPf5ayq8-2oo")
model = genai.GenerativeModel('gemini-pro')

def send_note(doc): 
    response = model.generate_content("Create a summary out of this document:" + doc)
    print(response.text)
    return response.text

testdoc=pull.pull_doc()
send_note(testdoc['Note'])