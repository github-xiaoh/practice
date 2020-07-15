import logging
import time

from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from dwebsocket import accept_websocket

from HttpRunnerManager import settings
from . import models
import json
from django.core.paginator import Paginator
from django.utils.safestring import mark_safe
from ApiManager.views import login_check
from .utils.releasefilm import mediaGetfilmList, mediaSendFilm, mediaAddphoto, mediaAddvideo, mediaGetPostiticeTitle, \
    goodsGetpositive, goodsAddspu, goodsAddsku, goodsGetSku, goodsEditSkuChannel, goodsEditSkuEnvironment, \
    goodsEditSkuExamine, goodsEditSkuGoodsStatus, cmsFilmRelease, getTimes, mediaAddsource, goodsEditProduct
from .utils.fileOperation import openFile, newFile
from .utils.common import Page


logger = logging.getLogger('HttpRunnerManager')


@login_check
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


@login_check
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


@login_check
def special_scene(request):

    if request.GET.get is None:
        return render(request,'special_scene.html')

    else:
        return render(request,'special_scene.html')




@accept_websocket
def real_time_log(request):
    if request.is_websocket():
        print('收到websocket请求')

        log_file = openFile(
            '/Users/chenhang/Desktop/pythonFile/python/untitled/practice/Django-program/HttpRunnerManager/logs/all.log')

        data = {"log_file": log_file}

        return render(request, 'ajax_logcat.html', data)

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


def ajax_logcat(request):

    name_dict = {
        'twz': 'Love python and Django',
        'zqxt': 'I am teaching Django'}

    return render(request, 'ajax_logcat.html', name_dict)


def ajax_list(request):
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(a)
    return HttpResponse(json.dumps(a), content_type='application/json')


def ajax_dict(request):
    name_dict = {
        'twz': 'Love python and Django',
        'zqxt': 'I am teaching Django'}
    return HttpResponse(json.dumps(name_dict), content_type='application/json')


def ajax_file(request):

    log_file = openFile(
        '/Users/chenhang/Desktop/pythonFile/python/untitled/practice/Django-program/HttpRunnerManager/logs/script.log')
    # print(log_file)

    # log_file2 = str(log_file.decode('utf-8')).split('\\n')
    log_list = []
    for i in log_file:
        log_list.append(i.splitlines())

    return HttpResponse(json.dumps(log_list), content_type='application/json')


def ajax_add(request):

    i1 = request.POST.get("i1")
    i2 = request.POST.get("i2")

    print(request)
    print(i1, i2)

    result = int(i1) + int(i2)

    return HttpResponse(result)

# Create your views here.
