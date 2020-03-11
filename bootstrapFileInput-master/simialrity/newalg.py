import webbrowser
from docx import Document
import os
import re
from simialrity import SaveJson
import numpy
from flask import g, render_template, request, current_app, redirect, url_for

# 断句
def get_sentence_set(doc_text):
	sentence_set_list = []
	for doc in doc_text:
		reg = r'\n|\t|\r|\0|\v|\f| |[(（]?[\d一二三四五六七八九十A-Za-z]+[）)][、.．．]?|[\d一二三四五六七八九十A-Za-z]+[、.．．]\d*'
		s_list = re.split(r'。|，|!|\?|？|；|······|:|：', re.sub(reg, '', doc))
		sentence_set_list.append(set(s_list))
	return sentence_set_list

# 获取文档的名称和内容
def get_doc_names_texts(files):
	names, texts = [], []
	for file in files:
		doc = Document(file)
		names.append(re.findall(r'[^/]+$', file)[0])
		texts.append(''.join([par.text for par in doc.paragraphs]))

	return names, texts

def simi(files):
	names, docs = get_doc_names_texts(files)
	sentences_set_list = get_sentence_set(docs)
	common_set = sentences_set_list[0]
	for item in sentences_set_list:
		common_set = common_set & item
	sentences_set_list = [item - common_set for item in sentences_set_list]

	# 计算显示的时候点的size 的大小

	# 生成D3.JS的nodes和edges结构
	nodes_len = len(sentences_set_list)
	temp_list, edges_list, nodes_list = [], [], []
	for i in range(nodes_len):
		nodes = {"name": names[i], "size": len(sentences_set_list[i])}
		nodes_list.append(nodes)
		for j in range(nodes_len):
			if i != j and {i, j} not in temp_list:
				temp_list.append({i, j})
				unit_set = sentences_set_list[i] | sentences_set_list[j]
				com_set = sentences_set_list[i] & sentences_set_list[j]
				sim = len(com_set) / len(unit_set)
				sim = round(sim + (0.01 if sim < 0.1 else 0), 2)
				edges = {"source": i, "target": j, "value": sim,
						 "sim_text": round(len(com_set) / len(unit_set) * 100, 2)}
				edges_list.append(edges)
	resp_data = {}
	resp_data['edges'] = edges_list
	resp_data['nodes'] = nodes_list
	return resp_data
