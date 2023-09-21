
while True:
    
    #Using quiddity sequence to calculate the entire frieze-----------------------------------------------
    QS=[]
    res=input("Please enter the quiddity sequence of your frieze:\n")
    QS = [int(i) for i in res]

    #S=Set of rows
    S=[[]]
    #Add the first row to S
    S[0]=[1]*len(QS)

    #Add the second row to S
    S.append(QS)

    #Add the remaining rows to S
    len_QS = len(QS)
    for i in range(1, len_QS-2):
        #i=1 corresponds to the third row
        S.append([])
    
        for j in range(len_QS):
            #除數
            if i==1:
                div=1
            else:
                div = S[i-1][(j+1) % len_QS]
                
            #新增元素
            try:
                S[i+1].append(int((S[i][j]*S[i][j+1]-1)/div))
            except IndexError:
                S[i+1].append(int((S[i][j]*S[i][0]-1)/div))    #[i][0]是因為循環


    print(S)  #Normal output

    #排版輸出----------------------------------------------------------------------

    for i in range(len(QS)-1):

        #每列開頭的空格
        for k in range(i):
            print("   ",end="")
    
        for l in range(2):
            #for l in range(2)是為了印兩遍
            for j in range(len(QS)):
                if S[i][j]<10:
                    print((chr(ord(str(S[i][j]))+65248)),end="") #若個位數則為全型，佔兩格正常空間
                else:
                    print(S[i][j],end="")  #否則為半型，佔兩格正常空間
                print("    ",end="")     
        print("")
        
    C=[] #C is the set of counts, C[1] rep. the num of 1
    for i in range (1,len(S)-1):
        for j in range (len(S[0])):
            C.append(S[i][j])
    for i in range(1,max(C)+1):
        print(i,":",C.count(i),"  ")

    print("\n")
    
    
    
        


















