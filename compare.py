import os

COMMON_MIN = 2

versions = [
    "1.0.00",
    "1.0.10",
    "1.1.00",
    "1.2.00",
    "1.2.20",
    "1.2.30",
    "1.2.40",
    "1.3.00",
    "1.3.22",
    "1.3.25",
    "1.3.30",
    "1.4.00",
    "1.4.02"]

files = []
largestFileSize = 0
for version in versions:
    filename = 'versions/uplay_install.manifest.' + version
    length = os.path.getsize(filename)
    if length > largestFileSize:
        largestFileSize = length
    files.append(open(filename, mode='rb'))

outFile = open('compare_out.txt', mode='w')

for curByte in range(largestFileSize):
    byteList = []
    for file in files:
        thisByte = file.read(1)
        if (thisByte != b''):
            byteList.append(thisByte)
    commonBytes = []
    commonBytesStrings = []
    for x in byteList:
        count = byteList.count(x)
        if count >= COMMON_MIN:
            if not x in commonBytes:
                commonBytes.append(x)
                commonBytesStrings.append(x.hex() + ' X' + str(count))

    if len(commonBytes) > 0:
        commonBytesStrings.sort()
        outFile.write('0x' + hex(curByte)[2:].zfill(6) + ': ' + str(commonBytesStrings) + '\n')
        # print(hex(curByte) + ': ', commonBytes)

