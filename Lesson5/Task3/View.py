from os import system

def print_matrix(matrix):
    system('cls')
    print('\n'.join([str().join(['{:4}'.format(item) for item in row]) for row in matrix]))
