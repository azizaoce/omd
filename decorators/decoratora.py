import sys
import datetime

#1
original_write = sys.stdout.write

def my_write(string_text):
    if string_text == '\n':
        return original_write('\n')
    original_write('[{}]: '.format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")) + string_text)
    return
    

sys.stdout.write = my_write
print('1, 2, 3')
sys.stdout.write = original_write
print('1, 2, 3')

#2
def timed_output(func):
    def wrapper(*args, **kwargs):
        original_write = sys.stdout.write
        def my_write_(string_text):
            if string_text == '\n':
                return original_write('\n')
            original_write('[{}]: '.format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")) + string_text)
            return
        sys.stdout.write = my_write
        result = func(*args, **kwargs)
        sys.stdout.write = original_write
        return 
    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')
print_greeting("Koshka")
