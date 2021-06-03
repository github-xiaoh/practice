from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
import json
from . import models




def test_menus(request):
    content = {
            "data": [{
                "id": 100,
                "authName": "用户管理",
                "path": "users",
                "children": [{
                    "id": 110,
                    "authName": "用户列表",
                    "path": "users",
                    "children": [],
                    "order": None
                }],
                "order": 1
            }, {
                "id": 200,
                "authName": "接口自动化",
                "path": "users",
                "children": [{
                    "id": 210,
                    "authName": "项目列表",
                    "path": "projectlist",
                    "children": [],
                    "order": None
                },{
                    "id": 220,
                    "authName": "模块列表",
                    "path": "modulelist",
                    "children": [],
                    "order": None
                },{
                    "id": 230,
                    "authName": "用例列表",
                    "path": "testlist",
                    "children": [],
                    "order": None
                },{
                    "id": 240,
                    "authName": "配置列表",
                    "path": "configlist",
                    "children": [],
                    "order": None
                },{
                    "id": 250,
                    "authName": "测试套件",
                    "path": "suitelist",
                    "children": [],
                    "order": None
                },{
                    "id": 260,
                    "authName": "测试报告",
                    "path": "reportlist",
                    "children": [],
                    "order": None
                },{
                    "id": 270,
                    "authName": "定时任务",
                    "path": "periodictask",
                    "children": [],
                    "order": None
                }],
                "order": 1
            },{
                "id": 300,
                "authName": "权限管理",
                "path": "rights",
                "children": [{
                    "id": 310,
                    "authName": "角色列表",
                    "path": "roles",
                    "children": [],
                    "order": None
                }, {
                    "id": 320,
                    "authName": "权限列表",
                    "path": "rights",
                    "children": [],
                    "order": None
                }],
                "order": 2
            }, {
                "id": 400,
                "authName": "测试管理",
                "path": "goods",
                "children": [
                    {
                    "id": 310,
                    "authName": "添加首映礼",
                    "path": "premiere",
                    "children": [],
                    "order": 1
                    }, {
                        "id": 420,
                        "authName": "添加专场",
                        "path": "special",
                        "children": [],
                        "order": 2
                    }, {
                        "id": 430,
                        "authName": "用户充值",
                        "path": "recharge",
                        "children": [],
                        "order": 3
                    },{
                        "id": 440,
                        "authName": "运营活动创建",
                        "path": "operation",
                        "children": [],
                        "order": 4
                    },
                ],
                "order": 3
            }, {
                "id": 500,
                "authName": "订单管理",
                "path": "orders",
                "children": [{
                    "id": 510,
                    "authName": "订单列表",
                    "path": "orders",
                    "children": [],
                    "order": None
                }],
                "order": 4
            }, {
                "id": 600,
                "authName": "数据统计",
                "path": "reports",
                "children": [{
                    "id": 610,
                    "authName": "数据报表",
                    "path": "reports",
                    "children": [],
                    "order": None
                }],
                "order": 5
            }],
            "meta": {
                "msg": "获取菜单列表成功",
                "status": 200
            }
        }

    return HttpResponse(json.dumps(content),content_type='application/json')

def test_page(request):

    pagenum = request.GET.get('pagenum')
    perPage = request.GET.get('pagesize')
    query = request.GET.get('query')

    if(pagenum == None):
        pagenum = 1
    if(perPage == None):
        perPage = 10

    if query == '' or query is None:
        setUserInfo = models.ClientUser.objects.all()
    else:
        setUserInfo = models.ClientUser.objects.filter(u_nickname__contains=query)

    pagtor = Paginator(setUserInfo,per_page=perPage)

    pagesize = pagtor.num_pages

    total = pagtor.count

    pagedata = pagtor.page(pagenum).object_list

    # print("页面总数",pagesize)
    # print("当前页数据",(pagedata))
    # print("页面总数据",total)

    userInfoList = []
    userInfo = {}
    for i in pagedata:

        # 把获取的数据添加到 用户信息dict中
        userInfo['id'] = i.id
        userInfo['u_mobile'] = i.u_mobile
        userInfo['u_nickname'] = i.u_nickname
        userInfo['u_image'] = i.u_image
        userInfo['u_update_time'] = i.u_update_time
        userInfo['u_status'] = i.u_status

        # 使用list集合整页数据
        userInfoList.append(userInfo)
        userInfo = {}

    result = {'code':200,'data':{'pagesize':pagesize,'total':total,'userList':userInfoList},'msg':'success'}

    # print(userInfo)
    # print(userInfoList)
    # return HttpResponse(json.dumps({'test':'123'}),content_type='application/json')
    return HttpResponse(json.dumps(result),content_type='application/json')



