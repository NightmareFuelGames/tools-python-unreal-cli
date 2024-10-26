# This file is used to initialize the package and import the necessary modules

import sys
import os

from uecli.validators.enviroment_validator import EnvironmentValidator

libs_abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(libs_abs_path)


from typing import final

from libs import * # noqa
import libs.uetools as uetools # noqa

from uecli.models.environment_vars import EnvironmentModel
from uecli.models.engine_model import EngineModel

#GLOBAL VARIABLES
CACHED_ENVIRONMENT_MODEL: EnvironmentModel = EnvironmentModel.load()
from uecli.validators.enviroment_validator import EnvironmentValidator
EnvironmentValidator.validate(CACHED_ENVIRONMENT_MODEL)

CACHED_ENGINE_MODEL: EngineModel = EngineModel.create(CACHED_ENVIRONMENT_MODEL)
from uecli.validators.engine_validator import EngineValidator
EngineValidator.validate(CACHED_ENGINE_MODEL)