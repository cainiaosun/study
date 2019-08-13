import sys,json
sys.path.append("..")
from base.datatable import DataTable
from util.write_log import Log
from jsonpath_rw import jsonpath,parse

class GetData:
    def __init__(self):
        pass

    # 获取一条案例的数据集合，并以字典的形式返回

    # 获取一条案例的所有请求数据，包含依赖案例

    # 获取token

    # 获取cookie

    def get_case_data(self,testcase):
        """
        # 获取一条案例的数据集合，并以字典的形式返回
        参数
            -testcase：案例名称或案例所在行
        """
        if isinstance(testcase,int):
            row=testcase
        else:
            row=DataTable().get_row(testcase)
        Case_ID = DataTable(column="Case_ID", row=row).value()
        is_excute = DataTable(column="是否执行", row=row).value()
        url = DataTable(column="url", row=row).value()
        method = DataTable(column="请求方式", row=row).value()
        is_headers = DataTable(column="is_headers", row=row).value()
        headers = DataTable(column="headers", row=row).value()
        depend_case = DataTable(column="依赖Case", row=row).value()
        depend_data = DataTable(column="依赖数据", row=row).value()
        depend_field = DataTable(column="依赖数据所属字段", row=row).value()
        data = json.loads(DataTable(column="请求数据", row=row).value())
        except_result = DataTable(column="预期结果", row=row).value()
        actual_result = DataTable(column="实际结果", row=row).value()
        excute_status = DataTable(column="执行状态", row=row).value()
        data = {
            "Case_ID": Case_ID,
            "is_excute":is_excute,
            "url": url,
            "method": method,
            "is_headers": is_headers,
            "headers":headers,
            "depend_case": depend_case,
            "depend_data": depend_data,
            "depend_field": depend_field,
            "data": data,
            "except_result":except_result,
            "actual_result":actual_result,
            "excute_status": excute_status
        }
        return data

    def get_request_data(self,testcase):
        """
        # 获取一条案例的所有请求数据，包含当前案例和依赖案例的所有请求数据
        参数
            --testcase：案例名称或案例所在行
        """
        list_01 = []
        request_data=self.get_case_data(testcase)
        def next_request_data(request_data):
            list_01.append(request_data)  # 将请求数据存储在list_01列表中
            #print(request_data)
            #print("依赖案例：",request_data["depend_case"])
            if request_data["depend_case"]:  # 存在依赖数据时，去获取依赖案例的请求数据
                row = DataTable().get_row(request_data["depend_case"])
                if row!=None:
                    request_data = self.get_case_data(row)
                    next_request_data(request_data)  # 递归执行，直至最后一个案例不存在依赖案例为止
                else:
                    msg="案例依赖关系错误："+request_data["Case_ID"] + "依赖的案例" + request_data["depend_case"] + "不存在"
                    Log().error(msg)
                    raise Exception(msg)
        next_request_data(request_data)  # 执行递归函数request
        list_01.reverse()
        return list_01  # 翻转请求数据列表，若案例a依赖b，b依赖c，翻转后数据对应：c,b,a

    def json_field(self,node,json_data):
        '''
        Find the corresponding value in the data source "jsonn_data" by a node "node".
            :param node:node,key[1].ch_key[2].sub_key
            :param json_data:a json_data,dict
            :return:find value,is a list
        '''
        json_exe = parse(node)
        male = json_exe.find(json.loads(json_data))
        para_value = [math.value for math in male]
        if para_value==[]:
            Log().warning("目标数据中没有node节点：json_field()")
        return para_value

class ModifyData:
    def __init__(self):
        pass

    def write_result(self,testcase,response_data):
        data=GetData().get_case_data(testcase)
        if data["is_excute"]=="否":
            DataTable("执行状态").set("跳过")
        else:
            except_result = json.loads(data["except_result"])
            actual_result = {}
            for key in except_result.keys():
                value = GetData().json_field(key, response_data)
                if value:
                    value = value[0]
                    actual_result[key] = value
            DataTable("实际结果").set(json.dumps(actual_result, indent=4))
            if actual_result == except_result:
                DataTable("执行状态").set("通过")
            else:
                DataTable("执行状态").set("失败")




if __name__=="__main__":
    DataTable.load("../case/testcase.xls")
    message={}
    case_data=GetData().get_case_data(2)
    message["case_data"]=case_data
    request_data=GetData().get_request_data(2)
    message["request_data"] = request_data
    print(DataTable().case_path)
    DataTable("实际结果").set("pass")
    json_data=json.dumps(message["case_data"]["data"])
    username=GetData().json_field("username",json_data)[0]
    message["username"] = username

    for key in message:
        print(key.ljust(13," ")+"=  "+str(message[key]))


