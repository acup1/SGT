#!python
import os
import curses


def git_add():
    pass


def comnpush():
    pass


menu = {
    "add -A": git_add,
    "commit & push": comnpush,
}


def main(stdscr):
    stdscr.clear()
    for i, j in enumerate(menu.keys()):
        stdscr.addstr(i, 0, j)
    stdscr.refresh()
    stdscr.move(0, 0)

    key = ""
    while key != curses.KEY_ENTER:
        key = stdscr.getch()
        stdscr.addstr(10, 0, char(curses.KEY_ENTER))
        stdscr.refresh()


if __name__ == "__main__":
    # Initialize curses and run the main function
    curses.wrapper(main)
