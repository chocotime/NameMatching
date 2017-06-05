'''
Handle Python version 2.x and 3.x
'''
try:
    import Tkinter as tk
    from Tkinter import messagebox
except ImportError:
    print("Version : 3.x --> try 't'kinter")
    import tkinter as tk
    from tkinter import messagebox
    
from PIL import Image, ImageTk
import sys
import LoveSum

# LoveSum 모듈을 사용하기 위해 객체 생성
game = LoveSum.LoveSum()

class GetNameFrame(tk.Frame):
    # GetNameFrame 객체 생성시 자동으로 실행되는 함수
    def __init__(self, parent, w, h):
        get_name_labels=[]
        tk.Frame.__init__(self, parent, width=w, height=h) # tk.Frame을 load하여 이 프레임을 참조(사용)
        self.config(bg = "Misty Rose") # bg = Background
        
        self.get_name1 = tk.Entry(self) #궁합을 볼 첫번 째 사람 입력하는 창 만들어줌
        self.get_name1.config(justify='center') # 문자 중앙 정렬 
        self.get_name1.config(bg="Light Sky Blue", fg="White") # fg = foreground : for font
        self.get_name1.config(bd=0, font=("a어린이신문", 15)) # bd = entry 창 border 크기
        
        #이름을 입력 창을 클릭 했을 때 공백을 띄우도록 설정
        self.get_name1.bind('<FocusIn>', self.in_entry1) 
        #이름을 입력 창에서 커서를 뗐을 때 다시 이름을 입력을 띄우도록 설정
        self.get_name1.bind('<FocusOut>', self.out_entry1)
        # 초기에 써져있을 문장
        self.get_name1.insert(0, "이름을 입력")
        self.get_name1.config(width=9)
        self.get_name1.place(x=65, y=10)
        
        get_name_labels.append(tk.Label(self, text="님이"))
        get_name_labels[0].config(bg="Misty Rose", fg="Medium Purple")
        get_name_labels[0].config(font=("a어린이신문", 15))
        get_name_labels[0].place(x=155, y=10)
        
        #궁합을 볼 두번 째 사람 입력하는 창을 만들어줌 ( 첫번째 입력창과 설정 동일 )
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
        
        #궁합을 확인할 수 있는 버튼을 만들어줌
        self.match_btn=tk.Button(self, text=" [ 궁합 보기 ] ")
        self.match_btn.config(font=("a블랙B", 16))
        self.match_btn.config(bg="Misty Rose", fg="Hot Pink")
        self.match_btn.config(activebackground="Misty Rose")
        self.match_btn.config(borderwidth=0, relief="solid")
        self.match_btn.config(command=self.match)
        self.match_btn.place(x=125,y=70)
        
    # 첫 번째 입력창을 마우스로 클릭했을 때 "이름을 입력" 상태라면 공백으로 만들어줌  
    def in_entry1(self, event):
        if self.get_name1.get() == "이름을 입력":
           self.get_name1.delete(0, "end")
           self.get_name1.insert(0, '')

    # 입력창에서 마우스를 뗐을 때 아무 것도 입력하지 않은 상태라면 "이름을 입력"으로 만듬
    def out_entry1(self, event):
        if self.get_name1.get() == '':
            self.get_name1.insert(0, "이름을 입력")
    # 위와 동일
    def in_entry2(self, event):
        if self.get_name2.get() == "이름을 입력":
           self.get_name2.delete(0, "end")
           self.get_name2.insert(0, '')
    # 위와 동일
    def out_entry2(self, event):
        if self.get_name2.get() == '':
            self.get_name2.insert(0, "이름을 입력")
    # [ 궁합보기 ] 버튼을 누르면 이름 입력 검사 , 출력함수 부르기, 궁합보기 버튼 제거
    def match(self):
        global name_1, name_2
        if len(self.get_name1.get()) !=3:
            messagebox.showwarning("< 이름 입력 오류 >", "3자 이름을 입력해주세요.")
        else:
            if len(self.get_name2.get()) !=3:
                messagebox.showwarning("< 이름 입력 오류 >", "3자 이름을 입력해주세요.")
            else:
                name_1=self.get_name1.get()
                name_2=self.get_name2.get()
                for i in range(3):
                    if ord(name_1[i])<44032 or ord(name_1[i]) > 55203 :
                        messagebox.showwarning("< 이름 입력 오류 >", "한글로만 입력해주세요.")
                        return None
                    elif ord(name_2[i])<44032 or ord(name_2[i]) > 55203 :
                        messagebox.showwarning("< 이름 입력 오류 >", "한글로만 입력해주세요.")
                        return None
                show_zone.showLoveSum()
                self.match_btn.destroy()
    # GetNameFrame을 초기화
    def clearFrame(self):
        global name_1, name_2 # 전역변수에 접근
        name_1=""
        name_2=""
        self.get_name1.delete(0, "end")
        self.get_name2.delete(0, "end")
        # 제거됬던 [ 궁합보기 ] 버튼도 추가
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

    # 이름 궁합 하는 과정을 하트로 띄워줌 
    def showLoveSum(self):
        self.clearFrame()
        global name_1, name_2
        name_tags=[]
        stroke_hrts=[]
        lovesum_hrts=[]
        
        game.set_names(name_1, name_2)
        game.doLoveSum()
        #각각 두 이름을 섞은 채로 화면에 띄워지도록 LoveSum모듈에서 섞어준 것을 받아옴
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
            stroke_hrts[i].config(text=str(game.stroke_stage[i]%10))
            stroke_hrts[i].config(bg="Lavender Blush", fg="White")
            stroke_hrts[i].config(compound=tk.CENTER)
            stroke_hrts[i].place(x=20+(60*i),y=80)
            stroke_hrts[i].update()
        pt=0 # 행에 대한 index를 맡음 
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
            pt+=5-i # 행이 증가할 때 마다 index를 증가시킴
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
        #궁합 다시보기 버튼을 만들어줌
        rematch_btn = tk.Button(self, text="궁합 다시 보기")
        rematch_btn.config(font=("a블랙B", 16))
        rematch_btn.config(bg="Light Sky Blue", fg="White")
        rematch_btn.config(activebackground="Light Sky Blue")
        rematch_btn.config(activeforeground="White")
        rematch_btn.config(borderwidth=0.2, relief="solid")
        rematch_btn.config(command=self.replay_matching)
        rematch_btn.place(x=0,y=30)
        #반대로 궁합보기 버튼을 만들어줌
        reverse_btn = tk.Button(self, text="반대로 궁합 보기")
        reverse_btn.config(font=("a블랙B", 16))
        reverse_btn.config(bg="Light Sky Blue", fg="White")
        reverse_btn.config(activebackground="Light Sky Blue")
        reverse_btn.config(activeforeground="White")
        reverse_btn.config(borderwidth=0.2, relief="solid")
        reverse_btn.config(command=self.reverse_matching)
        reverse_btn.place(x=200,y=30)

    # 다시 할때 reverse값은 default값으로 되돌림
    # 이 프레임(showFrame)과 이름입력 프레임(getFrame) 초기화
    def replay_matching(self):
        game.reverse=False
        get_zone.clearFrame()
        show_zone.clearFrame()

    #반대로 궁합보기 : LoveSum 모듈의 reverse값 반전, 이름 입력된 것 스위치 작업
    def reverse_matching(self):
        if game.reverse:
            game.reverse=False
        else:
            game.reverse=True

        tmp=get_zone.get_name1.get()
        get_zone.get_name1.delete(0, "end")
        get_zone.get_name1.insert(0, get_zone.get_name2.get())
        get_zone.get_name2.delete(0, "end")
        get_zone.get_name2.insert(0, tmp)
        get_zone.get_name1.update()
        get_zone.get_name2.update()
        show_zone.showLoveSum()
        
