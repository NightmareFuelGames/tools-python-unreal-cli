"""
Author: Kasper de Bruin kasperbruin8@gmail.com
Date: 2024-10-26 06:02:52
LastEditors: Kasper de Bruin kasperbruin8@gmail.com
LastEditTime: 2024-10-26 12:35:44
FilePath: uecli/commands/build_cook_run.py
Description: Wrapper around the build, cook and run command
"""
from os import environ

from uecli import EngineProperties, EnvironmentModel
from uecli.commands.command_base import CommandBase

from uetools.commands.uat.cook import CookGameUAT


class CookGameWrapper(CommandBase):
    """
    Wrapper around the build, cook and run command 
    """
    def __init__(self, engine: EngineProperties, environment: EnvironmentModel):
        """
        Constructor
        :param engine: The engine properties 
        :param environment:  The environment properties
        """
        super().__init__(engine, environment)
        self.args: CookGameUAT.Arguments = self.create(engine, environment)
        super().execute()
    
    def _execute(self) -> None:
        """
        Execute the command
        :return:  None
        """
        CookGameUAT.execute(self.args)

    @staticmethod
    def get_default_build_args(engine_properties: EngineProperties, environ_properties: EnvironmentModel) -> "CookGameUAT.Arguments":
        """
        Get the default arguments
        :param engine_properties:   The engine properties 
        :param environ_properties:  The environment properties
        :return:    The default arguments
        """
        args: CookGameUAT.Arguments = CookGameUAT.Arguments(engine_properties,environ_properties )
        args.project = environ_properties.project_path
        args.unrealexe = "UnrealEditor.exe"
        args.noP4 = True

        args.platform =     "Win64"
        args.profile =      "Development"
        args.clientconfig = "Development"
        args.serverconfig = "Development"

        args.cook = True
        args.build = True
        args.stage = True
        args.pak = True

        args.separatedebuginfo = True
        args.MapFile = True
        args.CrashReporter = True
        args.ForceDebugInfo = True
        args.logwindow = True

        args.compress = True
        args.archive = True
        
        args.archivedirectory = environ_properties.archive_path
        return args


    @staticmethod
    def create(engine_properties: EngineProperties, environ_properties: EnvironmentModel) -> "CookGameUAT.Arguments":
        """
        Create the arguments
        :param engine_properties: The engine properties 
        :param environ_properties:  The environment properties
        :return: 
        """
        args = CookGameWrapper.get_default_build_args(engine_properties, environ_properties)
        return args
    
