def main():
    men_name="조학근"
    girl_name="박홍주"
    dump = list()
    for i in range(6):
        if(i<3):
            dump.append(ord(men_name[i])-44032)
        else:
            dump.append(ord(girl_name[i%3])-44032)
    print( getLoveSum( getStroke(dump[0]), getStroke(dump[3]) ) )
    
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
    value_chosung = {
                        'ㄱ':2, 'ㄲ':4, 'ㄴ':2, 'ㄷ':3, 'ㄸ':6,
                        'ㄹ':5, 'ㅁ':4, 'ㅂ':4, 'ㅃ':8, 'ㅅ':2,
                        'ㅆ':4, 'ㅇ':1, 'ㅈ':3, 'ㅉ':6, 'ㅊ':4,
                        'ㅋ':3, 'ㅌ':4, 'ㅍ':4, 'ㅎ':3
                    }
    value_jungsung = {
                        'ㅏ':2, 'ㅐ':3, 'ㅑ':3, 'ㅒ':4, 'ㅓ':2,
                        'ㅔ':3, 'ㅕ':3, 'ㅖ':4, 'ㅗ':2, 'ㅘ':4,
                        'ㅙ':5, 'ㅚ':3, 'ㅛ':3, 'ㅜ':2, 'ㅝ':4,
                        'ㅞ':5, 'ㅟ':3, 'ㅠ':3, 'ㅡ':1, 'ㅢ':2,
                        'ㅣ':1
                     }
    value_jongsung = {
                        '':0, 'ㄱ':2, 'ㄲ':4, 'ㄳ':4, 'ㄴ':2,
                        'ㄵ':5, 'ㄶ':5, 'ㄷ':3, 'ㄹ':5, 'ㄺ':7,
                        'ㄻ':9, 'ㄼ':9, 'ㄽ':7, 'ㄾ':9, 'ㄿ':9,
                        'ㅀ':8, 'ㅁ':4, 'ㅂ':4, 'ㅄ':6, 'ㅅ':2,
                        'ㅆ':4, 'ㅇ':1, 'ㅈ':3, 'ㅊ':4, 'ㅋ':3,
                        'ㅌ':4, 'ㅍ':4, 'ㅎ':3
                    }
    stroke_chosung=value_chosung[chosung[(wordDump//588)]]
    wordDump-=(wordDump//588)*588
    stroke_jungsung=value_jungsung[jungsung[wordDump//28]]
    wordDump-=(wordDump//28)*28
    stroke_jongsung=value_jongsung[jongsung[wordDump]]
    return (stroke_chosung+stroke_jungsung+stroke_jongsung)
    
def getLoveSum(stroke1, stroke2):
    return (stroke1+stroke2)%10

def getResult(stroke1, stroke2):
    return stroke1*10+stroke2

''' 테스트 코드 '''
main()
print(getResult(7, 5))
