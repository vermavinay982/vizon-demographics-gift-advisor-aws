from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename
from detect_glasses import get_details
from give_image_paths import suggest_folder
import os
import glob
app=Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
	a = url_for('static', filename= 'img/vislogo.png')
	aa = url_for('static', filename= 'img/img_lights.jpg')
	ca = url_for('static', filename= 'img/img_snow.jpg')
	# return a
	recomm_files=[]
	al=[]
	cat_l=[]
	data_dict = {}
	target = a
	for i in range(19):
		recomm_files.append(a)
		al.append(aa)
		cat_l.append(ca)

	prefix='static/assets'
	all_file=[]
	for filename in glob.iglob(prefix+'/**/*.jpg',recursive = True):
		all_file.append(filename)
		# print(filename)


	if request.method == 'POST':
		f = request.files['file']
		name = f.filename
		print(name)
		f.save(secure_filename(f.filename))
		data_dict = get_details(name)
		recomm_files=suggest_folder(data_dict)

		target = url_for('static', filename= name)[1:]
		try:
			os.rename(name,target)
		except:
			pass
		# x = [str(i[1]) for i in li]
		# txt = '\n'.join(x)
		# return f'{txt}file uploaded successfully'

	return render_template('index.html', img_upl=target, img_list=recomm_files, all_list=all_file, result=data_dict, cat_list=cat_l)



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000,debug=True)