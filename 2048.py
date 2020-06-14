
#包含模块
import random
import msvcrt
 
#变量声明
MainL = [ [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0] ]
Victory_flag = 0
unchanged_flag = 0
 
##函数声明
#打印
def PrintData():
    print("—————————————————")
    for row in range(0, 4):
        print("|", end = " ")
        for col in range(0, 4):
            if(MainL[row][col] != 0):
                print("%5d |"%(MainL[row][col]), end = " "),
            else:
                print("      |", end = " "),
        print()
        print("—————————————————")
        
    return
 
#游戏开始初始化
def GameInit():
    #在两个位置随机生成两个数字“2”
    RandomNum1 = random.randint(0, 15)
    RandomNum2 = random.randint(0, 15)
    while RandomNum2 == RandomNum1:
        RandomNum2 = random.randint(0, 15)
        
    row = (int)(RandomNum1/4)
    col = RandomNum1%4
    MainL[row][col] = 2
 
    row = (int)(RandomNum2/4)
    col = RandomNum2%4
    MainL[row][col] = 2
    
    return
 
#每操作一次随机在一个为0的位置生成"2"
def DataRefresh():
    global Victory_flag
    #记录为值为0元素的个数
    count = 0
    #记录为0的元素的索引的列表
    ZeroL = [0]*16
    ZeroL1 = [0]*16    
    for index in range(0, 16):
        row = (int)(index/4)
        col = index%4
        if MainL[row][col] == 0:
            ZeroL[count] = index
            count += 1
            
    ZeroL1 = ZeroL[:]
    for i in ZeroL:
        if i == 0:
            ZeroL1.remove(i)
    ZeroL = ZeroL1
 
    if len(ZeroL) == 0:
        Victory_flag = 2
    else:
        RandomIndex = random.randint(0, len(ZeroL)-1)
        row = (int)(ZeroL[RandomIndex]/4)
        col = ZeroL[RandomIndex]%4
        MainL[row][col] = 2
 
    return
 
