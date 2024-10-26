"""Top level module for uetools"""

__descr__ = "Unreal Engine Tools"
__version__ = "2.1.1"
__license__ = "BSD 3-Clause License"
__author__ = "Pierre Delaunay"
__author_email__ = "pierre@delaunay.io"
__copyright__ = "2023 Pierre Delaunay"
__url__ = "https://github.com/kiwi-lang/uetools"

from rich.console import Console
from rich.theme import Theme

console = Console()
console.print(f"[bold blue]URL:[/bold blue] {__url__}")
console.print(f"[bold blue]Author:[/bold blue] {__author__}")
console.print(f"[bold blue]Version:[/bold blue] {__version__}")
console.print(f"[bold blue]License:[/bold blue] {__license__}")
console.print(f"[bold blue]{__descr__}[/bold blue]")

import re

import colorama
from colorama import Fore, Style

from uetools.core.conf import load_conf, update_conf

UE_LOG_FORMAT = re.compile(
    r"^(\[(?P<datetime>.*)\]\[\s*(?P<frame>\d*)\])?(?P<category>[A-Za-z]*): ((?P<verbosity>[A-Za-z]*):)?(?P<message>.*)"
)

UE_LOG_FORMAT_UTC = re.compile(
    r"^\[(?P<datetime>\d{4}\.\d{2}\.\d{2}-\d{2}\.\d{2}\.\d{2}:\d{3})\]\[\s*(?P<frame>\d*)\](?P<category>[A-Za-z]*): ((?P<verbosity>[A-Za-z]*):)?(?P<message>.*)"
)

UE_STDOUT_FORMAT = re.compile(
    r"^(?P<category>[A-Za-z]*): ((?P<verbosity>[A-Za-z]*):)?(?P<message>.*)"
)

def extract_category(message):
    """Extract the category from the message"""
    result = UE_STDOUT_FORMAT.search(message)

    if result:
        return result.group("category")

    return "Display"

def get_style_for_category(category):
    """Get the style for the category"""
    # 'logging.keyword' = {Style}
    # 'logging.level.notset' = {Style}
    # 'logging.level.debug' = {Style}
    # 'logging.level.info' = {Style}
    # 'logging.level.warning' = {Style}
    # 'logging.level.error' = {Style}
    # 'logging.level.critical' = {Style}

    if category == "Fatal":
        return "logging.level.critical"

    if category == "Error":
        return "logging.level.error"

    if category == "Warning":
        return "logging.level.warning"

    if category == "Display":
        return "logging.level.debug"

    if category == "Log":
        return "logging.level.info"

    if category == "Verbose":
        return "logging.level.debug"

    if category == "VeryVerbose":
        return "logging.level.debug"


def print(*args, sep=' ', end='\n', file=None):
    """Prints the message to the console"""
    category = extract_category(sep.join(args))
    category = category.lower()
    style = get_style_for_category(category)
    if style == None:
        style = "logging.level.debug"
    console.print(sep.join(args), end=end, style=f"{style}")

def debug(*args, sep=' ', end='\n', file=None):
    """Prints the message to the console"""
    category = "Display"
    # console.print(sep.join(args), end=end, style=f"{category}")

#
# from rich.theme import Theme
# theme = Theme({
#     "info": "blue",
#     "warning": "yellow",
#     "error": "bold red",
#     "success": "green",
#     "fatal": "bold magenta",
#     "display": "cyan",
#     "log": "dim white",
#     "verbose": "dim green",
#     "veryverbose": "dim cyan",
# })
#
#
# from typing import Optional, Union
#
# from rich.console import Console, JustifyMethod
# from rich.highlighter import RegexHighlighter
# from rich.logging import RichHandler
# from rich.style import Style
#
# # Verbosity colors
# verbosity_styles = {
#     "Fatal": "fatal",
#     "Error": "error",
#     "Warning": "warning",
#     "Display": "display",
#     "Log": "log",
#     "Verbose": "verbose",
#     "VeryVerbose": "veryverbose",
# }
#
#
#
# console = Console(theme=theme)
#
# console.print(f"[bold blue]URL:[/bold blue] {__url__}")
# console.print(f"[bold blue]Author:[/bold blue] {__author__}")
# console.print(f"[bold blue]Version:[/bold blue] {__version__}")
# console.print(f"[bold blue]License:[/bold blue] {__license__}")
# console.print(f"[bold blue]{__descr__}[/bold blue]")
#
#
# style: Optional[Union[str, Style]] = "dim"
#
# justify: Optional[JustifyMethod] = "left"
# markup: Optional[bool] = None
# highlight: bool = True
# log_locals: bool = False
#
#
#
#
# class RequestHighlighter(RegexHighlighter):
#     base_style = "req."
#     highlights = [
#         r"^(?P<protocol>\w+) (?P<method>\w+) (?P<path>\S+) (?P<result>\w+) (?P<stats>\[.+\])$",
#         r"\/(?P<filename>\w+\..{3,4})",
#     ]
# request_highlighter = RequestHighlighter()
#
#
# def print_custom(*args, sep=' ', end='\n', file=None):
#     """Print to console"""
#
#     """Custom print using rich console with log settings."""
#     console.log(*args, sep=sep, end=end, style=style, justify=justify, markup=markup, highlight=highlight)
#
#     if file is not None:
#         console.print("[bold red]Warning:[/bold red] The `file` parameter is not supported yet.")
#
# # result = self.regex.search(line)
# #
# # if result:
# #     data = result.groupdict()
# #
# #     if data["verbosity"] is None:
# #         data["verbosity"] = "Log"
# #
# #     if data["verbosity"] not in log_verbosity:
# #         msg = data["verbosity"]
# #         data["verbosity"] = "Log"
# #         data["message"] = f"{msg}: " + data["message"]
# #
# #     # Kepp track of bad logs and show a summary at the end
# #     if data["verbosity"] in bad_logs:
# #         self.bad_logs.append(LogLine(**data))
# #
# #     if self.suppress_duplicate_lines:
# #         h = hash(LogLine(**data))
# #
# #         # Line is not duplicate
# #         if h not in self.line_hash:
# #             self.format(**data)
# #             self.line_hash.add(h)
# #             self.prev_hash = h
# #     else:
# #         self.format(**data)
# # else:
# #     if self.print_non_matching:
# #         self.print(line, end="")
# #     else:
# #         log.debug("    Line did not match anything")
# #         log.debug("        - `%s`", line)
# #
# # # Error detection
# # for error_pat in ERROR_PATERNS:
# #     result = error_pat.search(line)
# #
# #     if result:
# #         data = result.groupdict()
# #
# #         rc = data.get("returncode", 0)
# #         if rc != 0:
# #             self.return_codes.append(int(rc))
# # Override the print function with the custom one
# print = print_custom