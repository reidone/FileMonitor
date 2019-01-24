from watchdog.events import FileSystemEventHandler
import time
class FileMonitor(FileSystemEventHandler):
    def on_moved(self, event):
        super(FileMonitor, self).on_moved(event)
        now_time = time.strftime("[\033[32m INFO \033[32m]\033[34m %H:%M:%S \033[34m", time.localtime())
        what = 'directory' if event.is_directory else 'file'

    def on_deleted(self, event):
        super(FileMonitor, self).on_deleted(event)
        now_time = time.strftime("[\033[32m INFO \033[32m]\033[34m %H:%M:%S \033[34m", time.localtime())
        what = 'directory' if event.is_directory else 'file'


    def on_modified(self, event):
        super(FileMonitor, self).on_modified(event)
        now_time = time.strftime("[\033[32m INFO \033[32m]\033[34m %H:%M:%S \033[34m", time.localtime())
        what = 'directory' if event.is_directory else 'file'
        
    def on_created(self, event):
        super(FileMonitor, self).on_moved(event)
        now_time = time.strftime("[\033[32m INFO \033[32m]\033[34m %H:%M:%S \033[34m", time.localtime())
        what = 'directory' if event.is_directory else 'file'
        