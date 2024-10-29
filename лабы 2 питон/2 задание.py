salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = spend - salary
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(months - 1):
    spend *= increase + 1
    money_capital += spend - salary
if int(money_capital) - money_capital != 0:
    money_capital = int(money_capital + 1)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
