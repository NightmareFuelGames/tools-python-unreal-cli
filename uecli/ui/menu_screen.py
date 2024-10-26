"""
Author: Kasper de Bruin kasperbruin8@gmail.com
Date: 2024-10-26 14:49:45
LastEditors: Kasper de Bruin kasperbruin8@gmail.com
LastEditTime: 2024-10-27 00:18:06
FilePath: uecli/ui/menu_screen.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
from typing import List, Dict, Union

from rich.panel import Panel
from rich.text import Text

from uecli.ui.screen import Screen


class MenuScreen(Screen):
        
        
    def __init__(self, menu_options: Dict[str, Screen], selected_index: int = 0):
        super().__init__()
        self.menu_options: Dict[str, Screen] = menu_options
        self.selected_index: int = selected_index

    def get_panel(self) -> Panel:
        return Panel(self.render_menu(), style="blue")

    def render_menu(self) -> Text:
        menu_text = Text()
        index = 0
        for option, screen in self.menu_options.items():
            if index == self.selected_index:
                menu_text.append(f"> {option}\n", style="bold red")
            else:
                menu_text.append(f"  {option}\n")
                
            index += 1
        return menu_text
    
    def get_selected_screen(self) -> Screen:
        return list(
            self.menu_options.values()
        )[self.selected_index]#todo change this to return just an var
    
    def render(self) -> Panel:
        return self.get_panel()  # Ensure render returns a Panel

    def handle_key(self, event):
        if event.name == "up":  # Move up
            self.selected_index = (self.selected_index - 1) % len(self.menu_options)
        elif event.name == "down":  # Move down
            self.selected_index = (self.selected_index + 1) % len(self.menu_options)
        elif event.name == "enter":
            print(f"Selected {self.menu_options[self.selected_index]}")
            