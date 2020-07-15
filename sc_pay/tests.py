from django.test import TestCase



# 添加片源路径 /filmPositive/addInfo
# {
#   "positiveTitleValue": 111111111,
#   "format": 123,
#   "positiveTitle": "string",
#   "movieName": "string",
#   "movieEnName": "string",
#   "trailerUrl": "string",
#   "trailerLength": 123,
#   "type": 123,
#   "movieSubtitle": 123,
#   "movieLanguage": 123,
#   "isNarrator": 123,
#   "videoTime": 123,
#   "audioIds": [
#     "123",
#     "321"
#   ],
#   "positiveList": [
#     {
#       "positiveId": 123,
#       "format": 123,
#       "kdmMovieId": 111111111111,
#       "movieUuid": "string",
#       "keyId": "string",
#       "codeType": 123,
#       "clarity": 123,
#       "clarityDesc": "string",
#       "url": "string",
#       "mapUrl": "string",
#       "movieSize": 1111111111,
#       "encryptedType": 123,
#       "zs": "string",
#       "qxd": "string"
#     },
#     {
#       "positiveId": 123,
#       "format": 123,
#       "kdmMovieId": 111111111111,
#       "movieUuid": "string",
#       "keyId": "string",
#       "codeType": 123,
#       "clarity": 123,
#       "clarityDesc": "string",
#       "url": "string",
#       "mapUrl": "string",
#       "movieSize": 1111111111,
#       "encryptedType": 123,
#       "zs": "string",
#       "qxd": "string"
#     }
#   ],
#   "screenType": 123,
#   "showChangeBtn": 123,
#   "encryptedType": 123
# }

import requests


url ="http://media-manage-test.smartcinemausa.com"

body = {"positiveTitleValue":0,"kdmMovieId":1,"filmId":11,"videoSeconds":1000,"movieSubtitle":3,"movieLanguage":4,"narratorTitle":"","audioId":"117","positiveTitle":"四个正片标题必须一样","isNarrator":"3","type":"0","screenType":1,"showChangeBtn":0,
        "streamList":[]}



# Create your tests here.
