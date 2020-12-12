from flask import Flask, render_template
#The text above allows you to import the render_template function from the flask module
app = Flask(__name__)

@app.route('/') #This determines the entry point; the / means the root of the website
def index():#This code makes Flask look for index.html in the templates directory that the app.py program is in.
    app.logger.info('user request for home page') #This logger logs when users move to home page
    return render_template('home.html')

@app.route('/Number3')
def sonic(): #This code makes Flask look for index.html in the templates directory that the app.py program is in.
    app.logger.info('user request for sonic page') #This logger logs when users move to sonic page
    return render_template('sonic.html')

@app.route('/Number2')
def zeroSuit():
    app.logger.info('user request for zeroSuit page')
    return render_template('zeroSuit.html')

@app.route('/Number1')
def king():
    app.logger.info('user request for king page')
    return render_template('king.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



