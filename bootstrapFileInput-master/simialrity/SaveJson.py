import os
import json


class SaveJson(object):

    def save_file(self, path, item):

        # 先将字典对象转化为可写入文本的字符串
        item = json.dumps(item, ensure_ascii=False)
        print(item)

        try:
            with open(path, "w+", encoding='utf-8') as f:
                f.seek(0)
                f.truncate()
                f.write("var message = " + item + "\n")
                print("^_^ write success")
            return True
        except Exception as e:
            print("write error==>", e)


if __name__ == '__main__':
    # 保存的文件名
    path = "test1.json"
    # 案例字典数据
    item = {"ID": "1001", "name": "Lattesea",
            "age": "21",
            "date": "1998-01-18", "sex": "男"}

    s = SaveJson()

    # 测试代码，循环写入三行，没有空行
    for i in range(3):
        s.save_file(path, item)