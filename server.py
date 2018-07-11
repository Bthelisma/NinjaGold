from flask import Flask, render_template, redirect, session,request
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'MySecret'


@app.route('/')
def ninjas():
    # if session.get('totalGoldCount') == None:
    if "totalGoldCount" not in session:
       session['totalGoldCount'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('ninjas.html')

@app.route('/process_money', methods=['POST'])
def process():

    if request.form ['building']== 'farm':
        goldmade = random.randint(10,21)
        # session['totalGoldCount'] += goldmade
        # time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
    elif request.form['building'] == 'cave':
        goldmade = random.randint(5,10)
    elif request.form['building'] == 'house':
        goldmade = random.randint(2,5)
    else:
        request.form['building'] == 'casino'
        goldmade = random.randint(-50,50)

    session['totalGoldCount'] += goldmade
    time = datetime.now().strftime("%Y/%m/%d %I:%M %p")

    if goldmade > 0:
        activity = "Earned {} at the {}! {}".format(goldmade, request.form['building'], time)
        print activity, "+"*50
    else:
        activity = "Entered a {} and lost {} gold ...Ouch".format(request.form['building'], -1 * goldmade)
        print activity, "-"*50
    session['activities'].append(activity)
    return redirect('/')



app.run(port=8000, debug=True)
