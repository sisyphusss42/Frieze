"""
This code calculates and outputs four fundamental regions of a frieze pattern given a quiddity sequence
It also ouputs the quantity of each digit in two fundamental regions
Created by Diego
"""

def get_quiddity_sequence():
    #Using quiddity sequence to calculate the entire frieze--------------------------------
    try:
        res = input("Please enter the quiddity sequence of your frieze:\n")
        QS = [int(i) for i in res]  #QS is short for quiddity sequence
        return(QS)
    except ValueError:
            print("Invalid input. Quiddity sequence should be a sequence of digits.")

def calculate_frieze_pattern(QS):
    len_QS = len(QS)
    #S is the set of rows
    S = [[] for _ in range(len_QS-1)]
    #Add the first row to S
    S[0] = [1]*len_QS
    #Add the second row to S
    S[1] = QS

    #Add the remaining rows to S
    for i in range(1, len_QS-2):  #i=1 corresponds to the second row
        for j in range(len_QS):
            #Find the divisor
            div = S[i-1][(j+1) % len_QS]
                
            #Append the elements
            S[i+1].append(int((S[i][j] * S[i][(j+1)%len_QS] - 1) / div))
    
    return S

def display_frieze_pattern(S):
    len_QS = len(S[0])
    #Formatted output----------------------------------------------------------------------
    for i in range(len_QS-1):
        row = "   " * i
        for l in range(2): #output four fundamental regions of the frieze
            for j in range(len_QS):
                if S[i][j]<10:
                    row += chr(ord(str(S[i][j]))+65248) #If one digit then fullwidth, 65248 is the fullwidth offset
                else:
                    row += S[i][j]  #else halfwidth
                row+="    "     
        print(row,"\n")

def count_digits(S): #Count the quantity of digits in two fundamental regions of the frieze
    counts = [digit for row in S[1:-1] for digit in row]
    max_count = max(counts)
    for i in range(1, max_count + 1):
        print(f"{i}: {counts.count(i)}  ")
    print("\n")

if __name__ == "__main__":
    while True:
        QS = get_quiddity_sequence()
        if (QS==[0]):
            break  #Enter 0 to terminate the code
        frieze_pattern = calculate_frieze_pattern(QS)
        print(frieze_pattern,"\n")
        display_frieze_pattern(frieze_pattern)
        count_digits(frieze_pattern)