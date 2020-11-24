
grid = [
    [0,0,0,0,7,0,0,8,4],
    [0,0,0,8,0,0,9,7,0],
    [0,1,0,0,0,0,2,0,0],
    [0,0,3,0,0,0,8,9,0],
    [8,2,0,4,9,0,0,3,6],
    [9,0,0,0,0,8,0,0,0],
    [0,7,0,0,0,0,0,0,0],
    [0,0,4,0,0,0,0,6,0],
    [1,0,6,0,0,7,3,0,2],
]



def print_matriz():
    for y in range(0,9):
        for x in range(0,9):
            if x in [2,5]:
                print(f'{grid[y][x]} ',end='')
                print('|', end='')
            else:
                print(f'{grid[y][x]} ',end='')
        print('')
        if y in [2,5]:
            print('------|'*2,end='')
            print('------')

    print()


#passos para ver se certo numero é possivel em certo espaço
def possible(x,y,n): 
    global grid          
    for i in range(0,9):          #varrer a linha a busca de n
        if grid[y][i] == n:
            return False
    for j in range(0,9):          #varrer a coluna a busca de n
        if grid[j][x] == n:   
            return False
    x0 = (x//3)*3               
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

#resolver o sudoku inteiro
def solve():
    for y in range(0,9):
        for x in range(0,9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(x,y,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print_matriz()       



#Programa principal

print_matriz()
solve()
