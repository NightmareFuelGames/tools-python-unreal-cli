"""
Author: Kasper de Bruin kasperbruin8@gmail.com
Date: 2024-10-26 06:03:22
LastEditors: Kasper de Bruin kasperbruin8@gmail.com
LastEditTime: 2024-10-26 09:19:30
FilePath: uecli/commands/command_base.py
Description: Base class for all commands(abstract)
"""

# Python program showing
# abstract base class work
from abc import ABC, abstractmethod

from typing import List, Optional

from uecli.models.engine_properties import EngineProperties
from uecli.models.environment_vars import EnvironmentModel

from uecli.validators.engine_validator import EngineValidator
from uecli.validators.enviroment_validator import EnvironmentValidator


class CommandBase(ABC):
    def __init__(self,  engine: EngineProperties,environment: EnvironmentModel):
        self.environment = environment
        EnvironmentValidator.validate(environment)
        
        self.engine = engine
        EngineValidator.validate(engine)
        
        
    def execute(self):
        print(f"Executing command: {self.__class__.__name__}\nwith {self.environment}\nand {self.engine}")
        self._execute()

    @abstractmethod
    def _execute(self):
        pass
