# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму 
# этих чисел S и их произведение P. Помогите Кате отгадать 
# задуманные Петей числа.
# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3

product_numbers = int(input())
sum_numbers = int(input())
res = []
for i in range(product_numbers + sum_numbers):
    if i == (product_numbers * i - sum_numbers)**0.5:
        res.append(i)
print(*res if len(res) == 2 else res + res)
