#create dictionary dict[index] = char
def encode_dict(): 
    file = open("encode.txt")
    encodeDict = {}
    index = 0
    for line in file:
        value = line.strip('\n')
        encodeDict[index] = value
        index+=1
    return encodeDict

#convert char to index
def get_key(char): 
    encodeDict = encode_dict()
    for index, value in encodeDict.items():
        if char == value:
            return index

class encode:
    #convert plaintext to index
    def encodeText(plaintext): 
        encodeDict = encode_dict()
        # Offset character index: B = 1, F = 5, etc.
        offset_key = 1
        encodedIndexList = [offset_key]
        for char in plaintext: 
            if char == ' ':
                encodedIndexList.append(' ')
            else:
                index = (get_key(char))
                encodedIndex = index - offset_key
                if encodedIndex < 0:
                    encodedIndex = encodedIndex + 44
                encodedIndexList.append(str(encodedIndex))
        #convert index to encodedText
        encodedText = ''
        for index in encodedIndexList:
            if index == ' ':
                encodedText = encodedText + ' '
            else:
                char = encodeDict[int(index)]
                encodedText = encodedText + char
        return encodedText

class decode:
    def decodeText(encodedText):
        encodeDict = encode_dict()
        offset_key = get_key(encodedText[0])
        encodedText = encodedText[1:]
        plaintext = ''
        for i in encodedText:
            if i == ' ':
                plaintext = plaintext + ' '
            else: 
                index = get_key(i)
                index = index + offset_key
                if index > 43:
                    index = index - 44
                char = encodeDict[int(index)]
                plaintext = plaintext + char
        return plaintext


print(encode.encodeText('HELLO WORLD'))
print(decode.decodeText('FC/GGJ RJMG.'))
print(decode.decodeText('BGDKKN VNQKC'))