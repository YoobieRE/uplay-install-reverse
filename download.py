# want http://uplaypc-s-ubisoft.cdn.ubi.com/uplaypc/downloads/3453/slices_v3/i/9201CEF18311615DE050F5F17D0A54F646BC5F50?_tkn_=exp=1643487323~acl=/uplaypc/downloads/3453/slices_v3/i/9201CEF18311615DE050F5F17D0A54F646BC5F50~data=e0ef48e3-1a89-419e-80c8-a008ef16379a~hmac=d86afde686e67dfba039ae8a08d63eea294e758108535d8422aa4e78733c3365
# out: http://uplaypc-s-ubisoft.cdn.ubi.com/uplaypc/downloads/3453/slices_v3/i/9201CEF18311615DE050F5F17D0A54F646BC5F50?_tkn_=exp=1643487401~acl=/uplaypc/downloads/3453/slices_v3/i/9201CEF18311615DE050F5F17D0A54F646BC5F50~data=e0ef48e3-1a89-419e-80c8-a008ef16379a~hmac=a6ea693e3a59f507b451459f03031528a0881d8e191d64bf1b99cc0dbe962ad4
import base64
from akamai.edgeauth import EdgeAuth

# NOTE: still can't find a valid encryption key
# ET_ENCRYPTION_KEY = '9201CEF18311615DE050F5F17D0A54F646BC5F50'
ET_ENCRYPTION_KEY = base64.b64decode('BKNesIH1lRGN1gXU9tq/1DJHdjQpKXx0sVuyyNfa8viGfoVZR7Sszcsx6DiD3dYWxuVCiXncIqniOebBRv01Aw==').hex()

ET_HOSTNAME = 'uplaypc-s-ubisoft.cdn.ubi.com'
DEFAULT_WINDOW_SECONDS = 500 # seconds
USER_ID = 'e0ef48e3-1a89-419e-80c8-a008ef16379a'
FILE_PATH = '/uplaypc/downloads/3453/slices_v3/i/9201CEF18311615DE050F5F17D0A54F646BC5F50'

et = EdgeAuth(**{'key': ET_ENCRYPTION_KEY,
                  'window_seconds': DEFAULT_WINDOW_SECONDS, 'payload': USER_ID, 'token_name': '_tkn_'})
token = et.generate_acl_token(FILE_PATH)
url = "http://{0}{1}?{2}={3}".format(ET_HOSTNAME, FILE_PATH, et.token_name, token)
print(url)