import json
import hexdump

# {
#     "1": "bin\\BattlEye\\BEClient_x64.dll",
#     "2": "5236496",
#     "3": "0",
#     "4": [
#     "se\"\\xf8\\xf1\\xcb\\xe0'\\xea\\x99\\xdb7\\xda\fR\\xa75",             <- 736522C3B8C3B1C38BC3A027EE9C81C3AAC299C39B37C39A0C52C2A735
#     "\\xe1V\u0018-E\\xc5\\xd9\\xfaPSY\\xbe!\u0014xj\\xf0\\xd6\\xda\\xc6"    <- C3A156182D45C385C399C3BA505359C2BE2114786AC3B0C396C39AC386
#     ],
#     "6": "5238032",
#     "7": [
#     {
#         "1": "3145728",
#         "2": "3134093",
#         "3": "\\xfc}˼ j\\xee\\xe6\\x8a\\xe7\u001d\\xd9$`Yw\\xec\\xe2U"     <- C3BC7DCBBC206A7FC3AEC3A6C28AC3A71DC39924605977C3ACC3A255
#     },
#     {
#         "1": "2090768",
#         "2": "1769405",
#         "3": "Mn\\xb1\\xe5&ӆ\u0015TTb\\xd4%\\xd7#\\xcdS\\xealQ"             <- 4D6EB1E526D38615545462D425D723CD53EA6C51
#     }
#     ]
# },

# http://uplaypc-s-ubisoft.cdn.ubi.com/uplaypc/downloads/3515/slices_v3/d/4D6EB1E526D38615545462D425D723CD53EA6C51   Where does the `d` come from?
#         ?_tkn_=exp=1621790115
#         ~acl=/uplaypc/downloads/3515/slices_v3/d/4D6EB1E526D38615545462D425D723CD53EA6C51
#         ~data=e0ef48e3-1a89-419e-80c8-a008ef16379a
#         ~hmac=8ac6adf9e358dde281c067425a5782a9f90ff57169e9cdbb5494fc48fba07dda

hex_string = '4D6EB1E526D38615545462D425D723CD53EA6C51'

b = bytes.fromhex(hex_string)
j = {
    'b': b.decode('utf-8', 'replace')
}
print(json.dumps(j))

json_string = 'Mn\xb1\xe5&ӆ\u0015TTb\xd4%\xd7#\xcdS\xealQ'
string_bytes = bytes(json_string, 'utf-8')
print(hexdump.dump(string_bytes, sep=''))
# 4D6EC2B1C3A526D38615545462C39425C39723C38D53C3AA6C51
