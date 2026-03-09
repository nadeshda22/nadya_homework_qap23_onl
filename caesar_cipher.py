alfavit_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alfavit_EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt():

    lang = input("Введите язык: ")
    step = int(input("Введите шаг:"))
    message = input("Введите сообщение для шифровки:").upper()
    result = ""

    if lang.lower() in ["ru", "русский"]:
        for i in message:
            place = alfavit_RU.find(i)
            new_place = (place + step) % len(alfavit_RU)

            if i in alfavit_RU:
                result += alfavit_RU[new_place]
            else:
                result += i

    elif lang.lower() in ["en", "english", "английский"]:
        for i in message:
            place = alfavit_EN.find(i)
            new_place = (place + step) % len(alfavit_EN)

            if i in alfavit_EN:
                result += alfavit_EN[new_place]
            else:
                result += i

    else:
        print("Неверно указан язык!")

    print(result)


def decrypt():

    lang = input("Введите язык: ")
    step = int(input("Введите шаг:"))
    message = input("Введите сообщение для дешифровки:").upper()
    result = ""

    if lang.lower() in ["ru", "русский"]:
        for i in message:
            place = alfavit_RU.find(i)
            new_place = (place - step) % len(alfavit_RU)

            if i in alfavit_RU:
                result += alfavit_RU[new_place]
            else:
                result += i

    elif lang.lower() in ["en", "english", "английский"]:
        for i in message:
            place = alfavit_EN.find(i)
            new_place = (place - step) % len(alfavit_EN)

            if i in alfavit_EN:
                result += alfavit_EN[new_place]
            else:
                result += i
    else:
        print("Неверно указан язык!")

    print(result)


while True:
    action = input("Выберите действие (1 - шифровка, 2 - расшифровка, 0 - выход): ")
    if action == "1":
        encrypt()
    elif action == "2":
        decrypt()
    elif action == "0":
        break
