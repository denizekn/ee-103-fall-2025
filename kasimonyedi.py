def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 3, x=10, y=20)
