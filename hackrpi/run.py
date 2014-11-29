from flask import Flask, render_template, request
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

@app.route('/feature_select', methods=['POST'])
def feature_select():
	from dynamic_query import filteredCluster

	print "I'm here!"
	if request.method == 'POST':
		print "POST method"
	featureList = request.form.get('featureList', '')
	featureList = featureList.split(";")
	featureList.pop()
	featureStr = []
	for flist in featureList:
		attrib = flist.split(",")
		print float(attrib[0]), float(attrib[1])
		featureStr.append([float(attrib[0]), float(attrib[1])])
	#for f in featureStr:
	#pass
	#print f, type(f)
	#featureValue.append([int(f[0]), int(f[1])])
	print featureStr
	filteredCluster(featureStr)
	#return jsonify(result=a + b)
	return None

if __name__ == '__main__':
	print "hello"
	app.run(debug=True)