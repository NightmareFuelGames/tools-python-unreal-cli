class EnvironmentValidator:
    """
    Validator for environment variables
    """
    from uecli.models.environment_vars import EnvironmentModel

    @staticmethod
    def validate(environment: EnvironmentModel) -> bool:
        """
        Validate the environment variables
        :param environment: The environment model
        :return:  True if all environment variables are set
        """
        for key, env_var in environment.cached_vars.items():
            if not env_var.is_valid:
                raise ValueError(f"Environment variable {key} is not set")

        return True