# 주 프로그램 창       
main_window = tk.Tk()
main_window.title("< 이름 궁합 >")
# 조절 안되게
main_window.resizable(width="False", height="False")
main_window.geometry("400x600")

try:
    main_window.iconbitmap("focus_heart.ico")
except:
    print("메인 윈도우 아이콘을 불러올 수 없습니다.")
    sys.exit(1)
# main_window 크기 바꾼 상태로 업데이트
main_window.update()

main_width=main_window.winfo_width()
main_height=main_window.winfo_height()

# Image Load and Resize, changing Tk image format
heart_png=Image.open("heart.png")
heart_png = heart_png.resize((50, 50), Image.ANTIALIAS)
focus_heart_png=Image.open("focus_heart.png")
focus_heart_png=focus_heart_png.resize((60, 60), Image.ANTIALIAS)
stage_hrt=ImageTk.PhotoImage(heart_png)
result_hrt=ImageTk.PhotoImage(focus_heart_png)

# Global Name
name_1=""
name_2=""

# Frame 객체들을 생성
show_zone = ShowMatchingFrame(main_window, main_width, (main_height/6)*4) # 4/6
get_zone = GetNameFrame(main_window, main_width, main_height/6) # 1/6
replay_zone = ReplayBtnsFrame(main_window, main_width, main_height/6) # 1/6

# Main Frame에 Pack방식으로 합침
get_zone.pack()
show_zone.pack()
replay_zone.pack()

# 종료버튼을 누를때까지 유지
main_window.mainloop()
