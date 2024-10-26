from pytube import YouTube, Playlist
from threading import Thread
import os


class YTDownloader:
    AVAILABLE_FORMATS = ['mp3', 'mp4']

    def __init__(self):
        self.download_dir = rf'.\downloads'
        self.format_ = 'mp3'

    def set_download_dir(self, new_dir):
        '''Set the desired download dir'''
        if os.path.isdir(new_dir):
            self.download_dir = new_dir
        else:
            raise Exception(f'"{new_dir}" is not a valid directory!')

    def get_abs_download_dir(self):
        '''Get the currently chosen download directory absolute path'''
        return os.path.abspath(self.download_dir)

    def set_format(self, new_format):
        '''Set the desired format'''
        if new_format in self.AVAILABLE_FORMATS:
            self.format_ = new_format
        else:
            raise Exception(f'{new_format} is unsupported format!\nSupported formats are as follows - {self.AVAILABLE_FORMATS}')

    def download_song(self, song_link: str):
        '''Download a single song'''
        vid = YouTube(song_link)

        if self.format_ == 'mp4':
            vid.streams.filter(progressive=True, file_extension=self.format_).order_by('resolution').desc().first().download(output_path=self.download_dir, filename=f'{vid.author} - {vid.title}.mp4')
        elif self.format_ == 'mp3':
            stream = vid.streams.filter(only_audio=True).order_by('bitrate').desc().first()
            stream.download(output_path=self.download_dir, filename=f'{vid.author} - {vid.title}.mp3')
        else:
            print('ERROR: Unsupported format')

    def download_multiple(self, song_links: list):
        '''Download multiple songs'''
        threads = []

        for song in song_links:
            tr = Thread(target=self.download_song, args=(song,))
            tr.start()
            threads.append(tr)

        for thread in threads:
            thread.join()

        return True

    def download_playlist(self, playlist_link: str):
        '''Download playlist'''
        pl = Playlist(playlist_link)
        self.download_multiple(pl)
