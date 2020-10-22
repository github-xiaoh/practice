import logging
import time
import os
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.urls import reverse
from dwebsocket import accept_websocket

from HttpRunnerManager import settings
from . import models
import json
from django.core.paginator import Paginator
from django.utils.safestring import mark_safe
from ApiManager.views import login_check
from .utils.releasefilm import mediaGetfilmList, mediaSendFilm, mediaAddphoto, mediaAddvideo, mediaGetPostiticeTitle, \
    goodsGetpositive, goodsAddspu, goodsAddsku, goodsGetSku, goodsEditSkuChannel, goodsEditSkuEnvironment, \
    goodsEditSkuExamine, goodsEditSkuGoodsStatus, cmsFilmRelease, getTimes, mediaAddsource, goodsEditProduct, \
    getGuestData, getPreProSpuList, getRoomData, editRoom, editDrawerInfo, goodsUpdateSku, updateStatus
from .utils.fileOperation import openFile, newFile
from .utils.common import Page, setup_log
from .utils.operation import Coupon_create

# log_testTools = setup_log("testTools")
log_testTools = logging.getLogger('testTools')

logger = logging.getLogger('testTools')
# logger = setup_log("testTools")

# @login_check
def userInfo(request, page_page):
    """
    项目列表
    :param request:
    :param mobile,account
    :return:
    """

    if request.GET.get('user_phone') is None or request.GET.get is None:
        return render(request, 'account.html')
    else:

        mobile = request.GET.get('user_phone')
        user_name = request.GET.get('user_name')
        print('手机号：', mobile)
        print('昵称：', user_name)
        dictL = request.GET
        print('请求数据：', dictL)
        userinfo = models.ClientUser.objects.filter(
            u_mobile__contains=mobile, u_nickname__contains=user_name)

        print("查询的用户结果：", userinfo[0])
        # 循环便利获取查询结果
        # for i in userinfo:
        #     print("uId：", i.u_mobile)

        page = Page(
            request_url='userInfo',
            page_page=page_page,
            info_data=userinfo,
            mobile=mobile,
            user_name=user_name)
        htmlStr = page.html_str()
        page_data = page.page_data()

        context = {'code': 0, 'msg': 'success', 'data': [htmlStr, page_data]}
        print(context)
        return render(request, 'account.html', context)
        # return
        # HttpResponse(json.dumps(context),content_type="application/json")


