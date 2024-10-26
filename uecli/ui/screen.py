"""
Author: Kasper de Bruin kasperbruin8@gmail.com
Date: 2024-10-26 22:38:14
LastEditors: Kasper de Bruin kasperbruin8@gmail.com
LastEditTime: 2024-10-26 23:13:55
FilePath: uecli/ui/screen.py
Description: The abstract class for all screens
"""

from abc import ABC, abstractmethod
from rich.panel import Panel
from rich.text import Text
import keyboard

class Screen(ABC):
    def __init__(self):
        #keyboard.on_press(callback=self.handle_key, suppress=True)

        # Set up key events only for left_screen
        keyboard.on_press(self.handle_key)
        
        
    def handle_key(self, event):
        print(f"Key pressed: {event.name}")
        pass
    
    @abstractmethod
    def render(self) -> Panel:
        return Panel("Abstract Screen", style="red")  # Placeholder panel to prevent NotRenderableError

    def __rich__(self) -> Panel:
        return self.render()
