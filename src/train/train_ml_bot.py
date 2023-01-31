from pathlib import Path
from schnapsen.bots.ml_bot import train_ML_model


replay_memory_filename: str = "games_dataset.txt"
replay_memories_directory: str = "src/data/datasets/"
replay_memory_location = Path(replay_memories_directory) / replay_memory_filename
model_name: str = "nnmodelv6"
model_dir: str = "src/models"
model_location = Path(model_dir) / model_name

train_ML_model(
    replay_memory_location=replay_memory_location,
    model_location=model_location,
    model_class="NN",
)
