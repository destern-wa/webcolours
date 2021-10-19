from tkinter import *
from colours import Colours
from threading import Timer


def main():
    """Creates a window with controls, and runs the window's main loop"""
    window = Tk(className="Web-colours")

    # Heading
    Label(window, text="Web colours, with complementary colours!", font="arial", height=3, padx=15)\
        .grid(row=0, column=0, columnspan=2)

    # Buttons
    Button(window, text="Start", width=25, height=2).grid(row=1, column=0)
    Button(window, text="Reset", width=25, height=2).grid(row=1, column=1)
    # Main colour
    Label(window, text="Main colour").grid(row=2, column=0, pady=20)
    main_colour_label = Label(window, font="Courier", text="#000000", bg="#000000", fg="#ffffff", width=12, height=2, pady=20)
    main_colour_label.grid(row=3, column=0)
    # Complimentary colour
    Label(window, text="Complementary colour", pady=20).grid(row=2, column=1)
    comp_colour_label = Label(window, font="Courier", text="#ffffff", bg="#ffffff", fg="#000000", width=12, height=2, pady=20)
    comp_colour_label.grid(row=3, column=1)
    # empty label for some extra spacing
    Label(window, text="").grid(row=4, column=0, columnspan=2)

    # Create a random colour list
    colours_list = Colours()

    # Function to update the colours on a 1 second timer
    def next_colours():
        # Get the next colours
        main_colour, comp_colour = colours_list.next()
        # Update the main colour
        main_colour_label.config(text=main_colour, bg=main_colour, fg=comp_colour)
        # Update the complementary colour
        comp_colour_label.config(text=comp_colour, bg=comp_colour, fg=main_colour)
        Timer(1, next_colours).start()

    # Start it off
    next_colours()

    window.mainloop()


if __name__ == '__main__':
    main()
