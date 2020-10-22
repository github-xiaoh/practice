# -*- coding:utf-8 -*-


# 海外卡券和票生成接口
import json
from .releasefilm import getTimes
import requests


day_times = getTimes()
now_time = int(round(day_times[0] *1000))
time_30 = int(round(day_times[1] * 1000))

print(now_time,time_30)

class Coupon_create():

    def __init__(self):
        self.url = "http://operation-manage-test.smartcinemausa.com/coupon/addActivity"

        self.Headers = {
            'Content-Type': "application/json",
            'X-User-Id':'163',
            'X-Region-Id':str(1)
        }

    def activity_list(self,couponType):
        url = "http://operation-manage-test.smartcinemausa.com/coupon/activityList"
        body = json.dumps({"page":1,"size":10,"activityType":0,"couponType":couponType,"discountType":"","resKey":"MENU_RESOURCE_VOUCHER"})
        result = requests.post(url=url,data=body,headers=self.Headers)
        resultJ = json.loads(result.content)
        # print(resultJ)
        return resultJ

    def audit_query_auditList(self):
        """
        :return:
        """
        url = "http://user-manage-test.smartcinemausa.com/common/audit/getAuditList"
        body = json.dumps({"resKey":"MENU_OMS_AUDIT_LIST","auditGenre":"","auditName":"","currentPage":1,"pageSize":20,"auditListType":0})
        result = requests.post(url=url,data=body,headers=self.Headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def audit_update(self,audit_id,activityId,auditGenre):
        """
        :param activityId:
        :param auditGenre:
        :return:
        """
        url = "http://user-manage-test.smartcinemausa.com/common/audit/updateAuditData"
        body = json.dumps({"auditStatus":1,"auditData":[{"id":str(audit_id),"dateId":activityId,"auditGenre":auditGenre}]})
        result = requests.post(url=url,data=body,headers=self.Headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ


    def coupon_duihuan_xilie(self):
        """
        :return:
        """
        body = json.dumps({
            "international": {
                "en_US": {
                    "headMarkUrl": "https://g.smartcinemausa.com/images/07e1547137c845a1b24e864eebce685d-488-92.png",
                    "displayName": "yingwen",
                    "pageTitle": "Smart Cinema Intl",
                    "activityRule": " 1. After coupon is successfully received, it will be automatically issued to the user, which can be viewed in “My Coupons”;\n 2. Coupons cannot be superimposed, and only one coupon can be used for a single order;\n 3. The specified movie coupon can only be used for the specified movie. The coupon for all movies can be used for any movie. Please refer to the name of the coupon and the scope of application;\n 4. The coupon will not be returned after it expires or is used;\n 5. The event has nothing to do with Apple;\n 6. The final interpretation of the other uses of this coupon is owned by this platform.",
                    "webchatMainHead": "Smart Cinema Intl. send you a red envelop for movie watching",
                    "webchatSubHead": "Gift coupon is delivered, choosing any movie you like",
                    "couponName": "Card name",
                    "couponRemarks": "Card ticket description",
                    "seriesName": "Series name"
                },
                "zh_CN": {
                    "headMarkUrl": "https://g.smartcinemausa.com/images/07e1547137c845a1b24e864eebce685d-488-92.png",
                    "displayName": "展示名称",
                    "pageTitle": "Smart Cinema Intl",
                    "activityRule": " 1. After coupon is successfully received, it will be automatically issued to the user, which can be viewed in “My Coupons”;\n 2. Coupons cannot be superimposed, and only one coupon can be used for a single order;\n 3. The specified movie coupon can only be used for the specified movie. The coupon for all movies can be used for any movie. Please refer to the name of the coupon and the scope of application;\n 4. The coupon will not be returned after it expires or is used;\n 5. The event has nothing to do with Apple;\n 6. The final interpretation of the other uses of this coupon is owned by this platform.",
                    "webchatMainHead": "分享主标题",
                    "webchatSubHead": "分享副标题",
                    "couponName": "Card name",
                    "couponRemarks": "Card ticket description",
                    "seriesName": "系列名称"
                }
            },
            "activityName": "测试-兑换-系列-北美",
            "activityTime": [
                "2020-05-07 00:00:00",
                "2020-05-13 23:59:59"
            ],
            "createrName": "陈航",
            "applicationDept": "质量保障中心",
            "applicationNote": "申请测试",
            "activityLabel": "测试",
            "channelName": "测试",
            "retailPricing": "4.29",
            "display": 0,
            "couponScene": 0,
            "couponType": 0,
            "discountType": 2,
            "couponSum": "10",
            "ticketPrice": 4.99,
            "monitorSwitch": 0,
            "userName": "",
            "mailInfo": [
                {
                    "id": 232,
                    "userId": 163,
                    "userName": "陈航",
                    "department": "质量保障中心",
                    "departmentCode": "",
                    "userEmail": "chenhang@smartcinema.com.cn",
                    "userMobile": "",
                    "createTime": "2019-11-30 14:04:56",
                    "modifyTime": "2019-11-30 14:04:56"
                }
            ],
            "surplusNotifyAll": [
                "A",
                "B"
            ],
            "monitorNum": 9,
            "monitorPercentage": 80,
            "allList": [
                {
                    "id": 232,
                    "userId": 163,
                    "userName": "陈航",
                    "department": "质量保障中心",
                    "departmentCode": "",
                    "userEmail": "chenhang@smartcinema.com.cn",
                    "userMobile": "",
                    "createTime": "2019-11-30 14:04:56",
                    "modifyTime": "2019-11-30 14:04:56"
                },
                {
                    "id": 244,
                    "userId": 197,
                    "userName": "赵利冬",
                    "department": "质量保障中心",
                    "departmentCode": "",
                    "userEmail": "zhaolidong@smartcinema.com.cn",
                    "userMobile": "",
                    "createTime": "2020-01-02 10:30:37",
                    "modifyTime": "2020-01-02 10:30:37"
                }
            ],
            "startValidateTime": now_time,
            "endValidateTime": time_30,
            "deptCode": "aih8",
            "ownerId": 163,
            "orgType": None,
            "backgroundColor": "https://g.smartcinema.com.cn/images/e2c847d9bcc84e609f8f4701c8300bf9-686-652.png",
            "filmPosterUrl": "https://g.smartcinemausa.com/images/5da4a1591b7e47c9aedbdfbd28719441-1268-1268.jpg",
            "icon": "",
            "couponValidateDays": "0",
            "videoType": [
                "1",
                "2"
            ],
            "playFilm": [
                "1",
                "2",
                "3"
            ],
            "fileLanguage": [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16"
            ],
            "filmAttribute": 2,
            "spuName": "qFPnbNcmzaR9XZg",
            "couponStartTime": now_time,
            "couponEndTime": time_30,
            "filmList": [
                {
                    "filmSort": 1,
                    "spuName": "北美陶明使用-usa",
                    "spuId": "6Appy7KQOKJQZEl",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "en_US": {
                            "spuName": "yingwen北美陶明使用-usa"
                        },
                        "zh_CN": {
                            "spuName": "北美陶明使用-usa"
                        }
                    }
                },
                {
                    "filmSort": 2,
                    "spuName": "北美张兵磊专用",
                    "spuId": "8Ft74yhYXJx5h2m",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "zh_TW": {
                            "spuName": "繁体北美张兵磊专用"
                        },
                        "ko_KR": {
                            "spuName": "韩文北美张兵磊专用"
                        },
                        "en_US": {
                            "spuName": "yingwen北美张兵磊专用"
                        },
                        "zh_CN": {
                            "spuName": "北美张兵磊专用"
                        }
                    }
                },
                {
                    "filmSort": 3,
                    "spuName": "中文sqlpingyin",
                    "spuId": "cKsv5dAQ0lF2vMo",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "zh_TW": {
                            "spuName": "繁体sqlpingyin"
                        },
                        "ko_KR": {
                            "spuName": "韩文sqlpingyin"
                        },
                        "en_US": {
                            "spuName": "yingwensqlpingyin"
                        },
                        "zh_CN": {
                            "spuName": "中文sqlpingyin"
                        }
                    }
                },
                {
                    "filmSort": 4,
                    "spuName": "带解说片源",
                    "spuId": "IgYGF8vk4ug3t0B",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "en_US": {
                            "spuName": "daijieshuopianyuan"
                        },
                        "zh_CN": {
                            "spuName": "带解说片源"
                        }
                    }
                },
                {
                    "filmSort": 5,
                    "spuName": "farirplay-test1",
                    "spuId": "qFPnbNcmzaR9XZg",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "zh_TW": {
                            "spuName": "繁体farirplay-test1"
                        },
                        "ko_KR": {
                            "spuName": "韩文farirplay-test1"
                        },
                        "en_US": {
                            "spuName": "yingwenfarirplay-test1"
                        },
                        "zh_CN": {
                            "spuName": "farirplay-test1"
                        }
                    }
                }
            ],
            "operatorName": "陈航",
            "redPacketId": "",
            "activityType": 0,
            "activityId": ""
        })

        result = requests.post(url=self.url,data=body,headers=self.Headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ


    def coupon_dinge_xilie(self):
        """
        :return:
        """
        body = json.dumps({
            "international": {
                "en_US": {
                    "headMarkUrl": "https://g.smartcinemausa.com/images/07e1547137c845a1b24e864eebce685d-488-92.png",
                    "displayName": "ying展示名称",
                    "pageTitle": "Smart Cinema Intl",
                    "activityRule": " 1. After coupon is successfully received, it will be automatically issued to the user, which can be viewed in “My Coupons”;\n 2. Coupons cannot be superimposed, and only one coupon can be used for a single order;\n 3. The specified movie coupon can only be used for the specified movie. The coupon for all movies can be used for any movie. Please refer to the name of the coupon and the scope of application;\n 4. The coupon will not be returned after it expires or is used;\n 5. The event has nothing to do with Apple;\n 6. The final interpretation of the other uses of this coupon is owned by this platform.",
                    "webchatMainHead": "Smart Cinema Intl. send you a red envelop ",
                    "webchatSubHead": "Gift coupon is delivered, choosing any movie ",
                    "couponName": "ying-卡券名称",
                    "couponRemarks": "ying-卡券说明",
                    "seriesName": "系列名称"
                },
                "zh_CN": {
                    "headMarkUrl": "https://g.smartcinemausa.com/images/07e1547137c845a1b24e864eebce685d-488-92.png",
                    "displayName": "简体-展示名称",
                    "pageTitle": "简体-页面标题",
                    "activityRule": " 1. After coupon is successfully received, it will be automatically issued to the user, which can be viewed in “My Coupons”;\n 2. Coupons cannot be superimposed, and only one coupon can be used for a single order;\n 3. The specified movie coupon can only be used for the specified movie. The coupon for all movies can be used for any movie. Please refer to the name of the coupon and the scope of application;\n 4. The coupon will not be returned after it expires or is used;\n 5. The event has nothing to do with Apple;\n 6. The final interpretation of the other uses of this coupon is owned by this platform.",
                    "webchatMainHead": "主标题",
                    "webchatSubHead": "副标题",
                    "couponName": "简体-卡券名称",
                    "couponRemarks": "简体-卡券说明",
                    "seriesName": "系列名称"
                }
            },
            "activityName": "测试-定额-系列-北美",
            "activityTime": [
                "2020-02-29T16:00:00.251Z",
                "2020-04-30T15:59:59.251Z"
            ],
            "createrName": "陈航",
            "applicationDept": "质量保障中心",
            "applicationNote": "测试",
            "activityLabel": "测试",
            "channelName": "测试",
            "retailPricing": "2.97",
            "display": 0,
            "couponScene": 0,
            "couponType": 1,
            "discountType": 2,
            "couponSum": "10",
            "price": "0.01",
            "ticketPrice": 4.99,
            "monitorSwitch": 0,
            "userName": "",
            "mailInfo": [
                {
                    "id": 232,
                    "userId": 163,
                    "userName": "陈航",
                    "department": "质量保障中心",
                    "departmentCode": "",
                    "userEmail": "chenhang@smartcinema.com.cn",
                    "userMobile": "",
                    "createTime": "2019-11-30 14:04:56",
                    "modifyTime": "2019-11-30 14:04:56"
                }
            ],
            "surplusNotifyAll": [
                "A",
                "B"
            ],
            "monitorNum": 9,
            "monitorPercentage": 80,
            "allList": [
                {
                    "id": 232,
                    "userId": 163,
                    "userName": "陈航",
                    "department": "质量保障中心",
                    "departmentCode": "",
                    "userEmail": "chenhang@smartcinema.com.cn",
                    "userMobile": "",
                    "createTime": "2019-11-30 14:04:56",
                    "modifyTime": "2019-11-30 14:04:56"
                }
            ],
            "startValidateTime": now_time,
            "endValidateTime": time_30,
            "deptCode": "aih8",
            "ownerId": 163,
            "orgType": None,
            "backgroundColor": "https://g.smartcinema.com.cn/images/e2c847d9bcc84e609f8f4701c8300bf9-686-652.png",
            "filmPosterUrl": "https://g.smartcinemausa.com/images/f0fb580f015d49758ea8daa9129cf6f6-1125-1954.jpg",
            "icon": "",
            "couponValidateDays": "0",
            "videoType": [
                "1",
                "2"
            ],
            "playFilm": [
                "1",
                "2",
                "3"
            ],
            "fileLanguage": [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16"
            ],
            "filmAttribute": 2,
            "spuName": "qFPnbNcmzaR9XZg",
            "couponStartTime": now_time,
            "couponEndTime": time_30,
            "filmList": [
                {
                    "filmSort": 1,
                    "spuName": "北美陶明使用-usa",
                    "spuId": "6Appy7KQOKJQZEl",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "en_US": {
                            "spuName": "yingwen北美陶明使用-usa"
                        },
                        "zh_CN": {
                            "spuName": "北美陶明使用-usa"
                        }
                    }
                },
                {
                    "filmSort": 2,
                    "spuName": "北美张兵磊专用",
                    "spuId": "8Ft74yhYXJx5h2m",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "zh_TW": {
                            "spuName": "繁体北美张兵磊专用"
                        },
                        "ko_KR": {
                            "spuName": "韩文北美张兵磊专用"
                        },
                        "en_US": {
                            "spuName": "yingwen北美张兵磊专用"
                        },
                        "zh_CN": {
                            "spuName": "北美张兵磊专用"
                        }
                    }
                },
                {
                    "filmSort": 3,
                    "spuName": "sqlpingyin",
                    "spuId": "cKsv5dAQ0lF2vMo",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "zh_TW": {
                            "spuName": "繁体sqlpingyin"
                        },
                        "ko_KR": {
                            "spuName": "韩文sqlpingyin"
                        },
                        "en_US": {
                            "spuName": "yingwensqlpingyin"
                        },
                        "zh_CN": {
                            "spuName": "sqlpingyin"
                        }
                    }
                },
                {
                    "filmSort": 4,
                    "spuName": "hello 北京",
                    "spuId": "h09aOYzoeEFv20a",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "en_US": {
                            "spuName": "Hello Beijing"
                        },
                        "zh_CN": {
                            "spuName": "hello 北京"
                        }
                    }
                },
                {
                    "filmSort": 5,
                    "spuName": "带解说片源",
                    "spuId": "IgYGF8vk4ug3t0B",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "en_US": {
                            "spuName": "daijieshuopianyuan"
                        },
                        "zh_CN": {
                            "spuName": "带解说片源"
                        }
                    }
                },
                {
                    "filmSort": 6,
                    "spuName": "双生",
                    "spuId": "n3uynQ2md1iuU8l",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "en_US": {
                            "spuName": "双生"
                        },
                        "zh_CN": {
                            "spuName": "双生"
                        }
                    }
                },
                {
                    "filmSort": 7,
                    "spuName": "farirplay-test1",
                    "spuId": "qFPnbNcmzaR9XZg",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "zh_TW": {
                            "spuName": "繁体farirplay-test1"
                        },
                        "ko_KR": {
                            "spuName": "韩文farirplay-test1"
                        },
                        "en_US": {
                            "spuName": "yingwenfarirplay-test1"
                        },
                        "zh_CN": {
                            "spuName": "farirplay-test1"
                        }
                    }
                }
            ],
            "operatorName": "陈航",
            "redPacketId": "",
            "activityType": 0,
            "activityId": ""
        })

        result = requests.post(url=self.url,data=body,headers=self.Headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ


    def coupon_lijian_xilie(self):
        """
        :return:
        """
        body = json.dumps({
            "international": {
                "en_US": {
                    "headMarkUrl": "https://g.smartcinemausa.com/images/07e1547137c845a1b24e864eebce685d-488-92.png",
                    "displayName": "ying展示名称",
                    "pageTitle": "Smart Cinema Intl",
                    "activityRule": " 1. After coupon is successfully received, it will be automatically issued to the user, which can be viewed in “My Coupons”;\n 2. Coupons cannot be superimposed, and only one coupon can be used for a single order;\n 3. The specified movie coupon can only be used for the specified movie. The coupon for all movies can be used for any movie. Please refer to the name of the coupon and the scope of application;\n 4. The coupon will not be returned after it expires or is used;\n 5. The event has nothing to do with Apple;\n 6. The final interpretation of the other uses of this coupon is owned by this platform.",
                    "webchatMainHead": "Smart Cinema Intl. send you a red envelop for movie watching",
                    "webchatSubHead": "Gift coupon is delivered, choosing any movie you like",
                    "couponName": "ying-卡券名称",
                    "couponRemarks": "ying-卡券说明",
                    "seriesName": "ying-系列名称"
                },
                "zh_CN": {
                    "headMarkUrl": "https://g.smartcinemausa.com/images/07e1547137c845a1b24e864eebce685d-488-92.png",
                    "displayName": "展示名称",
                    "pageTitle": "页面标题",
                    "activityRule": " 1.优惠券领取成功后，会自动发放至用户卡券中，可在“我的-卡券包”中查看;\n 2.优惠券不可叠加使用，单笔订单仅限使用1张优惠券;\n 3.指定影片优惠券仅可对该影片使用，全场优惠券可对任意影片使用，具体请以优惠券名称、适用范围说明为准;\n 4.优惠券到期或使用后，不予退回;\n 5.该活动与苹果公司无关;\n 6.本优惠券的其他使用事项的最终解释权归本平台所有。",
                    "webchatMainHead": "主标题",
                    "webchatSubHead": "附表你",
                    "couponName": "简体卡券名称",
                    "couponRemarks": "简体卡券说明",
                    "seriesName": "系列名称"
                }
            },
            "activityName": "测试-立减-系列-北美",
            "activityTime": [
                "2020-02-29T16:00:00.000Z",
                "2020-04-30T15:59:59.000Z"
            ],
            "createrName": "陈航",
            "applicationDept": "质量保障中心",
            "applicationNote": "测试",
            "activityLabel": "",
            "channelName": "测试",
            "retailPricing": "4.99",
            "display": 0,
            "couponScene": 0,
            "couponType": 2,
            "discountType": 2,
            "couponSum": "10",
            "price": "0.01",
            "ticketPrice": 4.99,
            "monitorSwitch": 0,
            "userName": "",
            "mailInfo": [
                {
                    "id": 232,
                    "userId": 163,
                    "userName": "陈航",
                    "department": "质量保障中心",
                    "departmentCode": "",
                    "userEmail": "chenhang@smartcinema.com.cn",
                    "userMobile": "",
                    "createTime": "2019-11-30 14:04:56",
                    "modifyTime": "2019-11-30 14:04:56"
                }
            ],
            "surplusNotifyAll": [
                "A",
                "B"
            ],
            "monitorNum": 9,
            "monitorPercentage": 80,
            "allList": [
                {
                    "id": 232,
                    "userId": 163,
                    "userName": "陈航",
                    "department": "质量保障中心",
                    "departmentCode": "",
                    "userEmail": "chenhang@smartcinema.com.cn",
                    "userMobile": "",
                    "createTime": "2019-11-30 14:04:56",
                    "modifyTime": "2019-11-30 14:04:56"
                }
            ],
            "startValidateTime": now_time,
            "endValidateTime": time_30,
            "deptCode": "aih8",
            "ownerId": 163,
            "orgType": None,
            "backgroundColor": "https://g.smartcinema.com.cn/images/e2c847d9bcc84e609f8f4701c8300bf9-686-652.png",
            "filmPosterUrl": "https://g.smartcinemausa.com/images/1cdcdbe908b546a2a20303b2d7415100-240-135.jpg",
            "icon": "",
            "couponValidateDays": "0",
            "videoType": [
                "1",
                "2"
            ],
            "playFilm": [
                "1",
                "2",
                "3"
            ],
            "fileLanguage": [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16"
            ],
            "filmAttribute": 2,
            "couponStartTime": now_time,
            "couponEndTime": time_30,
            "filmList": [
                {
                    "filmSort": 1,
                    "spuName": "北美陶明使用-usa",
                    "spuId": "6Appy7KQOKJQZEl",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1,2",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "en_US": {
                            "spuName": "yingwen北美陶明使用-usa"
                        },
                        "zh_CN": {
                            "spuName": "北美陶明使用-usa"
                        }
                    }
                },
                {
                    "filmSort": 2,
                    "spuName": "529影片中文名005",
                    "spuId": "9fH0J2GoIT9cQ7Y",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1,2",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "en_US": {
                            "spuName": "529english005"
                        },
                        "zh_CN": {
                            "spuName": "529影片中文名005"
                        }
                    }
                },
                {
                    "filmSort": 3,
                    "spuName": "sqlpingyin",
                    "spuId": "cKsv5dAQ0lF2vMo",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1,2",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "zh_TW": {
                            "spuName": "繁体sqlpingyin"
                        },
                        "ko_KR": {
                            "spuName": "韩文sqlpingyin"
                        },
                        "en_US": {
                            "spuName": "yingwensqlpingyin"
                        },
                        "zh_CN": {
                            "spuName": "sqlpingyin"
                        }
                    }
                },
                {
                    "filmSort": 4,
                    "spuName": "hello 北京",
                    "spuId": "h09aOYzoeEFv20a",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1,2",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "en_US": {
                            "spuName": "Hello Beijing"
                        },
                        "zh_CN": {
                            "spuName": "hello 北京"
                        }
                    }
                },
                {
                    "filmSort": 5,
                    "spuName": "farirplay-test1",
                    "spuId": "qFPnbNcmzaR9XZg",
                    "playFilm": "1,2,3",
                    "playName": "公映场,点映场,零点场",
                    "videoType": "1,2",
                    "fileLanguage": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
                    "filmAttribute": 2,
                    "international": {
                        "zh_TW": {
                            "spuName": "繁体farirplay-test1"
                        },
                        "ko_KR": {
                            "spuName": "韩文farirplay-test1"
                        },
                        "en_US": {
                            "spuName": "yingwenfarirplay-test1"
                        },
                        "zh_CN": {
                            "spuName": "farirplay-test1"
                        }
                    }
                }
            ],
            "operatorName": "陈航",
            "redPacketId": "",
            "activityType": 0,
            "activityId": ""
        })
        result = requests.post(url=self.url,data=body,headers=self.Headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ







# coupon = Coupon_create()
# coupon.coupon_duihuan_xilie()
# coupon.coupon_dinge_xilie()
# coupon.coupon_lijian_xilie()

# activity_data = coupon.coupon_duihuan_xilie()
# activity_data = coupon.coupon_dinge_xilie()
# activity_data = coupon.coupon_lijian_xilie()
# activity = json.loads(activity_data['data'])
# activity_id = str(activity['activityId'])
#
# print(type(activity_id),activity_id)
#
# audit_list = coupon.audit_query_auditList()
# print(audit_list['data']['pageData'])
# for pageData in audit_list['data']['pageData']:
#     print(pageData)
#     if (pageData['dateId'] == activity_id):
#         print("匹配活动ID成功")
#         audit_id = pageData['id']
#         break
#
# coupon.audit_update(audit_id,activity_id,'3')


# coupon.activity_list(couponType=2)
# activityData = coupon.activity_list(couponType=0)
# activityList = activityData['data']['list']
# activity_id = '3710'
# for activity in activityList:
#     print(activity)
#     print(type(activity['activityId']))
#     if str(activity["activityId"]) == activity_id:
#         # content['visibility'] = "visible"
#         # content['redPacketCode'] = activity['redPacketCode']
#         # content['code'] = activity['code']
#         print(activity['activityId'],activity_id)
#         print(activity['redPacketCode'],
#               "https://h5-us-test.smartcinema.com.cn/coupon-intl-us/index.html?couponCode=" + activity[
#                   'redPacketCode'])
#         print(activity['code'],
#               "https://h5-us-test.smartcinema.com.cn/exchange-common-intl-us/index.html?code=" + activity['code'])





