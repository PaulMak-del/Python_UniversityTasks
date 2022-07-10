'''
Формальная верификация головоломок из компьютерных игр

Одной из важных проблем, стоящих перед разработчиком компьютерных игр, является создание интересных головоломок, в которых отсутствуют тупиковые состояния (состояния, из которых нельзя достичь цели).

Формальную верификацию проведем следующим образом:

Реализовать игровую ситуацию в виде некоторого количества локаций с указанием перечня возможных действий в каждой из них.
Сгенерировать по реализованной игровой ситуации граф всех возможных игровых состояний, в котором ребра задают переходы из состояние в состояние.
Проанализировать граф состояний на предмет проверяемого игрового свойства.
'''

def go(room):
    def func(state):
        return dict(state, room=room)
    return func


def go_conditional(room, conditional):
    def func(state):
        if conditional(state):
            return dict(state, room=room)
        return state
    return func


def toggle_lever(lever):
    def func(state):
        new_state = dict(state)
        new_state[lever] = not new_state[lever]
        return new_state
    return func


game = {
    'room0': dict(
        left=go('room1'),
        up=go('room2'),
        right=go('room3')
    ),
    'room1': dict(
        up=go('room2'),
        right=go('room0')
    ),
    'room2': dict(
    ),
    'room3': dict(
        up=go('room4'),
        right=go('room5'),
        left=go_conditional('room0', lambda x: x['l1'] and x['l2'] and not x['l3'])
    ),
    'room4': dict(
        down=go('room3'),
        right=go('room5'),
        push_l1=toggle_lever('l1'),
        push_l2=toggle_lever('l2'),
        push_l3=toggle_lever('l3')
    ),
    'room5': dict(
        up=go('room4'),
        left=go('room3')
    )
}

START_STATE = dict(room='room0', l1=False, l2=False, l3=False)


def is_goal_state(s):
    """
    Проверить, является ли состояние целевым.
    На входе ожидается множество пар ключ-значение.
    """
    return ('room', 'room2') in s


def get_current_room(state):
    """
    Выдать комнату, в которой находится игрок.
    """
    return state['room']


def print_dot(graph, start_key):
    dead_ends = find_dead_ends(graph)
    print('digraph {')
    graph_keys = list(graph.keys())
    for x in graph:
        n = graph_keys.index(x)
        if dict(x) == start_key:
            print(f'n{n} [style="filled",fillcolor="dodgerblue",shape="circle"]')
        elif is_goal_state(x):
            print(f'n{n} [style="filled",fillcolor="green",shape="circle"]')
        elif x in dead_ends:
            print(f'n{n} [style="filled",fillcolor="red",shape="circle"]')
        else:
            print(f'n{n} [shape="circle"]')
    for x in graph:
        n1 = graph_keys.index(x)
        for y in graph[x]:
            n2 = graph_keys.index(y)
            print(f'n{n1} -> n{n2}')
    print('}')


def d2t(d):
    return tuple(d.items())


def make_model(game, start_state):
    graph = dict()
    to_visit = [start_state]
    visited = list()
    while to_visit:
        current_state = to_visit.pop()
        visited.append(current_state)
        # graph[d2t(current_state)] = list()
        graph.setdefault(d2t(current_state), list())
        for name, action in game[current_state['room']].items():
            new_state = action(current_state)
            if new_state not in visited and new_state not in to_visit:
                to_visit.append(new_state)
            graph[d2t(current_state)].append(d2t(new_state))
    return graph


def find_dead_ends(graph):
    result = list()
    for state in graph:
        is_dead = True
        to_visit = [state]
        visited = list()
        while to_visit:
            current_state = to_visit.pop()
            visited.append(current_state)
            for new_state in graph[current_state]:
                if new_state not in visited and new_state not in to_visit:
                    to_visit.append(new_state)
                if is_goal_state(new_state):
                    is_dead = False
                    break
        if is_dead:
            result.append(state)
    return result


graph = make_model(game, START_STATE)
print_dot(graph, START_STATE)
