import pandas as pd
import os

pd.options.plotting.backend = 'plotly'
INPUT_FILES_FOLDER = r'input_files'

def parse_file(file_path: str) -> pd.DataFrame:
    df = pd.read_excel(file_path)
    return df

def init_data_frames() -> list[pd.DataFrame]:
    data_frames : list[pd.DataFrame] = []

    for file in os.listdir(INPUT_FILES_FOLDER):
        file_path = os.path.join(INPUT_FILES_FOLDER, file)
        if not os.path.isfile(file_path):
            continue

        data_frames.append(parse_file(file_path))

    return data_frames


def main_func():
    data_frames = init_data_frames()
    fig = data_frames[0].plot(
        title="Pandas Backend Example", template="simple_white",
        labels=dict(index="time", value="money", variable="option"))


if __name__ == '__main__':
    main_func()