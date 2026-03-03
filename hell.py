я='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ы='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def а():
    ё=input('Введите язык: ')
    з=int(input('Введите шаг:'))
    х=input('Введите сообщение для шифровки:').upper()
    ъ=''
    if ё.lower() in['ru','русский']:
        for э in х:
            ю=я.find(э)
            ч=(ю+з)%len(я)
            if э in я:
                ъ+=я[ч]
            else:
                ъ+=э
    elif ё.lower() in['en','english','английский']:
        for э in х:
            ю=ы.find(э)
            ч=(ю+з)%len(ы)
            if э in ы:
                ъ+=ы[ч]
            else:
                ъ+=э
    else:
        print('Неверно указан язык!')
        return
    print(ъ)

def б():
    ё=input('Введите язык: ')
    з=int(input('Введите шаг:'))
    х=input('Введите сообщение для дешифровки:').upper()
    ъ=''
    if ё.lower() in['ru','русский']:
        for э in х:
            ю=я.find(э)
            ч=(ю-з)%len(я)
            if э in я:
                ъ+=я[ч]
            else:
                ъ+=э
    elif ё.lower() in['en','english','английский']:
        for э in х:
            ю=ы.find(э)
            ч=(ю-з)%len(ы)
            if э in ы:
                ъ+=ы[ч]
            else:
                ъ+=э
    else:
        print('Неверно указан язык!')
        return
    print(ъ)

while True:
    щ=input('Выберите действие (1 - шифровка, 2 - расшифровка, 0 - выход): ')
    if щ=='1':
        а()
    elif щ=='2':
        б()
    elif щ=='0':
        break