#按下"w"键 
def UpKey():
    global unchanged_flag
    for col in range(0, 4):        
        ##一、合0个数
        #1
        #0X00 ==> X000
        if MainL[0][col] == 0 and MainL[1][col] != 0 and MainL[2][col] == 0 and MainL[3][col] ==0:
            MainL[0][col] = MainL[1][col]
            MainL[1][col] = 0
            MainL[2][col] = 0
            MainL[3][col] = 0
        #2
        #00X0 ==> X000
        elif MainL[0][col] == 0 and MainL[1][col] == 0 and MainL[2][col] != 0 and MainL[3][col] ==0:
            MainL[0][col] = MainL[2][col]
            MainL[1][col] = 0
            MainL[2][col] = 0
            MainL[3][col] = 0            
        #3
        #000X ==> X000
        elif MainL[0][col] == 0 and MainL[1][col] == 0 and MainL[2][col] == 0 and MainL[3][col] !=0:
            MainL[0][col] = MainL[3][col]
            MainL[1][col] = 0
            MainL[2][col] = 0
            MainL[3][col] = 0          
        #4
        #0XX0 ==> XX00
        elif MainL[0][col] == 0 and MainL[1][col] != 0 and MainL[2][col] != 0 and MainL[2][col] != MainL[1][col] \
             and MainL[3][col] ==0:
            MainL[0][col] = MainL[1][col]
            MainL[1][col] = MainL[2][col]
            MainL[2][col] = 0
            MainL[3][col] = 0
        #5
        #0X0X ==> XX00
        elif MainL[0][col] == 0 and MainL[1][col] != 0 and MainL[2][col] == 0 and MainL[3][col] !=0 \
             and MainL[3][col] != MainL[1][col] :
            MainL[0][col] = MainL[1][col]
            MainL[1][col] = MainL[3][col]
            MainL[2][col] = 0
            MainL[3][col] = 0        
        #6
        #00XX ==> XX00
        elif MainL[0][col] == 0 and MainL[1][col] == 0 and MainL[2][col] != 0 and MainL[3][col] !=0 \
             and MainL[3][col] != MainL[2][col] :
            MainL[0][col] = MainL[2][col]
            MainL[1][col] = MainL[3][col]
            MainL[2][col] = 0
            MainL[3][col] = 0     
        #7
        #0XXX ==> XXX0
        elif MainL[0][col] == 0 and MainL[1][col] != 0 and MainL[2][col] != 0 and MainL[3][col] !=0 \
             and MainL[3][col] != MainL[2][col] and MainL[1][col] != MainL[2][col]:
            MainL[0][col] = MainL[1][col]
            MainL[1][col] = MainL[2][col]
            MainL[2][col] = MainL[3][col]
            MainL[3][col] = 0     
        #8
        #X0X0 ==> XX00
        elif MainL[0][col] != 0 and MainL[1][col] == 0 and MainL[2][col] != 0 and MainL[3][col] ==0 \
             and MainL[2][col] != MainL[0][col]:
            MainL[0][col] = MainL[0][col]
            MainL[1][col] = MainL[2][col]
            MainL[2][col] = 0
            MainL[3][col] = 0
        #9
        #X00X ==> XX00
        elif MainL[0][col] != 0 and MainL[1][col] == 0 and MainL[2][col] == 0 and MainL[3][col] !=0 \
             and MainL[3][col] != MainL[0][col]:
            MainL[0][col] = MainL[0][col]
            MainL[1][col] = MainL[3][col]
            MainL[2][col] = 0
            MainL[3][col] = 0
        #10
        #X0XX ==>XXX0
        elif MainL[0][col] != 0 and MainL[1][col] == 0 and MainL[2][col] != 0 and MainL[3][col] !=0 \
             and MainL[3][col] != MainL[2][col] and MainL[0][col] != MainL[2][col]:
            MainL[0][col] = MainL[0][col]
            MainL[1][col] = MainL[2][col]
            MainL[2][col] = MainL[3][col]
            MainL[3][col] = 0
        #11
        #XX0X ==> XXX0
        elif MainL[0][col] != 0 and MainL[1][col] != 0 and MainL[2][col] == 0 and MainL[3][col] !=0 \
             and MainL[3][col] != MainL[1][col] and MainL[1][col] != MainL[0][col]:
            MainL[0][col] = MainL[0][col]
            MainL[1][col] = MainL[1][col]
            MainL[2][col] = MainL[3][col]
            MainL[3][col] = 0
 
        ##二、合1个数
        #1
        #440X ==>8X00
        elif MainL[0][col] != 0 and MainL[1][col] == MainL[0][col] and MainL[2][col] == 0 and MainL[3][col] != 0:
            MainL[0][col] *= 2
            MainL[1][col] = MainL[3][col]
            MainL[2][col] = 0
            MainL[3][col] = 0   
        #2
        #44XX ==>8XX0
        elif MainL[0][col] != 0 and MainL[1][col] == MainL[0][col] and (MainL[2][col] != MainL[3][col] or (MainL[2][col]==0 and MainL[3][col]==0)):
            MainL[0][col] *= 2
            MainL[1][col] = MainL[2][col]
            MainL[2][col] = MainL[3][col]
            MainL[3][col] = 0        
        #3
        #404X ==> 8X00
        elif MainL[0][col] != 0 and MainL[1][col] == 0 and MainL[2][col] == MainL[0][col]:
            MainL[0][col] *= 2
            MainL[1][col] = MainL[3][col]
            MainL[2][col] = 0
            MainL[3][col] = 0
        #4
        #4004 ==> 8000
        elif MainL[0][col] != 0 and MainL[1][col] == 0 and MainL[2][col] == 0 and MainL[3][col] == MainL[0][col]:
            MainL[0][col] *= 2
            MainL[1][col] = 0
            MainL[2][col] = 0
            MainL[3][col] = 0
        #5
        #044X ==> 8X00
        elif MainL[0][col] == 0 and MainL[1][col] != 0 and MainL[2][col] == MainL[1][col]:
            MainL[0][col] = MainL[1][col];  MainL[0][col] *= 2
            MainL[1][col] = MainL[3][col]
            MainL[2][col] = 0
            MainL[3][col] = 0
        #6
        #0404 ==> 8000
        elif MainL[0][col] == 0 and MainL[1][col] != 0 and MainL[2][col] == 0 and MainL[3][col] == MainL[1][col]:
            MainL[0][col] = MainL[1][col];  MainL[0][col] *= 2
            MainL[1][col] = 0
            MainL[2][col] = 0
            MainL[3][col] = 0
        #7
        #X44X ==> X8X0
        elif MainL[0][col] != 0 and MainL[1][col] != 0 and MainL[2][col] == MainL[1][col] and MainL[0][col] != MainL[1][col]:
            MainL[0][col] = MainL[0][col]
            MainL[1][col] *=2
            MainL[2][col] = MainL[3][col] 
            MainL[3][col] = 0
        #8
        #X404 ==> X800
        elif MainL[0][col] != 0 and MainL[1][col] != 0 and MainL[2][col] == 0 and MainL[3][col] == MainL[1][col] \
             and MainL[0][col] != MainL[1][col] :
            MainL[0][col] = MainL[0][col]
            MainL[1][col] *=2
            MainL[2][col] = 0
            MainL[3][col] = 0
        #9
        #0044 ==> 8000
        elif MainL[0][col] == 0 and MainL[1][col] == 0 and MainL[2][col] != 0 and MainL[3][col] == MainL[2][col]:
            MainL[0][col] = MainL[2][col];  MainL[0][col] *= 2
            MainL[1][col] = 0
            MainL[2][col] = 0
            MainL[3][col] = 0
        #10
        #X044 ==> X800
        elif MainL[0][col] != 0 and MainL[1][col] == 0 and MainL[2][col] != 0 and MainL[2][col] != MainL[0][col] \
             and MainL[3][col] == MainL[2][col]:
            MainL[0][col] = MainL[0][col]
            MainL[1][col] = MainL[2][col];  MainL[1][col] *= 2
            MainL[2][col] = 0
            MainL[3][col] = 0
        #11
        #0X44 ==> X800
        elif MainL[0][col] == 0 and MainL[1][col] != 0 and MainL[2][col] != 0 and MainL[2][col] != MainL[1][col] \
             and MainL[3][col] == MainL[2][col]:
            MainL[0][col] = MainL[1][col]
            MainL[1][col] = MainL[2][col];  MainL[1][col] *= 2
            MainL[2][col] = 0
            MainL[3][col] = 0
        #12
        #XX44 ==> X800
        elif MainL[0][col] != 0 and MainL[1][col] != 0 and MainL[1][col] != MainL[0][col] and MainL[2][col] != 0 \
             and MainL[2][col] != MainL[1][col] and MainL[3][col] == MainL[2][col]:
            MainL[0][col] = MainL[0][col]
            MainL[1][col] = MainL[1][col]
            MainL[2][col] *= 2
            MainL[3][col] = 0
            
        ##二、合2个数
        #1
        #4422 ==>8400
        elif MainL[0][col] != 0 and MainL[1][col] == MainL[0][col] and MainL[2][col] != 0 and MainL[3][col] == MainL[2][col]:
            MainL[0][col] *= 2
            MainL[1][col] = MainL[2][col];  MainL[1][col] *= 2
            MainL[2][col] = 0
            MainL[3][col] = 0
 
        ##没有变化
        else:
            unchanged_flag += 1
 
    if unchanged_flag != 4:
        DataRefresh()
        PrintData()
        
    return
