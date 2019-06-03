import os

def gen_images():
    for i in range(1, 25):
        # print("file2byteslice -package images -input images/{}.png -output images/wall{}.go -var W{}_png".format(i, i, i))
        os.system("file2byteslice -package images -input images/{}.png -output images/wall{}.go -var W{}_png".format(i, i, i))