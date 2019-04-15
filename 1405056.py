import queue as q
import copy
import collections as c
import math
from sympy import *

bd_size = 3
start = [[0 for x in range(bd_size)] for y in range(bd_size)]
goal = [[0 for x in range(bd_size)] for y in range(bd_size)]
blank_x, blank_y, i = 0, 0, 1
for row in range(0, bd_size):
    for col in range(0, bd_size):
        if row == bd_size - 1 and col == bd_size - 1:
            goal[row][col] = 0
        else:
            goal[row][col] = i
            i += 1
        # start[row][col] = int(input())
        # if start[row][col] == 0:
        #     blank_x, blank_y = row, col


start[0][0] = 7
start[0][1] = 2
start[0][2] = 4
# start[0][3] = 9
start[1][0] = 5
start[1][1] = 0
start[1][2] = 6
# start[1][3] = 10
start[2][0] = 8
start[2][1] = 3
start[2][2] = 1
# start[2][3] = 11
# start[3][0] = 12
# start[3][1] = 13
# start[3][2] = 14
# start[3][3] = 15


# print("Start state")
# for row in range(0, bd_size):
#     for col in range(0, bd_size):
#         print(start[row][col], end='\t')
#     print()
#
# print("Goal state")
# for row in range(0, bd_size):
#     for col in range(0, bd_size):
#         print(goal[row][col], end='\t')
#     print()


def no_of_misplaced_tiles(initial, final):
    count = 0
    for i in range(0, bd_size):
        for j in range(0, bd_size):
            if initial[i][j] and initial[i][j] != final[i][j]:
                count += 1
    return count


def gen_legal_moves(x, y):  # returns allowable moves of blank tile
    new_moves = []
    move_offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    for i in move_offsets:
        new_x = x + i[0]
        new_y = y + i[1]
        if legal_coord(new_x) and legal_coord(new_y):
            new_moves.append((new_x, new_y))
    return new_moves


def legal_coord(x):
    if x in range(0, bd_size):
        return True
    else:
        return False


def blank_x_y(grid):
    x_y = []
    for row in range(0, bd_size):
        for col in range(0, bd_size):
            if grid[row][col] == 0:
                x_y.append(row)
                x_y.append(col)
                return x_y


def swap_elements(grid, new_positions, current_x_y):
    modified_grids_dict = {}
    i = len(dict)
    for pos in new_positions:
        modified_grid = copy.deepcopy(grid)
        modified_grid[pos[0]][pos[1]], modified_grid[current_x_y[0]][current_x_y[1]] = grid[current_x_y[0]][current_x_y[1]], grid[pos[0]][pos[1]]
        # output.write("child\n")
        print_grid(modified_grid)
        if modified_grid in dict.values():
            modified_key = list(dict.keys())[list(dict.values()).index(modified_grid)]
        else:
            modified_key = "entry " + str(i)
            i += 1
            dict.update({modified_key: copy.deepcopy(modified_grid)})
        modified_grids_dict.update({modified_key: copy.deepcopy(modified_grid)})
    print(dict)

    return modified_grids_dict


def print_grid(grid):
    for row in range(0, bd_size):
        for col in range(0, bd_size):
            print(grid[row][col], end=' ')
            # output.write(str(grid[row][col]) + " ")
        print()
        # output.write("\n")
    print()
    # output.write("\n")


print_grid(goal)


def print_array(grid):
    for i in range(0, bd_size * bd_size):
        print(grid[i], end=' ')
    print()


def print_path_in_file(grid):
    for row in range(0, bd_size):
        for col in range(0, bd_size):
            # print(grid[row][col], end=' ')
            output.write(str(grid[row][col]) + " ")
            print()
        output.write("\n")
    # print()
    output.write("\n")


def value_index(current_element, goal):
    index = {}
    for i in range(0, bd_size):
        for j in range(0, bd_size):
            if goal[i][j] == current_element:
                index["x"] = i
                index["y"] = j
                return index


def manhattan_distance(current, goal):
    manhattan_distance = 0
    for i in range(0, bd_size):
        for j in range(0, bd_size):
            if current[i][j] and current[i][j] != goal[i][j]:
                current_element = current[i][j]
                current_x = i
                current_y = j
                index_in_goal = value_index(current_element, goal)
                manhattan_distance += math.fabs(index_in_goal["x"] - current_x) + math.fabs(index_in_goal["y"] - current_y)
    return manhattan_distance


def euclidean_distance(current, goal):
    euclidean_distance = 0
    for i in range(0, bd_size):
        for j in range(0, bd_size):
            if current[i][j] and current[i][j] != goal[i][j]:
                current_element = current[i][j]
                current_x = i
                current_y = j
                index_in_goal = value_index(current_element, goal)
                dx = math.fabs(current_x - index_in_goal["x"])
                dy = math.fabs(current_y - index_in_goal["y"])
                euclidean_distance += math.sqrt(dx * dx + dy * dy)
    return euclidean_distance


