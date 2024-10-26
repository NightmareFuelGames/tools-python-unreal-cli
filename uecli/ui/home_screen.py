"""
Author: Kasper de Bruin kasperbruin8@gmail.com
Date: 2024-10-26 14:43:08
LastEditors: Kasper de Bruin kasperbruin8@gmail.com
LastEditTime: 2024-10-27 00:28:10
FilePath: uecli/ui/home_screen.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
from dataclasses import dataclass
from enum import Enum
from struct import Struct
from tkinter import Place
from typing import List, Dict, Callable

from rich.text import Text

from uecli.ui.screen import Screen
from uecli.ui.screens.placeholder_screen import Placeholder
from uecli.ui.screens.unreal_engine import UnrealEngineScreen

"""
Demonstrates a Rich "application" using the Layout and Live classes.

"""
from uecli.ui.menu_screen import MenuScreen
from uecli.ui.content_screen import ContentScreen

from rich.layout import Layout
from rich.panel import Panel

import keyboard
from time import sleep
from rich.live import Live

from uecli.ui import SplitItemOptions, SplitDirection, split_layout
from uecli.ui.screen import Screen


class Header:
    def __init__(self, title: str):
        self.title = title

    def __rich__(self):
        return Panel(Text(self.title, justify="center"), style="green")


class Footer:
    def __init__(self, title: str):
        self.title = title

    def __rich__(self):
        return Panel(Text(self.title, justify="center"), style="blue")


class Middle:
    def __init__(self, title: str):
        self.title = title

    def __rich__(self):
        return Panel(Text(self.title, justify="center"), style="yellow")


class Left:
    def __init__(self, title: str):
        self.title = title

    def __rich__(self):
        return Panel(Text(self.title, justify="center"), style="red")


class Right:
    def __init__(self, title: str):
        self.title = title

    def __rich__(self):
        return Panel(Text(self.title, justify="center"), style="blue")


class HomeScreen(Screen):

    def __init__(self):
        super().__init__()  # Corrected this line

        self.layout = Layout(name="root")
        layout = Layout()

        main_items = [SplitItemOptions("top", 1),
                      SplitItemOptions("middle", 6),
                      SplitItemOptions("bottom", 1)]

        layout = split_layout(
            layout, main_items, SplitDirection.COLUMN)

        layout["top"].update(Header("Header"))
        layout["bottom"].update(Footer("Footer"))

        body_items = [SplitItemOptions("left", 1),
                      SplitItemOptions("right", 10)]

        body_layout: Layout = layout["middle"]
        body_layout = split_layout(body_layout, body_items, SplitDirection.ROW)

        menu_left: MenuScreen = MenuScreen(
            {"UI Examples": Placeholder(), "Unreal Engine": UnrealEngineScreen()}
        )

        body_layout["left"].update(menu_left)
        body_layout["right"].update(menu_left.get_selected_screen())

        self.layout = layout
        self.running = True

    def render(self) -> Panel:
        pass

    def handle_key(self, event):
        if event.name == "q":
            self.running = False

    def run(self):

        with Live(self.layout, refresh_per_second=4, transient=True, screen=True):
            try:
                while self.running:
                    self.render()
                    sleep(0.1)
            except KeyboardInterrupt:
                pass
