import datetime
import json
import sys
import flask
import sqlite3

app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return flask.render_template('index.html')

@app.route('/recentData', methods=["GET"])
def getRecentData():

    return flask.jsonify(data)


@app.route('/evaluate', methods=["POST"])
def evaluate():
    contents = json.loads(request.data.decode("utf-8"))
    time = str(datetime.datetime.now())
    expression = contents['expression']    
    conn = sqlite3.connect('expressions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE expressions(
        expression text,
        solution text,
        time text
        )
        ''')
    c.execute('INSERT into expressions({},{},{})'.format(expression, execute(expression), time) )
    conn.commit()
    conn.close()
    return flask.jsonify(_success())

def _success():
    return {"status_code": 200, "text": "Success!"}

def execute(str):
    if str[-1] in '+-*/':
        str = str[:-2]
    

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
