list_of_data_files = [
    "ML_replay_memories/random_random_10k_games.txt",
    # "ML_replay_memories/random_random_10k_games2.txt",
]

output_file = "ML_replay_memories/games_dataset.txt"

# combine the data files
with open(output_file, "w") as output:
    for data_file in list_of_data_files:
        with open(data_file, "r") as input:
            for line in input:
                output.write(line)
