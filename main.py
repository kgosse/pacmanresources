import os

def gen_images():
    for i in range(1, 25):
        # print("file2byteslice -package images -input images/{}.png -output images/wall{}.go -var W{}_png".format(i, i, i))
        os.system("file2byteslice -package images -input images/{}.png -output images/wall{}.go -var W{}_png".format(i, i, i))
        print("images/wall{}.go".format(i))

def gen_bigdots():
    for i in range(1, 3):
        # print("file2byteslice -package images -input images/{}.png -output images/wall{}.go -var W{}_png".format(i, i, i))
        os.system("file2byteslice -package images -input images/BigDot{}.png -output images/BigDot{}.go -var BigDot{}_png".format(i, i, i))
        print("images/BigDot{}.go".format(i))

if __name__ == "__main__":
    # gen_images()
    gen_bigdots()
