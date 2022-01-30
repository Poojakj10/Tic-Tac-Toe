from random import randrange

def display_board(board):
	print("+-------" * 3,"+", sep="")
	for r in range(3):
		print("|       " * 3,"|", sep="")
		for c in range(3):
			print("|   " + str(board[r][c]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def enter_move(board):
	ok = False	# we need it to enter the loop
	while not ok:
		move = input("Enter your move: ")
		ok = len(move) == 1 and move >= '1' and move <= '9' # is user's input valid?
		if not ok:
			print("Bad move - please repeat your input!") # no, it isn't - do the input again
			continue
		move = int(move) - 1 	# cell's number from 0 to 8
		r = move // 3 	# cell's row
		c = move % 3		# cell's column
		sign = board[r][c]	# check the selected square
		ok = sign not in ['O','X']
		if not ok:	# it's occupied - to the input again
			print("Field already occupied - repeat your input!")
			continue
	board[r][c] = 'O' 	# set '0' at the selected square


def free_fields(board):
	free=[]
	for r in range(3):
		for c in range(3):
			if board[r][c] not in ['O','X']:
				free.append((r,c))

	return free

def victory(board,sgn):
	if sgn=='X':
		win='me'
	elif sgn=='O':
		win='you'
	else:
		win=None
	cross1=cross2=True
	for rc in range(3):
		if board[rc][0]==sgn and board[rc][1]==sgn and board[rc][2]==sgn:
			return win
		if board[0][rc]==sgn and board[1][rc]==sgn and board[2][rc]==sgn:
			return win
		if board[rc][rc]!=sgn:
			cross1=False
		if board[2-rc][2-rc] != sgn:
			cross2=False
	if cross1 or cross2:
		return win
	return None

def draw_move(board):
	free=free_fields(board)
	cnt=len(free)
	if cnt>0:
		t=randrange(cnt)
		r,c=free[t]
		board[r][c]='X'

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # make an empty board
board[1][1]='X'
free=free_fields(board)
human_turn=True
while len(free):
	display_board(board)
	if human_turn:
		enter_move(board)
		victor=victory(board,'O')
	else:
		draw_move(board)
		victor = victory(board, 'X')
	if victor!= None:
		break
	human_turn=not human_turn
	free=free_fields(board)

display_board(board)
if victor=='you':
	print("You won!")
elif victor=='me':
	print("I won!")
else:
	print("Tie!")