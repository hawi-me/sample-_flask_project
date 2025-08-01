from app import app

@app.route('/')
def Home():
    return "<p>what we this home?</p>"

@app.route('/index')
def index():
    return "<p>what we call it ?</p>"
