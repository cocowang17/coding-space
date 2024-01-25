# 绘制棋盘
def draw_board():
    print("  1 2 3 4 5 6 7 8 9")
    print("A B C D E F G H I J")

# 检查是否胜利
def check_win(over_pos):
    mp = {'A1': 1, 'A2': 2, 'A3': 3, 'A4': 4, 'A5': 5,
          'B1': 1, 'B2': 6, 'B3': 7, 'B4': 8, 'B5': 9,
          'C1': 1, 'C2': 10, 'C3': 11, 'C4': 12, 'C5': 13,
          'D1': 1, 'D2': 14, 'D3': 15, 'D4': 16, 'D5': 17,
          'E1': 1, 'E2': 18, 'E3': 19, 'E4': 20, 'E5': 21,
          'F1': 1, 'F2': 22, 'F3': 23, 'F4': 24, 'F5': 25,
          'G1': 1, 'G2': 26, 'G3': 27, 'G4': 28, 'G5': 29,
          'H1': 1, 'H2': 30, 'H3': 31, 'H4': 32, 'H5': 33,
          'I1': 1, 'I2': 34, 'I3': 35, 'I4': 36, 'I5': 37}
    # 判断横向是否胜利
    for i in range(1, 16):
        if over_pos[i] == 5:
            return True
    # 判断竖向是否胜利
    for j in range(1, 16):
        if over_pos[j * 5] == 5:
            return True
    # 判断左斜是否胜利
    for k in range(1, 16):
        if over_pos[k * 5 + 4 - (k % 5)] == 5:
            return True
    # 判断右斜是否胜利
    for l in range(1, 16):
        if over_pos[l * 5 + (l % 5)] == 5:
            return True
    # 判断没有胜利
    return False

# 玩家落子
def player_move(x, y):
    if pos[x][y] == 0:
        pos[x][y] = current_player
        if check_win(pos):
            print(f"{'黑方' if current_player == 2 else '白方'} 胜利")
            return
        # 交换玩家
        current_player = 3 - current_player
    else:
        print("该位置已有棋子，请重新选择位置！")

# 初始化棋盘和玩家
pos = [[' ' for _ in range(16)] for _ in range(16)]
current_player = 2

# 游戏循环
while True:
    draw_board()
    print("轮到", "黑方" if current_player == 2 else "白方", "落子")
    x, y = map(int, input("请输入坐标（A1-H9）：").split())
    player_move(x, y)
