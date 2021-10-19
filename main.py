from tkinter import *
from colours import Colours
from threading import Timer


def main():
    """Creates a window with controls, and runs the window's main loop"""
    # Create a random colour list
    colours_list = Colours()

    # Callback for pause/resume button
    def on_pause_toggle():
        # Toggle the pause state
        colours_list.is_paused = not colours_list.is_paused
        # Update the button
        pause_toggle_button.config(text="Resume" if colours_list.is_paused else "Pause")
        # Restart the updating if not paused
        if not colours_list.is_paused:
            next_colours()

    window = Tk(className="Web-colours")

    # Heading
    Label(window, text="Web colours, with complementary colours!", font="arial", height=3, padx=15)\
        .grid(row=0, column=0, columnspan=2)

    # Buttons
    pause_toggle_button = Button(window, text="Pause", width=25, height=2, command=on_pause_toggle)
    pause_toggle_button.grid(row=1, column=0)
    randomise_button = Button(window, text="Randomise", width=25, height=2)
    randomise_button.grid(row=1, column=1)

    # Main colour
    Label(window, text="Main colour").grid(row=2, column=0, pady=20)
    main_colour_label = Label(window, font="Courier 16 bold", text="#000000", bg="#000000", fg="#ffffff", width=12, height=2, pady=20)
    main_colour_label.grid(row=3, column=0)

    # Complimentary colour
    Label(window, text="Complementary colour", pady=20).grid(row=2, column=1)
    comp_colour_label = Label(window, font="Courier 16 bold", text="#ffffff", bg="#ffffff", fg="#000000", width=12, height=2, pady=20)
    comp_colour_label.grid(row=3, column=1)

    # empty label for some extra spacing
    Label(window, text="").grid(row=4, column=0, columnspan=2)

    # Function to update the colours on a 1 second timer
    def next_colours():
        """Updates colours on a 1 second timer"""
        if not colours_list.is_paused:
            # Get the next colours
            main_colour, comp_colour = colours_list.next()
            # Update the main colour
            main_colour_label.config(text=main_colour, bg=main_colour, fg=comp_colour)
            # Update the complementary colour
            comp_colour_label.config(text=comp_colour, bg=comp_colour, fg=main_colour)
            # Repeat after a second
            Timer(1, next_colours).start()

    # Start it off
    next_colours()
    window.mainloop()


if __name__ == '__main__':
    main()
