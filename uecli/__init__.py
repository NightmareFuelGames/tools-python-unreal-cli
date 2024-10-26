# This file is used to initialize the package and import the necessary modules


__version__ = "0.1.0"
__author__ = "Kasper de Bruin"
__url__ = ""

import sys
import os
from uecli.validators.enviroment_validator import EnvironmentValidator

libs_abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "libs"))
uetools = os.path.join(libs_abs_path, "uetools")

sys.path.append(libs_abs_path)
sys.path.append(uetools)

from libs import *  # noqa
import libs.uetools as uetools  # noqa

from uecli.models.environment_vars import EnvironmentModel
from uecli.models.engine_properties import EngineProperties

# GLOBAL VARIABLES
CACHED_ENVIRONMENT_MODEL: EnvironmentModel = EnvironmentModel.load()
from uecli.validators.enviroment_validator import EnvironmentValidator

EnvironmentValidator.validate(CACHED_ENVIRONMENT_MODEL)

CACHED_ENGINE_MODEL: EngineProperties = EngineProperties.create(CACHED_ENVIRONMENT_MODEL)
from uecli.validators.engine_validator import EngineValidator

engine_validation: {int, bool} = EngineValidator.validate(CACHED_ENGINE_MODEL)
