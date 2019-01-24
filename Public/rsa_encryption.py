import rsa,json


def ByteToHex(bins):
    return ''.join(["%02x" % x for x in bins]).strip()

def HexToByte(hexStr):
    return bytes.fromhex(hexStr)

ASNKEY = """-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQDwjs1tCSFINTS6KA4kIOjFyolFLYMUedpHaih8ALzFXbcKtYt/
O1b2AcriptgVY6vlCWowK7xGDwwcnlPJ1O4CRyP8xMdhTqfdBHMgMM1yliRnNugg
ptoRF0bm1mtSD7ySHFaNq3X2mxzoFDZxOcPI6mBx5GcjLntUQSbsAw16JwIDAQAB
AoGAIrsbYaCt03ULFc1urTyrHtNtGjXF9RDauPDUw4J/vqcXJE6tw0LX/VCo8CxS
ilQHn1vKnwXRevP1NbSOOFervRTGdlbvcaNwp2aG5G3zGZ7Wa63x1AgeH8HCqZKU
1tEmX/i+aZCcjr15TafmiTR3g45UgZCBbM45tzavp0hUf6ECQQD+UWkgdL+dNWYH
UUtt9opH0ujuGL+Q7vtRztZce6Yjv4WPP16dLhvFydRW+8EK/34pZ3iwqAKpekcI
Z1o8uw4vAkEA8iYYH1LHRsk8hEtBH32U3kDCStNUeqtKlkXQKJiRn8SGz+hQr2uj
zScN3NMynhuuUpWFGzUbqLQRDX1ySE2NiQJBAMsiRcEZ3693Zn5zzbcQlJUX/tun
QuRGLtHCT3Bhh2vIX6ryp+UOXjqWopez0RayypfRwRIBsNakB7bLrsUReBsCQC4n
7LkrwihP+2UMIyGpglLK7T3uAlBPjiwOqprSWg+mGjxO//IwBkz4gL/y0dcpV5UO
QwzolpkVmZqEqt/1SGECQDHHknlTxWYrgH9sUmlcr+MI4vKOVlurMUrv/JhLNz9F
SDnsyKdVNdUBy5eXZKsp1bfYF/FawDbWaue3zGN8r1U=
-----END RSA PRIVATE KEY-----"""
# print(ASNKEY)
private_key = rsa.PrivateKey.load_pkcs1(ASNKEY)


print(type(private_key))

d1 = {"is_reloan":1,
         "orderInfo":
             {"order_No":"257966423716870","order_no":"257966423716870","user_id":127023136,"id":75523384,"user_name":"高可可","register_time":1540782548,"status":80,"order_time":1547798574,"city":"上海","bank":"上海惠大网络科技有限公司","product":"闪借钱","product_id":10403937,"user_group_id":102955,"platform":"app","user_mobile":"18989898899"
              },
         "applyDetail":
             {"user_id":"320926195511175276","platform":"android","device_num":"862859038940504","tele_num":"","tele_name":"","phone_brand":"HONOR","device_info":"PRA-AL00X","ip_address":"140.207.3.238","gps_location":"121.367202,31.224723","GPS_Address":"上海市浦东新区浦东大道1472号后门"
              },
         "addInfo":"",
        }

ds = json.dumps(d1)
print(type(ds))

data = {
    "biz_data":ds
}

dic_list = sorted(data.items())
tmp_str = ''
print(dic_list)
for num in range(len(dic_list)):
    first_str = str(dic_list[num][0])
    last_str = str(dic_list[num][1])
    tmp_str += first_str + '=' + last_str
    if num != len(dic_list) -1:
        tmp_str += '&'

print(dic_list)
print(tmp_str)

signtrue = rsa.sign(tmp_str.encode(),private_key,'SHA-1')
print(signtrue)
signtrue = ByteToHex(signtrue)
print(signtrue)


