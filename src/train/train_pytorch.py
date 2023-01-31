from pathlib import Path
from time import time
from typing import List
from sklearn.neural_network import MLPClassifier
import joblib


replay_memory_location = Path("ML_replay_memories") / "test_replay_memory"
model_location = Path("ML_models") / "test_model"

# check that the replay memory dataset is found at the specified location
if not replay_memory_location.exists():
    raise ValueError(f"Dataset was not found at: {replay_memory_location} !")

# Check if model exists already
if model_location.exists():
    raise ValueError(
        f"Model at {model_location} exists already and overwrite is set to False. \nNo new model will be trained, process terminates"
    )


# data
data: List[List[int]] = []
targets: List[int] = []

with open(file=replay_memory_location, mode="r") as replay_memory_file:
    for line in replay_memory_file:
        feature_string, won_label_str = line.split("||")
        feature_list_strings: List[str] = feature_string.split(",")
        feature_list = [int(feature) for feature in feature_list_strings]
        won_label = int(won_label_str)
        data.append(feature_list)
        targets.append(won_label)

print("Dataset Statistics:")
samples_of_wins = sum(targets)
samples_of_losses = len(targets) - samples_of_wins
print("Samples of wins:", samples_of_wins)
print("Samples of losses:", samples_of_losses)

# training
hidden_layer_sizes = (500, 400, 100, 40)
learning_rate = 0.00015
regularization_strength = 0.00005

learner = MLPClassifier(
    hidden_layer_sizes=hidden_layer_sizes,
    learning_rate_init=learning_rate,
    alpha=regularization_strength,
    verbose=True,
    early_stopping=True,
    n_iter_no_change=6,
    activation="tanh",
)

start = time()
print("Starting training phase...")

model = learner.fit(data, targets)
# Save the model in a file
joblib.dump(model, model_location)
end = time.time()
print("The model was trained in ", (end - start) / 60, "minutes.")
