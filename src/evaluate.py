"""
Model Evaluation & Deployment Gating Logic

This module simulates production-safe model promotion.
Deployment is allowed only if new model performance
exceeds current production performance.
"""

def compare_model_performance(new_accuracy: float, production_accuracy: float):
    """
    Compare new model accuracy against production model accuracy.

    Args:
        new_accuracy (float): Accuracy of newly trained model
        production_accuracy (float): Accuracy of currently deployed model

    Returns:
        dict: Decision and reason
    """

    if new_accuracy > production_accuracy:
        return {
            "deploy": True,
            "reason": "New model outperforms production model."
        }
    else:
        return {
            "deploy": False,
            "reason": "New model does not meet production benchmark. Deployment blocked."
        }


if __name__ == "__main__":
    # Simulated values
    production_accuracy = 0.82
    new_model_accuracy = 0.84

    decision = compare_model_performance(new_model_accuracy, production_accuracy)

    print("Deployment Decision:", decision)

