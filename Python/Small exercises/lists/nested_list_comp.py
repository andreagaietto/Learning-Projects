board = [[num for num in range(1, 4)] for val in range(1, 4)]
print(board)
game_board = [["X" if num % 2 !=0 else "O" for num in range(1, 4)] for val in range(1,4)]
print(game_board)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[print(val) for val in l] for l in nested_list]

