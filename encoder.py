#create dictionary dict[index] = char
def encode_dict(): 
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()*+,-./'
    encodeDict, index = {}, 0
    for char in characters:
        encodeDict[index] = char
        index+=1
    return encodeDict

#convert char to index
def get_index(character): 
    encodeDict = encode_dict()
    for index, char in encodeDict.items():
        if character == char:
            return index

class encode:
    def __init__(self, plaintext, offsetkey):
        self.plaintext = plaintext
        self.offsetkey = offsetkey
    #convert plaintext to index
    def encodeText(self): 
        encodeDict = encode_dict()
        encodedIndexList = [get_index(self.offsetkey)]
        for char in self.plaintext: 
            if char == ' ':
                encodedIndexList.append(' ')
            else:
                index = (get_index(char))
                encodedIndex = index - get_index(self.offsetkey)
                if encodedIndex < 0:
                    encodedIndex += 44
                encodedIndexList.append(str(encodedIndex))
        #convert index to encodedtext
        encodedtext = ''
        for index in encodedIndexList:
            if index == ' ':
                encodedtext += ' '
            else:
                char = encodeDict[int(index)]
                encodedtext += char
        return encodedtext

class decode:
    def __init__(self, encodedtext):
        self.encodedtext = encodedtext
    #convert encodedtext to plaintext
    def decodeText(self):
        encodeDict = encode_dict()
        offset_key, self.encodedtext = get_index(self.encodedtext[0]), self.encodedtext[1:]
        plaintext = ''
        for char in self.encodedtext:
            if char == ' ':
                plaintext = plaintext + ' '
            else: 
                index = get_index(char)
                index += offset_key
                if index > 43:
                    index -= 44
                newChar = encodeDict[int(index)]
                plaintext += newChar
        return plaintext

text1,text2,text3 = encode('HELLO WORLD', 'B'), encode('HELLO WORLD', 'F'), encode('HELLO WORLD', 'X')
print (text1.encodeText())
print (text2.encodeText())
print (text3.encodeText())

encoded1,encoded2,encoded3 = decode('BGDKKN VNQKC'), decode('FC/GGJ RJMG.'), decode('X2Z669 /9*6Y')
print (encoded1.decodeText())
print (encoded2.decodeText())
print (encoded3.decodeText())