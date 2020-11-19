# -*- coding:utf-8 -*-

"""
    专场业务上线聚合
"""

import requests
import json
from testTools.utils.releasefilm import goodsEditSkuEnvironment,goodsEditSkuExamine,goodsEditSkuChannel,goodsEditSkuGoodsStatus,goodsUpdateSku,req_url

from testTools.utils.releasefilm import getTimes


def getPreProSpuList(regionId):
    """
    :param regionId:
    :return:
    """
    reqUrl = req_url('goods', "/spu/getPreProSpuList")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': str(regionId),
    }
    body = json.dumps(
        {
            "filmName": "",
            "type": 1
        }
    )

    result = requests.post(url=url,headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ

def getRoomData(regionId):
    """
    :param regionId:
    :return:
    """
    reqUrl = req_url('activity', "/inner/activity/getRoomData")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'X-Region-Id': str(regionId),
    }
    body = {
        "size": 20,
        "page": 1,
        'status': 0,
        'filmId': 4932917517541910,
        'filmName':'',
        'type':1,
        'begin': "",
        'end': "",
        'userName': "",
        'onlineStatus':0,
    }

    result = requests.get(url=url,headers=headers,params=body)
    resultJ = json.loads(result.content)
    return resultJ

def editRoom(specialName,regionId,startTime):
    """
    :param specialName:
    :param regionId:
    :param startTime:
    :return:
    """
    reqUrl = req_url('activity', "/inner/activity/editRoom")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': str(regionId),
    }
    body = json.dumps(
        {
            "international": {
                "ko_KR": {
                    "name": "测试-" + specialName,
                    "warmVoiceRecord": "",
                    "backPictureUrl": "https://g.smartcinemausa.com/images/f27d83b8088042fbaffc3141950989d4-700-466.jpg",
                    "activityImgUrl": "https://g.smartcinemausa.com/images/cdf8e8668a3841088f1e4f9ee669bfff-700-466.jpg",
                    "remark": "한글 은 테스트 에 사용 되 는 데 이 터 를 장의 별로 의미 있 는 표현 이 아니다.",
                    "filmName": "한국어北美测试全10分钟",
                    "spuReleaseEndtime": 1659235477,
                    "spuReleaseStartTime": 1591843477,
                    "spuId": "RXSiDR7t5JOVvjF",
                    "filmId": 4953006427116602,
                    "userName": "비행기 에 익숙 한 손님",
                    "userRemark": "비행기 에 익숙 한 손님",
                    "userImage": "",
                    "userId": 532,
                    "drawerList": []
                },
                "zh_TW": {
                    "name": "测试-" + specialName,
                    "warmVoiceRecord": "",
                    "backPictureUrl": "https://g.smartcinemausa.com/images/f27d83b8088042fbaffc3141950989d4-700-466.jpg",
                    "activityImgUrl": "https://g.smartcinemausa.com/images/cdf8e8668a3841088f1e4f9ee669bfff-700-466.jpg",
                    "remark": "한글 은 테스트 에 사용 되 는 데 이 터 를 장의 별로 의미 있 는 표현 이 아니다.",
                    "filmName": "한국어北美测试全10分钟",
                    "spuReleaseEndtime": 1659235477,
                    "spuReleaseStartTime": 1591843477,
                    "spuId": "RXSiDR7t5JOVvjF",
                    "filmId": 4953006427116602,
                    "userName": "비행기 에 익숙 한 손님",
                    "userRemark": "비행기 에 익숙 한 손님",
                    "userImage": "",
                    "userId": 532,
                    "drawerList": []
                },
                "zh_CN": {
                    "name": "测试-" + specialName,
                    "warmVoiceRecord": "",
                    "backPictureUrl": "https://g.smartcinemausa.com/images/f27d83b8088042fbaffc3141950989d4-700-466.jpg",
                    "activityImgUrl": "https://g.smartcinemausa.com/images/cdf8e8668a3841088f1e4f9ee669bfff-700-466.jpg",
                    "remark": "简体场次描述用来测试的数据，不是很有意义的一段语言描述",
                    "filmName": "한국어北美测试全10分钟",
                    "spuReleaseEndtime": 1659235477,
                    "spuReleaseStartTime": 1591843477,
                    "spuId": "RXSiDR7t5JOVvjF",
                    "filmId": 4953006427116602,
                    "userName": "비행기 에 익숙 한 손님",
                    "userRemark": "비행기 에 익숙 한 손님",
                    "userImage": "",
                    "userId": 532,
                    "drawerList": []
                },
                "en_US": {
                    "name": "测试-" + specialName,
                    "warmVoiceRecord": "",
                    "backPictureUrl": "https://g.smartcinemausa.com/images/f27d83b8088042fbaffc3141950989d4-700-466.jpg",
                    "activityImgUrl": "https://g.smartcinemausa.com/images/cdf8e8668a3841088f1e4f9ee669bfff-700-466.jpg",
                    "remark": "Korean session description is used to test the data, not a very meaningful language description",
                    "filmName": "testSource测试影片影迷",
                    "spuReleaseEndtime": 1596211199,
                    "spuReleaseStartTime": 1590940800,
                    "spuId": "UFrLVfOc3t0BPZe",
                    "filmId": 4932917517541910,
                    "userName": "비행기 에 익숙 한 손님",
                    "userRemark": "비행기 에 익숙 한 손님",
                    "userImage": "",
                    "userId": 532,
                    "drawerList": []
                }
            },
            "spuId": "UFrLVfOc3t0BPZe",
            "userNum": 50,
            "userId": 532,
            "beignTime": startTime,
            "playType": 0,
            "showOwnerPhoto": True,
            "filmId": 4932917517541910,
            "type": 1,
            "roomId": 0
        }
    )

    result = requests.post(url=url,headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ

def getDrawerInfo(roomId,regionId):
    """
    :param roomId:
    :param regionId:
    :return:
    """
    reqUrl = req_url('activity', "/inner/activity/getDrawerInfo")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': str(regionId),
    }
    body = {
        "roomId" : roomId
    }

    result = requests.get(url=url,headers=headers,params=body)
    resultJ = json.loads(result.content)
    return resultJ


