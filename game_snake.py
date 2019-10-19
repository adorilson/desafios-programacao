#! /usr/bin/python3

"""
http://www.checkio.org/mission/task/snake/
"""

SNAKE = '0'
CHERRY = 'C'
EMPTY = '.'
TREE = 'T'
BODY = '123456789'


TO_UP = 'U'
TO_DOWN = 'D'
TO_LEFT = 'L'
TO_RIGHT = 'R'
FORWARD = 'F'


def found(data, char):
    for i, line in enumerate(data):
        if char in line:
            return [i, line.index(char)]

def snake_direction(data, snake):
    if data[snake[0]-1][snake[1]]=='1':
        return TO_DOWN
    
    if data[snake[0]+1][snake[1]]=='1':
        return TO_UP
        
    if data[snake[0]][snake[1]-1]=='1':
        return TO_RIGHT
    
    if data[snake[0]][snake[1]+1]=='1':
        return TO_LEFT
        
    raise Exception('No body snake found')

def move_to(data, snake, cherry):
    if snake[1]==cherry[1]: # same column
        return TO_UP

def move_snake(data, snake):
    data[4] = data[4][:1] + '0' + data[4][2:]
    data[5] = data[5][:1] + '1' + data[5][2:]
    data[6] = data[6][:1] + '2' + data[6][2:]
    data[7] = data[7][:1] + '3' + data[7][2:]
    data[8] = data[8][:1] + '4' + data[8][2:]
    data[9] = data[9][:1] + '4' + data[9][2:]

def checkio(data):
    
    snake = found(data, SNAKE)
    cherry= found(data, CHERRY)
    
    if snake[0]==cherry[0]: # same line
        if snake[1]<cherry[1] and data[snake[0]][snake[1]+1]!='T':
            if snake_direction(data, snake)in [TO_UP, TO_DOWN]:
                return TO_LEFT
            if snake_direction(data, snake)in [TO_LEFT]:
                return FORWARD
            
    
    if snake == cherry:
        return step
    else:
        return step + checkio(data)
    
    #replace this for solution
    return "F" or "R" or "L" or "FRL"

#These "asserts" using only for self-checking and not necessary for auto-testing
data = []
data.append('.T.....T..')
data.append('.C........')
data.append('....T.....')
data.append('..T...T...')
data.append('..........')
data.append('.0...T....')
data.append('.1........')
data.append('.2.T...T..')
data.append('.3...T....')
data.append('.4........')

assert found(data, CHERRY)==[1, 1]
assert found(data, SNAKE)==[5, 1]
snake = found(data, SNAKE)
cherry = found(data, CHERRY)
assert snake_direction(data, snake) == TO_UP
assert move_to(data, snake, cherry) == TO_UP

new_data = data[:]
new_data[4] = new_data[4][:1] + '0' + new_data[4][2:]
new_data[5] = new_data[5][:1] + '1' + new_data[5][2:]
new_data[6] = new_data[6][:1] + '2' + new_data[6][2:]
new_data[7] = new_data[7][:1] + '3' + new_data[7][2:]
new_data[8] = new_data[8][:1] + '4' + new_data[8][2:]
new_data[9] = new_data[9][:1] + '4' + new_data[9][2:]
move_snake(data, snake)
assert data == new_data



