from flask import Flask,render_template, request 
  
app = Flask(__name__,template_folder="templates") 
  
@app.route("/") 
def hello(): 
    return render_template('index.html') #html doesn't exist yet, needs to be implemented
  
@app.route('/process', methods=['POST']) 
def get_username(): 
    data = request.form.get('data') 
    # process the data using Python code 
    result = data
    return result 

@app.route('/process', methods=['POST']) #Need to change process and Post accordingly to whats in html
def get_password(): 
    data = request.form.get('data') 
    # process the data using Python code 
    result = int(data)
    return str(result) 
  
if __name__ == '__main__': 
    app.run(debug=True) 