import os

class EngineValidator:
    from uecli import EngineModel

    @staticmethod
    def validate_engine_path(engine_path: str) -> bool:
        if not os.path.exists(engine_path):
            return False
        if not os.path.isdir(engine_path):
            return False
        if not os.path.exists(os.path.join(engine_path, "Engine")):
            return False
        if not os.path.exists(os.path.join(engine_path, "Engine", "Build")):
            return False
        if not os.path.exists(os.path.join(engine_path, "Engine", "Build", "Build.version")):
            return False
        return True

    @staticmethod
    def validate_engine_version(minimal_engine_version: {int, int, int},
                                current_engine_version: {int, int, int}) -> bool:
        for i in range(3):
            if current_engine_version[i] < minimal_engine_version[i]:
                return False
            if current_engine_version[i] > minimal_engine_version[i]:
                return True

    @staticmethod
    def validate(engine: EngineModel) -> bool:
        if not EngineValidator.validate_engine_path(engine.engine_path):
            raise ValueError("Engine path is not valid")
        if not EngineValidator.validate_engine_version(
                {0,0,0},
                engine.engine_version):
            raise ValueError("Engine version is not valid")
        return True

