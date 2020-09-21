from flask import current_app as app, render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/whatwedo')
def whatwedo():
    return render_template('whatwedo.html')

@app.route('/wherewework')
def wherewework():
    return render_template('wherewework.html')

@app.route('/whoweare')
def whoweare():
    return render_template('whoweare.html')

@app.route('/attorneys')
def attorneys():
    return render_template('attorneys.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/news')
def news():
    return render_template('news.html')