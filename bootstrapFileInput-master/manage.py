# -*- coding:utf-8 -*-
__author__ = '东方鹗'

import os
from app import create_app
from flask_script import Manager, Shell
from flask_script import Server


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app=app)
manager.add_command( "runserver", Server(host='127.0.0.1', port=5000, use_debugger=True, use_reloader=True))


def make_shell_context():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def test():
    """ 单元测试 """

    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(test=tests)

if __name__ == '__main__':
    manager.run()