# @login_check
def createfilm(request):
    """
    项目列表
    :param request:
    :param mobile,account
    :return:
    """

    if request.GET.get('film_name') is None or request.GET.get is None:
        context = {"toast": "暂未执行"}
        return render(request, 'create_film.html', context)

    else:

        filmName = request.GET.get('film_name')
        print(filmName)
        regionId = request.GET.get('region_Id')
        print(regionId)

        filmTime = getTimes()
        startTime = filmTime[0]
        endTime = filmTime[1]

        logger.info(
            "添加片源：{mediaAddsource}".format(
                mediaAddsource=mediaAddsource(
                    filmName, regionId)))
        # print("添加片源：", )

        mediaGetfilmlist = mediaGetfilmList(filmName, regionId)
        logger.info(
            "搜索影片列表：{mediaGetfilmlist}".format(
                mediaGetfilmlist=mediaGetfilmlist))
        # print("搜索影片列表：", mediaGetfilmlist)

        filmId = mediaGetfilmlist['data']['list'][0]['filmId']
        logger.info("依据搜索的影片列表查找影片ID：{filmId}".format(filmId=filmId))
        # print("依据搜索的影片列表查找影片ID：", filmId)

        logger.info(
            "在站点发布影片：{mediaSendFilm}".format(
                mediaSendFilm=mediaSendFilm(
                    filmId, filmName, regionId)))
        logger.info(
            "在站点发布影片：{mediaAddphoto}".format(
                mediaAddphoto=mediaAddphoto(
                    filmId, regionId)))
        logger.info(
            "为影片添加视频信息：{mediaAddvideo}".format(
                mediaAddvideo=mediaAddvideo(
                    filmId, regionId)))
        # print("在站点发布影片：", mediaSendFilm(filmId, filmName))
        # print("为影片添加图片信息：", mediaAddphoto(filmId))
        # print("为影片添加视频信息：", mediaAddvideo(filmId))
        # print("查找影片正片ID(废弃)：", mediaGetPostiticeTitle(filmId, filmName))

        goodsPositiveInfo = goodsGetpositive(filmId, regionId)['data'][0]
        logger.info(
            "影片正片片源信息：{goodsPositiveInfo}".format(
                goodsPositiveInfo=goodsPositiveInfo))
        # print("影片正片片源信息：",goodsPositiveInfo)

        if goodsPositiveInfo['positive']:
            goodsPositive = goodsPositiveInfo['positive'][0]['value']
            spuId = goodsGetpositive(filmId, regionId)['data'][0]['spuId']

            logger.info(
                "查找影片正片ID：{goodsPositive}".format(
                    goodsPositive=goodsPositive))
            logger.info("查找影片SpuID：{spuId}".format(spuId=spuId))
            logger.info(
                "添加商品SPU：{goodsAddspu}".format(
                    goodsAddspu=goodsAddspu(
                        filmId,
                        filmName,
                        startTime,
                        endTime,
                        regionId)))

            logger.info(
                "编辑商品SPU(打开投屏功能)：{goodsEditProduct}".format(
                    goodsEditProduct=goodsEditProduct(
                        spuId,
                        filmName,
                        startTime,
                        endTime,
                        regionId)))
            logger.info(
                "添加商品SKU：{goodsAddsku}".format(
                    goodsAddsku=goodsAddsku(
                        filmId,
                        filmName,
                        spuId,
                        goodsPositive,
                        startTime,
                        endTime,
                        regionId)))
            # print("查找影片正片ID：", goodsPositive)
            # print("查找影片SpuID", spuId)
            # print("添加商品SPU：", goodsAddspu(filmId, filmName, startTime, endTime))
            # print("添加商品SKU：", goodsAddsku(filmId, filmName, spuId, goodsPositive, startTime, endTime))

            skuId = goodsGetSku(spuId, regionId)['data']['list'][0]['skuId']

            # print("查找添加商品SkuID：", skuId)
            # print("编辑SKU发布渠道：", goodsEditSkuChannel(skuId))
            # print("编辑SKU发布环境：", goodsEditSkuEnvironment(skuId))
            # print("编辑SKU通过(预发)审核：", goodsEditSkuExamine(skuId))
            # print("编辑SKU发布上架：", goodsEditSkuGoodsStatus(filmId, skuId))
            # print("cms发布上线：", cmsFilmRelease(filmId))
            # print("添加成功")

            logger.info("查找添加商品SkuID：{skuId}".format(skuId=skuId))
            logger.info(
                "编辑SKU发布渠道：{goodsEditSkuChannel}".format(
                    goodsEditSkuChannel=goodsEditSkuChannel(
                        skuId, regionId)))
            logger.info(
                "编辑SKU发布环境：{goodsEditSkuEnvironment}".format(
                    goodsEditSkuEnvironment=goodsEditSkuEnvironment(
                        skuId, regionId)))
            logger.info(
                "编辑SKU通过(预发)审核：{goodsEditSkuExamine}".format(
                    goodsEditSkuExamine=goodsEditSkuExamine(
                        skuId, regionId)))
            logger.info(
                "编辑SKU发布上架：{goodsEditSkuGoodsStatus}".format(
                    goodsEditSkuGoodsStatus=goodsEditSkuGoodsStatus(
                        filmId, skuId, regionId)))

            cms_film_release = cmsFilmRelease(filmId, regionId)
            print(cms_film_release)
            if cms_film_release['msg'] == "服务器内部异常":
                logger.info("添加失败")
                print("添加失败")
            elif cms_film_release['msg'] == "success":
                logger.info("添加成功")
                print("添加成功")

            logger.info("cms发布上线：{cms_film_release}".format(
                cms_film_release=cms_film_release))

            context = {"toast": "添加成功"}

        else:
            context = {"toast": "影片正片片源为空，请添加片源"}

            logger.info("添加失败")
            # print("添加失败")

        return render(request, 'create_film.html', context)


