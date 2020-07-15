# -*- coding:utf-8 -*-

from django.core.paginator import Paginator
from django.utils.safestring import mark_safe




def page_info(url,modelsInfo,page_num,userId,accountBalance):

    paginator = Paginator(modelsInfo, 5)
    page_data = paginator.page(page_num)
    page_sum = paginator.num_pages
    # print('page：',page[0])
    # print('page：', page)
    # for j in range(0,len(page)):
    #     print('page:',page[j].u_mobile)

    # 获取总的页数
    print('获取总的页数：', page_sum)
    # 生成页码代码html
    htmlStr = ''
    if url=="account_balance":

        for i in range(1, page_sum + 1):
            htmlStr = htmlStr + '<li>' + '<a href="' + '/account/' + str(
                i) + '/?userId=' + userId + '&accountBalance=' + accountBalance + '">' + str(i) + '</a></li>'

        page_first = '<li><a href="/account/1' + '/?userId=' + userId + '&accountBalance=' + accountBalance + '">' + '首页</a></li>'
        page_last = '<li><a href="/account/' + str(
            page_sum) + '/?userId=' + userId + '&accountBalance=' + accountBalance + '">尾页</a></li>'
        htmlStr = mark_safe(page_first + htmlStr + page_last)
        print(htmlStr)

        return [htmlStr,page_data]
    else:
        return "输入正确的url"