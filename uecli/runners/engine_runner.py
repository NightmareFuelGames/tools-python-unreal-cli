from __future__ import annotations

from uecli import EngineProperties


class EngineRunner:

    @staticmethod
    def get_engine_version(engine_path: str) -> (int, int, int):
        import os
        import re
        get_engine_version_file = EngineProperties.get_engine_version_file_path(engine_path);

        if os.path.exists(get_engine_version_file):
            with open(get_engine_version_file, "r") as f:
                version_major: int = 0
                version_minor: int = 0
                version_patch: int = 0

                for line in f:
                    if "MajorVersion" in line:
                        version_major = int(re.findall(r'\d+', line)[0])
                    if "MinorVersion" in line:
                        version_minor = int(re.findall(r'\d+', line)[0])
                    if "PatchVersion" in line:
                        version_patch = int(re.findall(r'\d+', line)[0])

                return version_major, version_minor, version_patch
        else:
            raise FileNotFoundError(f"Engine version file not found: {get_engine_version_file}")


