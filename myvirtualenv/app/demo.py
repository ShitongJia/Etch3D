import os
import json
import urlparse
import base64
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
    return render_template('etch3d.html')

# @app.route('/uploadFile')
# def uploadFile():
#     return render_template('index.html')




@app.route('/editor')
def editor():
    return render_template('editor.html')	

@app.route('/sendServer', methods=['GET','POST'])
def send_as_png():
        datauri =  request.form['sendPNG']
       
        up = urlparse.urlparse(datauri)
        head, data = up.path.split(',', 1)
        bits = head.split(';')
        mime_type = bits[0] if bits[0] else 'text/plain'
        charset, b64 = 'ASCII', False
        for bit in bits:
            if bit.startswith('charset='):
                charset = bit[8:]
            elif bit == 'base64':
                b64 = True

        plaindata = data.decode("base64")

        with open('uploads/tmp.png', 'wb') as f:
            f.write(plaindata)


        return render_template('etch3d.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        if filename.rsplit('.', 1)[1] == 'vtk':
            return redirect(url_for('marching_cube',filename=filename))
        else:
            return redirect(url_for('uploaded_file',
                                filename=filename))



@app.route('/marchingCube')
def initial3Dview():
    return render_template('threeDview.html')

@app.route('/marchingCube/<filename>')
def marching_cube(filename):
    return render_template('Marching-Cubes.html',url=app.config['UPLOAD_FOLDER']+filename)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
 
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                            filename)


if __name__ == '__main__':
    app.run(
        debug=True
    )