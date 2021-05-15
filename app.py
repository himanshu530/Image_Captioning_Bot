from flask import Flask, render_template,redirect, request

import caption_it

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def predict_cap():
    if request.method == 'POST':
        f = request.files['userfile']
        path = "static/{}".format(f.filename)
        f.save(path)
        caption = caption_it.caption_this_image(path)

        result_dict = {
            'image' : path
            'caption' : caption
        }

    return render_template("index.html",dict = result_dict)

if __name__ == '__main__':
    app.run(debug=True)

