# Rich Menu Command Line Tool

## Introduction
This project is a command line tool that allows users to navigate through a menu of commands and execute them.

## Description
The Rich Menu Command Line Tool leverages Python's standard libraries to create an interactive user experience. Users can navigate a grid of commands using their keyboard.

## Installation Guide
To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage Guide
1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/6rz6/cli-rich-menu
   ```

2. **Navigate to the project directory:**
   
   ```bash
   cd cli-rich-menu
   ```

3. **Run the script:**
   
   ```bash
   python rich-menu-col.py
   ```

4. **Navigation:**
   - Use the **arrow keys** to navigate through the commands.
   - Press **Enter** to select a command.
   - To exit, press **Ctrl+C** at any time.

5. **Default Command:**
   - The initial command selected by default is the **shell command**.

### JSON Structure
The structure of the menu items is represented as a JSON array of objects:
```
[
    {"name": "⭐ whisper", "value": "command to execute"},
    {"name": "🔴 SearXNG Open Search", "value": "firefox 127.0.0.1:8081/"},
    {"name": "🔴 Windmill Codeless webhooks", "value": "firefox 127.0.0.1"},
    {"name": "🧡 DO-0-IP", "value": "ssh root@127.0.0.1 -i ~/.ssh/pk"},
    {"name": "🧡 DO-0-DyIP", "value": "ssh root@127.0.0.1 -i ~/.ssh/pk"},
    {"name": "🧡 sshr", "value": "ssh -l 127.0.0.1"},
    {"name": "✨ fabric", "value": "~/fabric/fabric "},
    {"name": "✨ fabric_extract_wisdom", "value": "~/fabric/fabric --pattern --extract_wisdom -s"},
    {"name": "✨ fabric_extract_youtube", "value": "fb --stream --pattern extract_wisdom -y "},
    {"name": "💚 nano_bashrc", "value": "nano ~/.bashrc"},
    {"name": "💚 source_bashrc", "value": "source ~/.bashrc"},
    {"name": "....."}
]
```
Each object contains the following fields:
- `name`: Represents the display name of the command, often including an emoticon.
- `value`: Represents the CLI command to be executed when selected.

Additionally, columns in the menu are divided based on the emoticon at the start of the data items.

## Functionality Overview
- **get_input()**: Captures user keyboard input for menu navigation, supporting arrow keys and enter key for selection.
- **execute_command(command_value)**: Executes the command associated with the selected menu item using the `subprocess` module.
- **exit_application()**: Gracefully exits the application.
- **main()**: Coordinates the application's flow, handling input and rendering the menu.
- **load_commands()**: (Assumed) Loads command data for the menu.
- **group_commands(commands)**: (Assumed) Groups commands into columns based on some criteria.
- **render_menu(columns, selected_row, selected_col)**: Displays the command menu in a structured format, highlighting the selected item.

## Known Issues
- **Blinking** occurs when an arrow key is pressed.
- Pressing **Enter** does not exit the menu cleanly.
- The CLI command does not always execute successfully.
- After running the CLI command, the application may be called multiple times due to the menu receiving background keyboard input.

## Release Notes
### Version 1.0.0
- Initial release of the Rich Menu Command Line Tool.
