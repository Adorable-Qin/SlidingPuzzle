import random           # Import random to get a random table to solve


def wel():
    print('\nWelcome to the Sliding Puzzle!\n'
          'In this game, you need to solve the puzzle by input four keys to move the adjacent number.\n'
          'For example, if you choose the game of 3 dimension, you need to resort the table like\n'
          '1 2 3\n'
          '4 5 6\n'
          '7 8\n'
          'Once the table is sorted by the correct order, the puzzle will be finished and you will be told your steps.\n')

def dimChoose():
    while True:
        n = input("Please enter the desired dimensions of the puzzle, minimum 3, up to and including 10:")
        try:
            if n.isdigit and int(n)>=3 and int(n)<=10:
                global dim
                dim = int(n)
                break
        except:
            print("Please input an integer between 3 and 10")

def blockIni():     #get an initial sorted list to create a table
    global dim
    global blocks
    arr = list(range(1,dim**2))
    arr.append(' ')
    numbers = arr
    for row in range(dim):
        blocks.append([])
        for column in range(dim):
            blocks[row].append(numbers[row*dim + column])

def priTable():
    print('\n')
    counts = 1
    global blocks
    for i in blocks:
        for j in i:         
            if j != ' ' and counts % dim !=0:
                 counts += 1
                 print('%3d'%j,end='')
            elif j != ' ' and counts % dim == 0:
                counts += 1
                print('%3d'%j,end='\n')
            elif j == ' ' and counts % dim != 0:
                counts += 1
                print('%3s'%j,end='')
            elif j == ' ' and counts % dim == 0:
                counts += 1
                print('%3s'%j,end='\n')
    print('\n')

# zeroCoor[0] means the row of the blank, zeroCoor[1] means the column of the blank
def move(direction):
    if direction == 'w' or direction == '0':
        if zeroCoor[0] != dim - 1:
            blocks[zeroCoor[0]][zeroCoor[1]] = blocks[zeroCoor[0] + 1][zeroCoor[1]]
            zeroCoor[0] += 1
            blocks[zeroCoor[0]][zeroCoor[1]] = ' '

    if direction == 's' or direction == '1':
        if zeroCoor[0] != 0:
            blocks[zeroCoor[0]][zeroCoor[1]] = blocks[zeroCoor[0] - 1][zeroCoor[1]]
            zeroCoor[0] -= 1
            blocks[zeroCoor[0]][zeroCoor[1]] = ' '

    if direction == 'a' or direction == '2':
        if zeroCoor[1] != dim - 1:
            blocks[zeroCoor[0]][zeroCoor[1]] = blocks[zeroCoor[0]][zeroCoor[1] + 1]
            zeroCoor[1] += 1
            blocks[zeroCoor[0]][zeroCoor[1]] = ' '

    if direction == 'd' or direction == '3':
        if zeroCoor[1] != 0:
            blocks[zeroCoor[0]][zeroCoor[1]] = blocks[zeroCoor[0]][zeroCoor[1] - 1]
            zeroCoor[1] -= 1
            blocks[zeroCoor[0]][zeroCoor[1]] = ' '

def checkResult():
    if blocks[dim -1][dim - 1] != ' ':                          # If the bottom of right is not a blank, there is no need to check other place
        return False

    for row in range(dim):
            for column in range(dim):
                if row == dim - 1 and column == dim - 1:        # We have checked the bottom of right, so we pass it.
                    pass
                elif blocks[row][column] != row * dim + column + 1:
                    return False
    return True

def randomTable():
    for i in range(500):
        ranNum = random.randint(0,3)
        n = str(ranNum)
        move(n)                         # let the sorted table move n times randomly to get a solvable table

def operation():
    global attempt
    if zeroCoor[0] == dim - 1 and zeroCoor[1] != dim - 1 and zeroCoor[1] != 0:                  # If the blank is at the boundery of bottom
        move(input('Please enter your move(s>down,a>left,d>right):'))
    elif zeroCoor[0] == 0 and zeroCoor[1] != dim - 1 and zeroCoor[1] != 0:                      # If the blank is at the boundery of top
        move(input('Please enter your move(w>up,a>left,d>right):'))
    elif zeroCoor[1] == dim - 1 and zeroCoor[0] != dim - 1 and zeroCoor[0] != 0:                # If the blank is at the boundery of right
        move(input('Please enter your move(w>up,s>down,d>right):')) 
    elif zeroCoor[1] == 0 and zeroCoor[0] != dim - 1 and zeroCoor[0] != 0:                      # If the blank is at the boundery of left
        move(input('Please enter your move(w>up,s>down,a>left):'))  
    elif zeroCoor[0] == dim - 1 and zeroCoor[1] == dim - 1:                                     # If the blank is at the bottom of right
        move(input('Please enter your move(s>down,d>right):'))  
    elif zeroCoor[0] == dim - 1 and zeroCoor[1] == 0:                                           # If the blank is at the bottom of left
        move(input('Please enter your move(s>down,a>left):')) 
    elif zeroCoor[0] == 0 and zeroCoor [1] == dim - 1:                                          # If the blank is at the top of right
        move(input('Please enter your move(w>up,d>right):'))  
    elif zeroCoor[0] == 0 and zeroCoor [1] == 0:                                                # If the blank is at the bottom of left
        move(input('Please enter your move(w>up,a>left):'))
    else:                                                               
        move(input('Please enter your move(w>up,s>down,a>left,d>right):'))
    priTable()
    attempt += 1
    checkResult()

wel()
dim = 0
blocks = []                         # the list storing the positions of numbers
dimChoose()
zeroCoor = [dim - 1,dim - 1]        # the initial position of the blank
blockIni()
randomTable()
priTable()
attempt = 0                         # reset the counter of the attempts
operation()

while True:
    result = checkResult()
    if result == False:
        operation()
    else:
        print('Congratulations! You have finished the game in ' + str(attempt) + ' steps')
        choose = input('Do you want to play again?(Y for Restart, any other key for quit):')
        if choose == 'Y':
            dim = 0
            blocks = []
            dimChoose()
            zeroCoor = [dim - 1,dim - 1]
            blockIni()
            randomTable()
            priTable()
            attempt = 0
        else:
            break
