from flask import Flask,render_template,request,url_for,redirect
from summarizer import Text_Summarizer

app = Flask(__name__)

def requestResults(name):
    result = Text_Summarizer(name)
    return result

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['POST','GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['submit']
        return redirect(url_for('success',name=user))

@app.route('/success/<name>')
def success(name):
    return str(requestResults(name))
    
if __name__=='__main__':
    app.debug=True
    app.run()