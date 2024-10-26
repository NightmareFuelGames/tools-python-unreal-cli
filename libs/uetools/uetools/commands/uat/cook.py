from dataclasses import dataclass

from argklass.command import Command

from uetools.commands.uat.arguments import BuildCookRunArguments
from uetools.core.conf import find_project, uat
from uetools.core.run import popen_with_format
from uetools.core.util import command_builder
from uetools.format.cooking import CookingFormatter


@dataclass
class _CommonArgs(BuildCookRunArguments):
    nop4: bool = True
    utf8output: bool = True
    nocompileeditor: bool = True
    skipbuildeditor: bool = True
    build: bool = True
    cook: bool = True
    stage: bool = True
    package: bool = True
    iostore: bool = True
    pak: bool = True
    prereqs: bool = True
    compressed: bool = True
    manifests: bool = True
    nocompileuat: bool = True
    archive: bool = True

    # we want to compile on the CI
    nocompile: bool = False


@dataclass
class DedicatedServerCookArgs(_CommonArgs):
    server: bool = True
    noclient: bool = True


@dataclass
class ClientCookArgs(_CommonArgs):
    client: bool = True


@dataclass
class GameCookArgs(_CommonArgs):
    pass


profiles = {
    "server": DedicatedServerCookArgs,
    "game": GameCookArgs,
    "client": ClientCookArgs,
}


class CookGameUAT(Command):
    """Cook your main game using UAT"""

    name: str = "cook"

    # fmt: off
    @dataclass
    class Arguments(BuildCookRunArguments):
        profile                                : str = None

        build                                  : bool = True
        cook                                   : bool = True
        package                                : bool = True
        stage                                  : bool = True
        prereqs                                : bool = True

        iostore                                : bool = True
        pak                                    : bool = True
        compressed                             : bool = True
        # unattended                            : bool = True
        # distribution                          : bool = True
        
        # Often set by the editor
        nop4                                   : bool = True
        utf8output                             : bool = True
        nocompileeditor                        : bool = False
        skipbuildeditor                        : bool = False
        nocompile                              : bool = False
        nocompileuat                           : bool = False
        nodebuginfo                            : bool = False
    # fmt: on

    def update_arguments(args, profile, default_type):
        defaults = default_type()
        for k, v in profile.items():

            if k not in args:
                args[k] = v
                continue

            # args has the default value, override
            if hasattr(defaults, k) and getattr(defaults, k) == args[k]:
                args[k] = v

    @staticmethod
    def execute(args: BuildCookRunArguments):
        assert args.project is not None

        args.project = find_project(args.project)

        if args.profile is not None:
            from dataclasses import asdict

            profile_name = vars(args).pop("profile")
            profile = profiles.get(profile_name, None)

            if profile is not None:
                CookGameUAT.update_arguments(
                    vars(args), asdict(profile()), CookGameUAT.Arguments
                )

        if args.archivedirectory is not None:
            args.archive = True

        if args.config is not None:
            config = vars(args)["config"]

            if BuildCookRunArguments.is_server(args):
                print("Server")
                args.serverconfig = config

            if BuildCookRunArguments.is_client(args):
                print("Client")
                args.clientconfig = config

        # this is some interactive crap
        uat_args = (
            []
        )  # [f"-ScriptsForProject=\"{args.project}\"", "Turnkey", "-UpdateIfNeeded", f"-project=\"{args.project}\""]
        build_cook_args = command_builder(args)

        cmd = [uat()] + uat_args + ["BuildCookRun"] + build_cook_args

        print(" ".join(cmd))

        returncode = 0
        fmt = CookingFormatter(24)
        fmt.print_non_matching = True
        returncode = popen_with_format(fmt, cmd, shell=False)
        fmt.summary()

        return returncode

COMMANDS = CookGameUAT
