from flask import Flask, render_template, url_for
app=Flask(__name__)

@app.route('/')
def index():
	a = url_for('static', filename= 'img/vislogo.png')
	aa = url_for('static', filename= 'img/img_lights.jpg')
	ca = url_for('static', filename= 'img/img_snow.jpg')
	# return a
	l=[]
	al=[]
	cat_l=[]
	dict = {'phy':50,'che':60,'maths':70, 'CSE':95}
	for i in range(19):
		l.append(a)
		al.append(aa)
		cat_l.append(ca)
	return render_template('index.html', img_list=l, all_list=al, result=dict, cat_list=cat_l)

if __name__ == '__main__':
	app.run(debug=True)