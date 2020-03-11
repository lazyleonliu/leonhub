# -*- coding:utf-8 -*-
__author__ = '东方鹗'

from flask import render_template, request, current_app, redirect, url_for
from . import basic
from werkzeug.utils import secure_filename
import os,stat,uuid
import datetime
from simialrity import newalg


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['docx', 'doc'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# 利用 file input 属性控制相关选项,如本例可实现多文件上传,但不显示上传按钮
@basic.route('/example_3', methods=['GET', 'POST'])
def example_3():
    if request.method == 'POST':
        file = request.files['input-2']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
    return render_template('learnd3.html')

# 设置为单按钮并隐藏文件选择输入框,在上传时显示上传等待图标
@basic.route('/example_5', methods=['GET', 'POST'])
def example_5():
    if request.method == 'POST':
        files = request.files.getlist('input-5[]')
        saved_files = []
        file_dir = datetime.datetime.now().strftime("%Y%m%d") + str(uuid.uuid4()).replace("-", "")
        save_dir = current_app.config['UPLOAD_FOLDER'] + file_dir
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                if not os.path.exists(save_dir):
                    os.mkdir(save_dir)
                    os.chmod(save_dir, stat.S_IRWXU | stat.S_IRGRP | stat.S_IRWXO)
                file.save("{0}/{1}".format(save_dir, filename))
                # file.save(os.path.join(save_dir, filename))
                saved_files.append(save_dir + '/' + filename)
        resp_data = newalg.simi(saved_files)
        return render_template('learnd3.html',resp_data=resp_data)
    else:
        return render_template('example_5.html')

@basic.route('/example_7', methods=['GET', 'POST'])
def example_7():
    if request.method == 'POST':
        files = request.files.getlist('input-7[]')
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    return render_template('example_7.html')