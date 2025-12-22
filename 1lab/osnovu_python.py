# -----------------------------------------------------------
#   Мій файл для ознайомлення з основами Python
#   Виконую завдання: змінні, типи даних, цикли, розгалуження,
#   try/except, контекст-менеджери, lambda, базові функції.
#   Пишу від першої особи.
# -----------------------------------------------------------

print("\n=== ЗМІННІ ТА ТИПИ ДАНИХ ===")

# Я знайомлюсь з основними типами Python
a = "змінна з текстом"
b = 1           # числова змінна int
b1 = 1.1        # числова змінна float
c = ["a", 1, 1.25, "Слово", a]   # список list
d = {"a": "Слово", "b": 1, a: b} # словник dict
e = ("a", a)    # кортеж tuple

# У set я спеціально пишу неправильний приклад,
# щоб побачити поведінку при додаванні несумісних типів
# (рядок + число викличе помилку, тому я це закоментовую)
# f = {"ss", a + b}
f = {"ss", a}   # правильний варіант

print("a:", a)
print("b:", b)
print("b1:", b1)
print("c:", c)
print("d:", d)
print("e:", e)
print("f:", f)


print("\n=== ВБУДОВАНІ КОНСТАНТИ ТА КЛЮЧОВІ СЛОВА ===")

print("Перша константа:", True)
print(f"Друга константа через f-string: {None}")

import sys
print("\nКлючові слова Python:")
help("keywords")


print("\n=== ВБУДОВАНІ ФУНКЦІЇ ===")
print("abs(-12.5) =", abs(-12.5))
print(f"abs(10) -> {abs(10)}")
print("round(3.14159, 2) =", round(3.14159, 2))


print("\n=== ЦИКЛИ ===")

# 1. Простий for
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")
else:
    print("Цикл успішно завершився (else).")

# 2. while
i = 0
while i < 3:
    print("Це while, i =", i)
    i += 1


print("\n=== РОЗГАЛУЖЕННЯ ===")

from random import randint

A = randint(0, 1)
if A == 1:
    print("A дорівнює 1")
else:
    print("A дорівнює 0")

# Тернарний оператор
print(f"Тернарний варіант: A={A}" if A else f"Тернарний варіант: A={A} але це 0")


print("\n=== TRY / EXCEPT / FINALLY ===")

A = 0
try:
    print("Спробую поділити 10 на A:", 10 / A)
except Exception as e:
    print("Сталася помилка ->", e)
finally:
    print("Finally виконується завжди.")


print("\n=== КОНТЕКСТ-МЕНЕДЖЕР ===")

# Я використовую контекст-менеджер для читання файлу
# (файл README.md має існувати, інакше буде помилка)
try:
    with open("README.md", "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            print(f"{idx})> {line.strip()}")
except FileNotFoundError:
    print("Файлу README.md не існує — але саме так працює with :)")


print("\n=== LAMBDA ===")

# Я визначаю звичайну функцію
def a_b_func(a, b):
    return a, b

# І лямбда-функцію
this_is_lambda = lambda first, age: f"Цей код написав: {first}, мені {age} років"

print("Звичайна функція:", a_b_func)
print("Лямбда-функція:", this_is_lambda)

print("Виклик лямбди:", this_is_lambda("Богдан", 100_000))
print("Виклик лямбди з розпакуванням:", this_is_lambda(*a_b_func("a", 1)))

print("\n=== ВСЕ ВИКОНАНО УСПІШНО ===")
