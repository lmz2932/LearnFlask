# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


# 尽量编写带拖尾/的URL
@app.route('/hello/')
def hello():
    return 'Hello world!'


# <variablename>接受不包含/的字符串，遇到/会截断
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


# <int:v>接受整型参数
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


# <string:v>接受不包含/的字符串，遇到/会截断
@app.route('/username/<string:username>')
def show_username(username):
    return 'Username %s' % username


# <float:v>接受浮点型参数
@app.route('/weight/<float:weight>')
def show_weight(weight):
    return 'Weight %.2f' % weight


# <path:v>接受字符串，遇到/不会截断
@app.route('/path/<path:directory>')
def show_directory(directory):
    return 'Path /%s' % directory


# <uuid:v>接受一个uuid字符串
@app.route('/request_id/<uuid:id>')
def show_request_id(id):
    return 'Request id: %s' % id


# <any:(v1, v2)>接受列表中的值，列表外的不接受
@app.route('/member/<any("mars", "suson"):member_name>')
def show_member(member_name):
    return 'Member: %s' % member_name
