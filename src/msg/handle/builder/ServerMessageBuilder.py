#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

import BaseBuilder


class ServerMessageBuilder(BaseBuilder.BaseBuilder):
    def __init__(self, msgBean, env):
        self.templateFile = "Server-message.template"
        self.genPath = "../out/server/app/service/"
        fileName = "message.js"
        BaseBuilder.BaseBuilder.__init__(self, msgBean, self.templateFile, self.genPath, fileName, env)

    def buildMsgFile(self):
        try:
            # 渲染模板
            stream = self.template.render(msgBeans=self.msgBean)
            # print stream

            # 生成文件
            self.genMsgFile(stream)

            return True
        except Exception, e:
            print e
            return False
