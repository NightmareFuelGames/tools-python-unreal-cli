from uecli.commands.build_cook_run import BuildCookArguments
from uecli import CACHED_ENVIRONMENT_MODEL
from uecli import CACHED_ENGINE_MODEL

def main():
    print("Hello World")
    print(CACHED_ENVIRONMENT_MODEL)
    print(CACHED_ENGINE_MODEL)
    cook_arguments:BuildCookArguments = BuildCookArguments(CACHED_ENGINE_MODEL, CACHED_ENVIRONMENT_MODEL)

    print(cook_arguments)
    cook_arguments.execute()



main()