# @login_check
def special_scene(request):

    if request.method == "GET":

        regionId = request.GET.get("regionId")
        logger.info("请求数据：{0}".format(request.GET))
        star_info_result = getGuestData(regionId)
        spu_list_result = getPreProSpuList(regionId)

        context = {'star_info': star_info_result['data'],'spu_list': spu_list_result['data'],"config_statis":"开始配置专场","regionId":regionId}
        # print(context)
        # context = {"star_info": "2", "spu_list": 3}

        return render(request,'special_scene.html',context)

    else:
        regionId = request.POST.get("region_Id")
        specialName = request.POST.get("special_name")
        userId = request.POST.get("star_user")
        filmId = request.POST.get("filmName")
        specialSynopsis = request.POST.get("special_synopsis")
        if userId  == "请选择" or filmId == "请选择":
            star_info_result = getGuestData(regionId)
            spu_list_result = getPreProSpuList(regionId)
            toast = "请选择场主或者影片"
            context = {'star_info': star_info_result['data'], 'spu_list': spu_list_result['data'],
                       "config_statis": "开始配置专场", "toast": toast,"regionId":regionId}
            return render(request,'special_scene.html',context)
        else:

            logger.info("请求数据：{0}".format(request.POST))

            regionId = regionId

            star_info_result = getGuestData(regionId)
            spu_list_result = getPreProSpuList(regionId)
            logger.info("场主用户列表：{star_info_result}".format(star_info_result=star_info_result))
            logger.info("影片信息列表：{spu_list_result}".format(spu_list_result=spu_list_result))

            for star in star_info_result['data']:
                if star['userId'] != int(userId):
                    request.session['msg'] = "没有匹配到userId"
                elif star['userId'] == int(userId):
                    userName = star['nickname']
                    for spu in spu_list_result['data']:
                        logger.info("====================进入影片呢循环====================")
                        if spu['filmId'] != int(filmId):
                            request.session['msg'] = "没有匹配到filmId"
                        elif spu['filmId']== int(filmId):
                            filmName = "한국어" + spu['filmName']
                            spuId = spu['spuId']
                            spuReleaseEndtime = spu['spuReleaseEndtime']
                            spuReleaseStartTime = spu['spuReleaseStartTime']

                            # 编辑场信息
                            room_info = editRoom(specialName, filmName, spuReleaseEndtime, spuReleaseStartTime, spuId,
                                                 filmId, userName, userId, regionId, int(round((time.time())) * 1000),specialSynopsis)
                            if room_info['msg'] == "获取影片正片信息为空":
                                logger.info("专场信息：{room_info}".format(room_info=room_info))
                                request.session['msg'] = "获取影片正片信息为空"
                                break
                            else:
                                # 获取场次ID
                                roomId = room_info['data']['id']
                                logger.info({"roomId:":roomId,"userName":userName,"filmName":filmName,"regionId":regionId})
                                logger.info("编辑场信息：{0}".format(editDrawerInfo(roomId, userName, filmName, regionId)))

                                # 获取专场列表信息，用于寻找skuId
                                special_list = getRoomData(filmId, regionId)
                                logger.info("专场列表信息：{special_list}".format(special_list=special_list))

                                special_info = special_list['data']['list']
                                logger.info("单个专场信息：{special_info}".format(special_info=special_info))

                                for room_id in special_info:
                                    # print("房间信息结果：", room_id)
                                    if room_id['roomId'] != roomId:
                                        request.session['msg'] = "没有匹配到roomId"
                                    elif room_id['roomId'] == roomId:
                                        sku_id = room_id['skuId']
                                        film_id = room_id['filmId']

                                        # print(sku_id, film_id)

                                        # 配置上线"预发"环境
                                        logger.info('配置上线"预发"环境：{0}'.format(goodsEditSkuEnvironment(sku_id, regionId)))

                                        # 审核通过
                                        logger.info('审核通过：{0}'.format(goodsEditSkuExamine(sku_id, regionId)))

                                        # 配置上线"线上"环境
                                        logger.info('配置上线"线上"环境：{0}'.format(goodsEditSkuEnvironment(sku_id, regionId)))

                                        # 配置绑定渠道
                                        logger.info('配置绑定渠道：{0}'.format(goodsEditSkuChannel(sku_id, regionId)))

                                        # 配置上架商品
                                        logger.info('配置上架商品：{0}'.format(goodsEditSkuGoodsStatus(film_id, sku_id, regionId)))

                                        # 查找正片信息ID
                                        logger.info("正片信息查询：{0}".format(goodsGetpositive(filmId, regionId)['data'][0]))
                                        goodsPositive = goodsGetpositive(filmId, regionId)['data'][0]['positive'][0]['value']
                                        logger.info("查找影片正片ID：{goodsPositive}".format(goodsPositive=goodsPositive))

                                        logger.info('修改商品价格：{0}'.format(
                                            goodsUpdateSku(spuId, filmId, filmName, sku_id, goodsPositive, spuReleaseStartTime,
                                                           spuReleaseEndtime)))
                                        # 配置专场上线
                                        logger.info('配置专场上线：{0}'.format(updateStatus(roomId, regionId)))
                                        request.session['msg'] = "配置成功"
                                        break

                            break
                    break
            request.session['url'] = reverse('sc_cms:special_scene')
            return redirect(reverse('sc_cms:redirect_page'))


