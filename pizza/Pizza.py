import click
from random import randint


class Pizza:
    def __init__(self, name, recipe, size):
        self.name = name
        self.recipe = recipe
        if size not in ['L', 'XL']:
            raise ValueError('Pizza size can be L and XL')
        self.size = size

    def __eq__(self, other):
        return self.recipe == other.recipe and self.size == other.size

    def dict(self):
        return {f'Ingredients of {self.name}': f'{", ".join([ingredient for ingredient in self.recipe])}',
                'size': self.size}


class Margherita(Pizza):
    def __init__(self, size: str = 'L'):
        super().__init__(name='Margherita 🧀', size=size, recipe=['tomato sauce', 'mozzarella', 'tomatoes'])


class Pepperoni(Pizza):
    def __init__(self, size: str = 'L'):
        super().__init__(name='Pepperoni 🍕', size=size, recipe=['tomato sauce', 'mozzarella', 'pepperoni'])


class Hawaiian(Pizza):
    def __init__(self, size: str = 'L'):
        super().__init__(name='Hawaiian 🍍', size=size, recipe=['tomato sauce', 'mozzarella', 'chicken', 'pineapples'])


def log(text: str):
    def decorator(function: callable):
        def wrapper(pizza):
            print(text.format(str(function(pizza))))
        return wrapper
    return decorator


@log('👨‍🍳 Приготовили за {}с!')
def bake(pizza):
    """готовит пиццу"""
    return randint(20, 100)


@log('🛵  Доставили за {}с!')
def deliver(pizza):
    """доставляет пиццу"""
    return randint(1, 15)


@log('🏠 Забрали за {}с!')
def pickup(pizza):
    """самовывоз"""
    return randint(1, 15)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', default='L')
def order(pizza: str, size: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    if pizza == 'margherita':
        order_pizza = Margherita(size)
    elif pizza == 'pepperoni':
        order_pizza = Pepperoni(size)
    elif pizza == 'hawaiian':
        order_pizza = Hawaiian(size)
    else:
        print('Available menu: margherita, pepperoni, hawaiian')
        return

    bake(order_pizza)

    if delivery:
        deliver(order_pizza)
    else:
        pickup(order_pizza)


@cli.command()
def menu():
    """выводит меню"""
    available = [Margherita, Pepperoni, Hawaiian]
    print('Our menu today:')
    for pizza in available:
        print(f'{pizza.__name__}', end=': ')
        print(*pizza().dict().values(), sep=' ❤ where size is ')


if __name__ == '__main__':
    cli()
