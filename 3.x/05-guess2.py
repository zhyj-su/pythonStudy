import random

num=random.randint(1,100)
print(num)

guess = int(input('请输入要猜的数:'))

while guess!=num:
    
    if guess>num:
        guess=int(input('猜大了,请重新猜'))

    else:
        guess=int(input('猜小了,请重新猜'))

    if guess ==  num:
        print('猜中了')

print('游戏结束!')