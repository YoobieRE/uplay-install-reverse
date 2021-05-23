import base64

import zlib


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

outFile = open(MANIFEST_FILE+'.unzipped', mode='wb')
outFile.write(decompressed)
outFile.close()
