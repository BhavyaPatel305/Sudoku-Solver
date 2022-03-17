import random
puzzle = [

    [-1,2,-1,  5,-1,1,   -1,9,-1],
    [8,-1,-1,  2,-1,3,   -1,-1,6],
    [-1,3,-1,   -1,6,-1,  -1,7,-1],
    
    [-1,-1,1,  -1,-1,-1,  6,-1,-1],
    [5,4,-1,   -1,-1,-1,  7,-1,-1],
    [-1,-1,2,  -1,-1,-1,  7,-1,-1],
    
    [-1,9,-1,  -1,3,-1,  -1,8,-1],
    [2,-1,-1,  8,-1,4,  -1,-1,7],
    [-1,1,-1,  9,-1,7,  -1,6,-1]
    ]

def empty_space_finder(puzzle):
    
    for i in range(0,9):
        for j in range(0,9):
            if(puzzle[i][j] == -1):
                return i,j
    return None,None

def Is_valid(puzzle,num,row,col):
    
    """These 3 if's checks for first 3 columns of Sudoku"""
    
    if (row<3) and (col<3):
        for i in range(0,3):
            for j in range(0,3):
                if puzzle[i][j] == num:
                    return False
                
    if row>=3 and row<6 and col<3:
        for i in range(3,6):
            for j in range(0,3):
                if puzzle[i][j] == num:
                    return False
                
    if row>=6 and row<9 and col<3:
        for i in range(6,9):
            for j in range(0,3):
                if puzzle[i][j] == num:
                    return False
                
    """These 3 if's checks for middle 3 columns of Sudoku"""
    
    if row<3 and col>=3 and col<6:
        for i in range(0,3):
            for j in range(3,6):
                if puzzle[i][j] == num:
                    return False
                
    if row>=3 and row<6 and col>=3 and col<6:
        for i in range(3,6):
            for j in range(3,6):
                if puzzle[i][j] == num:
                    return False
                
    if row>=6 and row<9 and col>=3 and col<6:
        for i in range(6,9):
            for j in range(3,6):
                if puzzle[i][j] == num:
                    return False
                
    """These 3 if's checks for last 3 columns of Sudoku"""
    
    if row<3 and col>=6 and col<9:
        for i in range(0,3):
            for j in range(6,9):
                if puzzle[i][j] == num:
                    return False
                
    if row>=3 and row<6 and col>=6 and col<9:
        for i in range(3,6):
            for j in range(6,9):
                if puzzle[i][j] == num:
                    return False
                
    if row>=6 and row<9 and col>=6 and col<9:
        for i in range(6,9):
            for j in range(6,9):
                if puzzle[i][j] == num:
                    return False
                
    
    """This part checks if the num is unique in the whole row where we are inserting this element."""
    
    
    row_vals = puzzle[row]
    if num in row_vals:
        return False
    
    """This part checks if the num is unique in the whole column where we are inserting this element."""
    
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    
    if num in col_vals:
        return False

        
    return True

def random_number_generator():
    num = random.randint(1,9)
    return num

def printsudoku(puzzle):
    print("\n-------------------------------------")
    for i in range(0,9):
        print("| ", end = "")
        for j in range(0,9):
            print(puzzle[i][j], end = " | ")
        print("\n-------------------------------------")
            
    
    
def main():
    
    while(True):
        row,col = empty_space_finder(puzzle)
        if row == None and col == None:
            break
            
        while(True):
            num = random_number_generator()
            check = Is_valid(puzzle,num,row,col)
            if (check == True):
                puzzle[row][col] = num
                break
    printsudoku(puzzle)
    
main()
