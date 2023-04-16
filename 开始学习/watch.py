#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
使用watchdog监听文件变动。
"""
from watchdog.events import FileModifiedEvent
from watchdog.observers import Observer
from subprocess import call

WATCH_PATH = r'D:\code\案列\Flask\开始学习'  # 监控目录


class WatchFile(FileModifiedEvent):

    def dispatch(self, event):
        # print("可以带入的参数", self._src_path)
        # print(event)
        call("python %s" % self._src_path, shell=True)


if __name__ == '__main__':
    # 实例化一个监控对象
    observer = Observer()
    event_handler = WatchFile(src_path="App.py")

    observer.schedule(
        event_handler=event_handler, path=WATCH_PATH, recursive=True)

    observer.start()

    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()
