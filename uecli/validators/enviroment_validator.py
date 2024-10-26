
class EnvironmentValidator:
    from uecli.models.environment_vars import EnvironmentModel

    @staticmethod
    def validate(environment: EnvironmentModel) -> bool:
        for key, env_var in environment.cached_vars.items():
            if not env_var.is_set:
                raise ValueError(f"Environment variable {key} is not set.")

        return True