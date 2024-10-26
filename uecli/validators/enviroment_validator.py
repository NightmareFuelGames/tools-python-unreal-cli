
class EnvironmentValidator:
    from uecli.models.environment_vars import EnvironmentModel

    @staticmethod
    def validate(environment: EnvironmentModel) -> bool:
        pass#TODO: Implement this method
    #     for key, env_var in environment.cached_vars.items():
    #         if not env_var.is_set:
    #             raise ValueError(f"Environment {key} variable is not set.")
    #
    #     return True