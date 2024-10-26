from enum import Enum


class ValidateEnvErrCode(Enum):
    SUCCESS = 0,

    ENGINE_PATH_NOT_SET = 1,
    ENGINE_PATH_NOT_EXISTS = 2,
    ENGINE_PATH_NOT_VALID = 3,

    ENGINE_VERSION_NOT_SET = 5,

    ENVIRONMENT_NOT_SET = 6

from . import *
