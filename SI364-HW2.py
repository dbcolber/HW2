## HW 2 
## SI 364 F17
## Due: September 24, 2017
## 500 points

#####

## [PROBLEM 1]

## Edit the following Flask application code so that if you run the application locally and go 
# to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number. 
# Once you enter a number and submit it to the form, you should then see a web page that says "Double your 
# favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says 
# "Double your favorite number is 4". Careful about types in your Python code!

## You can assume a user will always enter a number only.

import requests

from flask import Flask, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Hello!'

@app.route('/question')
def ask_question():
	s = """<!DOCTYPE html>
<html>
<body>

<form action="http://localhost:5000/result" method="GET">
  Please enter your favorite number:<br>
  <input type="text" name="number" value="">
  <br><br>
  <input type="submit" value="Submit">
</form> 

</body>
</html>""" 
	return s

@app.route('/result',methods = ['POST', 'GET'])
def res():
    if request.method == 'GET':
        result = request.args
        number1 = result.get('number')
        double = 2 * (int(number1))
        return "<b>" + "Double your favorite {0} is {1}".format(number1, double)

## MY INTERACTIVE DATA EXCHANGE




if __name__ == '__main__':
    app.run()


## [PROBLEM 2]

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, 
## and build it into the above code for a Flask application. 

# It should:
# - not be an exact repeat of something you did in class, but it can be similar
# - should include an HTML form (of any kind: text entry, radio button, checkbox... feel free to try out whatever you want)
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form (text entered, radio button selected, etc). So if a user has to enter a number, it should do an operation on that number. If a user has to select a radio button representing a song name, it should do a search for that song in an API.
# You should feel free to be creative and do something fun for you -- 
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)









