from time import sleep

import uecli
# from uecli.commands.build_cook_run import CookGameWrapper
# from uecli import CACHED_ENVIRONMENT_MODEL
# from uecli import CACHED_ENGINE_MODEL
# from uetools.core import *
#
#
# def main():
#     sleep(2)
#     cook_arguments:CookGameWrapper = CookGameWrapper(CACHED_ENGINE_MODEL, CACHED_ENVIRONMENT_MODEL)
#     cook_arguments.execute()


from uecli.ui.home_screen import HomeScreen
from uecli.ui import menu_screen
from uecli.ui import content_screen

home_screen:HomeScreen = HomeScreen()
home_screen.run()

# console = Console()
#
# selection = Menu.prompt(
#     "[bold]Would you rather:[/bold]",
#     items={
#         "invisibility": "Be able to turn invisible",
#         "fly": "Be able to fly",
#         "read-minds": "Be able to read people's minds",
#         "quit": "None of this nonsense",
#     },
# )
#
# if selection is None or selection is "quit":
#     console.print("[bold]:sparkles: quit[/bold]")
# else:
#     console.print(f"You have selected: [bold]{selection}[/bold]")
