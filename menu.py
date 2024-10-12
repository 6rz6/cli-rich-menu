#!/usr/bin/env python3
import json
import sys
import tty
import termios
import signal
import os
import subprocess
from rich.console import Console
from rich.table import Table
from rich.style import Style

console = Console()

def load_commands():
    try:
        with open('/home/rz1/dev/menu_app/commands2.json', 'r') as f:
            commands = json.load(f)
    except FileNotFoundError:
        commands = []
    # Ensure 'shell' and 'exit' menu items exist
    if not any(item['name'].strip() == 'shell' for item in commands):
        commands.insert(0, {"name": "shell", "value": "exit_application"})
    if not any(item['name'].strip() == 'exit' for item in commands):
        commands.append({"name": "exit", "value": "exit_application"})
    return commands

def group_commands(commands):
    # Group commands into specified columns
    columns = [[] for _ in range(5)]
    for item in commands:
        name = item['name'].strip()
        if name == 'shell' or name.startswith('⭐'):
            columns[0].append(item)
        elif name.startswith('🔴'):
            columns[1].append(item)
        elif name.startswith('🧡') or name.startswith('✨'):
            columns[2].append(item)
        elif name.startswith('💚') or name.startswith('nano_bashrc') or name.startswith('source_bashrc'):
            columns[3].append(item)
        elif name.startswith('💖'):
            columns[4].append(item)
    return columns

def render_menu(columns, selected_row, selected_col):
    # Calculate the maximum number of rows
    max_rows = max(len(col) for col in columns)
    # Prepare the table
    table = Table(show_header=False, box=None, expand=False)
    # Add columns to the table
    for _ in columns:
        table.add_column(justify="left", no_wrap=True)
    # Build the table rows
    for row in range(max_rows):
        row_items = []
        for col in range(len(columns)):
            items = columns[col]
            if row < len(items):
                item = items[row]
                idx = (row, col)
                if idx == (selected_row, selected_col):
                    style = Style(bold=True, color="magenta")
                else:
                    style = Style(bold=True, color="cyan")  # Use 'cyan' for bold aqua color
                label = item['name']
                # Remove any brackets from labels
                label = label.replace('[', '').replace(']', '').strip()
                row_items.append(f"[{style}]{label}[/{style}]")
            else:
                row_items.append("")
        table.add_row(*row_items)
    # Clear the console and render the menu
    console.clear()
    console.print(table)

def get_input():
    ch = sys.stdin.read(1)
    if ch == '\x1b':
        ch += sys.stdin.read(2)  # Read the next two bytes for arrow keys
        if ch == '\x1b[A':  # Up arrow
            return 'up'
        elif ch == '\x1b[B':  # Down arrow
            return 'down'
        elif ch == '\x1b[C':  # Right arrow
            return 'right'
        elif ch == '\x1b[D':  # Left arrow
            return 'left'
    elif ch in ['\n', '\r', ' ']:  # Enter key or space
        return 'enter'
    elif ch == '\x03':  # Ctrl+C
        exit_application()
    else:
        return None

def execute_command(command_value):
    # Execute the command
    if command_value == 'exit_application':
        sys.exit(0)
    else:
        command = os.path.expanduser(command_value).strip()
        # Replace 'py ' with 'python3 ' if needed
        command = command.replace('py ', 'python3 ')
        try:
            # Use subprocess.run to execute the command and wait for it to complete
            subprocess.run(f"bash -i -c \"{command}\"", shell=True)
        except Exception as e:
            console.print(f"[red]Error executing command: {e}[/red]")
    # Exit the application after executing the command
    sys.exit(0)

def exit_application():
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, lambda sig, frame: exit_application())
    commands = load_commands()
    columns = group_commands(commands)
    selected_row = 0  # Start with the first item
    selected_col = 0  # Start with the first column
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        while True:
            render_menu(columns, selected_row, selected_col)
            key = get_input()
            if key == 'up':
                selected_row = max(0, selected_row - 1)
            elif key == 'down':
                max_row = len(columns[selected_col]) - 1
                selected_row = min(max_row, selected_row + 1)
            elif key == 'left':
                selected_col = max(0, selected_col - 1)
                max_row = len(columns[selected_col]) - 1
                selected_row = min(selected_row, max_row)
            elif key == 'right':
                selected_col = min(len(columns) - 1, selected_col + 1)
                max_row = len(columns[selected_col]) - 1
                selected_row = min(selected_row, max_row)
            elif key == 'enter':
                break  # Exit the loop to execute the command
            # Ensure selected_row is within bounds
            selected_row = max(0, min(selected_row, len(columns[selected_col]) - 1))
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    # Clear the screen before executing the command
    console.clear()
    # Execute the selected command
    selected_item = columns[selected_col][selected_row]
    execute_command(selected_item['value'])

if __name__ == "__main__":
    main()
