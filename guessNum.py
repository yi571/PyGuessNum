import random

x = list(range(1,10))   #產生1~9的list
j = 0                   #打亂list的迴圈用變數
enterTime = 0           #猜測次數

while j<1000:           #打亂用迴圈

    i = random.randint(0,8)  #產生兩個隨機位置進行互換
    k = random.randint(0,8)
    #y = x[i]
    #z = x[k]
    x[i],x[k] = x[k],x[i]
    a = x
    j = j+1
#print(a[:4])

n = 1
while n == 1:           #遊戲迴圈
    inputNum =  input("請輸入4個1~9不重複的數字：\n")  #玩家輸入
    m = 0                                              #檢查重複用變數
    while m < len(inputNum):                           #檢查輸入是否重複迴圈
        if inputNum[m] in inputNum[m + 1 :]:
            print("你輸入的不是4個1~9不重複的數字！")
            break
        else:
            if inputNum.isdigit() is True and len(inputNum) == 4:   #檢查是否是數字及長度

                #print(inputNum)

                oneNum = int(inputNum[0:1])
                twoNum = int(inputNum[1:2])
                threeNum = int(inputNum[2:3])
                fourNum = int(inputNum[3:4])

                aNum = 0
                if oneNum == a[0]:
                    aNum = aNum + 1
                if twoNum == a[1]:
                    aNum = aNum + 1
                if threeNum == a[2]:
                    aNum = aNum + 1
                if fourNum == a[3]:
                    aNum = aNum + 1

                bNum = 0
                if oneNum == a[1] or oneNum == a[2] or oneNum == a[3]:
                    bNum = bNum + 1

                if twoNum == a[0] or twoNum == a[2] or twoNum == a[3]:
                    bNum = bNum + 1

                if threeNum == a[0] or threeNum == a[1] or threeNum == a[3]:
                    bNum = bNum + 1

                if fourNum == a[0] or fourNum == a[1] or fourNum == a[2]:
                    bNum = bNum + 1
                print(str(aNum) + "A" + str(bNum)+"B")

                enterTime += 1

                if  aNum == 4:
                    print("猜對了！")
                    print("一共猜了" + str(enterTime) + "次")
                    n = 0
                    break
                else:
                    n = 1

            else:
                print("你輸入的不是4個1~9不重複的數字！")
        break
    