#
import random
#מקבל אינפוט לגודל המטריצה
def input_matrix():
    
    matrix_size=int(input("enter size of matrix: "))
    return matrix_size

matrix_size=input_matrix()
    
    

#יוצר את המטריצה לפי האינפוט שהתקבל
    
def creata_matrix(rows=int,coloms=None):
    coloms=rows
    matrix=[]
    for i in range(rows):
        row=[]
        for j in range(coloms):
            row.append(0*rows)
        matrix.append(row)
    return matrix 

matrix=creata_matrix(matrix_size)


#מדפיס את המטריצה בדו מימדי

def matrix_printer(matrix):
    for i in range(len (matrix)):
        for j in range (len (matrix[i])):
            print(matrix[i][j],end=" ")
        print()

#ממקם צוללות באופן אקראי
def submarine_locator(matrix):
    # rund_num=random.randrange(0,len(matrix))
    for row in matrix:
        index = random.randint(0, len(row) - 1)  
        row[index] = 's'  
    return matrix
s_matrix=submarine_locator(matrix)

#קובע את מספר היריות
def number_of_shots(matrix):
    return len(matrix)*2
shots_number=number_of_shots(matrix)
   

def coordination_tester(matrix):
    while True:
        row_soht=int(input("enter row number: "))
        if row_soht > 10:
            print("enter one digit!")
            continue
        colom_shot=int(input('enter colom number: '))
        if colom_shot > 10 :
             print("enter one digit!")
             continue
        if row_soht > len(matrix) or colom_shot > len(matrix):
            print("your out of range")
            continue
        return [row_soht,colom_shot]





    
            
    


