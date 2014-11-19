from flask import Flask, render_template
from dynamic_query import filteredCluster  
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
def tables():pass
@app.route('/charts.html')
def charts():
    return render_template('charts.html')
@app.route('/landing')
def landing():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True)

def get_paraList():
 
    area = request.args.getlist('tx1')
    peri = request.args.getlist('tx2')
    compactness = request.args.getlist('tx3')
    assym = request.args.getlist('tx4')
    BoundaryIndex = request.args.getlist('tx5')
    contrast = request.args.getlist('tx6')
    energy = request.args.getlist('tx7')
    homogeneity = request.args.getlist('tx8')
    correlation = request.args.getlist('tx9')
    dissimilarity = request.args.getlist('tx10')
    asm = request.args.getlist('tx11')

    #print area
    filteredCluster(area,peri,compactness,assym,BoundaryIndex,contrast,energy,
        homogeneity,correlation,dissimilarity,assym)
     
    #return jsonify(result=a + b)
