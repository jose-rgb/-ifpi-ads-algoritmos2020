def do_twice(func, arg):
    func(arg)
    func(arg)



def print_twice(arg):
    print(arg)
    print(arg)


def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)

do_twice(print, 'spam')

do_four(print, 'spam')     




    