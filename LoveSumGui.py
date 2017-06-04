'''
Handle Python version 2.x and 3.x
'''
try:
    import Tkinter as tk
except ImportError:
    print("Version : 3.x --> try 't'kinter")
    import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import time
import sys
import LoveSum
game = LoveSum.LoveSum()

class GetNameFrame(tk.Frame):
    def __init__(self, parent, w, h):
        get_name_labels=[]
        tk.Frame.__init__(self, parent, width=w, height=h)
        self.config(bg = "Misty Rose")
        
        self.get_name1 = tk.Entry(self)
        self.get_name1.config(justify='center')
        self.get_name1.config(bg="Light Sky Blue", fg="White")
        self.get_name1.config(bd=0, font=("a어린이신문", 15))
        self.get_name1.bind('<FocusIn>', self.in_entry1)
        self.get_name1.bind('<FocusOut>', self.out_entry1)
        self.get_name1.insert(0, "이름을 입력")
        self.get_name1.config(width=9)
        self.get_name1.place(x=65, y=10)
        
        get_name_labels.append(tk.Label(self, text="님이"))
        get_name_labels[0].config(bg="Misty Rose", fg="Medium Purple")
        get_name_labels[0].config(font=("a어린이신문", 15))
        get_name_labels[0].place(x=155, y=10)
        
        self.get_name2 = tk.Entry(self)
        self.get_name2.config(justify='center')
        self.get_name2.config(bg="Light Sky Blue", fg="White")
        self.get_name2.config(bd=0, font=("a어린이신문", 15))
        self.get_name2.bind('<FocusIn>', self.in_entry2)
        self.get_name2.bind('<FocusOut>', self.out_entry2)
        self.get_name2.insert(0, "이름을 입력")
        self.get_name2.config(width=9)
        self.get_name2.place(x=205, y=10)

        get_name_labels.append(tk.Label(self, text="님을"))
        get_name_labels[1].config(bg="Misty Rose", fg="Medium Purple")
        get_name_labels[1].config(font=("a어린이신문", 15))
        get_name_labels[1].place(x=295, y=10)

        get_name_labels.append(tk.Label(self, text="얼마나 좋아할까요?"))
        get_name_labels[2].config(bg="Misty Rose", fg="Medium Purple")
        get_name_labels[2].config(font=("a어린이신문", 15))
        get_name_labels[2].place(x=130, y=45)
        
        self.match_btn=tk.Button(self, text=" [ 궁합 보기 ] ")
        self.match_btn.config(font=("a블랙B", 16))
        self.match_btn.config(bg="Misty Rose", fg="Hot Pink")
        self.match_btn.config(activebackground="Misty Rose")
        self.match_btn.config(borderwidth=0, relief="solid")
        self.match_btn.config(command=self.match)
        self.match_btn.place(x=125,y=70)
        
    def in_entry1(self, event):
        if self.get_name1.get() == "이름을 입력":
           self.get_name1.delete(0, "end")
           self.get_name1.insert(0, '')
    def out_entry1(self, event):
        if self.get_name1.get() == '':
            self.get_name1.insert(0, "이름을 입력")
            
    def in_entry2(self, event):
        if self.get_name2.get() == "이름을 입력":
           self.get_name2.delete(0, "end")
           self.get_name2.insert(0, '')
    def out_entry2(self, event):
        if self.get_name2.get() == '':
            self.get_name2.insert(0, "이름을 입력")

    def match(self):
        global name_1, name_2
        name_1=self.get_name1.get()
        name_2=self.get_name2.get()
        show_zone.showLoveSum()
        self.match_btn.destroy()
        
    def clearFrame(self):
        global name_1, name_2
        name_1=""
        name_2=""
        self.get_name1.delete(0, "end")
        self.get_name2.delete(0, "end")
        self.match_btn=tk.Button(self, text=" [ 궁합 보기 ] ")
        self.match_btn.config(font=("a블랙B", 16))
        self.match_btn.config(bg="Misty Rose", fg="Hot Pink")
        self.match_btn.config(activebackground="Misty Rose")
        self.match_btn.config(borderwidth=0, relief="solid")
        self.match_btn.config(command=self.match)
        self.match_btn.place(x=125,y=70)
        
