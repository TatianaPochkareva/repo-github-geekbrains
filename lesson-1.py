# задача №1
name = "Katya"
age = 25
city = "Tula"
print(age, city, name)

age = input("Enter age:")
name = input("enter name:")
print("Name:", name, "Age:", age)

#задача №2
sec = int(input("введите время в секундах:"))
hour = sec // 3600
min = (sec - hour * 3600) // 60
s = sec % 60
print(f"{hour:02}:{min:02}:{sec:02}")

# задача №3
n = input("введите число: ")
print(int(n) + int(n + n) + int(n + n + n))

# задача №4
num = int(input("введите число: "))
max = 0
while num > 0:
    last_dig = num % 10
    if last_dig > max:
        max = last_dig
        if max == 9:
            break
    num //= 10
print(" Самая большая цифра в числе: ", max)

# задача №5
g = int(input("введите выручку: "))
c = int(input("введите расходы: "))
p = g + c
if p > 0:
    print("вы в прибыли")
    print("рентабельность: ", p / g)
    k = int(input("количество сотрудников?: "))
    print("прибыль на одного сотрудника: ", p / k)
elif p == 0:
    print(" нулевая прибыль")
else:
    print("вы в убытке")

#задача №6
a = int(input("введите  а: "))
b = int(input("введите  b: "))
days = 1
print("результат: ")
while a < b:
    print(f"{days}- день: {round(a, 2)}")
    a = a * 1.1
    days += 1
print(f"на {days}-й день спортсмен достиг результата не менее {b} км")


