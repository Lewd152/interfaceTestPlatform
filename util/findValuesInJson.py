def traverseJson(json,value,ifcontains):
    if ifcontains == '包含':
        cjson = filteringJson()
        res = cjson.isExtend(json, value)
        # 最终返回True or False
        if res == True:
            return True
        if res == False:
            return False
    if ifcontains == '不包含':
        cjson = filteringJson()
        res = cjson.isExtend(json, value)
        # 最终返回True or False
        if res == True:
            return False
        if res == False:
            return True

class filteringJson(object):
    def getKeys(self,data):
        keysAll_list = []
        def getkeys(data):
            if (type(data) == type({})):
                keys = data.keys()
                for key in keys:
                    value = data.get(key)
                    if (type(value) != type({}) and type(value) != type([])):
                        keysAll_list.append(key)
                    elif (type(value) == type({})):
                        keysAll_list.append(key)
                        getkeys(value)
                    elif (type(value) == type([])):
                        keysAll_list.append(key)
                        for para in value:
                            if (type(para) == type({}) or type(para) == type([])):
                                getkeys(para)
                            else:
                                keysAll_list.append(para)
        getkeys(data)
        return keysAll_list

    def isExtend(self,data,tagkey):
        if(type(data)!=type({})):
            print('please input a json!')
        else:
            key_list=self.getKeys(data)
            for key in key_list:
                if(key==tagkey):
                    return True
        return False