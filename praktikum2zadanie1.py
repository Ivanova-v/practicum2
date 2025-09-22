silver_watch = 96
gold_watch = silver_watch / 16
summa = int(input())
prise_silver = 48
print(int((summa - prise_silver * silver_watch) / gold_watch))