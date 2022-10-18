print("sup buddy!")

# control structures


# if elif

x = int(input("please enter an integer: "))

if x < 0:
    x = 0
    print('negative changed to zero')
elif x == 0:
    print('zero')
elif x == 1:
    print('single')
else:
    print('more')

# for

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for i in range(5):
    print(i)

# definir funciones


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()


fib(3)
