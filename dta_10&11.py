'''
Задания с учебного сайта http://kispython.ru
'''
import struct


class main:

    def __init__(self):
        self._state = "A"
        self._graph = {
            ("A", "shift"): ("B", 0),
            ("B", "push"): ("C", 1),
            ("B", "shift"): ("D", 2),
            ("B", "sway"): ("E", 3),
            ("C", "shift"): ("C", 5),
            ("C", "push"): ("D", 4),
            ("D", "shift"): ("A", 7),
            ("D", "sway"): ("E", 6),
            ("E", "shift"): ("F", 8)
        }

    def shift(self):
        self._state, ret = self._graph[(self._state, "shift")]
        return ret

    def push(self):
        self._state, ret = self._graph[(self._state, "push")]
        return ret

    def sway(self):
        self._state, ret = self._graph[(self._state, "sway")]
        return ret


def main_1(table):
    # 1
    for row in table:
        del row[1]

    # 2
    it = 0
    copy = table[:]
    for row_1 in copy:
        for row_2 in copy[it + 1:]:
            if row_1 == row_2:
                table.remove(row_2)
        it += 1

    # 3
    for row in table[:]:
        if set(row) == {None}:
            table.remove(row)

    # 4, 5
    for row in table:
        if row[0] == 'Да':
            row[0] = 'Выполнено'
        else:
            row[0] = 'Не выполнено'

        name, mail = row[1].split(';')
        letter = name[0]
        for i in range(len(name)):
            if name[i] == ' ':
                name = letter + '.' + name[i+1:]
                break
        mail = mail.replace('@', '[at]')

        row[1] = mail
        row.insert(2, name)
    for row_id in range(len(table)):
        for col_id in range(row_id, len(table[row_id])):
            tmp = table[row_id][col_id]
            table[row_id][col_id] = table[col_id][row_id]
            table[col_id][row_id] = tmp

    return table


# Var 40
def parse(data, offset, type, arr_len):
    return list(struct.unpack(f'{arr_len}{type}', data[offset:offset + arr_len * struct.calcsize(type)]))


def parse_d(data, offset):
    result = dict()
    result['D1'] = parse(data, offset, '>B', 3)
    result['D2'] = struct.unpack('>d', data[offset + 3:offset + 3 + 8])
    return result


def parse_c(data, offset):
    result = dict()
    result['C1'] = struct.unpack('>Q', data[offset:offset + 8])[0]
    result['C2'] = parse(data, offset + 8, '>h', 2)
    result['C3'] = struct.unpack('>i', data[offset + 8 + 4:offset + 8 + 4 + 4])[0]
    result['C4'] = struct.unpack('>h', data[offset + 16:offset + 16 + 2])[0]
    result['C5'] = struct.unpack('>i', data[offset + 18:offset + 18 + 4])[0]
    return result


def parse_b(data, offset):
    result = dict()
    result['B1'] = parse_c(data, offset)
    result['B2'] = struct.unpack('>b', data[offset + 22:offset + 22 + 1])[0]
    return result


def parse_a(data, offset):
    result = dict()
    result['A1'] = struct.unpack('>I', data[offset:offset + 4])[0]
    a2_size, a2_addr = struct.unpack('>IH', data[offset + 4: offset + 4 + 6])
    a2_b_addrs = parse(data, offset + a2_addr, '>H', a2_size)
    result['A2'] = [parse_b(data, addr) for addr in a2_b_addrs]
    result['A3'] = ''.join([x.decode('ascii') for x in parse(data, offset + 10, '>c', 3)])
    result['A4'] = parse_d(data, struct.unpack('>I', data[offset + 13: offset + 13 + 4])[0])
    result['A5'] = struct.unpack('>I', data[offset + 17:offset + 17 + 4])[0]
    result['A6'] = struct.unpack('>Q', data[offset + 21:offset + 21 + 8])[0]
    result['A7'] = struct.unpack('>b', data[offset + 28:offset + 28 + 2])[0]
    return result


def main_2(data):
    return parse_a(data, 5)


var = (b'rZKQQ\x90\x84\xb1\x89\x00\x00\x00\x02\x00Qcop\x00\x00\x00U\x08\xef'
       b'\x17\\\xd5=c_#\xcd\x81\x89\x96j_\xa69\x9cuT\xc1b\xa9\xaf\xfeaO\xa8\xd0\xc7'
       b'U\xbf&\xdc\xa3\x13\xec)\xb1\xe6\xae.;G\x1d,\xe8q\xb5\x93\xd0\xbb\xe12q]6\xf7'
       b'\xa3\x00#\x00:\x8f\xc2\t?\xd7oi_\x89\x8fh')

table_e = [['Да', 'Да', 'Родион К. Довадман;dovadman99@gmail.com'],
           ['Да', 'Да', 'Родион К. Довадман;dovadman99@gmail.com'],
           [None, None, None],
           ['Да', 'Да', 'Мирослав Ч. Роколли;miroslav8@rambler.ru'],
           ['Да', 'Да', 'Одиссей Ф. Гибитянц;gibitanz61@yandex.ru'],
           ['Да', 'Да', 'Родион К. Довадман;dovadman99@gmail.com']]

table_q = [['Да', 'Родион К. Довадман;dovadman99@gmail.com'],
           ['Да', 'Мирослав Ч. Роколли;miroslav8@rambler.ru'],
           ['Да', 'Одиссей Ф. Гибитянц;gibitanz61@yandex.ru']]


main_1(table_e)

print(table_e)
