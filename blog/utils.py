import os, random


def random_photo(dir: str) -> str:
    return random.choice(os.listdir(dir))
