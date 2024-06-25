from flask import Flask,render_template
FAI=Flask(__name__)
@FAI.route('/priya')
def priya():
    return 'husband is honey when he gives money'
@FAI.route('/hi')
def hi():
    return render_template('hi.html')
FAI.run(debug=True,host='127.0.0.1',port=5000)