from flask import Flask, render_template, url_for, request, redirect
from gtts import gTTS
from caption import *
import warnings
warnings.filterwarnings("ignore")



app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
     img = request.files['image']

    # print(img)
    # print(img.filename)

     img.save("static/"+img.filename)


     caption = caption_this_image("static/"+img.filename)


     result_dic = {
     'image' : "static/" + img.filename,
     'description' : caption
     }

     song=gTTS(caption)
     song.save("static/"+img.filename+".mp3")
    return render_template('index.html', results = result_dic,songs=img.filename+".mp3")



if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.run(debug = False)
