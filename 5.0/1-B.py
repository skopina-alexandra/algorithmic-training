game1 = list(map(int,input().split(':')))
game2 = list(map(int,input().split(':')))
where = int(input())

sum1 = game1[0] + game2[0]
sum2 = game1[1] + game2[1]

if sum1 > sum2: # Уже выигрываем
    print(0)
else:
    sum1_guest = game2[0] if where == 1 else game1[0]
    sum2_guest = game1[1] if where == 1 else game2[1]

    if sum1 == sum2: # Общая суммая равна
        if sum1_guest > sum2_guest: # Но у нас больше гостевых => уже выиграли
            print (0)
        else: # Общая сумма равна, но у нас меньше либо равно гостевых => увеличиваем общую сумму на 1
            print(1) 
    else: # Общая сумма меньше
        goals_to_even = sum2 - sum1
        if where == 1: # Cейчас играем в гостях
            if sum1_guest >= sum2_guest:
                print(goals_to_even)      
            else:
                print(goals_to_even if goals_to_even + sum1_guest > sum2_guest else goals_to_even + 1)      
        else: # Сейчас играем дома
            if sum1_guest > sum2_guest:
                print(goals_to_even)
            else:
                print(goals_to_even + 1)