class ShowMatchingFrame(tk.Frame):
    def __init__(self, parent, w, h):
        tk.Frame.__init__(self, parent, width=w, height=h)
        self.config(bg = "Lavender Blush")
        
    def clearFrame(self):
        for widget in self.winfo_children():
            widget.destroy()
        game.clear()
    def reverse_matching(self):
        if game.reverse:
            game.reverse=False
        else:
            game.reverse=True
        self.showLoveSum()
        
    def replay_matching(self):
        game.reverse=False
        get_zone.clearFrame()
        self.clearFrame()
        
    def showLoveSum(self):
        self.clearFrame()
        global name_1, name_2
        name_tags=[]
        stroke_hrts=[]
        lovesum_hrts=[]
        
        game.set_names(name_1, name_2)
        game.doLoveSum()
        name_mixed = game.name_mix()
        for i in range(6):
            name_tags.append(tk.Label(self, text=name_mixed[i]))
            name_tags[i].config(font=("a블랙B", 16))
            name_tags[i].config(bg="Lavender Blush")
            if i%2:
                name_tags[i].config(fg="Salmon")
            else:
                name_tags[i].config(fg="Cornflower Blue")
            name_tags[i].place(x=30+(60*i),y=30)
            name_tags[i].update()
            stroke_hrts.append(tk.Label(self, image=stage_hrt))
            stroke_hrts[i].image=stage_hrt
            stroke_hrts[i].config(font=("a어린이신문", 20))
            stroke_hrts[i].config(text=str(game.stroke_stage[i]))
            stroke_hrts[i].config(bg="Lavender Blush", fg="White")
            stroke_hrts[i].config(compound=tk.CENTER)
            stroke_hrts[i].place(x=20+(60*i),y=80)
            stroke_hrts[i].update()
        pt=0
        # pt = .. i=0, 0 | i=1, 5 | i=2, 9 -> i=
        for i in range(4):
            for j in range(5-i):
                lovesum_hrts.append(tk.Label(self, image=stage_hrt))
                lovesum_hrts[pt+j].image=stage_hrt
                lovesum_hrts[pt+j].config(font=("a어린이신문", 20))
                exec("lovesum_hrts[pt+j].config(text=game.stage%d[%d])" % (i, j))
                lovesum_hrts[pt+j].config(bg="Lavender Blush", fg="White")
                lovesum_hrts[pt+j].config(compound=tk.CENTER)
                lovesum_hrts[pt+j].place(x=(50+30*i)+(60*j),y=130+50*i)
                lovesum_hrts[pt+j].update()
            pt+=5-i

        main_hrt=tk.Label(self, image=result_hrt)
        main_hrt.image=result_hrt
        main_hrt.config(font=("a블랙B", 15))
        main_hrt.config(text=game.get_lovesum_result())
        main_hrt.config(compound=tk.CENTER)
        main_hrt.config(bg="Lavender Blush", fg="White")
        main_hrt.place(x=165, y=335)
        main_hrt.update()
        
class ReplayBtnsFrame(tk.Frame):
    def __init__(self, parent, w, h):
        tk.Frame.__init__(self, parent, width=w, height=h)
        self.config(bg = "Misty Rose")
        
        rematch_btn = tk.Button(self, text="궁합 다시 보기")
        rematch_btn.config(font=("a블랙B", 16))
        rematch_btn.config(bg="Light Sky Blue", fg="White")
        rematch_btn.config(activebackground="Light Sky Blue")
        rematch_btn.config(activeforeground="White")
        rematch_btn.config(borderwidth=0.2, relief="solid")
        rematch_btn.config(command=show_zone.replay_matching)
        rematch_btn.place(x=0,y=30)

        reverse_btn = tk.Button(self, text="반대로 궁합 보기")
        reverse_btn.config(font=("a블랙B", 16))
        reverse_btn.config(bg="Light Sky Blue", fg="White")
        reverse_btn.config(activebackground="Light Sky Blue")
        reverse_btn.config(activeforeground="White")
        reverse_btn.config(borderwidth=0.2, relief="solid")
        reverse_btn.config(command=show_zone.reverse_matching)
        reverse_btn.place(x=200,y=30)
        
main_window = tk.Tk()
main_window.title("< 이름 궁합 >")
main_window.resizable(width="False", height="False")
main_window.geometry("400x600")
main_window["bg"] = "Dim Gray"

try:
    main_window.iconbitmap("focus_heart.ico")
except:
    print("메인 윈도우 아이콘을 불러올 수 없습니다.")
    sys.exit(1)

main_window.update()
def test(event):
    global name_1, name_2
    name_1="정덕호"
    name_2="윤예원"
    print("hello")
    
main_window.bind("1", test)

main_width=main_window.winfo_width()
main_height=main_window.winfo_height()
# Image Load
heart_png=Image.open("heart.png")
heart_png = heart_png.resize((50, 50), Image.ANTIALIAS)
focus_heart_png=Image.open("focus_heart.png")
focus_heart_png=focus_heart_png.resize((60, 60), Image.ANTIALIAS)
stage_hrt=ImageTk.PhotoImage(heart_png)
result_hrt=ImageTk.PhotoImage(focus_heart_png)
# Global Name
name_1=""
name_2=""

show_zone = ShowMatchingFrame(main_window, main_width, (main_height/6)*4)
get_zone = GetNameFrame(main_window, main_width, main_height/6)
replay_zone = ReplayBtnsFrame(main_window, main_width, main_height/6)

get_zone.pack()
show_zone.pack()
replay_zone.pack()

main_window.mainloop()
