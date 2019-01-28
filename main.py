import datetime
import json
import sys
import flask
import sqlite3

app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return flask.render_template('index.html')

@app.route('/recent_data', methods=["GET"])
def getRecentData():
    data = get10()
    return flask.jsonify(data)


@app.route('/evaluate', methods=["POST"])
def evaluate():
    contents = json.loads(flask.request.data.decode("utf-8"))
    time = str(datetime.datetime.now())
    expression = contents['expression']
    insert(expression)
    return flask.jsonify(get10())

def _success():
    return {"status_code": 200, "text": "Success!"}


def get10():
    conn = sqlite3.connect('expressions.db')
    c = conn.cursor()
    c.execute(''' SELECT expression from expressions order by time DESC limit 10''')
    returnme = []
    for a in c.fetchall():
        returnme.append(a[0])
    conn.close()
    return returnme

def insert(expr):
    ans = 0
    try:
        ans = eval(expr)
    except:
        ans = 'division by zero'
    time = str(datetime.datetime.now())
    display = "{} = {}".format(expr, ans)
    conn = sqlite3.connect('expressions.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE expressions
             (expression text, time text)''')
    except:
        print('press f')
    c.execute("INSERT INTO expressions VALUES ('{}','{}');".format(display, time) )
    conn.commit()
    conn.close()


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
