# generate FLask API
#

from flask import Flask, render_template
import os
import hashlib

app = Flask(__name__)
pic_folder = os.path.join('static')
app.config['UPLOAD_FOLDER'] = pic_folder


@app.route('/')
def image():
    pic_path = os.path.join(
        app.config['UPLOAD_FOLDER'], 'Flask-API--main\static\index.jpg')
    with open(pic_path, 'rb') as f:
        file_contents = f.read()
        file_md5 = hashlib.md5(file_contents).hexdigest()

    return render_template('index.html', image=pic_path, file_md5=file_md5)


@app.route('/helloworld')
def helloworld():
    return 'HELLO WORLD'


if __name__ == '__main__':
    app.run(debug=True)
