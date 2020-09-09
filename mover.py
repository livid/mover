#!/usr/bin/env python
# coding=utf-8

import datetime
import getpass
import os
import os.path
import shutil
import time


def move():
    today = datetime.datetime.today()
    prefix = '/Users/' + getpass.getuser() + '/'
    desktop = prefix + 'Desktop/'
    drawer = prefix + 'Documents/Drawer/'
    dst = drawer + today.strftime('%Y%m') + '/'

    if not os.path.exists(dst):
        os.mkdir(dst)
        print("Folder created: %s" % (dst))

    files = os.listdir(desktop)

    now = time.time()

    days = 86400 * 7

    for item in files:
        if (not item.startswith('.')) and (not item.endswith('.icloud')):
            file = desktop + item
            accessed = os.path.getatime(file)
            diff = now - accessed
            if diff > (days):
                print("Stale File: %s (Last Accessed: %f seconds ago)" % (file, diff))
                shutil.move(file, dst + item)
                message = item
                #gntp.notifier.mini(message, applicationName="Mover", title="File Moved")
            else:
                print("Fresh File: %s (Last Accessed: %f seconds ago)" % (file, diff))


if __name__ == "__main__":
    move()
