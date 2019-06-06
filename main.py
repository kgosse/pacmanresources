import os

def gen_walls():
    for i in range(1, 25):
        os.system("file2byteslice -package images -input images/{}.png -output images/wall{}.go -var W{}_png".format(i, i, i))
        print("images/wall{}.go".format(i))

def gen_bigdots():
    for i in range(1, 3):
        os.system("file2byteslice -package images -input images/BigDot{}.png -output images/BigDot{}.go -var BigDot{}_png".format(i, i, i))
        print("images/BigDot{}.go".format(i))

def gen_dot():
    os.system("file2byteslice -package images -input images/Dot.png -output images/Dot.go -var Dot_png")
    print("images/Dot.go")

def gen_pacman():
    for i in range(1, 9):
        os.system("file2byteslice -package images -input images/pacman{}.png -output images/pacman{}.go -var Pacman{}_png".format(i, i, i))
        print("images/pacman{}.go".format(i))

def gen_blinky():
    for i in range(1, 9):
        os.system("file2byteslice -package images -input images/blinky{}.png -output images/blinky{}.go -var Blinky{}_png".format(i, i, i))
        print("images/blinky{}.go".format(i))

def gen_clyde():
    for i in range(1, 9):
        os.system("file2byteslice -package images -input images/clyde{}.png -output images/clyde{}.go -var Clyde{}_png".format(i, i, i))
        print("images/clyde{}.go".format(i))

def gen_inky():
    for i in range(1, 9):
        os.system("file2byteslice -package images -input images/inky{}.png -output images/inky{}.go -var Inky{}_png".format(i, i, i))
        print("images/inky{}.go".format(i))

def gen_pinky():
    for i in range(1, 9):
        os.system("file2byteslice -package images -input images/pinky{}.png -output images/pinky{}.go -var Pinky{}_png".format(i, i, i))
        print("images/pinky{}.go".format(i))

if __name__ == "__main__":
    # gen_walls()
    # gen_bigdots()
    # gen_dot()
    # gen_pacman()
    # gen_blinky()
    # gen_clyde()
    gen_inky()
    gen_pinky()
