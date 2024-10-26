from __future__ import annotations
from uecli.models.environment_vars import EnvironmentModel

class EngineProperties:

    def __init__(self, engine_path: str, engine_version: tuple[int, int, int]):
        """
        Constructor
        :param engine_path: The path to the engine ../?UE_5.4?/Engine <--install location of the engine
        :param engine_version: The version of the engine
        """
        self.engine_path: str = engine_path
        self.engine_version: tuple[int, int, int] = engine_version

    def __str__(self):
        return (f"EngineData("
                f"\n     engine_path={self.engine_path}"
                f"\n     engine_version={self.engine_version}"
                f"\n)")

    @staticmethod
    def get_engine_version_file_path(engine_base_path: str) -> str:
        """
        Get the engine version file path
        :param engine_base_path:  The base path of the engine ../?UE_5.4?/Engine <--install location of the engine
        :return:  The engine version file path
        """
        import os
        return os.path.join(engine_base_path, "Build", "Build.version")

    @staticmethod
    def create(env_vars: EnvironmentModel) -> EngineProperties:
        """
        Create the engine properties
        :param env_vars:  The environment variables
        :return:  The engine properties
        """
        from uecli.runners.engine_runner import EngineRunner

        engine_version: (int, int, int) = (
            EngineRunner.get_engine_version(env_vars.engine_path)
        )
        engine_data = EngineProperties(
            env_vars.get("ENGINE_PATH").value,
            engine_version
        )
        return engine_data