def editDrawerInfo(roomId,regionId):
    """
    :param roomId:
    :param regionId:
    :return:
    """
    reqUrl = req_url('activity', "/inner/activity/editDrawerInfo")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': str(regionId),
    }
    body = json.dumps(
        {
            "roomId": roomId,
            "international": {
                "ko_KR": {
                    "drawerList": [{
                        "type": 1,
                        "show": 1,
                        "title": "전용관",
                        "userName": "비행기 에 익숙 한 손님",
                        "userImage": "",
                        "userRemark": "비행기 에 익숙 한 손님"
                    }, {
                        "type": 2,
                        "show": 1,
                        "title": "영화",
                        "filmName": "国外鸿空测试",
                        "filmType": "코믹/다큐멘터리/로맨스",
                        "filmImg": "",
                        "descInfo": "根据2018年5月14日四川航空3U8633航班机组成功处置特情真实事件改编。机组执行航班任务时，在万米高空突遇驾驶舱风挡玻璃爆裂脱落、座舱释压的极端罕见险情，生死关头，他们临危不乱、果断应对、正确处置，确保了机上全部人员的生命安全，创造了世界民航史上的奇迹。",
                        "subTitle": "",
                        "content": ""
                    }, {
                        "type": 3,
                        "show": 1,
                        "title": "주 제목 사용자 정의",
                        "subTitle": "사용자 정의 눈 에 띄 는 내용",
                        "content": "사용자 정의 내용 을 사용 하여 H5 전단 전시 에 사용 합 니 다."
                    }]
                },
                "en_US": {
                    "drawerList": [{
                        "type": 1,
                        "show": 1,
                        "title": "Host introduction",
                        "userName": "비행기 에 익숙 한 손님",
                        "userImage": "",
                        "userRemark": "비행기 에 익숙 한 손님"
                    }, {
                        "type": 2,
                        "show": 1,
                        "title": "Movie information",
                        "filmName": "国外鸿空测试",
                        "filmType": "Comedy/Documentary/Romance",
                        "filmImg": "https://g.smartcinemausa.com/images/a9f172f04f4c4cdf82e4127e637f40e6-1057-1511.jpg",
                        "descInfo": "根据2018年5月14日四川航空3U8633航班机组成功处置特情真实事件改编。机组执行航班任务时，在万米高空突遇驾驶舱风挡玻璃爆裂脱落、座舱释压的极端罕见险情，生死关头，他们临危不乱、果断应对、正确处置，确保了机上全部人员的生命安全，创造了世界民航史上的奇迹。",
                        "subTitle": "",
                        "content": ""
                    }, {
                        "type": 3,
                        "show": 1,
                        "title": "Custom main title",
                        "content": "Custom content for H5 front display",
                        "subTitle": "Customize eye-catching content"
                    }]
                },
                "zh_CN": {
                    "drawerList": [{
                        "type": 1,
                        "show": 1,
                        "title": "场主介绍",
                        "userName": "비행기 에 익숙 한 손님",
                        "userImage": "",
                        "userRemark": "비행기 에 익숙 한 손님"
                    }, {
                        "type": 2,
                        "show": 1,
                        "title": "影片介绍",
                        "filmName": "国外鸿空测试",
                        "filmType": "喜剧/纪录片/爱情",
                        "filmImg": "https://g.smartcinemausa.com/images/a9f172f04f4c4cdf82e4127e637f40e6-1057-1511.jpg",
                        "descInfo": "根据2018年5月14日四川航空3U8633航班机组成功处置特情真实事件改编。机组执行航班任务时，在万米高空突遇驾驶舱风挡玻璃爆裂脱落、座舱释压的极端罕见险情，生死关头，他们临危不乱、果断应对、正确处置，确保了机上全部人员的生命安全，创造了世界民航史上的奇迹。",
                        "subTitle": "",
                        "content": ""
                    }, {
                        "type": 3,
                        "show": 1,
                        "title": "自定义主标题",
                        "subTitle": "自定义醒目内容",
                        "content": "自定义内容，用来H5前段展示使用"
                    }]
                }
            }
        }
    )

    result = requests.post(url=url, headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ


def updateStatus(roomId,regionId):
    """
    :param roomId:
    :param regionId:
    :return:
    """
    reqUrl = req_url('activity', "/inner/activity/updateStatus")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': str(regionId),
    }
    body = json.dumps(
        {
            "roomId": roomId,
            "onlineStatus": 1
        }
    )

    result = requests.post(url=url,headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ



special_name = "测试专场-韩国-CH0"
regionId = '2'
spuId = "RXSiDR7t5JOVvjF"
filmId =  "4932917517541910"
spuName = "北美测试全10分钟"


# filmTime = getTimes()
# startTime = filmTime[2]
#
# print(startTime)
#
# # 获取专场信息筛选roomId
# room_info = editRoom(special_name,regionId,startTime)
# print("专场信息：",room_info)
#
# roomId = room_info['data']['id']
#
# # 获取专场信息，编辑专场传递信息
# print("获取专场信息：",getDrawerInfo(roomId,regionId))
# print("编辑场信息:：",editDrawerInfo(roomId,regionId))
#
# # 获取专场列表信息，用于寻找skuId
# special_list = getRoomData(regionId)
# print("专场列表信息",special_list)
#
# special_info = special_list['data']['list']
# print("单个专场信息：",special_info)
#
# for room_id in special_info:
#     print("房间信息结果：",room_id)
#     if room_id['roomId'] == roomId:
#         sku_id = room_id['skuId']
#         film_id = room_id['filmId']
#         break
#     else:
#         continue
#
# print(sku_id,film_id)
#
#
# # 配置上线"预发"环境
# print('配置上线"预发"环境：',goodsEditSkuEnvironment(sku_id,regionId))
#
# # 审核通过
# print('审核通过：',goodsEditSkuExamine(sku_id,regionId))
#
# # 配置上线"线上"环境
# print('配置上线"线上"环境：',goodsEditSkuEnvironment(sku_id,regionId))
#
# # 配置绑定渠道
# print('配置绑定渠道：',goodsEditSkuChannel(sku_id,regionId))
#
# # 配置上架商品
# print('配置上架商品：',goodsEditSkuGoodsStatus(film_id,sku_id,regionId))
#
# print('修改商品价格：',goodsUpdateSku(spuId,filmId,spuName,sku_id,"4932956157102918",1591843477,1659235477))
#
# # 配置专场上线
# print('配置专场上线：',updateStatus(roomId,regionId))
