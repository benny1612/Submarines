#

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





