import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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

def set_correct_tool_name(data_frame: pd.DataFrame):
    tool_name = data_frame['Program'][0]

    if ('viewer' in data_frame['Program'][0].lower()
        or 'gndv' in data_frame['Program'][0].lower()):
        tool_name = 'GNDV'
    elif ('cruncher' in data_frame['Program'][0].lower()
          or 'gndc' in data_frame['Program'][0].lower()):
        tool_name = 'GNDC'

    data_frame.loc[:, 'Program'] = tool_name


def installed_versions_count(fig: go.Figure, data_frames: list[pd.DataFrame]):
    for df in data_frames:
        fig.append_trace(
            go.Histogram(x=df['Version'], name=df['Program'][0]),
            row=1, col=1
        )

def unique_users_count(fig: go.Figure, data_frames: list[pd.DataFrame]):
    for df in data_frames:
        tmp_df = df.drop_duplicates(subset=['Email'])
        fig.append_trace(
            go.Histogram(x=tmp_df['Program'], name=df['Program'][0]),
            row=2, col=1
        )

def main_func():
    # 'Machine Name', 'Username', 'Email', 'Location', 'Publisher', 'Program', 'Version'
    data_frames = init_data_frames()
    for df in data_frames:
        set_correct_tool_name(df)

    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=('Installed Versions Count', 'Unique Users Count')
        )

    installed_versions_count(fig, data_frames)
    unique_users_count(fig, data_frames)

    fig.update_layout(title_text='Tool Name statistics')

    fig.update_xaxes(title_text='Tool Version', row=1, col=1)
    fig.update_yaxes(title_text='Count', row=1, col=1)

    fig.update_xaxes(title_text='User Email', row=2, col=1)
    fig.update_yaxes(title_text='Count', row=2, col=1)

    fig.show()

if __name__ == '__main__':
    main_func()