def convert_2d_to_1d(initial):
    result = []
    for row in range(0, bd_size):
        for col in range(0, bd_size):
            result.append(initial[row][col])
    return result


def pos_array(initial):
    pos = [-1 for i in range(0, bd_size * bd_size)]
    for element in range(0, bd_size * bd_size):
        pos[initial[element]] = element
    return pos


def n_max_swap(initial, goal):
    swap_cost = 0
    initial_1d = convert_2d_to_1d(initial)
    print("current permutation")
    print_array(initial_1d)
    pos = pos_array(initial_1d)
    print("current position")
    print_array(pos)
    goal_1d = convert_2d_to_1d(goal)
    while initial_1d != goal_1d:
        swap_cost += 1
        print(swap_cost)
        initial_1d[pos[7]], initial_1d[pos[pos[7]]] = initial_1d[pos[pos[7]]], initial_1d[pos[7]]
        print("current permutation")
        print_array(initial_1d)
        pos = pos_array(initial_1d)
        print("current position")
        print_array(pos)
    print("end")
    return swap_cost


def no_of_tiles_out_of_row_col(current, goal):
    out_of_row = 0
    out_of_col = 0
    for i in range(0, bd_size):
        for j in range(0, bd_size):
            if current[i][j] and current[i][j] != goal[i][j]:
                current_element = current[i][j]
                current_row = i
                current_col = j
                index_in_goal = value_index(current_element, goal)
                goal_row = index_in_goal["x"]
                goal_col = index_in_goal["y"]
                if current_row != goal_row:
                    out_of_row += 1
                if current_col != goal_col:
                    out_of_col += 1
    return out_of_row + out_of_col


# n_max_swap(start, goal)

def reconstruct_path(came_from, start, goal):
    path = c.OrderedDict()
    current = goal
    while current != start:
        current_key = list(dict.keys())[list(dict.values()).index(current)]
        path[current_key] = current
        current = came_from[current_key]
    path[list(dict.keys())[list(dict.values()).index(start)]] = start
    output.write("Printing paths\n")
    for k in reversed(list(path.keys())):
        print_path_in_file(path[k])
    # output.write("Heuristic: Number of misplaced tiles\n")
    output.write("Paths Printed\n")
    output.write("Required moves: " + str(len(path) - 1) + "\n")
    output.write("Expanded nodes: " + str(expanded_node) + "\n")
    output.write("Solution depth: " + str(solution_depth) + "\n")
    output.write("Effective branching factor: " + str(expanded_node ** (1 / solution_depth)) + "\n")


output = open("output_1.txt", "w")
frontier = q.PriorityQueue()
frontier.put(start, 0)
dict = {"start": start, "goal": goal}
expanded_dict = {}
came_from = {}
cost_so_far = {}
visited = {"start": True}
level = {"start": 0}
came_from["start"] = None
cost_so_far["start"] = 0
item = 0
expanded_node = 0
solution_depth = 0
while not frontier.empty():
    current = frontier.get()
    current_key = list(dict.keys())[list(dict.values()).index(current)]
    print("grid " + str(item))
    item += 1
    print_grid(current)
    if no_of_misplaced_tiles(current, goal) == 0:
        print("milse")
        solution_depth = level[current_key]
        break
    current_x_y = blank_x_y(current)
    print("blank_x_y")
    print(current_x_y[0], current_x_y[1])
    new_positions = gen_legal_moves(current_x_y[0], current_x_y[1])
    print("new_positions")
    for pos in new_positions:
        print(pos, end=' ')
    print()
    # expanded_dict[current_key] = current
    # expanded_node += 1
    modified_grids = swap_elements(current, new_positions, current_x_y)
    for key_next in modified_grids.keys():
        # print("1")
        next = modified_grids[key_next]
        if key_next not in visited.keys():
            level[key_next] = level[current_key] + 1
            visited[key_next] = True

        # print(dict.values())
        new_cost = cost_so_far[list(dict.keys())[list(dict.values()).index(current)]] + no_of_misplaced_tiles(current, next)
        if key_next not in cost_so_far or new_cost < cost_so_far[key_next]:
            cost_so_far[key_next] = new_cost
            print(cost_so_far)
            priority = new_cost + no_of_misplaced_tiles(next, goal)
            if next not in expanded_dict.values():
                frontier.put(next, priority)
                came_from[key_next] = current
    expanded_dict[current_key] = current
    expanded_node += 1

print("end")
reconstruct_path(came_from, start, goal)
