from PIL import Image
def toBinary(text):
    binaryResult = ""
    for x in text:
        toBin = format(ord(x), 'b')
        while(len(toBin) < 8):
            toBin = '0'+ toBin
        binaryResult = binaryResult + toBin
    return binaryResult + '0111110001111100'  #ADDS END KEY, '||'  IN BINARY


def toChar(binaryData):
    try:
        decimalData = int(binaryData,2)
    except(ValueError):
        return '|'
    charData = chr(decimalData)
    return str(charData)

userChoice = input("Hello and welcome to my app for image steganograpy: \nType 0 for overwriting information on a photo\nType 1 for reading an image\nType 2 for information\nYour input: ")


if(userChoice == "0"):
    # START START START START START START START START 
    userPicture = input("Enter the photo's name + file extension:\n")
    img = Image.open(f'C:\\xampp\\htdocs\\121223044\\1_VPRupr\\test\\{userPicture}')
    # getFirstColor = img.getpixel((0,0))[0] GET THE FIRST COLOR OF A PIXEL
    userInput = input("Enter the information you are trying to hide :)\n")
    binaryResult = toBinary(userInput)
    for x in range(0,len(binaryResult)):
        curRedPixel = img.getpixel((0,x))[0]
        curGreenPixel = img.getpixel((0,x))[1]
        curBluePixel = img.getpixel((0,x))[2]
        redPixelDec = curRedPixel % 10
        if binaryResult[x] == '0':
            img.putpixel((x,0),((curRedPixel - redPixelDec),curGreenPixel,curBluePixel))
        else:
            img.putpixel((x,0),((curRedPixel - redPixelDec) + 1,curGreenPixel,curBluePixel))
    newData = img.getdata()
    newImage = Image.new(img.mode,img.size)
    newImage.putdata(newData)
    newImage.save("C:\\xampp\\htdocs\\121223044\\1_VPRupr\\test\\result.png")
    # END END END END END END END END END END END END END

elif(userChoice == "1"):

    userPicture = input("Enter the photo's name + file extension:\n")
    img = Image.open(f'C:\\xampp\\htdocs\\121223044\\1_VPRupr\\test\\{userPicture}')
    filePointer = 1
    exitVerify = 0
    exitValue = ""
    resultString = ""
    binaryData = ""


    while(exitValue != '||'):
        curRedPixel =(img.getpixel((filePointer-1,0))[0])%10
        binaryData = binaryData + str(curRedPixel)
        if (filePointer % 8 == 0):
            if(toChar(binaryData) != '|'):
                resultString = resultString + toChar(binaryData)
                binaryData = ""
            else:
                if(toChar(binaryData) != '|'):
                    resultString = resultString + toChar(binaryData)
                    binaryData = "" 
                    exitValue = ""
                else:
                    exitValue = exitValue + toChar(binaryData)
                    binaryData = ""
        filePointer += 1
    if(resultString == ''):
        print("This picture has no hidden message in it!")
    else:
        print(resultString)

elif(userChoice == "2"):
    print("Steganography is the technique of hiding data within an ordinary, nonsecret file or message to avoid detection; the hidden data is then extracted at its destination. Steganography use can be combined with encryption as an extra step for hiding or protecting data. If you choose option 0 you will have to choose which picture to edit and enter the desired prompt. If you decide that you want option 1 you will again have to enter the file name and you will receive the hidden message")


