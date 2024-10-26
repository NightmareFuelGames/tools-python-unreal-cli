"""
Author: Kasper de Bruin kasperbruin8@gmail.com
Date: 2024-10-26 14:50:18
LastEditors: Kasper de Bruin kasperbruin8@gmail.com
LastEditTime: 2024-10-26 23:59:35
FilePath: uecli/ui/content_screen.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
from rich.panel import Panel
from uecli.ui.screen import Screen


class ContentScreen(Screen):
    def render(self) -> Panel:
        return Panel("Right Screen", style="Blue")

    def handle_key(self, key: str):
        pass
