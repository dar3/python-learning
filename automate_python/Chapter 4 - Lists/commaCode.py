spam = ['apples', 'bananas', 'tofu', 'cats']
emptyList = []


def commaFunction(words):
    for i in words:
        if i != words[-1]:
            print(i + ',', end=" ")

        if i == words[-1]:
            print('and', words[-1], end=" ")


commaFunction(emptyList)
