#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

import os
import shutil

from jinja2 import *

from src.msg.handle.builder import *


# 消息文件生成
def MsgFileBuild(temPath, messageBeans):
    # 加载模板文件
    env = Environment(loader=FileSystemLoader(temPath))
    # print env.list_templates()

    # 清空并重新生成 消息生成目录
    outPath = "../out"
    if os.path.exists(outPath):
        shutil.rmtree(outPath)
        os.makedirs(outPath)

    # 循环所有消息结构
    builder = None
    for msgBean in messageBeans:
        # 服务端消息生成
        if "CS" == msgBean.typeCS:
            builder = ServerLogicBuilder.ServerLogicBuilder(msgBean, env)
            if not builder.buildMsgFile():
                print "server msgbuild error in ServerLogicBuilder, msgName = " + msgBean.cmd

        builder = ServerMsgModelBuilder.ServerMsgModelBuilder(msgBean, env)
        if not builder.buildMsgFile():
            print "server msgbuild error in ServerMsgModelBuilder, msgName = " + msgBean.cmd


    # 服务端message.lua
    builder = ServerMessageBuilder.ServerMessageBuilder(messageBeans, env)
    if not builder.buildMsgFile():
        print "server msgbuild error in ServerMessageBuilder, message.js"

    # 服务端MessageType.js
    builder = ServerMsgTypeBuilder.ServerMsgTypeBuilder(messageBeans, env)
    if not builder.buildMsgFile():
        print "server msgbuild error in ServerMsgTypeBuilder, MessageType.js"

    # 服务端MessageAuth.js
    builder = ServerMsgAuthBuilder.ServerMsgAuthBuilder(messageBeans, env)
    if not builder.buildMsgFile():
        print "server msgbuild error in ServerMsgAuthBuilder, MessageAuth.js"

    # 客户端端MessageType.js
    builder = ClientMsgTypeBuilder.ClientMsgTypeBuilder(messageBeans, env)
    if not builder.buildMsgFile():
        print "server msgbuild error in ClientMsgTypeBuilder, MessageType.js"

    # 客户端端reqMsg.js
    builder = ClientReqMsgBuilder.ClientReqMsgBuilder(messageBeans, env)
    if not builder.buildMsgFile():
        print "server msgbuild error in ClientReqMsgBuilder, reqMsg.js"

