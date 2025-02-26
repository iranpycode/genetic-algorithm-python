import random

# تابع هدف (Fitness Function)
def fitness(x):
    return x**2

# ایجاد جمعیت اولیه شامل 10 فرد تصادفی
population = [random.uniform(-10, 10) for _ in range(10)]

# اجرای الگوریتم برای 10 نسل
for generation in range(10):
    # مرتب‌سازی جمعیت بر اساس مقدار تابع هدف
    population.sort(key=fitness, reverse=True)
    
    # انتخاب بهترین ۵ فرد و جایگزینی ۵ فرد دیگر با نمونه‌های تصادفی
    new_population = population[:5] + [random.uniform(-10, 10) for _ in range(5)]
    population = new_population

# نمایش بهترین راه‌حل به‌دست‌آمده
print("Best solution:", population[0])
