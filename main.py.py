import os
import sqlite3
import random
from datetime import datetime

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

# Настройка размера для теста на ПК (эмуляция телефона)
Window.size = (360, 640)

KV = '''
ScreenManager:
    AuthScreen:
    VaultScreen:

<AuthScreen>:
    name: 'auth'
    MDBoxLayout:
        orientation: 'vertical'
        padding: "20dp"
        spacing: "20dp"
        md_bg_color: 0, 0, 0, 1

        MDLabel:
            text: "PrivDate"
            halign: "center"
            font_style: "H3"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            bold: True

        MDTextField:
            id: pass_input
            hint_text: "Введите пароль"
            password: True
            mode: "fill"
            fill_color_normal: 0.1, 0.1, 0.1, 1
            theme_text_color: "Custom"
            text_color_normal: 1, 1, 1, 1

        MDRaisedButton:
            text: "ВОЙТИ"
            pos_hint: {"center_x": .5}
            size_hint_x: 0.8
            md_bg_color: 1, 1, 1, 1
            text_color: 0, 0, 0, 1
            on_release: root.check_password()

<VaultScreen>:
    name: 'vault'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0, 0, 0, 1

        MDTopAppBar:
            title: "PrivDate Vault"
            anchor_title: "left"
            right_action_items: [["plus", lambda x: root.add_item()], ["cog", lambda x: None]]
            md_bg_color: 0, 0, 0, 1
            specific_text_color: 1, 1, 1, 1

        MDTabs:
            id: tabs
            background_color: 0, 0, 0, 1
            indicator_color: 1, 1, 1, 1
            
            Tab:
                title: "ФОТО"
                MDScrollView:
                    MDGridLayout:
                        id: photo_grid
                        cols: 3
                        row_default_height: '110dp'
                        row_force_default: True
                        adaptive_height: True
                        padding: "10dp"
                        spacing: "10dp"

            Tab:
                title: "ЗАМЕТКИ"
                MDScrollView:
                    MDList:
                        id: notes_list

<Tab@MDFloatLayout+MDTabsBase>:
'''

class AuthScreen(Screen):
    def check_password(self):
        # Упрощенная логика для примера (в реальности сверяем с БД)
        pwd = self.ids.pass_input.text
        if len(pwd) >= 4:
            self.manager.current = 'vault'
        else:
            self.ids.pass_input.error = True

class VaultScreen(Screen):
    def on_enter(self):
        self.load_content()

    def load_content(self):
        # Здесь будет логика загрузки из SQLite
        pass

    def add_item(self):
        # Здесь вызов галереи через plyer
        pass

class PrivDateApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_string(KV)

if __name__ == '__main__':
    PrivDateApp().run()