"""
Author: Kasper de Bruin kasperbruin8@gmail.com
Date: 2024-10-27 00:10:20
LastEditors: Kasper de Bruin kasperbruin8@gmail.com
LastEditTime: 2024-10-27 00:27:13
FilePath: uecli/ui/screens/placeholder_screen.py
Description: This is a placeholder screen
"""
from typing import List

from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich.progress import track
from rich.table import Table
from rich.columns import Columns

import uecli
from uecli.ui import SplitItemOptions, SplitDirection
from uecli.ui.content_screen import ContentScreen
from uecli.logger import LogMessage, g_info, print, G_LOGGER

class Placeholder(ContentScreen):
    def __init__(self):
        super().__init__()

    def example_log(self) -> Text:
        """
        Example of a log, display the test_data
        """
        g_info("test")

        log: Text = Text()


        info_log_messages: List[LogMessage] = G_LOGGER.all_messages
        for log_message in info_log_messages:
            log.append(log_message.formatted_msg)



        return log

    def example_panel(self) -> Table:
        # split in half
        table = Table(title="JSON-RPC Examples")
        table.add_column("logger")
        table.add_column("severity")
        table.add_column("time")
        table.add_column("log")

        info_log_messages: List[LogMessage] = G_LOGGER.all_messages
        for log_message in info_log_messages:
            datetime_formatted: str  = log_message.time.strftime("%Y-%m-%d %H:%M:%S")
            table.add_row(
                G_LOGGER.name,
                log_message.log_severity.name,
                datetime_formatted,
                log_message.formatted_msg)


        return table

    def create_layout(self) -> Layout:
        layout: Layout = Layout(name="placeholder")
        split_options: List[SplitItemOptions] = [
            SplitItemOptions(name="log", ratio=1),
            SplitItemOptions(name="table", ratio=1)
        ]
        
        uecli.ui.split_layout(layout,
                              split_options,
                              SplitDirection.ROW)

        layout["log"].update(self.example_log())
        layout["table"].update(self.example_panel())

        return layout
    
    def render(self) -> Panel:
        return Panel(self.create_layout(), title="Placeholder Screen")

    def handle_key(self, event):
        print(f"Key pressed: {event.name}")
        pass
