"""
Environment-Based Model Promotion Logic

This module simulates controlled promotion of model artifacts
across Dev → PreProd → Prod environments.
"""

class ModelDeployer:

    def __init__(self, model_version: str):
        self.model_version = model_version

    def deploy_to_environment(self, environment: str):
        """
        Simulate deployment to specific environment.

        Args:
            environment (str): dev | preprod | prod
        """

        print(f"Deploying model version {self.model_version} to {environment.upper()} environment")

    def promote_model(self):
        """
        Controlled promotion flow:
        Dev → PreProd → Prod
        """

        self.deploy_to_environment("dev")
        self.deploy_to_environment("preprod")
        self.deploy_to_environment("prod")


if __name__ == "__main__":
    model = ModelDeployer("v2026_02_15")
    model.promote_model()
