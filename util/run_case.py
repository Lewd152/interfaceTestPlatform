# coding=utf-8
import json

from util import findValuesInJson
from util.aSingleInterfaceAutomation import requestInterface
from util.reportHtml import *

class TestMathMethod (unittest.TestCase):

    def test01(caseUrl,caseMethod,caseHeader,caseParam,caseCheckValue,caseChecktype):
        res = requestInterface(url=caseUrl, method=caseMethod, headers=caseHeader, data=caseParam)
        date = json.loads(res)
        ress = findValuesInJson.traverseJson(date, caseCheckValue, caseChecktype)
        return ress