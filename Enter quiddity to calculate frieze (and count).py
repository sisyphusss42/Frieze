"""
This code calculates and outputs four fundamental regions of a frieze pattern given a quiddity sequence
It also ouputs the quantity of each digit in two fundamental regions
Created by Diego
"""

def get_quiddity_sequence():
    try:
        #Enter 0 to terminate the code
        res = input("Please enter the quiddity sequence of your frieze (e.g. 31221): \n")
        QS = [int(i) for i in res]  #QS is short for quiddity sequence
        return(QS)
    except ValueError:
            print("Invalid input. Quiddity sequence should be a sequence of digits.")

def calculate_frieze_pattern(QS):
    len_QS = len(QS)
    #S is the set of rows
    S = [[] for _ in range(len_QS-1)]
    try:
        #Add the first row to S
        S[0] = [1]*len_QS
        #Add the second row to S
        S[1] = QS
    except IndexError:  #This means there's a problem with the quiddity sequence
        return 0

    #Add the remaining rows to S
    for i in range(1, len_QS-2):  #i=1 corresponds to the second row
        for j in range(len_QS):
            #Find the divisor
            div = S[i-1][(j+1) % len_QS]
            #Append the elements
            try:
                S[i+1].append(int((S[i][j] * S[i][(j+1)%len_QS] - 1) / div))
            except ZeroDivisionError:  #This also means there's a problem with the quiddity sequence
                return 0
    if (max(S[-1]) != 1): #This also means there's a problem with the quiddity sequence
        return 0
    return S

def display_frieze_pattern(S):
    len_QS = len(S[0])
    for i in range(len_QS-1):
        row = "   " * i
        for l in range(2): #Output four fundamental regions of the frieze
            for j in range(len_QS):
                if S[i][j]<10:
                    row += chr(ord(str(S[i][j]))+65248) #If one digit then fullwidth, 65248 is the fullwidth offset
                else:
                    row += str(S[i][j])  #else halfwidth
                row+="    "     
        print(row,"\n")

def count_digits(S): #Count the quantity of digits in two fundamental regions of the frieze
    counts = [digit for row in S[1:-1] for digit in row]
    max_count = max(counts)
    for i in range(1, max_count + 1):
        print(f"{i}: {counts.count(i)} ")
    print("\n")

if __name__ == "__main__":
    while True:
        QS = get_quiddity_sequence()
        if (QS==[0]):
            break
        frieze_pattern = calculate_frieze_pattern(QS)
        if frieze_pattern == 0:
            print("This isn't a valid quiddity sequence. Please try again.\n")
        else:
            #print(frieze_pattern,"\n")
            display_frieze_pattern(frieze_pattern)
            count_digits(frieze_pattern)