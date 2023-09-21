"""
This code calculates and outputs four fundamental regions of a frieze pattern given a quiddity sequence.
It also ouputs the quantity of each digit in two fundamental regions
Created by Diego
"""

while True:
    
    #Using quiddity sequence to calculate the entire frieze--------------------------------
    res=input("Please enter the quiddity sequence of your frieze:\n")
    QS = [int(i) for i in res]
    len_QS = len(QS)
    
    #S=Set of rows
    S=[[] for i in range(len_QS-1)]
    #Add the first row to S
    S[0]=[1]*len_QS
    #Add the second row to S
    S[1]=QS

    #Add the remaining rows to S
    for i in range(1, len_QS-2):  #i=1 corresponds to the second row
        for j in range(len_QS):
            #Find the divisor
            div = S[i-1][(j+1) % len_QS]
                
            #Append the elements
            S[i+1].append(int((S[i][j]*S[i][(j+1)%len_QS]-1)/div))

    print(S,"\n")  #Normal output
    
    #Formatted output----------------------------------------------------------------------
    for i in range(len_QS-1):
        row="   "*i
        for l in range(2): #output two unit frieze
            for j in range(len_QS):
                if S[i][j]<10:
                    row+=chr(ord(str(S[i][j]))+65248) #If one digit then fullwidth
                else:
                    row+=S[i][j]  #else halfwidth
                row+="    "     
        print(row,"\n")
    
    C=[] #C is the set of counts, C[1] rep. the num of 1
    for i in range (1,len(S)-1):
        for j in range (len(S[0])):
            C.append(S[i][j])
    for i in range(1,max(C)+1):
        print(i,":",C.count(i),"  ")

    print("\n")


