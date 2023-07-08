from tkinter import Tk, Button, Label, E, filedialog, messagebox


# window creation
window = Tk()
window.title("Shortcut Creator")
window.configure(background="#1abc9c")
window.resizable(False, False)


# global variables
file_list = []
lb_list = []

# functions
def file_get_box():
    global file_list

    box = filedialog.askopenfilenames(multiple = True)
    for i in range(len(box)):
        file_list.append(box[i]) # appends every *path* to file_list

    msg = messagebox.askquestion(title = "More?", message = "Would you like to choose more files from a different directory?")
    if msg == "yes":
        file_get_box()
    else:
        current_files()

def create_box():
    box = filedialog.asksaveasfilename(defaultextension = ".bat")
    with open(box, "a", encoding="ansi") as f: # creates and writes to batch file (ansi enconding is for cyrillic characters to work properly)
        f.write(construct_batch())

    current_files()
    
def construct_batch():  # most important function, constructs the .bat file
    global file_list    # theres 2 commands for every opened file: going to the files directory (cd...) and opening the file (start "" "path")

    res = "@chcp 1251\n" # this is for cyrillic characters to work properly (at least this makes russian work ¯\_(ツ)_/¯)
    for i in file_list:  # beautiful code incoming
        dir_path = i.split("/")
        dir_path.remove(dir_path[len(dir_path) - 1])
        dir_path = "/".join(dir_path) + "/"
        res += "cd \"" + dir_path + "\"\nstart \"\" \"" + i + "\"\n"

    file_list = []
    return res

def current_files(): # displays the currently selected files
    global file_list, lb_list

    for i in lb_list:
        i.destroy()
    
    lb_list.clear()

    for i in file_list:
        lb = Label(
                text = i, pady=5, background = "#1abc9c"
            )
        lb_list.append(lb)
        lb.pack()

def clear_files():
    global file_list

    file_list = []
    current_files()

# buttons

file_get_button = Button(
        text = "Choose files to open", command = file_get_box,
        background = "#1abc9c", pady = 10
    )
file_get_button.pack()

create_button = Button(
        text = "Create shortcut", command = create_box,
        background = "#1abc9c", pady = 10
    )
create_button.pack()

clear_button = Button(
        text = "Clear files", command = clear_files,
        background = "#1abc9c", pady = 10
    )
clear_button.pack()

# instruction labels

ins_label1 = Label(
        text = "1. Press the 'Choose files to open' button.\nChoose files from ONE directory, it will then ask if you want to choose more files from ANOTHER directory.",
        background = "#1abc9c", pady = 10
    )
ins_label1.pack()

ins_label2 = Label(
        text = "2. Press the 'Create shortcut' button.\nChoose a name for your shortcut and where you want to place it.\nIn the 'Name' field include only the name, without the extension",
        background = "#1abc9c", pady = 10
    )
ins_label2.pack()


# extra labels

current_list_label = Label(
        text = "Currently selected files: ",
        background = "#1abc9c",
        pady=25
    )
current_list_label.pack()

window.mainloop()