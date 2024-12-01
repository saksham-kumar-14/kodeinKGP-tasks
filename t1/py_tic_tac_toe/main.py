import random

def cal_score(grid, x, y, chance):

    if check_win(grid, 'O'):
        return 1
    if check_win(grid, 'X'):
        return -1
    if check_draw(grid):
        return 0

    if chance == 'O':
        score = -float('inf')

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '.':
                    grid[i][j] = 'O'
                    score = max(score, cal_score(grid, i, j, 'X'))
                    grid[i][j] = '.'

        return score
    else:
        score = float('inf')

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '.':
                    grid[i][j] = 'X'
                    score = min(score, cal_score(grid, i, j, 'O'))
                    grid[i][j] = '.'

        return score



def select(grid):

    score = -float('inf')
    ans = (0,0)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                grid[i][j] = 'O'
                cscore = cal_score(grid, i, j, 'X')
                grid[i][j] = '.'
                if cscore > score:
                    score = cscore
                    ans = (i, j)

    print(ans)
    return ans

def check_win(grid, k):
    for i in range(0, 3):
        if k == grid[i][0] == grid[i][1] == grid[i][2]:
            return 1
        if k == grid[0][i] == grid[1][i] == grid[2][i]:
            return 1
    if k == grid[0][0] == grid[1][1] == grid[2][2]:
        return 1
    if k == grid[0][2] == grid[1][1] == grid[2][0]:
        return 1
    return 0

def check_draw(grid):
    draw = True
    for i in grid:
        for j in i:
            if j == '.':
                draw = False
                break
    if draw:
        return 1
    return 0

def print_grid(grid):
    for i in grid:
        for j in i:
            print(j, end=" ")
        print()

def game_over(grid):

    if check_win(grid, 'O'):
        print("Computer wins!")
        return 1
    if check_win(grid, 'X'):
        print("You win!")
        return 1

    if check_draw(grid):
        print("Game draw")
        return 1

    return 0

def main():
    grid = [ ['.', '.', '.'],
             ['.', '.', '.'],
             ['.', '.', '.']
        ]

    flag = True
    play_first = random.choice([0, 1])

    while flag :

        # computer chance
        if not play_first:
            i, j = select(grid)
            grid[i][j] = 'O'

        if game_over(grid):
            flag = False
            print_grid(grid)
            break

        # player chance
        print_grid(grid)
        print('''
        1 - to mark 1st cell
        2 - to mark 2nd cell and so on.
        ''')

        move = int(input("Enter your move: "))

        i = (move-1)//3
        j = (move-1)%3
        while i > 2 or j > 2 or grid[i][j] != '.' :
            print(grid)
            print(i, j)
            move = int(input("Enter valid input"))

        grid[i][j] = 'X'

        if game_over(grid):
            flag = False
            print_grid(grid)
            break


        # computer chance
        if play_first:
            i, j = select(grid)
            grid[i][j] = 'O'

        if game_over(grid):
            flag = False
            print_grid(grid)
            break


print("Game begins.")
main()
print("Game ends.")
