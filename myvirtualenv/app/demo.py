import os
import json
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,json,jsonify
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
	

@app.route('/sendServer', methods=['GET','POST'])
def send_as_svg():
        svgStr =  request.form['sendSvg']
        print svgStr
        return render_template('receiveSvg.html',str=svgStr)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return redirect(url_for('uploaded_file',
                                filename=filename))


@app.route('/marchingCube')
def marching_cube():
    return render_template('Marching-Cubes.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # if filename.rsplit('.', 1)[1] == 'vtk':
    #     send_from_directory(app.config['UPLOAD_FOLDER'],
    #                             filename)
    #     return render_template('Marching-Cubes.html')
        

    # else: 
        return send_from_directory(app.config['UPLOAD_FOLDER'],
                                filename)


if __name__ == '__main__':
    app.run(
        debug=True
    )