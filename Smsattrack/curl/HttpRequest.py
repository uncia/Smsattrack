#!/usr/bin/env python
# coding=utf-8
__author__ = 'pyphrb'
import requests
import json
import sys
class Http(object):

    def __init__(self, url, mobile, payload, param=None):

        self.__url = url
        self.payload = payload
        self.mobile = mobile
        self.param = param
        self.post_param = None
        self.get_param = None
        self.session = requests.session()
        self.request_param = None
        self.getResponse = None
        self.postRespone = None

    def get_request(self):
        self.get_param = self.payload + self.mobile
        self.request_param = self.__url + self.get_param
        try:
            self.getResponse = requests.get(url=self.request_param)
        except requests.HTTPError as e:
            print(e)
        return self.getResponse.text
    def post_request(self):
        self.post_param = {self.param:self.mobile}
        self.request_param = self.__url + self.payload
        self.postRespone = requests.post(self.request_param, json.dumps(self.post_param))
        return self.postRespone.text

#request = Http("http://member.ync365.com", "13034614731", "/check/getcode?mobile=")
#for i in range(10):
 #   request.get_request()
