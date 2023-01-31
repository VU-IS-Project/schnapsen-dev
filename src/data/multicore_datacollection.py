import multiprocessing
from random import Random
from pathlib import Path
from schnapsen.bots import RdeepBot
from schnapsen.game import Bot, SchnapsenGamePlayEngine
from schnapsen.bots.ml_bot import MLDataBot


def collect_data(core_number) -> None:
    """Collect data from the sensors and store it in the database."""
    # define replay memory database creation parameters
    num_of_games: int = 10000
    replay_memory_dir: str = "generated_data"
    replay_memory_filename: str = f"dataset_rd32s16d_10k_games_{core_number}.txt"
    replay_memory_location = Path(replay_memory_dir) / replay_memory_filename

    bot_1_behaviour: Bot = RdeepBot(num_samples=32, depth=16, rand=Random(420420))
    bot_2_behaviour: Bot = RdeepBot(num_samples=32, depth=16, rand=Random(696969))
    delete_existing_older_dataset = False

    # check if needed to delete any older versions of the dataset
    if delete_existing_older_dataset and replay_memory_location.exists():
        print(
            f"An existing dataset was found at location '{replay_memory_location}', which will be deleted as selected."
        )
        replay_memory_location.unlink()

    # in any case make sure the directory exists
    replay_memory_location.parent.mkdir(parents=True, exist_ok=True)

    # create new replay memory dataset, according to the behaviour of the provided bots and the provided random seed
    engine = SchnapsenGamePlayEngine()
    replay_memory_recording_bot_1 = MLDataBot(
        bot_1_behaviour, replay_memory_location=replay_memory_location
    )
    replay_memory_recording_bot_2 = MLDataBot(
        bot_2_behaviour, replay_memory_location=replay_memory_location
    )

    for i in range(1, num_of_games + 1):
        if i % 500 == 0:
            print(f"Progress: {i}/{num_of_games} on core {core_number}")
        engine.play_game(
            replay_memory_recording_bot_1, replay_memory_recording_bot_2, Random(i)
        )

    print(
        f"Replay memory dataset recorder for {num_of_games} games.\nDataset is stored at: {replay_memory_location}"
    )


if __name__ == "__main__":
    # get number of cpu cores
    num_cores = multiprocessing.cpu_count()
    print(f"Number of cores: {num_cores}")

    # run the data collection in parallel
    with multiprocessing.Pool(num_cores) as pool:
        pool.map(collect_data, range(num_cores))
