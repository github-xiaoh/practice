import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os

from HttpRunnerManager.settings import EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD



def newFile(reportPath):
    #列举test_dir目录下的所有文件，结果以列表形式返回。
    lists=os.listdir(reportPath)
    #sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    #最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn:os.path.getmtime(reportPath+'/'+fn))
    #获取最新文件的绝对路径
    file_path=os.path.join(reportPath,lists[-1])
#    L=file_path.split('\\')
#    file_path='\\\\'.join(L)
    return file_path


def send_email_reports(receiver, html_report_path):
    if '@sina.com' in EMAIL_SEND_USERNAME:
        smtp_server = 'smtp.sina.com'
    elif '@163.com' in EMAIL_SEND_USERNAME:
        smtp_server = 'smtp.163.com'
    else:
        smtp_server = 'smtp.qq.com'

    subject = "接口自动化测试报告"

    with io.open(html_report_path, 'r', encoding='utf-8') as stream:
        send_file = stream.read()
    # print(send_file)

    att = MIMEText(send_file, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = "attachment;filename = TestReports.html"

    body = MIMEText("附件为定时任务生成的接口测试报告，请查收，谢谢！", _subtype='html', _charset='gb2312')

    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['from'] = EMAIL_SEND_USERNAME
    msg['to'] = receiver
    msg.attach(att)
    msg.attach(body)

    smtp = smtplib.SMTP_SSL(smtp_server,465)
    # smtp.connect(smtp_server)
    # smtp.starttls()
    smtp.login(EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD)
    smtp.sendmail(EMAIL_SEND_USERNAME, receiver.split(','), msg.as_string())
    smtp.quit()


# if __name__ == '__main__':
    # send_email_reports('##@qq.com, example@163.com', 'D:\\HttpRunnerManager\\reports\\2018-06-05 15-58-00.html')
    # send_email_reports('443990096@qq.com','/Users/chenhang/Desktop/pythonFile/python/untitled/practice/Django-program/HttpRunnerManager2/reports/1580196360.html')