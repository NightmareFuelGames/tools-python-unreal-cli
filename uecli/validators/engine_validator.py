import os

from uecli.validators import ValidateEnvErrCode


class EngineValidator:
    """
    Engine validator
    """
    from uecli import EngineProperties

    @staticmethod
    def validate_engine_path(engine_path: str) -> (bool, int):
        """
        Validate the engine paths
        :param engine_path: The path to the engine ../?UE_5.4?/Engine <--install location of the engine
        :return: True if the engine path is valid
        """
        if not os.path.exists(engine_path):
            return False, ValidateEnvErrCode.ENGINE_PATH_NOT_FOUND
        if not os.path.isdir(engine_path):
            return False, ValidateEnvErrCode.ENGINE_PATH_IS_NOT_A_DIRECTORY
        if not os.path.exists(os.path.join(engine_path,  "Build")):
            return False, ValidateEnvErrCode.ENGINE_BUILD_FOLDER_NOT_FOUND
        if not os.path.exists(os.path.join(engine_path, "Build", "Build.version")):
            return False, ValidateEnvErrCode.ENGINE_VERSION_FILE_NOT_FOUND

        return True, ValidateEnvErrCode.SUCCESS

    @staticmethod
    def validate_engine_version(minimal_engine_version: (int, int, int),
                                current_engine_version: (int, int, int)) -> bool:
        """
        Validate the engine version
        :param minimal_engine_version: The required engine version
        :param current_engine_version: The current engine version
        :return: True if the engine version is valid
        """
        major_current = minimal_engine_version[0]
        minor_current = minimal_engine_version[1]
        patch_current = minimal_engine_version[2]

        major_target = current_engine_version[0]
        minor_target = current_engine_version[1]
        patch_target = current_engine_version[2]

        if (major_current != major_target or
                minor_current != minor_target or
                patch_current != patch_target):
            return False

        return True

    @staticmethod
    def validate(engine: EngineProperties) -> (bool, int):
        """
        Validate engine properties
        :param engine: The engine properties
        :return: True if the engine properties are valid
        """
        engine_path_validation: (bool, int) = EngineValidator.validate_engine_path(engine.engine_path)
        if not engine_path_validation[0]:
            return engine_path_validation

        current_engine_version = engine.engine_version
        minimal_engine_version = (5, 4, 4)

        if not EngineValidator.validate_engine_version(
                minimal_engine_version, current_engine_version):
            return False, ValidateEnvErrCode.ENGINE_VERSION

        return True, ValidateEnvErrCode.SUCCESS
