from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/feature_select', methods=['POST'])
def feature_select():
	from dynamic_query import filteredCluster

	if request.method == 'POST':
		print "POST Method"
	
	featureList = request.form.get('featureList', '')
	featureList = featureList.split(";")
	featureList.pop()
	featureStr = []
	print "Reached flist", featureList
	for flist in featureList:
		attrib = flist.split(",")
		if attrib[1] == '0.001' or attrib[1] == '1.001':
			featureStr.append(None)
		else:	
			featureStr.append([float(attrib[0]), float(attrib[1])])
	#for f in featureStr:
	#pass
	#print f, type(f)
	#featureValue.append([int(f[0]), int(f[1])])
	print "FeatureString: ", featureStr
        dataDir = "/home/sumit/nuclei/data"
        imgPath = "TCGA-02-0010-01Z-00-DX4.07de2e55-a8fe-40ee-9e98-bcb78050b9f7.004096.000000"
	filteredCluster(featureStr, imgPath, dataDir)
	return 'OK'

if __name__ == '__main__':
	app.run(debug=True)
