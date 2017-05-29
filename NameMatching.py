'''
44032 ( : '가') + 초성 * 21 ( 중성 갯수 ) * 28 ( 종성 갯수 ) + 중성 * 28 + 종성 
'''
def init():
    men_name=input("남자 이름 입력 : ")
    girl_name=input("여자 이름 입력 : ")
    # 이름 순서 바꾸기
    reverse = False
    main_process(men_name, girl_name, reverse)
    
def main_process(men_name, girl_name, reverse):
    dump = list()
    stage_a = list()
    stage_b = list()
    for i in range(3):
        if not reverse:
            dump.append(ord(men_name[i])-44032)
            dump.append(ord(girl_name[i])-44032)
        else:
            dump.append(ord(girl_name[i])-44032)
            dump.append(ord(men_name[i])-44032)
        stage_a+=[getStroke(dump[2*i]), getStroke(dump[2*i+1])]
        
    print(stage_a)
    
    for i in range(4):
        for j in range(5-i):
            if(i&1):
                tmp = getLoveSum(stage_b[j], stage_b[j+1])
                stage_a.append(tmp)
            else:
                tmp = getLoveSum(stage_a[j], stage_a[j+1])
                stage_b.append(tmp)
        if(i&1):
            stage_b=[]
            print(stage_a)
        else:
            stage_a=[]
            print(stage_b)

    print(" 결과 : %d " % getResult(stage_a[0], stage_a[1]))    
    
def getStroke(wordDump):
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
    return (stroke_chosung+stroke_jungsung+stroke_jongsung)
    
def getLoveSum(stroke1, stroke2):
    return (stroke1+stroke2)%10

def getResult(stroke1, stroke2):
    return stroke1*10+stroke2

''' 테스트 코드 '''
init()
