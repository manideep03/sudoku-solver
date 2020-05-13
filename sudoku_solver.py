board = [
    [5,4,0,0,2,0,8,0,6],
    [0,1,9,0,0,7,0,0,3],
    [0,0,0,3,0,0,2,1,0],
    [9,0,0,4,0,5,0,2,0],
    [0,0,1,0,0,0,6,0,4],
    [6,0,4,0,3,2,0,8,0],
    [0,6,0,0,0,0,1,9,0],
    [4,0,2,0,0,9,0,0,5],
    [0,9,0,0,7,0,4,0,2]
]

# function for printing SUDOKU board 
def print_broad(board):
	for i in range(len(board)):
		if i%3==0 and i!=0:
			print('----------------------')
		for j in range(len(board[0])):
			if j % 3 ==0 and j != 0:
				print('| ',end='')
			if j == 8:
				print(board[i][j])
			else:
				print(str(board[i][j])+' ',end='')

# function using for finding empty position in the board 
# NOTE : in this board empty pos are denoted by '0'
def find_empty_pos(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return (i,j)
	return None 
# function for checking valid number in valid point or not 
def check_validity(board , num , pos):
	#checking row for valid number is inserted or not 
	for i in range(len(board[0])):
		if board[pos[0]][i] == num and pos[1] != i:
			return False
	#checking col for valid number is inserted or not
	for i in range(len(board)):
		if board[i][pos[1]] == num and pos[0] != i:
			return False
	# check the local 3 X 3 box
	box_x = pos[1]//3 #getting 3 x 3 X position in board
	box_y = pos[0]//3 #getting 3 x 3 Y position in board 
	for i in range(box_y * 3 ,box_y * 3+3):
		for j in range(box_x * 3 ,box_x * 3+3):
			if board[i][j] == num and (i,j) != pos:
				return False
	return True


# main function which solves board 
# method used backpropagation using recursion 

def solve_board(board):
	find_pos = find_empty_pos(board)
	# checking the board 
	# if complete loop will break
	if not find_pos : 
		return True
	else :
		row,col = find_pos
	# possible number checking 
	for i in range(1,10):
		if check_validity(board, i, (row,col)):
			board[row][col] = i 

			if solve_board(board):
				return True
			board[row][col] = 0
	return False
print_broad(board)
print(' ')
print('solved board')
print(' ')
solve_board(board)
print_broad(board)
