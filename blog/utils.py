import os, random


def random_user_photo(dir: str) -> str:
    return random.choice(os.listdir(dir))
