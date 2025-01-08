from flask import Flask,render_template,request

app = Flask(__name__)



@app.route("/") #Decorater
def home ():
 data = [
      {'name':'shalu','age':20},
      {'name':'shreya','age':'19'},
      {'name':'anchal','age':'24'},
      {'name':'anish','age':'18'}
 ]
 return render_template('index.html', data=data)


@app.route("/contact", methods=['GET','POST'])
def contact():
   data={}
   if request.method='POST':
       data=request.form
   return render_template("contact.html",data=data)    

