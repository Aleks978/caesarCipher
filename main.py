while True:

    alft_UA = 'АБВГҐДЕЄЖЗИіїЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГҐДЕЄЖЗИіїЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    alft_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shfr = int(input('cipher key: '))
    text = input("text: ").upper()
    res = ''
    lang = input('choose language UA/EU (1/2): ')
    if lang == '1':
        for i in text:
            a = alft_UA.find(i)
            new_a = a + shfr
            if i in alft_UA:
                res += alft_UA[new_a]
            else:
                res += i
    else:
        for i in text:
            a = alft_EU.find(i)
            new_a = a + shfr
            if i in alft_EU:
                res += alft_EU[new_a]
            else:
                res += i
    print(res)