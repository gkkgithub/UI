import requests,json

URL = 'http://47.100.11.197:7004/rong360/dataflow/loanentry/basic_push'
sign = '2f88aae6a3dff886c2c9fdea1626c17457ac25cdc744274c670930f94b00fa87d9a0dc67692391a146b5e9f3161e6a23a669a34dadb2f01bcb2db7188eaec5025b6cfcdd3dad53d47ba054789d4ec16990a2f70a3efb3719f22fd4aacd556f98d1195f78d5d240491af5b0e881139e01434860ee96f716dd91c192fbdbdcc7b0'
d1 = {"is_reloan":1,
         "orderInfo":
             {"order_No":"257966423716870","order_no":"257966423716870","user_id":127023136,"id":75523384,"user_name":"高可可","register_time":1540782548,"status":80,"order_time":1547798574,"city":"上海","bank":"上海惠大网络科技有限公司","product":"闪借钱","product_id":10403937,"user_group_id":102955,"platform":"app","user_mobile":"18989898899"
              },
         "applyDetail":
             {"user_id":"320926195511175276","platform":"android","device_num":"862859038940504","tele_num":"","tele_name":"","phone_brand":"HONOR","device_info":"PRA-AL00X","ip_address":"140.207.3.238","gps_location":"121.367202,31.224723","GPS_Address":"上海市浦东新区浦东大道1472号后门"
              },
         "addInfo":"",
        }

ddd = json.dumps(d1)
print(type(ddd))

data = {
    "biz_data":ddd
}

data['sign'] = sign
print(type(data))

print(data)
re = requests.post(url=URL,data=data)
print(re.json())
print(re.status_code)