# coding=utf-8
import unittest
import HTMLTestRunnerNew
import time

#生成报告  传入case
def runCaseReportHtml(caseModel,title,tester,description):
    # 存储测试用例
    suite = unittest.TestSuite()

    # 创建一个加载器
    loader = unittest.TestLoader()

    # 从测试模块里面去找测试用例
    suite.addTest(loader.loadTestsFromModule(caseModel))
    datetime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # 测试报告
    with open(str(datetime)+"report.html", 'wb') as file:
        runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                                  verbosity=2,
                                                  description=description,
                                                  title=title,
                                                  tester=tester)
        runner.run(suite)