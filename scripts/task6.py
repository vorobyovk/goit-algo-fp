def greedy_algorithm(items, budget):
    # Обчислюємо співвідношення калорій до вартості для кожної страви
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    total_calories = 0
    chosen_items = []
    for item, info in sorted_items:
        if budget >= info["cost"]:
            chosen_items.append(item)
            total_calories += info["calories"]
            budget -= info["cost"]
    return chosen_items, total_calories

# Тестування
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}
budget = 100
chosen_items, total_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Обрані страви:", chosen_items)
print("Загальна калорійність:", total_calories)

def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    # Створюємо таблицю для зберігання максимальних калорій для кожного можливого бюджету
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        item_name = item_names[i - 1]
        cost = items[item_name]["cost"]
        calories = items[item_name]["calories"]
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]
    # Визначаємо обрані страви
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name = item_names[i - 1]
            chosen_items.append(item_name)
            w -= items[item_name]["cost"]
    return chosen_items, dp[n][budget]

# Приклад використання
chosen_items, total_calories = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Обрані страви:", chosen_items)
print("Загальна калорійність:", total_calories)