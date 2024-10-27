from typing import Optional

from rich.console import Console
from rich.style import Style
import pathlib

from rich.text import Text
from rich_theme_manager import Theme, ThemeManager
from rich_theme_manager.theme import SAMPLE_TEXT, attribute_str, _bold, color_bar, list_union

from rich.table import Table
from rich.panel import Panel
from rich import box

THEMES = [
    Theme(
        name="dark",
        description="Dark mode theme",
        tags=["dark"],
        styles={
            "info": "dim cyan",
            "warning": "bold magenta",
            "danger": "bold red",
        },
    ),
    Theme(
        name="light",
        description="Light mode theme",
        styles={
            "info": Style(color="#22863a", bold=True),
            "warning": Style(color="#032f62", bold=True),
            "danger": Style(color="#b31d28", bold=True, underline=True, italic=True),
        },
    ),
    Theme(
        name="mono",
        description="Monochromatic theme",
        tags=["mono", "colorblind"],
        styles={
            "info": "italic",
            "warning": "bold",
            "danger": "reverse bold",
        },
    ),
    Theme(
        name="custom-catppuccin",
        description="Custom theme",
        styles={
            "logger.trace": Style(color="blue", dim=True, italic=True),
            "logger.info": Style(color="cyan", bold=True),
            "logger.warning": Style(color="magenta", bold=True),
            "logger.error": Style(color="red", bold=True),
        },
    )
]

# you can specify a config directory to save/load themes to/from
G_THEME_DIR = pathlib.Path("themes")
G_THEME_DIR.expanduser().mkdir(parents=True, exist_ok=True)

if not G_THEME_DIR.exists():
    G_THEME_DIR.mkdir(parents=True, exist_ok=True)

if not G_THEME_DIR.is_dir():
    raise ValueError(f"Invalid theme directory: {G_THEME_DIR}")

G_THEME_MANAGER = ThemeManager(theme_dir=G_THEME_DIR, themes=THEMES)
G_THEME_MANAGER.list_themes()

######################
# Custom Themes
G_CUSTOM_CATPUCCIN_FRAPPE = G_THEME_MANAGER.get("custom-catppuccin")

from rich.console import Console

console = Console(theme=G_CUSTOM_CATPUCCIN_FRAPPE)

def _style_name_table_col(
        table: Table,
        style_name: str,
        style: Style,
        sample_text: str) -> (
        Table):

    console.print(
        *list(
            theme._preview(
                sample_text=sample_text or SAMPLE_TEXT, show_path=show_path
            )
        )
    )

    return table


#
# def print_style(
#         style: Style, text: str = SAMPLE_TEXT) -> Panel:
#     table = Table(
#         style=style,
#         title="Style",
#         title_justify="center",
#         show_header=True,
#         show_lines=True,
#         header_style="bold",
#         box=box.SQUARE,
#     )
#
#     for column in [
#         "style",
#         "color",
#         "color",
#         "bgcolor",
#         "bgcolor",
#         "attributes",
#         "example",
#     ]:
#         table.add_column(column)
#
#     table = _style_name_table_col(table, "style", style, text)
#
#     table = table
#     return Panel(table)

