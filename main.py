#Первый файл тестового проекта по созданию приложения на андроиде. 20-03-2025

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text=f"Привет, это мое первое тестове приложение (пока без кнопочек)!\nР.С. 25.03.2025")

if __name__ == "__main__":
    MyApp().run()