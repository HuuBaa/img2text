# -*- coding: utf-8 -*-
from flask import render_template,Flask,request,make_response,send_file
from image2text import image2text
import StringIO

from wtforms import SubmitField,IntegerField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from config import config



app=Flask(__name__)
csrf = CSRFProtect(app)
bootstrap=Bootstrap(app)
app.config.from_object(config)
app.debug=True

class UploadForm(FlaskForm):
    upload=FileField(u'选择图片',validators=[
            FileRequired(),
            FileAllowed(['jpg', 'jpe', 'jpeg', 'png', 'gif', 'svg', 'bmp'],message=u'请上传图片')
        ])
    width=IntegerField(u'字符画宽(横向字符数,纵向自适应)',default=90)
    submit=SubmitField(u'转换成字符画')


@app.route('/',methods=['POST','GET'])
def index():
    form=UploadForm()
    txts=''
    if form.validate_on_submit():
        f=form.upload.data
        width=form.width.data
        img=f.read()
        imgs=StringIO.StringIO(img)
        txts=image2text(imgs,int(width))

    return render_template('index.html',form=form,txts=txts)

