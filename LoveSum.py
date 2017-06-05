#
# Do Love Sum using Unicode Hangul System
#
# Copyright (c) 2017 by Jeong Deok Ho
# License: LGPL (see lgpl.txt)
#

# Unicode 한글
# 가 에서 시작해서 초성 이동 + 중성 이동 + 종성 이동을 거친다.
# <ex>
#     예 = 44032(가) + (ㅇ위치)*21*28 + (ㅖ위치)*28 + (''위치)
#     예 = 44032 + 11*21*28 + 7 * 28 + 0 = 50696
#

class LoveSum:
    name_1=""
    name_2=""
    reverse = False
    stroke_stage = list()
    stage0 = list()
    stage1 = list()
    stage2 = list()
    stage3 = list()
    # Class내 변수 지정 개념
    def set_names(self, name_1, name_2):
        self.name_1=name_1
        self.name_2=name_2

    def name_mix(self):
        tmp=list()
        for i in range(3):
            if not self.reverse:
                tmp.append(self.name_1[i])
                tmp.append(self.name_2[i])
            else:
                tmp.append(self.name_2[i])
                tmp.append(self.name_1[i])
        return tmp
    # 실제로 LoveSum을 진행하여 Stage들에 수 상태들을 저장
    def doLoveSum(self):
        dump = list()
        for i in range(3):
            if not self.reverse:
                dump.append(ord(self.name_1[i])-44032)
                dump.append(ord(self.name_2[i])-44032)
            else:
                dump.append(ord(self.name_2[i])-44032)
                dump.append(ord(self.name_1[i])-44032)
            self.stroke_stage+=[self.getStroke(dump[2*i]), self.getStroke(dump[2*i+1])]
            
        for i in range(5):
            self.stage0.append((self.stroke_stage[i]+self.stroke_stage[i+1])%10)
            
        for i in range(1,4,1):
            for j in range(5-i):
                # exec: 문자열 포멧의 명령을 실행
                exec("self.stage%d.append((self.stage%d[j]+self.stage%d[j+1])%%10)" % (i, i-1, i-1))
        
    def get_lovesum_result(self):
        return self.stage3[0]*10+self.stage3[1]
    
    # 초성, 중성, 종성 순으로 인덱싱, 획 수 대로 딕셔너리 처리
    # 이 둘을 바탕으로 계산한 한 글자의 획수 리턴
    def getStroke(self, wordDump):
        chosung = [
                    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ',
                    'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
                    'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ',
                    'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
                  ]
        jungsung = [
                    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ',
                    'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
                    'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ',
                    'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
                    'ㅣ'
                   ]
        jongsung = [
                    '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ',
                    'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ',
                    'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ',
                    'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                    'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ',
                    'ㅌ', 'ㅍ', 'ㅎ'
                   ]
        stroke_jaeum = {
                            '':0, 'ㄱ':2, 'ㄲ':4, 'ㄳ':4, 'ㄴ':2,
                            'ㄵ':5, 'ㄶ':5, 'ㄷ':3, 'ㄸ':6,'ㄹ':5,
                            'ㄺ':7, 'ㄻ':9, 'ㄼ':9, 'ㄽ':7, 'ㄾ':9,
                            'ㄿ':9, 'ㅀ':8, 'ㅁ':4, 'ㅂ':4, 'ㅃ':8,
                            'ㅄ':6, 'ㅅ':2, 'ㅆ':4, 'ㅇ':1, 'ㅈ':3,
                            'ㅉ':6, 'ㅊ':4, 'ㅋ':3, 'ㅌ':4, 'ㅍ':4,
                            'ㅎ':3
                        }

        stroke_moeum = {
                            'ㅏ':2, 'ㅐ':3, 'ㅑ':3, 'ㅒ':4, 'ㅓ':2,
                            'ㅔ':3, 'ㅕ':3, 'ㅖ':4, 'ㅗ':2, 'ㅘ':4,
                            'ㅙ':5, 'ㅚ':3, 'ㅛ':3, 'ㅜ':2, 'ㅝ':4,
                            'ㅞ':5, 'ㅟ':3, 'ㅠ':3, 'ㅡ':1, 'ㅢ':2,
                            'ㅣ':1
                         }
        stroke_chosung=stroke_jaeum[chosung[(wordDump//588)]]
        wordDump-=(wordDump//588)*588
        stroke_jungsung=stroke_moeum[jungsung[wordDump//28]]
        wordDump-=(wordDump//28)*28
        stroke_jongsung=stroke_jaeum[jongsung[wordDump]]
        # 10글자 이상일시 다시 0부터 시작함
        return (stroke_chosung+stroke_jungsung+stroke_jongsung)
    
    def clear(self):
        self.name_1=""
        self.name_2=""
        self.stroke_stage = []
        self.stage0 = []
        self.stage1 = []
        self.stage2 = []
        self.stage3 = []
        
''' 테스트 코드 '''
if __name__ == "__main__":
    game = LoveSum();
    game.set_names("정덕호", "윤예원")
    game.doLoveSum()
    print(game.stroke_stage)
    for i in range(4):
        exec("print(game.stage%d)" % i)
    print(game.get_lovesum_result(),"%")