#end of the function "UpKey()"
 
#按下"s"键
def DownKey():
    global unchanged_flag
    for col in range(0, 4):
        ##一、合0个数
        #1
        #00X0 ==> 000X
        if MainL[3][col] == 0 and MainL[2][col] != 0 and MainL[1][col] == 0 and MainL[0][col] ==0:
            MainL[3][col] = MainL[2][col]
            MainL[2][col] = 0
            MainL[1][col] = 0
            MainL[0][col] = 0
        #2
        #0X00 ==> 000X
        elif MainL[3][col] == 0 and MainL[2][col] == 0 and MainL[1][col] != 0 and MainL[0][col] ==0:
            MainL[3][col] = MainL[1][col]
            MainL[2][col] = 0
            MainL[1][col] = 0
            MainL[0][col] = 0            
        #3
        #X000 ==> 000X
        elif MainL[3][col] == 0 and MainL[2][col] == 0 and MainL[1][col] == 0 and MainL[0][col] !=0:
            MainL[3][col] = MainL[0][col]
            MainL[2][col] = 0
            MainL[1][col] = 0
            MainL[0][col] = 0          
        #4
        #0XX0 ==> 00XX
        elif MainL[3][col] == 0 and MainL[2][col] != 0 and MainL[1][col] != 0 and MainL[1][col] != MainL[2][col] \
             and MainL[0][col] ==0:
            MainL[3][col] = MainL[2][col]
            MainL[2][col] = MainL[1][col]
            MainL[1][col] = 0
            MainL[0][col] = 0
        #5
        #X0X0 ==> 00XX
        elif MainL[3][col] == 0 and MainL[2][col] != 0 and MainL[1][col] == 0 and MainL[0][col] !=0 \
             and MainL[0][col] != MainL[2][col] :
            MainL[3][col] = MainL[2][col]
            MainL[2][col] = MainL[0][col]
            MainL[1][col] = 0
            MainL[0][col] = 0        
        #6
        #XX00 ==> 00XX
        elif MainL[3][col] == 0 and MainL[2][col] == 0 and MainL[1][col] != 0 and MainL[0][col] !=0 \
             and MainL[0][col] != MainL[1][col] :
            MainL[3][col] = MainL[1][col]
            MainL[2][col] = MainL[0][col]
            MainL[1][col] = 0
            MainL[0][col] = 0     
        #7
        #XXX0 ==> 0XXX
        elif MainL[3][col] == 0 and MainL[2][col] != 0 and MainL[1][col] != 0 and MainL[0][col] !=0 \
             and MainL[0][col] != MainL[1][col] and MainL[2][col] != MainL[1][col]:
            MainL[3][col] = MainL[2][col]
            MainL[2][col] = MainL[1][col]
            MainL[1][col] = MainL[0][col]
            MainL[0][col] = 0     
        #8
        #0X0X ==> 00XX
        elif MainL[3][col] != 0 and MainL[2][col] == 0 and MainL[1][col] != 0 and MainL[0][col] ==0 \
             and MainL[1][col] != MainL[3][col]:
            MainL[3][col] = MainL[3][col]
            MainL[2][col] = MainL[1][col]
            MainL[1][col] = 0
            MainL[0][col] = 0
        #9
        #X00X ==> 00XX
        elif MainL[3][col] != 0 and MainL[2][col] == 0 and MainL[1][col] == 0 and MainL[0][col] !=0 \
             and MainL[0][col] != MainL[3][col]:
            MainL[3][col] = MainL[3][col]
            MainL[2][col] = MainL[0][col]
            MainL[1][col] = 0
            MainL[0][col] = 0
        #10
        #XX0X ==> 0XXX
        elif MainL[3][col] != 0 and MainL[2][col] == 0 and MainL[1][col] != 0 and MainL[0][col] !=0 \
             and MainL[0][col] != MainL[1][col] and MainL[1][col] != MainL[3][col]:
            MainL[3][col] = MainL[3][col]
            MainL[2][col] = MainL[1][col]
            MainL[1][col] = MainL[0][col]
            MainL[0][col] = 0
        #11
        #X0XX ==> 0XXX
        elif MainL[3][col] != 0 and MainL[2][col] != 0 and MainL[1][col] == 0 and MainL[0][col] !=0 \
             and MainL[0][col] != MainL[2][col] and MainL[2][col] != MainL[3][col]:
            MainL[3][col] = MainL[3][col]
            MainL[2][col] = MainL[2][col]
            MainL[1][col] = MainL[0][col]
            MainL[0][col] = 0
 
        ##二、合1个数
        #1
        #X044 ==>00X8
        elif MainL[3][col] != 0 and MainL[2][col] == MainL[3][col] and MainL[1][col] == 0 and MainL[0][col] != 0:
            MainL[3][col] *= 2
            MainL[2][col] = MainL[0][col]
            MainL[1][col] = 0
            MainL[0][col] = 0   
        #2
        #XX44 ==>0XX8
        elif MainL[3][col] != 0 and MainL[2][col] == MainL[3][col] and (MainL[1][col] != MainL[0][col] or (MainL[1][col]==0 and MainL[0][col]==0)):
            MainL[3][col] *= 2
            MainL[2][col] = MainL[1][col]
            MainL[1][col] = MainL[0][col]
            MainL[0][col] = 0        
        #3
        #X404 ==> 00X8
        elif MainL[3][col] != 0 and MainL[2][col] == 0 and MainL[1][col] == MainL[3][col]:
            MainL[3][col] *= 2
            MainL[2][col] = MainL[0][col]
            MainL[1][col] = 0
            MainL[0][col] = 0
        #4
        #4004 ==> 0008
        elif MainL[3][col] != 0 and MainL[2][col] == 0 and MainL[1][col] == 0 and MainL[0][col] == MainL[3][col]:
            MainL[3][col] *= 2
            MainL[2][col] = 0
            MainL[1][col] = 0
            MainL[0][col] = 0
        #5
        #X440 ==> 00X8
        elif MainL[3][col] == 0 and MainL[2][col] != 0 and MainL[1][col] == MainL[2][col]:
            MainL[3][col] = MainL[2][col];  MainL[3][col] *= 2
            MainL[2][col] = MainL[0][col]
            MainL[1][col] = 0
            MainL[0][col] = 0
        #6
        #4040 ==> 0008
        elif MainL[3][col] == 0 and MainL[2][col] != 0 and MainL[1][col] == 0 and MainL[0][col] == MainL[2][col]:
            MainL[3][col] = MainL[2][col];  MainL[3][col] *= 2
            MainL[2][col] = 0
            MainL[1][col] = 0
            MainL[0][col] = 0
        #7
        #X44X ==> 0X8X
        elif MainL[3][col] != 0 and MainL[2][col] != 0 and MainL[1][col] == MainL[2][col] and MainL[3][col] != MainL[2][col] :
            MainL[3][col] = MainL[3][col]
            MainL[2][col] *=2
            MainL[1][col] = MainL[0][col] 
            MainL[0][col] = 0
        #8
        #404X ==> 008X
        elif MainL[3][col] != 0 and MainL[2][col] != 0 and MainL[1][col] == 0 and MainL[0][col] == MainL[2][col]:
            MainL[3][col] = MainL[3][col]
            MainL[2][col] *=2
            MainL[1][col] = 0
            MainL[0][col] = 0
        #9
        #4400 ==> 0008
        elif MainL[3][col] == 0 and MainL[2][col] == 0 and MainL[1][col] != 0 and MainL[0][col] == MainL[1][col]:
            MainL[3][col] = MainL[1][col];  MainL[3][col] *= 2
            MainL[2][col] = 0
            MainL[1][col] = 0
            MainL[0][col] = 0
        #10
        #440X ==> 008X
        elif MainL[3][col] != 0 and MainL[2][col] == 0 and MainL[1][col] != 0 and MainL[1][col] != MainL[3][col] \
             and MainL[0][col] == MainL[1][col]:
            MainL[3][col] = MainL[3][col]
            MainL[2][col] = MainL[1][col];  MainL[2][col] *= 2
            MainL[1][col] = 0
            MainL[0][col] = 0
        #11
        #44X0 ==> 008X
        elif MainL[3][col] == 0 and MainL[2][col] != 0 and MainL[1][col] != 0 and MainL[1][col] != MainL[2][col] \
             and MainL[0][col] == MainL[1][col]:
            MainL[3][col] = MainL[2][col]
            MainL[2][col] = MainL[1][col];  MainL[2][col] *= 2
            MainL[1][col] = 0
            MainL[0][col] = 0
        #12
        #44XX ==> 08XX
        elif MainL[3][col] != 0 and MainL[2][col] != 0 and MainL[2][col] != MainL[3][col] and MainL[1][col] != 0 \
             and MainL[1][col] != MainL[2][col] and MainL[0][col] == MainL[1][col]:
            MainL[3][col] = MainL[3][col]
            MainL[2][col] = MainL[2][col]
            MainL[1][col] *= 2
            MainL[0][col] = 0
            
        ##二、合2个数
        #1
        #4422 ==>0084
        elif MainL[3][col] != 0 and MainL[2][col] == MainL[3][col] and MainL[1][col] != 0 and MainL[0][col] == MainL[1][col]:
            MainL[3][col] *= 2
            MainL[2][col] = MainL[1][col];  MainL[2][col] *= 2
            MainL[1][col] = 0
            MainL[0][col] = 0
 
        ##没有变化
        else:
            unchanged_flag += 1
            
    if unchanged_flag != 4:
        DataRefresh()
        PrintData()
 
    return
