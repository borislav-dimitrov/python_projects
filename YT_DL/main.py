from downloader import YTDownloader
from gui import Application
from history import HistoryManager


if __name__ == '__main__':
    downloader = YTDownloader()
    history = HistoryManager()
    try:
        app = Application(download_mgr=downloader, history_mgr=history)
        app.run()
    except Exception as ex:
        with open(rf'.\log.txt', 'a') as log_file:
            log_file.writelines(f'[{history.generate_timestamp()[3]}]: {ex}\n')
        raise ex
