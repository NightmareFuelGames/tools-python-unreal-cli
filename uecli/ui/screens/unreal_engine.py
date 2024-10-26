"""
Author: Kasper de Bruin kasperbruin8@gmail.com
Date: 2024-10-27 00:02:05
LastEditors: Kasper de Bruin kasperbruin8@gmail.com
LastEditTime: 2024-10-27 00:08:01
FilePath: uecli/ui/screens/unreal_engine.py
Description:  This is the Unreal Engine tools screen
"""

from rich.panel import Panel
from rich.text import Text

from uecli.ui.content_screen import ContentScreen

class UnrealEngineScreen(ContentScreen):
    def __init__(self):
        super().__init__()
        
    def render(self) -> Panel:
        return Panel("Unreal Engine Screen", style="red")  # Placeholder panel to prevent NotRenderableError

    def handle_key(self, event):
        print(f"Key pressed: {event.name}")
        pass