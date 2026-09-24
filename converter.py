"""Простой конвертер величин."""

def main():
    print("Конвертер величин")
    print("1 - Длина (m, km, cm)")
    print("2 - Масса (kg, g, t)")
    print("3 - Температура (C, F)")

    choice = input("Что конвертируем? (1/2/3): ").strip()
    value = float(input("Введите число: ").replace(",", "."))
    src = input("Из какой единицы: ").strip()
    dst = input("В какую единицу: ").strip()

    if choice == "1":
        table = {"m": 1, "km": 1000, "cm": 0.01}
        result = value * table[src] / table[dst]
    elif choice == "2":
        table = {"kg": 1, "g": 0.001, "t": 1000}
        result = value * table[src] / table[dst]
    elif choice == "3":
        if src == "C" and dst == "F":
            result = value * 9 / 5 + 32
        elif src == "F" and dst == "C":
            result = (value - 32) * 5 / 9
        else:
            result = value
    else:
        print("Неверный выбор")
        return

    print(f"\n{value} {src} = {round(result, 2)} {dst}")


if __name__ == "__main__":
    main()