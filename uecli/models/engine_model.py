from __future__ import annotations
from uecli.models.environment_vars import EnvironmentModel

class EngineModel:

    def __init__(self, engine_path: str, engine_version: tuple[int, int, int]):
        self.engine_path: str = engine_path
        self.engine_version: tuple[int, int, int] = engine_version

    def __str__(self):
        return (f"EngineData("
                f"\n     engine_path={self.engine_path}"
                f"\n     engine_version={self.engine_version}"
                f"\n)")

    @staticmethod
    def create(env_vars: EnvironmentModel) -> EngineModel:
        from uecli.runners.engine_runner import EngineRunner

        engine_version: {int, int, int} = EngineRunner.get_current_engine_version(env_vars.engine_path)
        engine_data = EngineModel(
            env_vars.get("ENGINE_PATH").value,
            engine_version
        )
        return engine_data