def test_report(request):

    return render(request,'report_template.html')


from .utils.operation import Operation_tickets_Inc,Operation_tickets_Zh

def operation_ticket_create_zh(request):

    if request.method == 'GET':
        channel = request.GET.get('channel')
        operation_tickets = Operation_tickets_Zh(channel=channel)
        movieList = operation_tickets.getGoodsInfo()
        schedule_list = {"code": 0, "msg": "success", "data": []}
        for movieList_schedule in movieList['data']:
            if movieList_schedule['schedule'] == '特邀场':
                schedule_list['data'].append(movieList_schedule)

        return HttpResponse(json.dumps(schedule_list), content_type='application/json')

    if request.method == 'POST':

        # 获取json请求数据
        json_str = request.body
        json_data = json.loads(json_str)
        filmName = json_data['filmName']
        startTime = json_data['onlineStartTime']
        endTime = json_data['onlineEndTime'] - 100000000
        skuId = json_data['skuId']
        spuId = json_data['spuId']
        activityName = json_data['activityName']
        channel = json_data['channel']
        print(json_data)
        print(endTime)

        operation_tickets = Operation_tickets_Zh(channel=channel)
        # 生成票码
        createTicket = operation_tickets.getTiccketInfo(activityName,filmName,startTime,endTime,skuId,spuId)
        # 审核票
        getAuditInfo = operation_tickets.getAuditData()['data']['pageData']
        auditUserInfo = operation_tickets.getUserInfo()['data'][0]
        for audiInfo in getAuditInfo:
            if audiInfo['ownerId'] == auditUserInfo['userId']:
                operation_tickets.updateAuditData(audiInfo['id'],audiInfo['dateId'])

        return HttpResponse(json.dumps(createTicket),content_type='application/json')

def operation_ticket_create_inc(request):

    if request.method == 'GET':
        regionId = request.GET.get('regionId')
        channel = request.GET.get('channel')
        operation_tickets = Operation_tickets_Inc(regionId,channel=channel)
        movieList = operation_tickets.getGoodsInfo()
        schedule_list = {"code": 0,"msg": "success","data": []}
        for movieList_schedule in movieList['data']:
            if movieList_schedule['schedule'] == '特邀场':
                schedule_list['data'].append(movieList_schedule)

        return HttpResponse(json.dumps(schedule_list),content_type='application/json')


    if request.method == 'POST':
        regionId = '1'
        print(request)

        # 获取json请求数据
        json_str = request.body
        json_data = json.loads(json_str)
        filmName = json_data['filmName']
        startTime = json_data['onlineStartTime']
        endTime = json_data['onlineEndTime']
        skuId = json_data['skuId']
        spuId = json_data['spuId']
        activityName = json_data['activityName']
        channel = json_data['channel']

        operation_tickets = Operation_tickets_Inc(regionId,channel=channel)
        # 生成票码
        createTicket = operation_tickets.getTiccketInfo(activityName,filmName,startTime,endTime,skuId,spuId)
        # 审核票
        getAuditInfo = operation_tickets.getAuditData()['data']['pageData']
        auditUserInfo = operation_tickets.getUserInfo()['data'][0]
        for audiInfo in getAuditInfo:
            if audiInfo['ownerId'] == auditUserInfo['userId']:
                operation_tickets.updateAuditData(audiInfo['id'],audiInfo['dateId'])

        return HttpResponse(json.dumps(createTicket),content_type='application/json')

# Create your views here.
