# -*- coding:utf-8 -*-
__author__ = '东方鹗'

from flask import render_template, request, jsonify, current_app
from . import advanced
from werkzeug.utils import secure_filename
import os

def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@advanced.route('/delete', methods=['GET', 'POST'])
def delete():
	key = request.form.get('key')
	print(key)

	return jsonify()


@advanced.route('/example_1', methods=['GET', 'POST'])
def example_1():
	return render_template('exam_1.html')


@advanced.route('/example_2', methods=['GET', 'POST'])
def example_2():
	return render_template('exam_2.html')


@advanced.route('/example_5', methods=['GET', 'POST'])
def example_5():
	return render_template('exam_5.html')

@advanced.route('/example_8', methods=['GET', 'POST'])
def example_8():
	return render_template('exam_8.html')


@advanced.route('/example_9', methods=['GET', 'POST'])
def example_9():
	if request.method == 'POST':
		file = request.files['input-2']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
	return render_template('exam_9.html')

@advanced.route('/example_11', methods=['GET', 'POST'])
def example_11():
	return render_template('exam_11.html')
