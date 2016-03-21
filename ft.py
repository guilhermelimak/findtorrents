#!/usr/bin/python3
import katapi
import tpbapi
import subprocess
import platform
from builtins import input

import util


def open_magnet(magnet):
    if platform.system() == "Linux":
        subprocess.call(['xdg-open', magnet])
    elif platform.system() == "Darwin":
        subprocess.call(['open', magnet])


def search(query):
    tpb = tpbapi.TpbApi()
    kat = katapi.KatApi()

    torrent_list = kat.search(query) + tpb.search(query)

    i = 0
    # Number of torrents to appear per page
    while i < 25:
        util.print_torrent(i, torrent_list[int(i)]['name'].strip(),
                           torrent_list[int(i)]['seeders'].strip(),
                           torrent_list[int(i)]['size'].strip())
        i += 1

    print()
    to_download = input("Choose movie to download > ")

    magnet = torrent_list[int(to_download)]["magnet"].strip()
    open_magnet(magnet)

query = input("Search > ")

search(query)
