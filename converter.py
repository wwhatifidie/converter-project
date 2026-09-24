
import sys


def parse_line(line):
    """'5 km -> m' → (5.0, 'km', 'm')."""
    left, right = line.split("->")
    value_str, src = left.split()
    return float(value_str), src, right.strip()


def convert(value, src, dst):
    """Универсальный конвертер."""
    if src in ("m", "km", "cm") and dst in ("m", "km", "cm"):
        table = {"m": 1, "km": 1000, "cm": 0.01}
        return value * table[src] / table[dst]

    if src in ("kg", "g", "t") and dst in ("kg", "g", "t"):
        table = {"kg": 1, "g": 0.001, "t": 1000}
        return value * table[src] / table[dst]

    if src == "C" and dst == "F":
        return value * 9 / 5 + 32
    if src == "F" and dst == "C":
        return (value - 32) * 5 / 9
    if src == dst:
        return value

    raise ValueError(f"Не знаю: {src} -> {dst}")


def interactive():
    """Интерактивный режим."""
    print("Конвертер величин")
    print("1 - Длина (m, km, cm)")
    print("2 - Масса (kg, g, t)")
    print("3 - Температура (C, F)")

    choice = input("Что конвертируем? (1/2/3): ").strip()
    value = float(input("Введите число: ").replace(",", "."))
    src = input("Из какой единицы: ").strip()
    dst = input("В какую единицу: ").strip()

    result = convert(value, src, dst)
    print(f"\n{value} {src} = {round(result, 2)} {dst}")


def batch(path):
    """Пакетный режим: читает файл построчно."""
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            value, src, dst = parse_line(line)
            result = convert(value, src, dst)
            print(f"{value} {src} = {round(result, 2)} {dst}")


def main():
    if len(sys.argv) > 1:
        batch(sys.argv[1])
    else:
        interactive()


if __name__ == "__main__":
    main()