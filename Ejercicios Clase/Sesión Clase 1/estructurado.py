def jump(name):
    print(name, "salta!")

def movement(name, direction):
    print("\n", name, "se mueve a la", direction, end="")

def run_and_jump(name, direction):
    movement(name, direction)
    print(" y ", end="")
    jump(name)


if __name__ == "__main__":

    player1 = 'Mario'
    player2 = 'Aire acondicionado'

    enemy1 = 'Koopa Troopa'
    enemy2 = 'Goomba'

    jump(player2)
    movement(player1, 'izquierda')
    run_and_jump(player1, 'derecha')