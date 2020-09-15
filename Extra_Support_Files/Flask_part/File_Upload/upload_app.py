from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from detect_glasses import get_details

app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      name = f.filename
      print(name)
      f.save(secure_filename(f.filename))
      li = get_details(name)
      print(li)
      x = [str(i[1]) for i in li]
      txt = '\n'.join(x)
      return f'{txt}file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)