import shutil
from pathlib import Path


def create_files(nr_of_days: int = 25):
    """
    Create dayXX.py files and dayXX_input.txt files if they do not exist and initialize them with the template
    :return:
    """
    aoc_days_path = Path('./aoc_days')
    for i in range(1, nr_of_days + 1):
        aoc_days_path.joinpath(f'day{i:02}_input.txt').touch()
        dst_path = aoc_days_path.joinpath(f'day{i:02}.py')
        if not dst_path.exists():
            shutil.copyfile('./aoc_helper/dayXX_template.txt', dst_path)
