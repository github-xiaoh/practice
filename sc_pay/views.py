from django.shortcuts import render
from sc_pay import models
from django.core.paginator import Paginator
from django.utils.safestring import mark_safe
from .utils.common import page_info

def account_balance(request,page_num):

    """
    项目列表
    :param request,page_num:
    :param userId,accountBalance
    :return:
    """
    userId = request.GET.get('userId')
    accountBalance = request.GET.get('accountBalance')
    regionId = request.GET.get('regionID')
    print('用户ID：', userId)
    print('充值影点数：', accountBalance)
    print('充值区域ID：', regionId)
    dictL = request.GET
    print('请求数据：', dictL)

    userinfo = models.PayAccountDetails.objects.filter(user_id=userId)
    print("查询的用户结果：", userinfo[0])
    if userinfo:
        rechange = models.PayAccountDetails.objects.filter(user_id=userId,is_del=1,region_id=regionId).update(account_balance=accountBalance)
        if rechange:
            print("充值成功")
        else:
            print("充值失败")

        # for i in userinfo:
        #     print("查询的用户影点数：", i.account_balance)

    pageInfo = page_info("account_balance",userinfo,page_num,userId,accountBalance)

    # id = models.ClientUser.objects.get(id=420)
    # context = model_to_dict(id)

    context = {'code': 0, 'msg': 'success', 'data2': pageInfo}
    print(context)
    return render(request, 'account.html', context)
    # return HttpResponse(json.dumps(context),content_type="application/json")


# Create your views here.
