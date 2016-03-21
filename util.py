from colorama import init, Fore, Back, Style

init()


def print_torrent(index, name, seeders, size):
    print(Fore.GREEN, index,
          Fore.RED, name,
          Fore.BLUE, size,
          Fore.CYAN, seeders,
          Style.RESET_ALL)