#end of the function "DownKey()"
 
#按下"a"键
def LeftKey():
    global unchanged_flag
    for row in range(0, 4):
        ##一、合0个数
        #1
        #0X00 ==> X000
        if MainL[row][0] == 0 and MainL[row][1] != 0 and MainL[row][2] == 0 and MainL[row][3] ==0:
            MainL[row][0] = MainL[row][1]
            MainL[row][1] = 0
            MainL[row][2] = 0
            MainL[row][3] = 0
        #2
        #00X0 ==> X000
        elif MainL[row][0] == 0 and MainL[row][1] == 0 and MainL[row][2] != 0 and MainL[row][3] ==0:
            MainL[row][0] = MainL[row][2]
            MainL[row][1] = 0
            MainL[row][2] = 0
            MainL[row][3] = 0            
        #3
        #000X ==> X000
        elif MainL[row][0] == 0 and MainL[row][1] == 0 and MainL[row][2] == 0 and MainL[row][3] !=0:
            MainL[row][0] = MainL[row][3]
            MainL[row][1] = 0
            MainL[row][2] = 0
            MainL[row][3] = 0          
        #4
        #0XX0 ==> XX00
        elif MainL[row][0] == 0 and MainL[row][1] != 0 and MainL[row][2] != 0 and MainL[row][2] != MainL[row][1] \
             and MainL[row][3] ==0:
            MainL[row][0] = MainL[row][1]
            MainL[row][1] = MainL[row][2]
            MainL[row][2] = 0
            MainL[row][3] = 0
        #5
        #0X0X ==> XX00
        elif MainL[row][0] == 0 and MainL[row][1] != 0 and MainL[row][2] == 0 and MainL[row][3] !=0 \
             and MainL[row][3] != MainL[row][1] :
            MainL[row][0] = MainL[row][1]
            MainL[row][1] = MainL[row][3]
            MainL[row][2] = 0
            MainL[row][3] = 0        
        #6
        #00XX ==> XX00
        elif MainL[row][0] == 0 and MainL[row][1] == 0 and MainL[row][2] != 0 and MainL[row][3] !=0 \
             and MainL[row][3] != MainL[row][2] :
            MainL[row][0] = MainL[row][2]
            MainL[row][1] = MainL[row][3]
            MainL[row][2] = 0
            MainL[row][3] = 0     
        #7
        #0XXX ==> XXX0
        elif MainL[row][0] == 0 and MainL[row][1] != 0 and MainL[row][2] != 0 and MainL[row][3] !=0 \
             and MainL[row][3] != MainL[row][2] and MainL[row][1] != MainL[row][2]:
            MainL[row][0] = MainL[row][1]
            MainL[row][1] = MainL[row][2]
            MainL[row][2] = MainL[row][3]
            MainL[row][3] = 0     
        #8
        #X0X0 ==> XX00
        elif MainL[row][0] != 0 and MainL[row][1] == 0 and MainL[row][2] != 0 and MainL[row][3] ==0 \
             and MainL[row][2] != MainL[row][0]:
            MainL[row][0] = MainL[row][0]
            MainL[row][1] = MainL[row][2]
            MainL[row][2] = 0
            MainL[row][3] = 0
        #9
        #X00X ==> XX00
        elif MainL[row][0] != 0 and MainL[row][1] == 0 and MainL[row][2] == 0 and MainL[row][3] !=0 \
             and MainL[row][3] != MainL[row][0]:
            MainL[row][0] = MainL[row][0]
            MainL[row][1] = MainL[row][3]
            MainL[row][2] = 0
            MainL[row][3] = 0
        #10
        #X0XX ==>XXX0
        elif MainL[row][0] != 0 and MainL[row][1] == 0 and MainL[row][2] != 0 and MainL[row][3] !=0 \
             and MainL[row][3] != MainL[row][2] and MainL[row][0] != MainL[row][2]:
            MainL[row][0] = MainL[row][0]
            MainL[row][1] = MainL[row][2]
            MainL[row][2] = MainL[row][3]
            MainL[row][3] = 0
        #11
        #XX0X ==> XXX0
        elif MainL[row][0] != 0 and MainL[row][1] != 0 and MainL[row][2] == 0 and MainL[row][3] !=0 \
             and MainL[row][3] != MainL[row][1] and MainL[row][1] != MainL[row][0]:
            MainL[row][0] = MainL[row][0]
            MainL[row][1] = MainL[row][1]
            MainL[row][2] = MainL[row][3]
            MainL[row][3] = 0
 
        ##二、合1个数
        #1
        #440X ==>8X00
        elif MainL[row][0] != 0 and MainL[row][1] == MainL[row][0] and MainL[row][2] == 0 and MainL[row][3] != 0:
            MainL[row][0] *= 2
            MainL[row][1] = MainL[row][3]
            MainL[row][2] = 0
            MainL[row][3] = 0   
        #2
        #44XX ==>8XX0
        elif MainL[row][0] != 0 and MainL[row][1] == MainL[row][0] and (MainL[row][2] != MainL[row][3] or (MainL[row][2]==0 and MainL[row][3]==0)):
            MainL[row][0] *= 2
            MainL[row][1] = MainL[row][2]
            MainL[row][2] = MainL[row][3]
            MainL[row][3] = 0        
        #3
        #404X ==> 8X00
        elif MainL[row][0] != 0 and MainL[row][1] == 0 and MainL[row][2] == MainL[row][0]:
            MainL[row][0] *= 2
            MainL[row][1] = MainL[row][3]
            MainL[row][2] = 0
            MainL[row][3] = 0
        #4
        #4004 ==> 8000
        elif MainL[row][0] != 0 and MainL[row][1] == 0 and MainL[row][2] == 0 and MainL[row][3] == MainL[row][0]:
            MainL[row][0] *= 2
            MainL[row][1] = 0
            MainL[row][2] = 0
            MainL[row][3] = 0
        #5
        #044X ==> 8X00
        elif MainL[row][0] == 0 and MainL[row][1] != 0 and MainL[row][2] == MainL[row][1]:
            MainL[row][0] = MainL[row][1];  MainL[row][0] *= 2
            MainL[row][1] = MainL[row][3]
            MainL[row][2] = 0
            MainL[row][3] = 0
        #6
        #0404 ==> 8000
        elif MainL[row][0] == 0 and MainL[row][1] != 0 and MainL[row][2] == 0 and MainL[row][3] == MainL[row][1]:
            MainL[row][0] = MainL[row][1];  MainL[row][0] *= 2
            MainL[row][1] = 0
            MainL[row][2] = 0
            MainL[row][3] = 0
        #7
        #X44X ==> X8X0
        elif MainL[row][0] != 0 and MainL[row][1] != 0 and MainL[row][2] == MainL[row][1] and MainL[row][0] != MainL[row][1]:
            MainL[row][0] = MainL[row][0]
            MainL[row][1] *=2
            MainL[row][2] = MainL[row][3] 
            MainL[row][3] = 0
        #8
        #X404 ==> X800
        elif MainL[row][0] != 0 and MainL[row][1] != 0 and MainL[row][2] == 0 and MainL[row][3] == MainL[row][1] \
             and MainL[row][0] != MainL[row][1] :
            MainL[row][0] = MainL[row][0]
            MainL[row][1] *=2
            MainL[row][2] = 0
            MainL[row][3] = 0
        #9
        #0044 ==> 8000
        elif MainL[row][0] == 0 and MainL[row][1] == 0 and MainL[row][2] != 0 and MainL[row][3] == MainL[row][2]:
            MainL[row][0] = MainL[row][2];  MainL[row][0] *= 2
            MainL[row][1] = 0
            MainL[row][2] = 0
            MainL[row][3] = 0
        #10
        #X044 ==> X800
        elif MainL[row][0] != 0 and MainL[row][1] == 0 and MainL[row][2] != 0 and MainL[row][2] != MainL[row][0] \
             and MainL[row][3] == MainL[row][2]:
            MainL[row][0] = MainL[row][0]
            MainL[row][1] = MainL[row][2];  MainL[row][1] *= 2
            MainL[row][2] = 0
            MainL[row][3] = 0
        #11
        #0X44 ==> X800
        elif MainL[row][0] == 0 and MainL[row][1] != 0 and MainL[row][2] != 0 and MainL[row][2] != MainL[row][1] \
             and MainL[row][3] == MainL[row][2]:
            MainL[row][0] = MainL[row][1]
            MainL[row][1] = MainL[row][2];  MainL[row][1] *= 2
            MainL[row][2] = 0
            MainL[row][3] = 0
        #12
        #XX44 ==> X800
        elif MainL[row][0] != 0 and MainL[row][1] != 0 and MainL[row][1] != MainL[row][0] and MainL[row][2] != 0 \
             and MainL[row][2] != MainL[row][1] and MainL[row][3] == MainL[row][2]:
            MainL[row][0] = MainL[row][0]
            MainL[row][1] = MainL[row][1]
            MainL[row][2] *= 2
            MainL[row][3] = 0
            
        ##二、合2个数
        #1
        #4422 ==>8400
        elif MainL[row][0] != 0 and MainL[row][1] == MainL[row][0] and MainL[row][2] != 0 and MainL[row][3] == MainL[row][2]:
            MainL[row][0] *= 2
            MainL[row][1] = MainL[row][2];  MainL[row][1] *= 2
            MainL[row][2] = 0
            MainL[row][3] = 0
 
        ##没有变化
        else:
            unchanged_flag += 1
        
    if unchanged_flag != 4:
        DataRefresh()
        PrintData()
 
    return
