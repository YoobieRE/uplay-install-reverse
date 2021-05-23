import base64
import blackboxprotobuf
import zlib
from protobuf_inspector.types import StandardParser
from google.protobuf.json_format import MessageToJson
from google.protobuf.message import DecodeError
from google.protobuf import text_format
import protos.manifest_pb2 as Manifest
import json

def print_sample(plaintextBytes, cipher):
    plaintext = plaintextBytes.decode()
    sample = plaintextBytes[:300]
    print(cipher + ":\n" + sample)

MANIFEST_FILE = 'files/wdl_uplay_install.manifest'
PAYLOAD_START = 356

manifestBytes = open(MANIFEST_FILE, mode='rb').read()
base64KeyBytes = manifestBytes[12:356]
print('base64 key: ' + base64KeyBytes.decode())
decodedKeyBytes = base64.decodebytes(base64KeyBytes)

ciphertext = manifestBytes[PAYLOAD_START:]

# print('first byte:', hex(ciphertext[0]))

decompressed = zlib.decompress(ciphertext)

outFile = open(MANIFEST_FILE+'.pb', mode='wb')
outFile.write(decompressed)
outFile.close()

manifest = Manifest.Manifest()
manifest.ParseFromString(decompressed)
with open(MANIFEST_FILE + '.json', 'w') as jsfile:
    actual_json_text = MessageToJson(manifest)
    jsfile.write( actual_json_text )

# Types: https://github.com/ydkhatri/blackboxprotobuf/blob/master/blackboxprotobuf/lib/types/type_maps.py#L29
# typedef = json.loads(open('combined.typedef.json', mode='r').read())

# message, typedef = blackboxprotobuf.protobuf_to_json(decompressed, message_type=None, bytes_as_hex=False) # set to True when all strings are notated
# outFile = open(MANIFEST_FILE+'.json', mode='w')
# outFile.write(message)
# outFile.close()

# outFile = open('output.typedef.json', mode='w')
# outFile.write(json.dumps(typedef, indent=2))
# outFile.close()

# parser = StandardParser()
# with open(MANIFEST_FILE+'.pb', 'rb') as fh:
#    output = parser.parse_message(fh, "message")
# print(output)