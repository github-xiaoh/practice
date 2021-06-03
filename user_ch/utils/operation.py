# -*- coding:utf-8 -*-

import requests
import json


class Operation_tickets_Zh():
    '''
    # 国内赠票相关
    '''

    def __init__(self,channel):
        self.channel = channel

        self.headers = {
            'Content-Type': 'application/json',
            'X-User-Id': '89',
        }


    def getGoodsInfo(self):
        '''
        # 获取影片列表
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /outside/getGoodsFilmList
        :return:
        '''

        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/outside/getGoodsFilmList'

        params = {
            'groundStatus':'1,2',
            'screenType':'4,6,7,9,10,11'
        }

        result = requests.get(url=host + path, headers=self.headers,params=params)
        resultJ = json.loads(result.content)
        # print(resultJ)
        return resultJ

    def getUserInfo(self):
        '''
        # x-origin-host: http://user-manage-test.smartcinema-inc.com
        # x-origin-path: /user/warning/queryUserInfo
        :return:
        '''

        host = f'http://user-manage-{self.channel}.smartcinema-inc.com'
        path = '/user/warning/queryUserInfo'

        body = json.dumps({"department": "质量保障中心",'departmentCode': "aih8"})

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        # print(resultJ)
        return resultJ

    def getTiccketInfo(self,activityName,filmname,startTime,endTime,skuId,spuId):
        '''
        # x-origin-host: http://ticket-manage-test.smartcinema-inc.com
        # x-origin-path: /activity/entry
        :return:
        '''

        host = 'http://ticket-manage-test.smartcinema-inc.com'
        path = '/activity/entry'

        userInfo = self.getUserInfo()['data'][0]

        body = json.dumps({
            "activityName": activityName,
            "filmName": filmname,
            "operatorName": userInfo['userName'],
            "department": "质量保障中心",
            "operatorExplain": "测试活动票码定制生成",
            "activityLabel": "",
            "retailPricing": "0.99",
            "warningSwitch": "2",
            "acceptLimit": 1,
            "newUser": 0,
            "districtLimit": 1,
            "activityType": 0,
            "inventory": "10",
            "price": "25",
            "orgCode": "ORG20200610154900181012",
            "videoType": 1,
            "scheduleType": 4,
            "language": "原声",
            "allowedWatch": 0,
            "activityTime": ["2020-08-31T16:00:00.000Z", "2021-10-31T15:59:59.000Z"],
            "contractCode": "CONTRACT20201102174253861013",
            "display": 0,
            "contractType": 1,
            "allList": [{
                "id": userInfo['id'],
                "userId": userInfo['userId'],
                "userName": userInfo['userName'],
                "department": "质量保障中心",
                "departmentCode": "aih8",
                "userEmail": "chenhang@smartcinema.com.cn",
                "userMobile": "18403558945",
                "createTime": "2020-05-21 17:23:22",
                "modifyTime": "2020-05-21 17:23:22"
            }],
            "enterType": 0,
            "roomData": {},
            "deptCode": "aih8",
            "ownerId": userInfo['userId'],
            "planList": [],
            "startTime": startTime,
            "endTime": endTime,
            "filmType": 1,
            "ticketSkuId": skuId,
            "file": "",
            "spuId": spuId,
            "mailInfo": [],
            "roomName": "",
            "pageTitle": "移动电影院",
            "mainTitle": "移动电影院",
            "subTitle": "欢迎使用移动电影院",
            "activityRule": " 1.每个手机号限领一张电影票。赠票被领取后，所有权将从赠票方转至领票方;\n 2.未注册过'移动电影院'的用户，领票后，应先下载'移动电影院'App，以领票手机号完成注册，即可在App的'放映'区看到该赠票，并可开始观影;\n 3.已注册过'移动电影院'的用户，建议使用注册手机号领票。领取赠票后，可在App的'放映'区看到该赠票，并可开始观影;\n 4.领票成功后，应在'移动电影院'影片上映期内完成观影。影片下线后，将无法再观影;\n 5.'移动电影院'保留法律范围内的最终解释权。如有疑问，请致电官方客服： 4006-2018-05。",
            "linkNum": 1,
            "webchatMainHead": "移动电影院邀您看电影《测试20分钟电影》",
            "webchatSubHead": "获取了国内外各大奖项，拿到手软！！！",
            "icon": "https://g.smartcinema.com.cn/images/0a78cca92af54f7da8fe8f9a92d7a2a4-1268-1268.jpg",
            "starImg": "",
            "subscript": "",
            "sponsorLogo": ""
        })

        result = requests.post(url=host + path, headers=self.headers, data=data)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def getAuditData(self):
        """
        获取审核列表
        # x-origin-host: http://user-manage-test.smartcinema-inc.com
        # x-origin-path: /common/audit/getAuditList
        :return:
        """

        host = f'http://user-manage-{self.channel}.smartcinema-inc.com'
        path = '/common/audit/getAuditList'

        body = json.dumps({"resKey":"MENU_OMS_AUDIT_LIST","auditGenre":"","auditName":"","currentPage":1,"pageSize":20,"auditListType":0})

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        # print(resultJ)

        return resultJ


    def updateAuditData(self,aduitId,activityId):
        """
        审核票接口
        # x-origin-host: http://user-manage-test.smartcinema-inc.com
        # x-origin-path: /common/audit/updateAuditData
        :param activityId:
        :return:
        """

        host = f'http://user-manage-{self.channel}.smartcinema-inc.com'
        path = '/common/audit/updateAuditData'

        body = json.dumps({"auditStatus":1,"auditData":[{"id":aduitId,"dateId":activityId,"auditGenre":"5"}]})

        result = requests.post(url=host+path,headers=self.headers,data=body)
        resultJ = json.loads(result.content)
        # print(resultJ)

        return resultJ


