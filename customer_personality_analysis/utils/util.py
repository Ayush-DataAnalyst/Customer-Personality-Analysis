import os

def create_directories(paths: list):
    for path in paths:
        os.makedirs(path, exist_ok=True)

