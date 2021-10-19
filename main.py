from tkinter import *


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
    Label(window, font="Courier", text="#000000", bg="#000000", fg="#ffffff", width=12, height=2, pady=20).grid(row=3, column=0)
    # Complimentary colour
    Label(window, text="Complementary colour", pady=20).grid(row=2, column=1)
    Label(window, font="Courier", text="#ffffff", bg="#ffffff", fg="#000000", width=12, height=2, pady=20).grid(row=3, column=1)
    # empty label for some extra spacing
    Label(window, text="").grid(row=4, column=0, columnspan=2)

    window.mainloop()


if __name__ == '__main__':
    main()
