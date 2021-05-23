import base64
import blackboxprotobuf
import zlib
from protobuf_inspector.types import StandardParser
import json

def print_sample(plaintextBytes, cipher):
    plaintext = plaintextBytes.decode()
    sample = plaintextBytes[:300]
    print(cipher + ":\n" + sample)

MANIFEST_FILE = 'files/wd1_uplay_install.manifest'
PAYLOAD_START = 356

manifestBytes = open(MANIFEST_FILE, mode='rb').read()
base64KeyBytes = manifestBytes[12:356]
print('base64 key: ' + base64KeyBytes.decode())
decodedKeyBytes = base64.decodebytes(base64KeyBytes)

ciphertext = manifestBytes[PAYLOAD_START:]

# print('first byte:', hex(ciphertext[0]))

decompressed = zlib.decompress(ciphertext)

outFile = open(MANIFEST_FILE+'.unzipped', mode='wb')
outFile.write(decompressed)
outFile.close()

typedef = json.loads(open('combined.typedef.json', mode='r').read())

message, typedef = blackboxprotobuf.protobuf_to_json(decompressed, message_type=typedef)
outFile = open(MANIFEST_FILE+'.json', mode='w')
outFile.write(message)
outFile.close()

outFile = open('output.typedef.json', mode='w')
outFile.write(json.dumps(typedef, indent=2))
outFile.close()

parser = StandardParser()
with open(MANIFEST_FILE+'.unzipped', 'rb') as fh:
   output = parser.parse_message(fh, "message")
# print(output)