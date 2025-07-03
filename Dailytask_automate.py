import pyautogui
import time
import datetime
import os

# --- Configuration ---
# Define the path where you want to save your daily note.
# Make sure the directory exists.
DAILY_NOTE_DIR = os.path.join(os.path.expanduser("~"), "Documents", "DailyNotes")
if not os.path.exists(DAILY_NOTE_DIR):
    os.makedirs(DAILY_NOTE_DIR) # Create the directory if it doesn't exist

# Define the search query for the browser task
BROWSER_SEARCH_QUERY = "What's new in Social Eagle today?"

# --- Helper Functions ---

def pause_and_print(message, duration=1):
    """Prints a message and pauses for a specified duration."""
    print(f"[STATUS] {message}")
    time.sleep(duration)

def open_notepad_and_write_note():
    """Automates opening Notepad, writing a daily note, and saving it."""
    pause_and_print("Starting Notepad automation...")

    # 1. Open Notepad using the Run dialog (Windows specific)
    pyautogui.hotkey('win', 'r') # Press Win + R to open Run dialog
    pause_and_print("Opened Run dialog.", 0.5)
    pyautogui.write('notepad') # Type 'notepad'
    pyautogui.press('enter') # Press Enter to launch Notepad
    pause_and_print("Notepad opened.", 2) # Give Notepad time to load

    # 2. Write the daily note
    today_date = datetime.date.today().strftime("%Y-%m-%d")
    note_content = f"Daily Note for {today_date}\n\n" \
                   f"Tasks completed:\n" \
                   f"- Task 1\n" \
                   f"- Task 2\n\n" \
                   f"Plans for tomorrow:\n" \
                   f"- Plan A\n" \
                   f"- Plan B\n\n" \
                   f"Thoughts:\n" \
                   f"Automated by PyAutoGUI at {datetime.datetime.now().strftime('%H:%M:%S')}"
    pyautogui.write(note_content, interval=0.01) # Type the note content with a small interval
    pause_and_print("Note content typed.", 1)

    # 3. Save the note
    pyautogui.hotkey('ctrl', 's') # Press Ctrl + S to open Save As dialog
    pause_and_print("Opened Save As dialog.", 1)

    # Construct the full file path
    file_name = f"Daily_Note_{today_date}.txt"
    full_file_path = os.path.join(DAILY_NOTE_DIR, file_name)

    # Type the full file path into the Save As dialog
    pyautogui.write(full_file_path)
    pause_and_print(f"Typed file path: {full_file_path}", 0.5)
    pyautogui.press('enter') # Press Enter to save
    pause_and_print("Note saved.", 2) # Give time for save operation

    # 4. Close Notepad
    pyautogui.hotkey('alt', 'f4') # Press Alt + F4 to close the active window
    pause_and_print("Notepad closed.", 1)
    print("Notepad automation finished.")

def open_browser_and_search():
    """Automates opening a browser, navigating to Google, and performing a search."""
    pause_and_print("Starting browser automation...")

    # 1. Open default web browser (e.g., Chrome, Edge, Firefox)
    # This command varies by OS. On Windows, 'start chrome' or 'start msedge'
    # can be used in cmd, but pyautogui's hotkey is more universal for opening default.
    # A simple way to open the default browser to a URL is to use os.startfile or webbrowser module.
    # However, since we want to demonstrate pyautogui, we'll simulate opening it.
    # For a more robust browser opening, consider:
    # import webbrowser
    # webbrowser.open('https://www.google.com')
    # time.sleep(5) # Wait for browser to open

    # For pyautogui demo, let's assume a browser shortcut is on the taskbar or desktop
    # Or we can use the Run dialog again for a common browser executable
    pyautogui.hotkey('win', 'r') # Open Run dialog
    pause_and_print("Opened Run dialog for browser.", 0.5)
    pyautogui.write('chrome') # Or 'msedge', 'firefox' depending on your default browser
    pyautogui.press('enter')
    pause_and_print("Browser opened (assuming Chrome/Edge).", 4) # Give browser time to load

    # 2. Navigate to Google (assuming browser is open and active)
    pyautogui.hotkey('ctrl', 'l') # Focus address bar (Ctrl+L is common for most browsers)
    pause_and_print("Focused address bar.", 0.5)
    pyautogui.write('https://www.google.com') # Type Google URL
    pyautogui.press('enter') # Go to Google
    pause_and_print("Navigated to Google.", 3) # Wait for Google to load

    # 3. Perform a search
    # Assuming Google search bar is visible and active, or we can click it
    # For simplicity, we'll assume it's ready for typing.
    pyautogui.write(BROWSER_SEARCH_QUERY, interval=0.05) # Type the search query
    pause_and_print(f"Typed search query: '{BROWSER_SEARCH_QUERY}'", 1)
    pyautogui.press('enter') # Press Enter to perform search
    pause_and_print("Search performed.", 3) # Wait for search results

    # You can add more steps here, e.g., scrolling, clicking links.
    # For now, we'll just leave the browser open to show the results.
    print("Browser automation finished.")

# --- Main Execution ---
if __name__ == "__main__":
    print("--- PyAutoGUI Daily Tasks Automation ---")
    print("Script will start in 5 seconds. Please do not touch your mouse or keyboard.")
    print("To stop the script at any time, quickly move your mouse to any screen corner.")
    time.sleep(5) # Give user time to prepare

    try:
        # Task 1: Automate daily note creation
        open_notepad_and_write_note()
        pause_and_print("\nMoving to next task in 3 seconds...", 3)

        # Task 2: Automate browser search
        open_browser_and_search()
        pause_and_print("\nAutomation complete!", 2)

    except pyautogui.FailSafeException:
        print("\n[STOPPED] PyAutoGUI Fail-Safe triggered. Script terminated.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")
        print("Please review the error message and check your script/environment.")

    print("\n--- Script End ---")