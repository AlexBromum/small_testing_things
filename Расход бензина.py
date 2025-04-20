import tkinter as tk
from tkinter import messagebox


# Исходная функция расчёта стоимости поездки
def calculate_fuel_cost():
    try:
        # Получение данных из полей ввода
        fuel_default = int(entry_fuel_default.get())
        way = int(entry_way.get())
        fuel_price = float(entry_fuel_price.get())

        # Проверка на положительные значения
        if fuel_default <= 0:
            messagebox.showinfo(
                "Ошибка",
                "Ваша машина не может не потреблять бензина. Или вам не нужен этот расчёт.",
            )
            return
        if way <= 0:
            messagebox.showinfo(
                "Ошибка",
                "Если вы не проехали ни одного километра, то и бензина вы не потратили.",
            )
            return
        if fuel_price <= 0:
            messagebox.showinfo(
                "Ошибка",
                "Было бы замечательно, если бы бензин был бесплатный. Но он платный.",
            )
            return

        # Обработка
        fuel = (fuel_default / 100) * way
        final_price = fuel * fuel_price

        # Вывод результата в метку
        result_label.config(
            text=f"На поездку в {way} км вы израсходовали {fuel:.1f} литров бензина.\n"
            f"При цене в {fuel_price} рублей придётся заплатить: {final_price:.1f} рублей."
        )
    except ValueError:
        messagebox.showerror("Ошибка", "Введите правильные числовые значения.")


# Создание главного окна
root = tk.Tk()
root.title("Калькулятор стоимости топлива")
root.geometry("400x300")

# Метки и поля ввода
tk.Label(root, text="Сколько бензина потребляет машина за 100 км?").pack(pady=5)
entry_fuel_default = tk.Entry(root)
entry_fuel_default.pack()

tk.Label(root, text="Сколько километров вы проехали?").pack(pady=5)
entry_way = tk.Entry(root)
entry_way.pack()

tk.Label(root, text="Сколько стоит литр бензина?").pack(pady=5)
entry_fuel_price = tk.Entry(root)
entry_fuel_price.pack()

# Кнопка для запуска расчёта
calculate_button = tk.Button(root, text="Рассчитать", command=calculate_fuel_cost)
calculate_button.pack(pady=10)

# Метка для отображения результата
result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=20)

# Запуск основного цикла программы
root.mainloop()
