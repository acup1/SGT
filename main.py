#!python
import os
import curses
import subprocess


def script_exec():
    global selected_script
    if selected_script != -1:
        os.execl(*[f"./actions/{menu[selected_script]}"] * 2)


def get_cmd_text(cmd: str):
    return subprocess.run(cmd.split(), capture_output=True, text=True).stdout


menu = os.listdir("actions")

selected_script = -1


def main(stdscr):
    global selected_script
    stdscr.clear()

    list_len = len(menu)
    pos_menu = {}

    stdscr.addstr("branches:\n")
    stdscr.addstr(get_cmd_text("git branch"))

    stdscr.addstr("select action(q for exit):\n")
    for i, j in enumerate(menu):
        y, x = stdscr.getyx()
        pos_menu[y] = i
        stdscr.addstr(f"  {i}: {j}\n")
    stdscr.refresh()
    stdscr.move(min(pos_menu.keys()), 0)
    y, x = stdscr.getyx()

    key = 0
    while 1:
        key = stdscr.getch()
        if key == curses.KEY_UP:
            if min(pos_menu.keys()) <= y - 1:
                stdscr.move(y - 1, 0)
            y, x = stdscr.getyx()
        if key == curses.KEY_DOWN:
            if y + 1 <= max(pos_menu.keys()):
                stdscr.move(y + 1, 0)
            y, x = stdscr.getyx()
        if chr(key) == "q":
            break
        if chr(key) == "\n":
            selected_script = pos_menu[y]
            break


if __name__ == "__main__":
    curses.wrapper(main)
    script_exec()
