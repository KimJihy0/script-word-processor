import os


def get_input_file_path(file_name: str) -> str:
    file_path = f"./input/{file_name}"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    return file_path

def get_output_file_path(file_name: str) -> str:
    file_path = f"./output/{file_name}"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    return file_path