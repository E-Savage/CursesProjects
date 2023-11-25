import curses

def draw_tasks(stdscr, tasks):
    # Implement the logic to draw the list of tasks

    for task in tasks:
        
    # pass

def add_task(stdscr, tasks):
    # Implement the logic to add a new task
    pass

def toggle_task(stdscr, tasks, selected_task):
    # Implement the logic to toggle the completion status of a task
    pass

def delete_task(stdscr, tasks, selected_task):
    # Implement the logic to delete a task
    pass

def main(stdscr):
    # Set up initial tasks
    tasks = ["Task 1", "Task 2", "Task 3"]
    
    # Set up initial selected task
    selected_task = 0

    # Turn off cursor blinking
    curses.curs_set(0)

    # Main loop
    while True:
        # Clear the screen
        stdscr.clear()

        # Draw the list of tasks
        draw_tasks(stdscr, tasks)

        # Get user input
        key = stdscr.getch()

        # Handle user input
        if key == ord('q'):
            # Quit the application
            break
        elif key == ord('a'):
            # Add a new task
            add_task(stdscr, tasks)
        elif key == ord(' '):
            # Toggle completion status of the selected task
            toggle_task(stdscr, tasks, selected_task)
        elif key == ord('d'):
            # Delete the selected task
            delete_task(stdscr, tasks, selected_task)
        elif key == curses.KEY_UP and selected_task > 0:
            # Move the selection up
            selected_task -= 1
        elif key == curses.KEY_DOWN and selected_task < len(tasks) - 1:
            # Move the selection down
            selected_task += 1

if __name__ == "__main__":
    # Run the curses application
    curses.wrapper(main)
