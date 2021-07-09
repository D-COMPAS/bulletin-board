#数字列から■で構成された文字に変換する
def numprint(numlist):
    numchars =[
"""
■■■■■■■■
■      ■
■      ■
■      ■
■■■■■■■■
""",
"""
       ■
       ■
       ■
       ■
       ■
""",
"""
■■■■■■■■
       ■
■■■■■■■■
■       
■■■■■■■■
""",
"""
■■■■■■■■
       ■
■■■■■■■■
       ■
■■■■■■■■
""",
"""
■      ■
■      ■
■■■■■■■■
       ■
       ■
""",
"""
■■■■■■■■
■       
■■■■■■■■
       ■
■■■■■■■■
""",
"""
■■■■■■■■
■       
■■■■■■■■
■      ■
■■■■■■■■
""",
"""
■■■■■■■■
■      ■
■      ■
       ■
       ■
""",
"""
■■■■■■■■
■      ■
■■■■■■■■
■      ■
■■■■■■■■
""",
"""
■■■■■■■■
■      ■
■■■■■■■■
       ■
■■■■■■■■
""",
"""
        
    ■   
        
    ■   
        
"""
]
    #配列セットアップ
    for i in range(len(numchars)):
        #ヘッダーとフッターを削除して改行ごとに配列化
        numchars[i] = numchars[i].split('\n')[1:6]

    tex = ""
    for i in range(5):
        for j in numlist:

            tex += str(numchars[j][i])+'  '
        tex +='\n'

    return tex


import time,datetime
import os
today = datetime.datetime.fromtimestamp(time.time())
#print(today.strftime('%Y %m %d %I:%M:%S %p'))

t = list(time.strftime('%I'))
t.append('10')
t += list(time.strftime('%M'))
t = [int(i) for i in t]

t =[0,0,10,0,0]
count = 14*60+30#時間
dec = 10
for i in range(count)[::-1]:
    min = int(i/60)

    if min >9:
        t[0] = int(min /dec)
        t[1] = int(min%dec)
    else:
        t[0] = 0
        t[1] = min

    sec = int(i%60)
    if sec >9:
        t[3] = int(sec / dec)
        t[4] = int(sec % dec)
    else:
        t[3] = 0
        t[4] = sec
    
    os.system('cls')
    print(numprint(t))
    time.sleep(1)
    
else:
    os.system('cls')
    print(numprint(t).replace('■','□'))
        
    




