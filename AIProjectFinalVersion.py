from array import *
from random import *
import copy
import math

lst = []

def createBoard( number ):
    board = []
    for x in range(number):
        row = []
        for y in range(number):
            row.append(randint(-1,1))
        board.append(row)
    return board

def showBoard( board ):
    for index in board:
        print(index)

def possiblePlaces( board , place):
    places = []
    if( place[0] -1 >= 0):
        places.append([place[0]-1,place[1]])
    if(place[0] +1 < len(board) ):
        places.append([place[0]+1,place[1]])
    if(place[1] -1 >= 0):
        places.append([place[0],place[1]-1])
    if(place[1] +1 < len(board)):
        places.append([place[0],place[1]+1])
    return places




def alphaBeta(board,numberOfMoves,currPlace,previousPlace,depth,maximizingPlayer,alpha,beta):
    if (depth == numberOfMoves ):
        best = currPlace
        return ( board[currPlace[0]][currPlace[1]]  , best )      
    if ( maximizingPlayer ):
        bestMove = -(math.inf)
        previousPlace = currPlace
        Places = possiblePlaces( board , currPlace)
        best = None
        for nextMove in Places:
            board[nextMove[0]][nextMove[1]] = board[nextMove[0]][nextMove[1]] + board[currPlace[0]][currPlace[1]]   
            move = alphaBeta(board,numberOfMoves,nextMove,previousPlace,depth + 1,False , alpha , beta )[0]
            board[nextMove[0]][nextMove[1]] = board[nextMove[0]][nextMove[1]] - board[currPlace[0]][currPlace[1]]
            if move > bestMove:
                bestMove = move
                best = nextMove
                lst.append(best)
            alpha = max(alpha,bestMove)
            if (alpha >= beta):
                break
        return  board[nextMove[0]][nextMove[1]] , best 
    else:
        bestMove = math.inf
        place=[-1,0,1]
        best = None
        for nextMove in place:
            temp = board[previousPlace[0]][previousPlace[1]]
            board[previousPlace[0]][previousPlace[1]] = nextMove
            move= alphaBeta(board,numberOfMoves,currPlace,previousPlace,depth,True , alpha , beta )[0]
            board[previousPlace[0]][previousPlace[1]] = temp
            if move < bestMove:
                bestMove = move
                best = nextMove
            beta = min(beta,bestMove)
            if( alpha >= beta):
                break
        return board[currPlace[0]][currPlace[1]] , best


def play(board ,numOfMoves,minScore):
    currPlace = [2,0]
    previousPlace = [] 
    numberOfMoves = numOfMoves
    for x in range (numOfMoves):
        showBoard(board)
        BestMove = alphaBeta(board,numberOfMoves,currPlace,previousPlace,0,True , -(math.inf) , math.inf)[1]
        print("BestMove: ",BestMove)
        board[BestMove[0]][BestMove[1]] = board[BestMove[0]][BestMove[1]] + board[currPlace[0]][currPlace[1]]
        board[currPlace[0]][currPlace[1]] = randint(-1,1)
        previousPlace = currPlace
        currPlace[0] = BestMove[0]
        currPlace[1] = BestMove[1]
        if( x == numOfMoves-1 ):
            showBoard(board)
    print("Minimum Goal:",minScore," ","Current Score:",board[currPlace[0]][currPlace[1]])
    if(board[currPlace[0]][currPlace[1]] >= minScore):
        print("YOU WIN")
    else:
        print("YOU LOSE")
        

    
N = int(input("Enter Your Number of Moves:"))
M = int(input("Enter Your minimum Goal:"))
Board = createBoard(3)
play(Board ,N,M)
