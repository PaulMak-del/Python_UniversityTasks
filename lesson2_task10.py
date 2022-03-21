import re


def do_magic(array):
    count = 0
    for string in array:
        match = re.search("\w.\d{1,2} \d{1,2}", string)
        if match is not None:
            # print(match[0])
            var = (match[0].split())[-1]
            word = match[0]
            if re.fullmatch("[kKкК]", word[0]):
                print("ИКБО-", end='')
            elif re.fullmatch("[BвВvV]", word[0]):
                print("ИВБО-", end='')
            elif re.fullmatch("[HнН]", word[0]):
                print("ИНБО-", end='')

            num = re.search("\d+", word)
            print(num[0], end='')

            print(" вариант: " + var)
            count += 1

    print(count)


bad_subj = ['main.py', 'k17 14', 'K13 18', 'к02 1', 'ИВБО-11 Вариант№14', 'к02 21', '1.3.py', 'В 11 4',
            '\ufeff\u200b\u200bк20 21', 'B7 21', 'Фамилия Имя Задача 1.1', 'В03 12', 'к08 24', 'к07 23',
            '1.2.py, 1.3.py, 1.4.py', '1.1.py', 'K14 23', 'в7 ', 'к6 ', '\u200b\u200bк20 21', 'к2 в3', 'В104',
            'В1013', 'B3 29', 'v10 15', 'k13 30', 'В 7 10', 'Фамилия И.О. к7 31', '1.2.py', 'К10', 'ПитонН4 н11',
            'K13 28', 'К4', 'K17 10', 'и4 11', 'Н1', 'н01 28', 'б3 5', 'Re: в6 28', 'к-11 3', '2_1.py, 2_2.py']

bad_subj2 = ['ИВБО-11 Вариант№14',
            'B7 21',
            'к2 в3', 'В104',
            'В1013', 'B3 29', 'Фамилия И.О. к7 31', 'ПитонН4 н11',
            'и4 11', 'Re: в6 28']

do_magic(bad_subj)