class Operation_tickets_Inc():
    '''
    # 海外赠票相关
    '''

    def __init__(self,regionId,channel):
        self.regionId = regionId
        self.channel = channel

        self.headers = {
            'Content-Type': 'application/json',
            'X-Region-Id': str(self.regionId),
            'X-User-Id': '163',
        }


    def getGoodsInfo(self):
        '''
        # 获取影片列表
        # x-origin-host: http://aws-goods-manage-test.smartcinema-inc.com
        # x-origin-path: /outside/getGoodsFilmList
        :return:
        '''

        host = f'http://aws-goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/outside/getGoodsFilmList'

        result = requests.get(url=host+path,headers=self.headers)
        resultJ = json.loads(result.content)
        # print(resultJ)
        return resultJ

    def getUserInfo(self):
        '''
        # 获取用户信息
        # x-origin-host: http://aws-user-manage-test.smartcinema-inc.com
        # x-origin-path: /user/warning/queryUserInfo
        :return:
        '''

        host = f'http://aws-user-manage-{self.channel}.smartcinema-inc.com'
        path = '/user/warning/queryUserInfo'

        body = json.dumps({"department":"质量保障中心"})

        result = requests.post(url=host+path,headers=self.headers,data=body)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ


    def getTiccketInfo(self,activityName,filmname,startTime,endTime,skuId,spuId):
        '''
        # 生成票链接
        # x-origin-host: http://aws-operation-manage-test.smartcinema-inc.com
        # x-origin-path: c
        :return:
        '''

        host = f'http://aws-operation-manage-{self.channel}.smartcinema-inc.com'
        path = '/activity/entry'

        userInfo = self.getUserInfo()['data'][0]
        body = json.dumps({
            "international":{
                "en_US":{
                    "pageTitle":"Smart Cinema Intl",
                     "titleType":0,
                     "mainTitle":"移动电影院",
                     "subTitle":"欢迎使用移动电影院",
                     "activityRule":"1. Each mobile number or email is limited to one movie ticket. After the ticket is received, ownership will be transferred from the ticket holder to the receiver;\n 2. Users who have not registered for 'Smart Cinema USA' should download the app first and complete the registration with the mobile number or email of the ticket. You can see the ticket in the 'Screening' section of the app and then start watching;\n 3. Users who have registered for 'Smart Cinema USA' are advised to use the registered mobile number or email to get the ticket. After receiving the free ticket, you can see it in the 'Screening' section of the app and then start watching;\n 4. After receiving the ticket successfully, you can watch the movie during its screening period in the 'Smart Cinema USA' . After the movie goes offline, you will no longer be able to watch it;\n 5. 'Smart Cinema USA' reserves the right of final interpretation within the law.",
                     "webchatMainHead":"A movie ticket in Smart Cinema Intl. is ready for you","webchatSubHead":"Wonderful movies are available for you with the ticket"
                },
                "zh_CN":{
                    "pageTitle":"Smart Cinema Intl",
                    "titleType":0,"mainTitle":"移动电影院",
                    "subTitle":"欢迎使用移动电影院",
                    "activityRule":"1. Each mobile number or email is limited to one movie ticket. After the ticket is received, ownership will be transferred from the ticket holder to the receiver;\n 2. Users who have not registered for 'Smart Cinema USA' should download the app first and complete the registration with the mobile number or email of the ticket. You can see the ticket in the 'Screening' section of the app and then start watching;\n 3. Users who have registered for 'Smart Cinema USA' are advised to use the registered mobile number or email to get the ticket. After receiving the free ticket, you can see it in the 'Screening' section of the app and then start watching;\n 4. After receiving the ticket successfully, you can watch the movie during its screening period in the 'Smart Cinema USA' . After the movie goes offline, you will no longer be able to watch it;\n 5. 'Smart Cinema USA' reserves the right of final interpretation within the law.",
                    "webchatMainHead":"A movie ticket in Smart Cinema Intl.",
                    "webchatSubHead":"Wonderful movies are available"
                }
            },
            "activityName":activityName,
            "filmName":filmname,
            "activityTime":["2019-09-30T16:00:00.000Z","2027-07-31T15:59:59.000Z"],
            "operatorName":userInfo['userName'],
            "department":"质量保障中心",
            "operatorExplain":"活动票码定制生成-测试使用",
            "activityLabel":"",
            "channelName":"渠道名称",
            "retailPricing":"4.99",
            "acceptLimit":1,
            "districtLimit":1,
            "activityType":0,
            "inventory":"10",
            "price":4.99,
            "warningSwitch":2,
            "videoType":1,
            "filmVersion":1,
            "scheduleType":4,
            "display":0,
            "allList":[{
                "id":userInfo['id'],
                "userId":userInfo['userId'],
                "userName":userInfo['userName'],
                "department":"质量保障中心",
                "departmentCode":"",
                "userEmail":userInfo['userEmail'],
                "userMobile":"",
                "createTime":"2019-11-30 14:04:56",
                "modifyTime":"2019-11-30 14:04:56"
            }],
            "enterType":0,
            "roomData":{},
            "deptCode":"aih8",
            "ownerId":userInfo['userId'],
            "startTime":startTime,
            "endTime":endTime,
            "filmType":1,
            "ticketSkuId":skuId,
            "file":"",
            "spuId":spuId,
            "mailInfo":[],
            "roomName":"",
            "blackMask":0,
            "isFuzzy":0,
            "icon":"",
            "facebookImage":"",
            "starImg":"",
            "subscript":""
        })

        result = requests.post(url=host+path,headers=self.headers,data=body)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def getAuditData(self):
        """
        获取审核列表
        x-origin-host: http://aws-user-manage-test.smartcinema-inc.com
        x-origin-path: /common/audit/getAuditList
        :return:
        """

        host = f'http://aws-user-manage-{self.channel}.smartcinema-inc.com'
        path = '/common/audit/getAuditList'

        body = json.dumps({"resKey":"MENU_OMS_AUDIT_LIST","auditGenre":"","auditName":"","currentPage":1,"pageSize":20,"auditListType":0})

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        print(resultJ)

        return resultJ

    def updateAuditData(self,aduitId,activityId):
        """
        审核票接口
        x-origin-host: http://aws-user-manage-test.smartcinema-inc.com
        x-origin-path: /common/audit/updateAuditData
        :param activityId:
        :return:
        """

        host = f'http://aws-user-manage-{self.channel}.smartcinema-inc.com'
        path = '/common/audit/updateAuditData'

        body = json.dumps({"auditStatus":1,"auditData":[{"id":aduitId,"dateId":activityId,"auditGenre":"5"}]})

        result = requests.post(url=host+path,headers=self.headers,data=body)
        resultJ = json.loads(result.content)
        # print(resultJ)

        return resultJ

    def getH5Token(self):
        '''
        获取H5页面token
        x-origin-host: https://aws-api-test.smartcinemausa.com
        x-origin-path: /user/passwordLogin
        :return:
        '''

        host = f'https://aws-api-{self.channel}.smartcinemausa.com'
        path = '/user/web/h5/passwordLogin'

        body = json.dumps({
            'uMobile':18403558945,
            'uCode':'4679',
            'uPassword':'3be4673c751088c3cc72c76c56321606',
            'uAreaCode':86,
            'uCid':'1',
            'uLgtype':1
        })

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        print(resultJ)

        return resultJ

class Preimere():
    def __init__(self):
        pass

    def preimere_create(self):
        pass



''' 国内赠票调试 '''

# operation_treate = Operation_tickets_Zh('prod')
# # operation_treate.getTiccketInfo('2','2',12432434,2342344,'33','sdcxj342sdcd')
# # operation_treate.updateAuditData(4237,691)
#
# q = operation_treate.getGoodsInfo()['data']
# print(q)
# j={}
# for k in q:
#     if k['skuId'] == 2005:
#         print(k)
#         j = k
#         break
# l = operation_treate.getTiccketInfo('测试使用',j['filmName'],j['onlineStartTime'],j['onlineEndTime'],j['skuId'],j['spuId'])
#
# print(l)

''' 海外赠票调试 '''

# operation_treate = Operation_tickets_Inc(1,'prod')
# # operation_treate.getUserInfo()

# q = operation_treate.getGoodsInfo()['data']
# print(q)
# j={}
# for k in q:
#     if k['skuId'] == 1442:
#         print(k)
#         j = k
#         break
# l = operation_treate.getTiccketInfo('测试使用',j['filmName'],j['onlineStartTime'],j['onlineEndTime'],j['skuId'],j['spuId'])
#
# print(l)

