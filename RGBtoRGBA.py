from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


Config.set("graphics", "width", "700")
Config.set("graphics", "height", "700")
Config.set("graphics", "resizable", "1")
Config.set("graphics", "show_cursor", "1")


class FirstApp(App):
    def build(self):
        # Создаём контейнер с вертикальной ориентацией
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.label_r = Label(
            text="Введите R",
            font_size=30,
            size_hint=(1, 0.1),
            color=(1, 1, 1, 1),
        )

        self.r_input = TextInput(
            font_size=20,
            size_hint=(1, 0.1),  # Задаём размер, ширина 100%, высота 20% от экрана
            height=30,
            multiline=False,  # Текст будет вводиться в одну строку
            background_color=(0.8, 0.8, 0.8, 1),
        )

        self.label_g = Label(
            text="Введите G",
            font_size=30,
            size_hint=(1, 0.1),
            color=(1, 1, 1, 1),
        )

        self.g_input = TextInput(
            font_size=20,
            size_hint=(1, 0.1),  # Задаём размер, ширина 100%, высота 20% от экрана
            height=30,
            multiline=False,  # Текст будет вводиться в одну строку
            background_color=(0.8, 0.8, 0.8, 1),
        )

        self.label_b = Label(
            text="Введите B",
            font_size=30,
            size_hint=(1, 0.1),
            color=(1, 1, 1, 1),
        )

        self.b_input = TextInput(
            font_size=20,
            size_hint=(1, 0.1),  # Задаём размер, ширина 100%, высота 10% от экрана
            height=30,
            multiline=False,  # Текст будет вводиться в одну строку
            background_color=(0.8, 0.8, 0.8, 1),
        )

        button = Button(
            text="Перевести",
            bold=True,
            font_size=40,
            background_color=[0.9, 0.6, 0, 1],
            background_normal="",
            size_hint=(1, 0.2),
        )

        button.bind(on_press=self.update_TextInput)
        self.result_input = TextInput(
            text="Здесь будет результат",
            multiline=False,
            cursor_blink=False,
            readonly=True,
            font_size=50,
            size_hint=(1, 0.5),
            halign="center",
            padding_y=[50, 50],
            background_color=(0.8, 0.8, 0.8, 1),
        )

        # Добавляем виджеты в layout
        layout.add_widget(self.label_r)
        layout.add_widget(self.r_input)
        layout.add_widget(self.label_g)
        layout.add_widget(self.g_input)
        layout.add_widget(self.label_b)
        layout.add_widget(self.b_input)
        layout.add_widget(self.result_input)
        layout.add_widget(button)

        return layout

    def update_TextInput(self, instance):

        r_digit = self.r_input.text
        g_digit = self.g_input.text
        b_digit = self.b_input.text

        r_digit = float(r_digit)
        g_digit = float(g_digit)
        b_digit = float(b_digit)

        r = r_digit / 255
        g = g_digit / 255
        b = b_digit / 255
        a = 1

        self.result_input.text = (
            f"{r:.2f}, {g:.2f}, {b:.2f}, {a}"  # Изменяем текст в TextInput
        )
        self.result_input.background_color = (r, g, b, a)  # Изменяем цвет в TextInput


if __name__ == "__main__":
    FirstApp().run()
