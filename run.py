import base64
import pgpy


def print_sample(plaintextBytes, cipher):
    plaintext = plaintextBytes.decode()
    sample = plaintextBytes[:300]
    print(cipher + ":\n" + sample)

MANIFEST_FILE = 'files/wd1_uplay_install.manifest'
PAYLOAD_START = 361

manifestBytes = open(MANIFEST_FILE, mode='rb').read()
base64KeyBytes = manifestBytes[12:356]
print('base64 key: ' + base64KeyBytes.decode())
decodedKeyBytes = base64.decodebytes(base64KeyBytes)

ciphertext = manifestBytes[PAYLOAD_START:]

key, _ = pgpy.PGPKey.from_blob(decodedKeyBytes)
# key2, _ = pgpy.PGPKey.from_blob(base64KeyBytes)

print(key)

# rsaPub = RSA.import_key(decodedKeyBytes)
# dsaPub = DSA.import_key(decodedKeyBytes)
# eccPub = ECC.import_key(decodedKeyBytes)
# aesCyper = ChaCha20.new()

# rsaOaep = PKCS1_OAEP.new(rsaPub)
# rsaAes = AES.new(rsaPub)
# rsav15 = PKCS1_v1_5.new(rsaPub)
# rsaCc20 = ChaCha20.new(rsaPub)

# print_sample(aesCyper.decrypt(ciphertext), 'aesCyper')