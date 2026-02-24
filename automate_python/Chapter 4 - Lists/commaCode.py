spam = ['apples', 'bananas', 'tofu', 'cats']
spam2 = ['1', '22', '333', '4444']
numbersList = [1, 2, 3, 4, 5]
emptyList = []


def commaFunction(words):
    for i in words:
        if i != words[-1]:
            print(str(i) + ',', end=" ")

        if i == words[-1]:
            print('and', words[-1], end=" ")


commaFunction(spam)
# commaFunction(spam2)
# commaFunction(numbersList)
# commaFunction(emptyList)
