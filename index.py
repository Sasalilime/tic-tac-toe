map = [
      [' . ', ' . ', ' . '],
      [' . ', ' . ', ' . '],
      [' . ', ' . ', ' . ']
]


def draw():
    for i in range(3):
        for j in range(3):
            print(map[i][j], end="")
        print()


while True:
    draw()
    a = int(input('[1-9] ? > '))
