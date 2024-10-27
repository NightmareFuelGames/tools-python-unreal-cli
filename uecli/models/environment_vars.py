from __future__ import annotations



class EnvironmentVar:
    """
    Model for environment variables
    """
    def __init__(self, key: str, value=None, can_be_none: bool = False):
        """
        Constructor
        :param key: the key of the environment variable
        :param value:  the value of the environment variable
        :param can_be_none:  True if the value can be None
        """
        self.key: str = key
        self.value = value
        self.can_be_none = can_be_none

    @property
    def is_set(self) -> bool:
        """
        Check if the value is set
        :return:  True if the value is set
        """
        return self.value is not None

    @property
    def is_valid(self) -> bool:
        """
        Check if the value is valid, i.e. set or can be None
        :return: True if the value is valid
        """
        return self.is_set or self.can_be_none

    def __str__(self):
        return f"[{self.key}={self.value}]"

class EnvironmentModel:
    """
    Model for environment variables
    """
    from typing import Dict

    has_been_loaded: bool = False
    cached_vars: Dict = {
        'ENGINE_PATH': EnvironmentVar("ENGINE_PATH", None),
        'ARCHIVE_PATH': EnvironmentVar("ARCHIVE_PATH", None),
        'PROJECT_PATH': EnvironmentVar("PROJECT_PATH", None),
        'ENGINE_MAJOR': EnvironmentVar("ENGINE_MAJOR", 5),
        'ENGINE_MINOR': EnvironmentVar("ENGINE_MINOR", 4),
        'ENGINE_PATCH': EnvironmentVar("ENGINE_PATCH", 4),
    }


    @property
    def engine_path(self):
        return self.cached_vars.get("ENGINE_PATH").value

    @property
    def archive_path(self):
        return self.cached_vars.get("ARCHIVE_PATH").value

    @property
    def project_path(self):
        return self.cached_vars.get("PROJECT_PATH").value

    @property
    def minimal_engine_version(self) -> {int, int, int}:
        return (self.cached_vars.get("ENGINE_MAJOR").value,
                self.cached_vars.get("ENGINE_MINOR").value,
                self.cached_vars.get("ENGINE_PATCH").value)

    def get(self, key: str) -> EnvironmentVar:
        return self.cached_vars.get(key)

    def __str__(self):
        return (f"EnvironmentModel ("
                f"\n" + "\n".join([f""
                                   f"     {val}" for key, val in self.cached_vars.items()])
                + "\n )")


    @classmethod
    def _fetch_dot_and_env(cls) -> Dict:
        import dotenv
        import os

        dotenv.load_dotenv(
            override=True,
            verbose=True)

        # values:Dict[str, Optional[str]] = dotenv.dotenv_values()
        # for key, value in values.items():
        #     print(f"Loaded {key}={value}")

        for key, env_var in cls.cached_vars.items():
            env_var.value = os.getenv(key)

        return cls.cached_vars

    @classmethod
    def load(cls, force_reload: bool = False) -> "EnvironmentModel":
        import os
        if cls.has_been_loaded and not force_reload: #use cached vars
            return cls()

        cls.has_been_loaded = True
        cls.cached_vars = EnvironmentModel._fetch_dot_and_env()

        for key, env_var in cls.cached_vars.items():
            env_var.key = key
            env_var.value = os.getenv(key)

        return cls()
