import math
import turtle

def draw_tree(branch_length, level, t):
    if level > 0:
        # Малюємо основну гілку
        t.forward(branch_length)
        # Переходимо до лівої гілки
        angle = 45  # Кут між гілками
        t.left(angle)
        draw_tree(branch_length * math.sqrt(2) / 2, level - 1, t)
        # Переходимо до правої гілки
        t.right(2 * angle)
        draw_tree(branch_length * math.sqrt(2) / 2, level - 1, t)
        # Повертаємося до початкового положення
        t.left(angle)
        t.backward(branch_length)

def main():
    # Введення рівня рекурсії з перевіркою на правильність (цикл)
    while True:
        try:
            recursion_level = int(input("Введіть рівень рекурсії (1-9): "))
            # Рівень рекурсії повинен бути більше 0 але менше 10
            if 0 < recursion_level < 10:
                break
            else:
                print("Рівень рекурсії повинен бути більше 0 але менше 10")
        except ValueError:
            print("Введіть ціле число в діапазоні від 1 до 9")

    # Ініціалізуємо черепаху
    screen = turtle.Screen()
    t = turtle.Turtle()
    # Налаштовуємо черепаху
    t.left(90)  # Повертаємо черепаху вгору
    t.speed(0)  # Максимальна швидкість малювання
    # Починаємо малювати дерево
    draw_tree(100, recursion_level, t)
    # Завершуємо
    screen.exitonclick()

if __name__ == "__main__":
    main()