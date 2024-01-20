class MyClass:
    # Ініціалізація глобальної змінної
    global_var = 0

    def __init__(self, global_var):
        # Ініціалізація аргумента з тим самим іменем, що й глобальна змінна
        self.global_var = global_var
        # Інкрементування глобального аргументу
        MyClass.global_var += 1

# Створення нового об'єкта
obj1 = MyClass(10)
print(MyClass.global_var) # Вивід: 1

# Створення нового об'єкта
obj2 = MyClass(20)
print(MyClass.global_var) # Вивід: 2

obj3 = MyClass(30)
print(MyClass.global_var) # Вивід: 3