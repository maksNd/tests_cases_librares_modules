from flask import Flask, request, render_template

app = Flask(__name__)


# @app.route('/post')
# def load_page():
#     return render_template('load_form.html')
#
# @app.route('/post_uploaded', methods=['POST'])
# def get_file_from_form():
#     file = request.files.get('file')
#     print(file)
#     print(file.filename)
#     return file.filename


@app.route('/post')
def page_post_form():
    return render_template('post_form.html')


@app.route('/post_uploaded', methods=['POST'])
def page_post_upload():
    picture = request.files.get("picture")
    picture.save(picture.filename)
    return picture.filename


app.run(host='127.0.0.1', port=7777)
