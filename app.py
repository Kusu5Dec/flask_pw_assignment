from flask import Flask,render_template,request
app=Flask(__name__)

#------------------------------------------------------------------------------------------------------------------------------------


#question 1:


@app.route('/')
def text():
    return "hello world!"
@app.route('/test')
def system():
    return "hello kusum"


#------------------------------------------------------------------------------------------------------------------------------


#question 2:


@app.route('/firsts')
def first():
    return render_template("page1.html")
@app.route('/second')
def second_page():
     return render_template("page2.html")



#----------------------------------------------------------------------------------------------------------------------------------

#question 3:

@app.route('/static')
def statics():
    return "this is static url"
@app.route('/dynamic/<url>/<text>')
def dyn(url,text):
     return render_template("dynamic.html",URL=url,text=text)
 
 
#------------------------------------------------------------------------------------------------------------------------------------------------ 


#question 4:


@app.route('/user_input',methods = ['POST','GET'])
def user():
    form_data =""
    if request.method == 'POST':
        form_data= request.form['Name']
    return render_template('form.html',form_data=form_data)
    

        
   

 
 

