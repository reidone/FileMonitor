from watchdog.events import FileSystemEventHandler
import time
class FileMonitor(FileSystemEventHandler):
    def on_moved(self, event):
        super(FileMonitor, self).on_moved(event)
        now_time = time.strftime("[\033[32m INFO \033[0m]\033[34m %H:%M:%S \033[0m", time.localtime())
        what = 'directory' if event.is_directory else 'file'
        print "{0} {1} Moved : from {2} to {3}".format(now_time, what, event.src_path, event.dest_path)

    def on_deleted(self, event):
        super(FileMonitor, self).on_deleted(event)
        now_time = time.strftime("[\033[32m INFO \033[0m]\033[34m %H:%M:%S \033[0m", time.localtime())
        what = 'directory' if event.is_directory else 'file'
        print "{0} {1} Deleted : {2} ".format(now_time, what, event.src_path)

    def on_modified(self, event):
        super(FileMonitor, self).on_modified(event)
        now_time = time.strftime("[\033[32m INFO \033[0m]\033[34m %H:%M:%S \033[0m", time.localtime())
        what = 'directory' if event.is_directory else 'file'
        print "{0} {1} Modified : {2} ".format(now_time, what, event.src_path)
        
    def on_created(self, event):
        super(FileMonitor, self).on_moved(event)
        now_time = time.strftime("[\033[32m INFO \033[0m]\033[34m %H:%M:%S \033[0m", time.localtime())
        what = 'directory' if event.is_directory else 'file'
        print "{0} {1} Created : {2} ".format(now_time, what, event.src_path)
        