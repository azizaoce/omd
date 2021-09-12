def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def step2_umbrella():
    print('Зонт забрала подруга, а утка не знает об этом. Вернись и скажи "нет". Утке хотят сделать сюрприз, пусть так и будет.')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def step2_no_umbrella():
    print('Умница! Скоро утке подарят много новых зонтиков.')



if __name__ == '__main__':
    step1()
