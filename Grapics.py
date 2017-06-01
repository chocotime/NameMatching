'''
Handle Python version 2.x and 3.x
'''
try:
    import Tkinter as tk
except ImportError:
    print("Version : 3.x --> try 't'kinter")
    import tkinter as tk

class MainWindow:
    def __init__(self, window):
        main_width=window.winfo_width()
        main_height=window.winfo_height()
        self.get_frame(window, main_width, main_height*0.25).pack()
        self.show_frame(window, main_width, main_height*0.60).pack()
        self.replay_frame(window, main_width, main_height*0.15).pack()

    def get_frame(self, parent, width, height):
        get_name_zone = tk.Frame(parent, width=width, height=height)
        get_name_zone["bg"] = "red"
        return get_name_zone
    
    def show_frame(self, parent, width, height):
        show_matching_zone = tk.Frame(parent, width=width, height=height)
        show_matching_zone["bg"] = "yellow"
        return show_matching_zone
    
    def replay_frame(self, parent, width, height):
        replay_btns_zone = tk.Frame(parent, width=width, height=height)
        replay_btns_zone["bg"] = "green"
        return replay_btns_zone

main_window = tk.Tk()
main_window.geometry("450x900")
main_window.update()

main_window["bg"] = "Dim Gray"
app = MainWindow(main_window)

main_window.mainloop()
