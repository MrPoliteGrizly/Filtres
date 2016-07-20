from PIL import Image
from os import listdir

path = listdir("photo")
print("В папке:", len(path), "фото")
path_l = len(path)

print("Фильтры:\n"
      "pretty\nhell\ngrey\nred\nnew\nloop")
a = input("Выберите фильтр: ")


for path in path:
        print("Фильтр приминилcя к: " + path)
        im = Image.open("photo/" + path)
        pix = im.load()
        x, y = im.size

        p = 0

        if a == "pretty":
            for i in range(x):
                for j in range(y):
                    r, g, b = pix[i, j]
                    # grey = (r + g + b) // 3
                    pix[i, j] = r, b, g

        elif a == "hell":
            for i in range(x):
                for j in range(y):
                     r, g, b = pix[i, j]
                     # grey = (r + g + b) // 3
                     pix[i, j] = r + 255, b, g

        elif a == "grey":
            for i in range(x):
                for j in range(y):
                    r, g, b = pix[i, j]
                    grey = (r + g + b) // 2
                    pix[i, j] = grey, grey, grey

        elif a == "red":
            for i in range(x):
                for j in range(y):
                    r, g, b = pix[i, j]
                    grey = (r + g + b) // 3
                    pix[i, j] = 150 + r, g, b

        elif a == "new":
            for i in range(x // 2):
                for j in range(y):
                    r, g, b = pix[i, j]
                    grey = (r + g + b) // 3
                    pix[i, j] = 150 + r, g, b
            for i in range(x):
                for j in range(y):
                    r, g, b = pix[i, j]
                    grey = (r + g + b) // 3
                    pix[i, j] = r, g + 100, b

        elif a == "loop":
            for i in range(x):
                for j in range(y):
                    r, g, b = pix[i, j]
                    pix[i, j] = b, g + 150, r

        im.show()
        # im.save("photo/" + path) # Сохранение файлов(можно делать только 1 раз)








