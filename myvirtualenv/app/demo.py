import os

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = 'uploads/'

app.config['ALLOWED_EXTENSIONS'] = set(['svg', 'vtk', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/editor')
def editor():
	return render_template('editor.html')
	

@app.route('/save',methods=['GET','POST'])
def save_as_svg():
	data = request.form['data']
	output_format = request.form['outpur_format']
	filename = secure_filename(file.filename)
	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	

@app.route('/upload', methods=['GET','POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return redirect(url_for('uploaded_file',
                                filename=filename))

@app.route('/uploads/<filename>')
def uploadedSVG_file(filename):
    if filename.rsplit('.', 1)[1] == 'vtk':
        return render_template('loadVTK.html',filename)

    else: 
        return send_from_directory(app.config['UPLOAD_FOLDER'],
                                filename)





if __name__ == '__main__':
    app.run(
        debug=True
    )