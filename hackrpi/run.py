from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ru')
def ru():
    return render_template('index.backup.html')
@app.route('/style')
def style():
    return render_template('style.html')
@app.route('/admin')
def admin():
    return render_template('admin.html')
@app.route('/tables.html')
def tables():
    return render_template('tables.html')
@app.route('/charts.html')
def charts():
    return render_template('charts.html')
@app.route('/landing')
def landing():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True)