#end of the function "LeftKey()"
 
#按下"d"键
def RightKey():
    global unchanged_flag
    for row in range(0, 4):
        ##一、合0个数
        #1
        #00X0 ==> 000X
        if MainL[row][3] == 0 and MainL[row][2] != 0 and MainL[row][1] == 0 and MainL[row][0] ==0:
            MainL[row][3] = MainL[row][2]
            MainL[row][2] = 0
            MainL[row][1] = 0
            MainL[row][0] = 0
        #2
        #0X00 ==> 000X
        elif MainL[row][3] == 0 and MainL[row][2] == 0 and MainL[row][1] != 0 and MainL[row][0] ==0:
            MainL[row][3] = MainL[row][1]
            MainL[row][2] = 0
            MainL[row][1] = 0
            MainL[row][0] = 0            
        #3
        #X000 ==> 000X
        elif MainL[row][3] == 0 and MainL[row][2] == 0 and MainL[row][1] == 0 and MainL[row][0] !=0:
            MainL[row][3] = MainL[row][0]
            MainL[row][2] = 0
            MainL[row][1] = 0
            MainL[row][0] = 0          
        #4
        #0XX0 ==> 00XX
        elif MainL[row][3] == 0 and MainL[row][2] != 0 and MainL[row][1] != 0 and MainL[row][1] != MainL[row][2] \
             and MainL[row][0] ==0:
            MainL[row][3] = MainL[row][2]
            MainL[row][2] = MainL[row][1]
            MainL[row][1] = 0
            MainL[row][0] = 0
        #5
        #X0X0 ==> 00XX
        elif MainL[row][3] == 0 and MainL[row][2] != 0 and MainL[row][1] == 0 and MainL[row][0] !=0 \
             and MainL[row][0] != MainL[row][2] :
            MainL[row][3] = MainL[row][2]
            MainL[row][2] = MainL[row][0]
            MainL[row][1] = 0
            MainL[row][0] = 0        
        #6
        #XX00 ==> 00XX
        elif MainL[row][3] == 0 and MainL[row][2] == 0 and MainL[row][1] != 0 and MainL[row][0] !=0 \
             and MainL[row][0] != MainL[row][1] :
            MainL[row][3] = MainL[row][1]
            MainL[row][2] = MainL[row][0]
            MainL[row][1] = 0
            MainL[row][0] = 0     
        #7
        #XXX0 ==> 0XXX
        elif MainL[row][3] == 0 and MainL[row][2] != 0 and MainL[row][1] != 0 and MainL[row][0] !=0 \
             and MainL[row][0] != MainL[row][1] and MainL[row][2] != MainL[row][1]:
            MainL[row][3] = MainL[row][2]
            MainL[row][2] = MainL[row][1]
            MainL[row][1] = MainL[row][0]
            MainL[row][0] = 0     
        #8
        #0X0X ==> 00XX
        elif MainL[row][3] != 0 and MainL[row][2] == 0 and MainL[row][1] != 0 and MainL[row][0] ==0 \
             and MainL[row][1] != MainL[row][3]:
            MainL[row][3] = MainL[row][3]
            MainL[row][2] = MainL[row][1]
            MainL[row][1] = 0
            MainL[row][0] = 0
        #9
        #X00X ==> 00XX
        elif MainL[row][3] != 0 and MainL[row][2] == 0 and MainL[row][1] == 0 and MainL[row][0] !=0 \
             and MainL[row][0] != MainL[row][3]:
            MainL[row][3] = MainL[row][3]
            MainL[row][2] = MainL[row][0]
            MainL[row][1] = 0
            MainL[row][0] = 0
        #10
        #XX0X ==> 0XXX
        elif MainL[row][3] != 0 and MainL[row][2] == 0 and MainL[row][1] != 0 and MainL[row][0] !=0 \
             and MainL[row][0] != MainL[row][1] and MainL[row][1] != MainL[row][3]:
            MainL[row][3] = MainL[row][3]
            MainL[row][2] = MainL[row][1]
            MainL[row][1] = MainL[row][0]
            MainL[row][0] = 0
        #11
        #X0XX ==> 0XXX
        elif MainL[row][3] != 0 and MainL[row][2] != 0 and MainL[row][1] == 0 and MainL[row][0] !=0 \
             and MainL[row][0] != MainL[row][2] and MainL[row][2] != MainL[row][3]:
            MainL[row][3] = MainL[row][3]
            MainL[row][2] = MainL[row][2]
            MainL[row][1] = MainL[row][0]
            MainL[row][0] = 0
 
        ##二、合1个数
        #1
        #X044 ==>00X8
        elif MainL[row][3] != 0 and MainL[row][2] == MainL[row][3] and MainL[row][1] == 0 and MainL[row][0] != 0:
            MainL[row][3] *= 2
            MainL[row][2] = MainL[row][0]
            MainL[row][1] = 0
            MainL[row][0] = 0   
        #2
        #XX44 ==>0XX8
        elif MainL[row][3] != 0 and MainL[row][2] == MainL[row][3] and (MainL[row][1] != MainL[row][0] or (MainL[row][1]==0 and MainL[row][0]==0)):
            MainL[row][3] *= 2
            MainL[row][2] = MainL[row][1]
            MainL[row][1] = MainL[row][0]
            MainL[row][0] = 0        
        #3
        #X404 ==> 00X8
        elif MainL[row][3] != 0 and MainL[row][2] == 0 and MainL[row][1] == MainL[row][3]:
            MainL[row][3] *= 2
            MainL[row][2] = MainL[row][0]
            MainL[row][1] = 0
            MainL[row][0] = 0
        #4
        #4004 ==> 0008
        elif MainL[row][3] != 0 and MainL[row][2] == 0 and MainL[row][1] == 0 and MainL[row][0] == MainL[row][3]:
            MainL[row][3] *= 2
            MainL[row][2] = 0
            MainL[row][1] = 0
            MainL[row][0] = 0
        #5
        #X440 ==> 00X8
        elif MainL[row][3] == 0 and MainL[row][2] != 0 and MainL[row][1] == MainL[row][2]:
            MainL[row][3] = MainL[row][2];  MainL[row][3] *= 2
            MainL[row][2] = MainL[row][0]
            MainL[row][1] = 0
            MainL[row][0] = 0
        #6
        #4040 ==> 0008
        elif MainL[row][3] == 0 and MainL[row][2] != 0 and MainL[row][1] == 0 and MainL[row][0] == MainL[row][2]:
            MainL[row][3] = MainL[row][2];  MainL[row][3] *= 2
            MainL[row][2] = 0
            MainL[row][1] = 0
            MainL[row][0] = 0
        #7
        #X44X ==> 0X8X
        elif MainL[row][3] != 0 and MainL[row][2] != 0 and MainL[row][1] == MainL[row][2] and MainL[row][3] != MainL[row][2] :
            MainL[row][3] = MainL[row][3]
            MainL[row][2] *=2
            MainL[row][1] = MainL[row][0] 
            MainL[row][0] = 0
        #8
        #404X ==> 008X
        elif MainL[row][3] != 0 and MainL[row][2] != 0 and MainL[row][1] == 0 and MainL[row][0] == MainL[row][2]:
            MainL[row][3] = MainL[row][3]
            MainL[row][2] *=2
            MainL[row][1] = 0
            MainL[row][0] = 0
        #9
        #4400 ==> 0008
        elif MainL[row][3] == 0 and MainL[row][2] == 0 and MainL[row][1] != 0 and MainL[row][0] == MainL[row][1]:
            MainL[row][3] = MainL[row][1];  MainL[row][3] *= 2
            MainL[row][2] = 0
            MainL[row][1] = 0
            MainL[row][0] = 0
        #10
        #440X ==> 008X
        elif MainL[row][3] != 0 and MainL[row][2] == 0 and MainL[row][1] != 0 and MainL[row][1] != MainL[row][3] \
             and MainL[row][0] == MainL[row][1]:
            MainL[row][3] = MainL[row][3]
            MainL[row][2] = MainL[row][1];  MainL[row][2] *= 2
            MainL[row][1] = 0
            MainL[row][0] = 0
        #11
        #44X0 ==> 008X
        elif MainL[row][3] == 0 and MainL[row][2] != 0 and MainL[row][1] != 0 and MainL[row][1] != MainL[row][2] \
             and MainL[row][0] == MainL[row][1]:
            MainL[row][3] = MainL[row][2]
            MainL[row][2] = MainL[row][1];  MainL[row][2] *= 2
            MainL[row][1] = 0
            MainL[row][0] = 0
        #12
        #44XX ==> 08XX
        elif MainL[row][3] != 0 and MainL[row][2] != 0 and MainL[row][2] != MainL[row][3] and MainL[row][1] != 0 \
             and MainL[row][1] != MainL[row][2] and MainL[row][0] == MainL[row][1]:
            MainL[row][3] = MainL[row][3]
            MainL[row][2] = MainL[row][2]
            MainL[row][1] *= 2
            MainL[row][0] = 0
            
        ##二、合2个数
        #1
        #4422 ==>0084
        elif MainL[row][3] != 0 and MainL[row][2] == MainL[row][3] and MainL[row][1] != 0 and MainL[row][0] == MainL[row][1]:
            MainL[row][3] *= 2
            MainL[row][2] = MainL[row][1];  MainL[row][2] *= 2
            MainL[row][1] = 0
            MainL[row][0] = 0
            
        ##没有变化
        else:
            unchanged_flag += 1
 
    if unchanged_flag != 4:
        DataRefresh()
        PrintData()
 
    return
#end of the function "RightKey()"
            
#主任务
def main():
    GameInit()
    PrintData()
    global Victory_flag
    global unchanged_flag
    while Victory_flag == 0:
        a = ord(msvcrt.getch())
        unchanged_flag = 0
        if a == 119:    #"w"键
            UpKey()
        elif a == 115:  #"s"键
            DownKey()
        elif a == 97:   #"a"键
            LeftKey()
        elif a == 100:  #"d"键
            RightKey()
        elif a == 113:  #"q"键
            break
 
        #判断胜利条件
        for index in range(0, 16):
            row = (int)(index/4)
            col = index%4
            if MainL[row][col] == 2048:
                Victory_flag = 1
                print("游戏胜利！按任意键退出")
                a = ord(msvcrt.getch())
                if a == 113:
                    break
            
        #判断失败条件
        if Victory_flag == 2:
            print("游戏失败！按任意键退出")
            a = ord(msvcrt.getch())
            if a == 113:
                break
 
if __name__ == '__main__':
    main()