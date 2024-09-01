# Import the necessary modules from tkinter for GUI creation and file handling dialogues.
from tkinter import *
from tkinter.filedialog import *

# Initial filename variable that will hold the path of the current file.
filename = None

# Function to create a new file.
def newFile():
    global filename  # Declare filename as global to modify it.
    filename = "Untitled"  # Set a default file name.
    text.delete(0.0, END)  # Clear the text widget.

# Function to save the current file.
def saveFile():
    global filename
    t = text.get(0.0, END)  # Get text content from the text widget.
    f = open(filename, 'w')  # Open the file in write mode.
    f.write(t)  # Write the text to the file.
    f.close()  # Close the file after writing.

# Function to save the current file with a new name.
def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')  # Open a save as dialog box.
    t = text.get(0.0, END)  # Get text from the text widget.
    try:
        f.write(t.rstrip())  # Write the trimmed text to the file.
    except:
        showerror(title="Oops!", message="Unable to save file...")  # Show error if save fails.

# Function to open an existing file.
def openFile():
    f = askopenfile(mode='r')  # Open a file dialog box to select a file to read.
    t = f.read()  # Read the file.
    text.delete(0.0, END)  # Clear the text widget.
    text.insert(0.0, t)  # Insert the read content into the text widget.

# Create the main window.
root = Tk()
root.title("text editor")  # Set the window title.
root.minsize(width=400, height=400)  # Set the minimum size of the window.
root.maxsize(width=400, height=400)  # Set the maximum size of the window.

# Create a Text widget for text editing.
text = Text(root, width=400, height=400)
text.pack()  # Pack the text widget into the root window.

# Create a menu bar.
menubar = Menu(root)
filemenu = Menu(menubar)
# Add menu items for various file operations.
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()  # Add a separator line.
filemenu.add_command(label="Quit", command=root.quit)  # Add quit option to the menu.
menubar.add_cascade(label="File", menu=filemenu)  # Add the File menu to the menubar.

root.config(menu=menubar)  # Configure the root window to display the menubar.
root.mainloop()  # Start the event loop to run the application.

