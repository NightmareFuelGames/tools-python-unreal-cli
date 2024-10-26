from __future__ import annotations

class EnvironmentVar:
    def __init__(self, key: str, value=None):
        self.key: str = key
        self.value = value

    @property
    def is_set(self) -> bool:
        return self.value is not None

    @property
    def is_valid(self) -> bool:
        return self.is_set

    def __str__(self):
        return f"[{self.key}={self.value}]"

class EnvironmentModel:
    from typing import Dict

    has_been_loaded: bool = False
    cached_vars: Dict = {
        'ENGINE_PATH': EnvironmentVar("ENGINE_PATH", None),
        'PROJECT_PATH': EnvironmentVar("PROJECT_PATH", None),
        'MINIMAL_ENGINE_VERSION_MAJOR': EnvironmentVar("MINIMAL_ENGINE_VERSION_MAJOR", 5),
        'MINIMAL_ENGINE_VERSION_MINOR': EnvironmentVar("MINIMAL_ENGINE_VERSION_MINOR", 4),
        'MINIMAL_ENGINE_VERSION_PATCH': EnvironmentVar("MINIMAL_ENGINE_VERSION_PATCH", 0),
    }


    @property
    def engine_path(self):
        return self.cached_vars.get("ENGINE_PATH").value

    @property
    def project_path(self):
        return self.cached_vars.get("PROJECT_PATH").value

    @property
    def minimal_engine_version(self) -> {int, int, int}:
        return (self.cached_vars.get("MINIMAL_ENGINE_VERSION_MAJOR").value,
                self.cached_vars.get("MINIMAL_ENGINE_VERSION_MINOR").value,
                self.cached_vars.get("MINIMAL_ENGINE_VERSION_PATCH").value)

    def get(self, key: str) -> EnvironmentVar:
        return self.cached_vars.get(key)

    def __str__(self):
        return (f"EnvironmentModel ("
                f"\n" + "\n".join([f""
                                   f"     {val}" for key, val in self.cached_vars.items()])
                + "\n )")

    @classmethod
    def _fetch_dot_and_env(cls) -> Dict:
        from dotenv import load_dotenv as _load_dotenv
        import os

        _load_dotenv()

        for key, env_var in cls.cached_vars.items():
            env_var.value = os.getenv(key)

        return cls.cached_vars

    @classmethod
    def load(cls) -> "EnvironmentModel":
        import os
        if cls.has_been_loaded:
            return cls()

        cls.has_been_loaded = True
        cls.cached_vars = EnvironmentModel._fetch_dot_and_env()

        for key, env_var in cls.cached_vars.items():
            env_var.key = key
            env_var.value = os.getenv(key)

        return cls()
