import numpy as np
number=np.random.randint(1,100)
count=0
while True:
    count+=1
    predict_num=int(input('введи число '))

    if predict_num > number:
        print('уменьши число ')
    if predict_num < number:
        print('увеличь число ')
    else:
        print('верно')
        break
print("Конец")


