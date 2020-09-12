from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename
from detect_glasses import get_details

app=Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
	a = url_for('static', filename= 'img/vislogo.png')
	aa = url_for('static', filename= 'img/img_lights.jpg')
	ca = url_for('static', filename= 'img/img_snow.jpg')
	# return a
	l=[]
	al=[]
	cat_l=[]
	data_dict = {}
	
	for i in range(19):
		l.append(a)
		al.append(aa)
		cat_l.append(ca)

	if request.method == 'POST':
		f = request.files['file']
		name = f.filename
		print(name)
		f.save(secure_filename(f.filename))
		li = get_details(name)
		print(li)
		data_dict = {}
		for i in li:
			data_dict[i[0]]=i[1]

		# x = [str(i[1]) for i in li]
		# txt = '\n'.join(x)
		# return f'{txt}file uploaded successfully'

	return render_template('index.html', img_list=l, all_list=al, result=data_dict, cat_list=cat_l)



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000,debug=True)