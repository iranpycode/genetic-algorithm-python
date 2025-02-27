import random

# تابع هدف (Fitness Function)
def fitness(x):
    return -1 * (x**2 - 4*x + 6)  # تابعی که می‌خواهیم بیشینه مقدار آن را پیدا کنیم

# ایجاد جمعیت اولیه شامل 10 فرد تصادفی
population = [random.uniform(-10, 10) for _ in range(10)]

# اجرای الگوریتم برای 10 نسل
for generation in range(10):
    # مرتب‌سازی جمعیت بر اساس مقدار تابع هدف
    population.sort(key=fitness, reverse=True)

    # انتخاب بهترین ۵ فرد
    best_individuals = population[:5]

    # ایجاد ۵ فرد جدید از طریق ترکیب و جهش
    new_individuals = []
    for _ in range(5):
        parent1, parent2 = random.sample(best_individuals, 2)  # انتخاب دو والد تصادفی از بین برترین‌ها
        child = (parent1 + parent2) / 2  # ترکیب دو والد برای تولید فرزند
        if random.random() < 0.3:  # 30% احتمال جهش
            child += random.uniform(-0.5, 0.5)  # جهش کوچک
        new_individuals.append(child)

    # ترکیب والدین برتر و افراد جدید برای تشکیل نسل بعدی
    population = best_individuals + new_individuals

# نمایش بهترین راه‌حل به‌دست‌آمده
print("Best solution:", population[0], "Fitness:", fitness(population[0]))
