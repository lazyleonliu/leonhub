import os
from win32com import client as wc
import docx

import pythoncom


# 在传入的doc文件的路径下另存为一个docx文件
def con_doc_to_docx(file_paths):
    print(file_paths)
    pythoncom.CoInitialize()
    for i in range(len(file_paths)):
        file = os.path.splitext(file_paths[i])
        # print(file[1])
        if file[1] == u'.doc':
            word = wc.Dispatch('kwps.Application')
            doc = word.Documents.Open(file_paths[i])  # 目标路径下的文件
            doc.SaveAs(file_paths[i] + u'x', 12, False, "", True, "", False, False, False, False)
            # 此处会关闭所有当前打开的word文档
            doc.Close()
            word.Quit()
            dele_doc(file_paths[i])
            file_paths[i] = file_paths[i] + u'x'
    return file_paths

def dele_doc(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False


if __name__ == '__main__':
    file_paths = [u"D:\\mygit\leonhub\\bootstrapFileInput-master\\app\lib\\static\\upload\\20200312a7baac84b3c44754b0f78e53cd9b1e4f/stest1.doc",
                  u"D:\\mygit\leonhub\\bootstrapFileInput-master\\app\lib\\static\\upload\\20200312a7baac84b3c44754b0f78e53cd9b1e4f/stest2.docx"]
    con_doc_to_docx(file_paths)

