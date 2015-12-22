#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

import BaseBuilder


class ClientMsgTypeBuilder(BaseBuilder.BaseBuilder):
    def __init__(self, msgBean, env):
        self.templateFile = "Client-msgType.template"
        self.genPath = "../out/client/www/js/enum/"
        fileName = "Enum_MsgType.js"
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
