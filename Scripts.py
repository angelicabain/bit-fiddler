import csv
import random
import string as strin

def writeToCSV(data):
    with open('script-output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for item in data:
            if len(item) > 0:
                writer.writerow([item])
            else:
                writer.writerow([])


def createArray(string):
    stringLength = len(string)

    data = []

    emptyString = ''
    for i in range(0, stringLength):
        emptyString += ' '

    data.append(emptyString)

    while data[-1] != string:
        currString = data[-1]
        currArr = list(currString)
        for i in range(0, stringLength):

            #start with blanks
            if currArr[i] == ' ' and i != 3:
                if random.randint(0,20) == 0:
                    currArr[i] = str(random.choice((0,1)))
            #transition to 0,1
            elif currArr[i] == '0' or currArr[i] == '1':
                if random.randint(0,10) == 0:
                    currArr[i] = random.choice(strin.ascii_letters)
                else:
                    currArr[i] = str(random.choice((0,1)))

            #transition to letters
            elif currArr[i] != string[i]:
                if random.randint(0,20) == 0:
                    currArr[i] = string[i]
                else:
                    currArr[i] = random.choice(strin.ascii_letters)

        newString = ''.join(currArr)
        data.append(newString)

        #end with match




    print('Final data')
    for item in data:
        print(item)

    writeToCSV(data)




def createArrayOUTDATED(string):
    stringLength = len(string)
    data = ['']
    characters = list(string)
    

    currLen = 0
    while currLen < stringLength:
        binaryString = []
        for i in range (0, currLen + 1):
        
            if(random.randint(0,15) == 0):
                binaryString.append(random.choice(strin.ascii_letters))
            else:
                binaryString.append(str(random.randint(0,1)))
        
        if random.randint(0,5) == 0:
            currLen += 1

        data.append(''.join(binaryString))
        
        print(data[-1])

    # for i in range(0, stringLength):
    #     for k in range (0, random.randint(5, 10)):
    #         binaryString = []
    #         # for k in range (0, random.randint(10, 50)):
    #         for j in range (0,i + 1):
    #             binaryString.append(str(random.randint(0,1)))
    #         # print(binaryString)
    #         data.append(''.join(binaryString))
    #         print(data[-1])

    print('Done Starting Data')

    binaryString = data[-1]
    count = 0
    while binaryString != string:
        binArray = list(binaryString)
        for i in range(len(binArray)):

            if binArray[i] != string[i]:
                if random.randint(0,10) == 0:
                    binArray[i] = string[i]
                else:
                    if binArray[i] == '0' or binArray[i] == '1':
                        if random.randint(0,5) == 0:
                            binArray[i] = random.choice(strin.ascii_letters)
                        else:
                            binArray[i] = str(random.randint(0,1))
                    else:
                        if random.randint(0,50) == 0:
                            binArray[i] = string[i]
                        else:
                            binArray[i] = random.choice(strin.ascii_letters)

            #if not a match
            # if binArray[i] != string[i]:
            #     if random.randint(0,7) == 0:
            #         binArray[i] = string[i]
            #     else:
            #         binArray[i] = str(random.randint(0,1))


            # if is a match
            # else:
            #     if random.randint(0,7) == 0:
            #         if random.randint(0,1) == 0:
            #             binArray[i] = str(random.randint(0,1))
            #         else:
            #             binArray[i] = str(random.choice(string))


        binaryString = ''.join(binArray)
        data.append(binaryString)
        print(data[-1])
        count += 1

        
                

    



    print('Final data')
    for item in data:
        print(item)

    writeToCSV(data)


def main():
    string = 'Bit Fiddler'
    createArrayOUTDATED(string)


if __name__ == "__main__":
    main()