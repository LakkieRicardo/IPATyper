import curses, json, sys, os.path, pyperclip

def QueryWord(word_list: list, search_term: str) -> list:
    # Ignore case
    search_term = search_term.lower()
    result = []
    for entry in word_list:
        if search_term in entry["symbol"].lower() or search_term in entry["name"].lower():
            result.append(entry)
            continue
        if "terms" in entry:
            for term in entry["terms"].split(" "):
                if search_term in term.lower():
                    result.append(entry)
                    break
    
    return result

# Function to run the user interface
def SearchPrompt(stdscr, word_list: list):

    # Initialize colors
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.init_pair(2, curses.COLOR_WHITE, -1)
    curses.init_pair(3, curses.COLOR_BLUE, -1)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_WHITE)

    stdscr.clear()

    def RenderPrompt(y):
        stdscr.addstr(y, 0, " > ", curses.color_pair(1))

    def GetEntryString(entry: dict) -> str:
        name = entry["name"]
        symbol = entry["symbol"]
        return f"[{symbol}] ({name})"

    def RenderQueryResultsEllipsis(y, x):
        stdscr.addstr(y, x, "...", curses.color_pair(1))

    def RenderQueryResults(start_y, start_x, result_list):
        for i, result in enumerate(result_list):
            stdscr.addstr(start_y + i, start_x, GetEntryString(result), curses.color_pair(3))
            stdscr.clrtoeol()
            if i == 4:
                RenderQueryResultsEllipsis(start_y + 5, start_x)
                stdscr.clrtoeol()
                break

    def RenderSelection(selection_idx: int, old_selection_idx: int, last_results: list, start_y: int):
        if selection_idx != -1:
            # Update the new selection
            result = GetEntryString(last_results[selection_idx])
            # Adding an extra 1 in the Y to account for the prompt
            stdscr.addstr(start_y + selection_idx + 1, 3, f">{result}", curses.color_pair(4))
            stdscr.clrtoeol()

        if old_selection_idx < 5:
            # Reset the old selection
            last_result = GetEntryString(last_results[old_selection_idx])
            stdscr.addstr(start_y + old_selection_idx + 1, 3, f" {last_result}", curses.color_pair(3))
        elif old_selection_idx == 5:
            # Clear arrow and draw the ellipsis
            stdscr.addch(start_y + old_selection_idx + 1, 3, " ")
            RenderQueryResultsEllipsis(start_y + old_selection_idx + 1, 4)
        else:
            # Move to the old selection so that it gets cleared using clrtoeol
            stdscr.addch(start_y + old_selection_idx + 1, 3, " ")
        stdscr.clrtoeol()

    # Checks if we can fit a new query line onto the screen. If false, the screen should be cleared first
    def CheckBoundsForNewQuery():
        curses.update_lines_cols()
        return y_idx + 7 < curses.LINES

    search_term = ""
    y_idx = 1
    RenderPrompt(y_idx)
    last_results = [] # Used to keep track of how many results are currently displayed and to update selected item
    selection_idx = -1

    ALLOWED_CHARS = "()-"
    # Main user input loop
    while True:
        user_text = stdscr.getkey()
        # Used to determine whether the selection is going off screen
        curses.update_lines_cols()
        if user_text == "\n":
            word_list = QueryWord(word_list, search_term)
            y_idx += min(6, len(last_results)) # Move past result items
            y_idx += 2 # Padding between searches
            last_results = [] # Ignore what was displayed before
            search_term = ""
            selection_idx = -1

            # Clear the screen if we are going to go past the boundaries
            if not CheckBoundsForNewQuery():
                stdscr.clear()
                y_idx = 1
            
            RenderPrompt(y_idx)
        elif user_text == "\x1b" and len(last_results) > 0: # Escape key
            old_selection_idx = selection_idx
            selection_idx = -1
            RenderSelection(selection_idx, old_selection_idx, last_results, y_idx)
        elif user_text == "\t":
            if selection_idx == -1:
                # Display query results
                query_result = QueryWord(word_list, search_term)
                RenderQueryResults(y_idx + 1, 4, query_result)
                stdscr.clrtobot()
                last_results = query_result
            else:
                # Copy query results selection to clipboard
                selection_symbol = last_results[selection_idx]["symbol"]
                pyperclip.copy(selection_symbol)
        elif user_text == "\x08" and len(search_term) > 0: # If backspace is pressed and the seach term isn't blank
            search_term = search_term[:-1]
        elif user_text.isalnum() or user_text in ALLOWED_CHARS:
            search_term += user_text
        # Down arrow, increase selection idx
        # Only move down if within selection and not off screen
        elif user_text == "KEY_C2" and selection_idx < len(last_results) - 1 and selection_idx + y_idx + 3 < curses.LINES:
            old_selection_idx = selection_idx
            selection_idx += 1
            RenderSelection(selection_idx, old_selection_idx, last_results, y_idx)
        elif user_text == "KEY_A2" and selection_idx > -1: # Up arrow, decrease selection idx
            old_selection_idx = selection_idx
            selection_idx -= 1
            RenderSelection(selection_idx, old_selection_idx, last_results, y_idx)
        stdscr.addstr(y_idx, 3, f"{search_term}", curses.color_pair(2))
        stdscr.clrtoeol()


if __name__ != "__main__":
    print("Run this as a main file")
    sys.exit(1)

if not os.path.exists("ipa-typer.json"):
    print("The ipa-typer.json file must be included to run!")
    sys.exit(2)

with open("ipa-typer.json", "r", encoding="utf-8") as dictionary_file:
    word_list = json.load(dictionary_file)
    
    curses.wrapper(lambda stdscr : SearchPrompt(stdscr, word_list))