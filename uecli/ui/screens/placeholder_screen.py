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


class Placeholder(ContentScreen):
    test_data = [
        {
            "jsonrpc": "2.0",
            "method": "sum",
            "params": [None, 1, 2, 4, False, True],
            "id": "1",
        },
        {
            "jsonrpc": "2.0",
            "method": "notify_hello",
            "params": [7],
            "id": "2",
        },
        {
            "jsonrpc": "2.0",
            "method": "subtract",
            "params": [42, 23],
            "id": "3"
        },
    ]

    def __init__(self):
        super().__init__()

    def example_log(self) -> Text:
        """
        Example of a log, display the test_data
        """
        log = Text()
        for data in self.test_data:
            log.append(f"[bold]{data['jsonrpc']}[/bold] {
            data['method']} {data['params']} {data['id']}")
        return log

    def example_panel(self) -> Table:
        # split in half
        table = Table(title="JSON-RPC Examples")
        table.add_column("jsonrpc")
        table.add_column("method")
        table.add_column("params")
        table.add_column("id")

        for data in self.test_data:
            table.add_row(data["jsonrpc"], data["method"], data["id"])

        return table

    def create_layout(self) -> Layout:
        layout: Layout = Layout(name="placeholder")
        split_options: List[SplitItemOptions] = [
            SplitItemOptions(name="log", ratio=1),
            SplitItemOptions(name="table", ratio=1)
        ]
        
        uecli.ui.split_layout(layout, split_options, SplitDirection.ROW)
        
        return layout
    
    def render(self) -> Panel:
        return Panel(self.create_layout(), style="red")

    def handle_key(self, event):
        print(f"Key pressed: {event.name}")
        pass