def coupon_create(request):

    if request.method == "GET":

        content = {'toast':'请选择类型并提交创建','visibility':"none"}
        return render(request, 'create_operation.html',content)
    else:
        auditGenre = request.POST.get('auditGenre')
        print(request)
        print("票券类型：",auditGenre)

        print("执行票券创建")
        coupon = Coupon_create()

        if auditGenre == '1':
            print("创建兑换券")
            couponType = 0
            activity_data = coupon.coupon_duihuan_xilie()
        elif auditGenre == '2':
            print("定额券")
            couponType = 1
            activity_data = coupon.coupon_dinge_xilie()
        elif auditGenre == '3':
            print("立减券")
            couponType = 2
            activity_data = coupon.coupon_lijian_xilie()
        else:
            activity_data = {'code':200,'data':"活动创建失败，请宠幸创建"}

        activity = json.loads(activity_data['data'])
        activity_id = str(activity['activityId'])

        print(type(activity_id), activity_id)

        audit_list = coupon.audit_query_auditList()
        print(audit_list['data']['pageData'])
        for pageData in audit_list['data']['pageData']:
            print(pageData)
            if (pageData['dateId'] == activity_id):
                print("匹配活动ID成功")
                audit_id = pageData['id']
                coupon.audit_update(audit_id, activity_id, auditGenre)
                content = {'toast':'创建成功'}
                break

        activityData = coupon.activity_list(couponType)
        activityList = activityData['data']['list']
        for activity in activityList:
            if int(activity_id) == activity["activityId"]:
                content['visibility'] = "visible"
                content['redPacketCode'] = activity['redPacketCode']
                content['code'] = activity['code']
                print(activity['redPacketCode'],
                      "https://h5-us-test.smartcinema.com.cn/coupon-intl-us/index.html?couponCode=" + activity[
                          'redPacketCode'])
                print(activity['code'],
                      "https://h5-us-test.smartcinema.com.cn/exchange-common-intl-us/index.html?code=" + activity['code'])
                break



        return render(request,'create_operation.html',content)




# @login_check
def real_time_log(request):
    return render(request,'msg_status.html')

        # with open(settings.LOG_FILE, 'r', encoding='UTF-8') as f:
        #     log_length = len(f.readlines())
        #     time.sleep(1)
        # while True:
        #     with open(settings.LOG_FILE, 'r', encoding='UTF-8') as f:
        #         contents = f.readlines()
        #         length_tmp = len(contents)
        #     for i in range(log_length, length_tmp):
        #         req.websocket.send(contents[i].encode('utf-8'))
        #     log_length = length_tmp
        #     time.sleep(1)


# 日志请求文件
def ajax_file(request):
    dir_file = '/Users/chenhang/Desktop/pythonFile/python/untitled/practice/Django-program/HttpRunnerManager/logs/script.log'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = openFile(os.path.join(BASE_DIR,'logs/script.log'))
    # print(log_file)

    # log_file2 = str(log_file.decode('utf-8')).split('\\n')
    log_list = []
    for i in log_file:
        log_list.append(i.splitlines())

    return HttpResponse(json.dumps(log_list), content_type='application/json')





def ajax_logcat(request):

    name_dict = {
        'twz': 'Love python and Django',
        'zqxt': 'I am teaching Django',
        'toast': '这是一个提示文案'
    }

    regionId = request.GET.get("regionId")
    log_testTools.info("这是获取的区域ID：{0}".format(regionId))
    request.session['url'] = "/sc_cms/ajaxLogcat/"

    return render(request, 'ajax_logcat.html', name_dict)

def redirect_url(request):
    print("开始跳转")
    redirect_url_1 = reverse('sc_cms:redirectUrl')
    print(redirect_url_1)
    print(reverse('sc_cms:redirectUrl'))
    print(reverse('sc_cms:ajax_test'))
    print("跳转a-test.html页面")
    # return redirect(reverse('sc_cms:ajax_test'))
    return render(request,'a-test.html')


def ajax_req(request):

    if request.method == "POST":
        print("进入了ajax_req 请求")
        req = request.POST
        logger.info("请求数据：{req}".format(req=req))

        response = {
            "code": 200,
            "msg": "Succeeded",
            "data" : {
                'twz': 'Love python and Django',
                'zqxt': 'I am teaching Django'
            }
        }
        return HttpResponse(json.dumps(response), content_type='application/json')


def ajax_list(request):
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(a)
    return HttpResponse(json.dumps(a), content_type='application/json')


def ajax_dict(request):
    name_dict = {
        'twz': 'Love python and Django',
        'zqxt': 'I am teaching Django'}
    return HttpResponse(json.dumps(name_dict), content_type='application/json')


def ajax_add(request):

    if request.method == 'POST':

        i1 = request.POST.get("i1")
        i2 = request.POST.get("i2")

        print(request)
        print(i1, i2)

        result = int(i1) + int(i2)

        return HttpResponse(result)
    else:
        print(request)

        i1 = request.GET.get("a")
        i2 = request.GET.get("b")

        print(i1, i2)

        result = int(i1) + int(i2)

        return HttpResponse(result)


# Create your views here.
