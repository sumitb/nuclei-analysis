from flask import Flask, render_template
import analysis
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/m')
def indexm():
    return render_template('indexm.html')
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
@app.route('/charts.html')
def charts():
    return render_template('charts.html')
@app.route('/landing')
def landing():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True)

def get_paraList():
    paraList = []
    paraList0 = ['Area','50','100'] #request.args.get('area','min','max', type=int)
    paraList1 = ['para','20', '50'] #.args.get('para','min','max', type=int)
    for i in range(1):  #range(10)
    	paraList.append(paraList+str(i))
   """a = request.args.get('a', 0, type=int)
   b = request.args.get('b', 0, type=int)
   a = request.args.get('a', 0, type=int)
   b = request.args.get('b', 0, type=int)
   a = request.args.get('a', 0, type=int)
   b = request.args.get('b', 0, type=int)
   a = request.args.get('a', 0, type=int)
   b = request.args.get('b', 0, type=int)
   a = request.args.get('a', 0, type=int)"""
   #f is path of allfeaturefile.csv
    filteredCluster(paraList) 
   #return jsonify(result=a + b)
