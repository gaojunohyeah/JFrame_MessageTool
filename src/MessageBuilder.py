#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

import sys
sys.path.append("..")

from src.msg.handle import *


# 消息路径
messagePath = "../config"
# 模板路径
templatePath = "../template"

# 获取传入的参数
if (len(sys.argv) == 2):
    messagePath = str(sys.argv[1])

# 修改默认编码格式
reload(sys)
sys.setdefaultencoding('utf8')

print "-------------message build start-------------"
# 读取消息配置表
messageBeans = MsgXmlRead.loadMsgXML(messagePath)
# print messageBeans

# 加载模板文件
MsgTemRead.MsgFileBuild(templatePath, messageBeans)

print "--------------message build end--------------"
