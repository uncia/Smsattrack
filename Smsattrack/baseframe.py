#!/usr/bin/env python
# coding=utf-8
# code by china bitch army
__author__ = 'pyphrb'
__qq__ = 959297822
from pprint import pprint
from optparse import OptionParser, OptionGroup
from curl import HttpRequest

SMS_BOMBING = \
    "just for sms bombing the style copy beebeeto just use the tools thank my girl friend"

class SmsFrame(object):
    sms_exp = {
        'exp': {
            'name': None,
            'author': 'SMS_BOMBING',
            'create_time': '2014-12-11'
        }
    }
    def __init__(self, shell=True):
        if shell:
            self.shell = shell

    def _init_parser(self, do_parse=True):
        self.parser = OptionParser()
        self.parser.add_option("-m", "--mobile", action="store_true", dest="mobile", default=None,\
                               help="attack user mobile number")
        if do_parse:
            (self.options, self.args) = self.parser.parse_args()
            if not self.options.mobile:
                self.parser.print_help()
                return False
            else:
                return True
    def run(self):
        if self._init_parser():
            self.verify(self.args[0])

    def verify(self, mobile):
        #self.request = HttpRequest.Http("http://member.ync365.com", "13034614731", "/check/getcode?mobile=")
        #if "\"ok\":\"1\"" in self.request.get_request():
        #    print 'attack success send a spam message' + 'to' + self.args[0]
        pass

if __name__ == "__main__":
    print(SmsFrame.run())