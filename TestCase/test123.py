dic = {
       "biz_data":
        {"is_reloan":1,
         "orderInfo":
             {"order_No":"257966423716870","order_no":"257966423716870","user_id":127023136,"id":75523384,"user_name":"高可可","register_time":1540782548,"status":80,"order_time":1547798574,"city":"上海","bank":"上海惠大网络科技有限公司","product":"闪借钱","product_id":10403937,"user_group_id":102955,"platform":"app","user_mobile":""
              },
         "applyDetail":
             {"platform":"android","device_num":"862859038940504","tele_num":"","tele_name":"","phone_brand":"HONOR","device_info":"PRA-AL00X","ip_address":"140.207.3.238","gps_location":"121.367202,31.224723","GPS_Address":"上海市浦东新区浦东大道1472号后门"
              },
         "addInfo":"",
        },
    "sign": "t9XNZXVv6Z7oh0Uevy0QoI/LPHUzM2D4vP2bZFX1RWTa78UWNXWRINJvcHJCqTRx+RfCq7sUU5AxL8aARNzT4jQEfhS9NhBsX0bFvslXTg+GfCvAJhp5X0XHaeAhmb2zdFveJ9vBDii8wkhUJCPWnDLZQ+6jVeTt9Xb83o8Q4mA="
}

print(dic['biz_data']['orderInfo'])
dic = sorted(dic['biz_data'].items())
print(dic)
