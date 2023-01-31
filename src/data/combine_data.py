list_of_data_files = [
    "src/data/datasets/dataset10core_0.txt",
    "src/data/datasets/dataset10core_1.txt",
    "src/data/datasets/dataset10core_2.txt",
    "src/data/datasets/dataset10core_3.txt",
    "src/data/datasets/dataset16core_1.txt",
    # "src/data/datasets/dataset16core_2.txt",
]

output_file = "src/data/datasets/games_dataset.txt"

# combine the data files
with open(output_file, "w") as output:
    for data_file in list_of_data_files:
        with open(data_file, "r") as input:
            for line in input:
                output.write(line)
