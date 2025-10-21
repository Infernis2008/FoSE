previous = int(input("введите предыдущее показание: "))
current = int(input("введите текущее показание: "))

if current >= previous:
    vol = current - previous
else:
    vol = current + 10000 - previous

if vol <= 300:
    price = 21
elif vol <= 600:
    price = 21 + (vol - 300) * 0.06
elif vol <= 800:
    price = 21 + 300 * 0.06 + (vol - 600) * 0.04
else:
    price = 21 + 300 * 0.06 + 200 * 0.04 + (vol - 800) * 0.025

avg_price = price / vol

print(f"Предыдущее: {current}")
print(f"Текущее: {previous}")
print(f"Испольщовано: {vol} m^3")
print(f"К оплате: {price:.2f}$")

print(f"Средняя цена за кубометр: {avg_price:.2f}$")
