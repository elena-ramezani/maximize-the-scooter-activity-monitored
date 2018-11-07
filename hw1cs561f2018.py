import pdb
import copy
global dimension, police_number, solutions


def scooter_index(solutions ,list_file):
    all_result = []
    for solution in solutions:
        activity_point = 0
        for number in all_list[3:]:
            if number != '':
                r, col = number.split(',')
                row = int(r)
                column = int(col)
                if solution[row][column]==1:
                    activity_point +=1
        all_result.append(activity_point)
    return max(all_result)


def print_solutions(solutions):
    for ite, sol in enumerate(solutions):
        for row in sol:
            print(row)
        print(ite)


def placment_police(board, column, no_police_on_board):
    if column >= dimension or no_police_on_board == input_police_number:
        return True

    for row_iter in range(dimension):
        if issafe(board, row_iter, column):
            board[row_iter][column] = 1
            no_police_on_board = no_police_on_board + 1

            if no_police_on_board == input_police_number:
                if board not in solutions:
                    add_solution(board)

            placment_police(board, column + 1, no_police_on_board)
            no_police_on_board = no_police_on_board - 1
            board[row_iter][column] = 0

        #placment_police(board, column + 1, no_police_on_board)
    #no_police_on_board = no_police_on_board - 1
    board[row_iter][column] = 0





    #return False


def add_solution(board):
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)


def issafe(board, row, column):
    for i in range(column):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, dimension, 1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def ss():
    if placment_police(board, 0, 0) == False:
        print('no solution')
        return False

    return True

if __name__ == "__main__":
    input_file = open('input3.txt', 'r')
    output_file = open('output.txt', 'w')
    lines = input_file.readlines()
    #pdb.set_trace()
    all_list = []
    for line in lines:
        list_line = line.replace('\r', '').replace('\n', '')
        all_list.append(list_line)

    dimension = int(all_list[0])
    input_police_number = int(all_list[1])
    scooter_number = int(all_list[2])
    #print scooter_number
    #print input_police_number
    #print dimension
    board = [[0 for i in xrange(dimension)] for i in xrange(dimension)]
    solutions = []
    #pdb.set_trace()
    ss()
    #pdb.set_trace()
    #print_solutions(solutions)

    result = scooter_index(solutions, all_list)
    #print result
    #print("Total solutions = {}".format(len(solutions)))
    #pdb.set_trace()
    output_file.write(str(result))
    output_file.close()







