from enum import Enum


class ValidateEnvErrCode(Enum):
    SUCCESS = 0,

    ENGINE_PATH_NOT_FOUND = 1,
    ENGINE_PATH_IS_NOT_A_DIRECTORY = 2,
    ENGINE_FOLDER_NOT_FOUND = 3,
    ENGINE_BUILD_FOLDER_NOT_FOUND = 5,
    ENGINE_VERSION_FILE_NOT_FOUND = 6,


    ENGINE_VERSION_MISMATCH = 7,

from . import *
