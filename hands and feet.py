# coding: utf-8
import time
import random
allwords=['蘇貞昌','牛奶','母老虎','馬英九','美猴王','外星人','賽車','感冒','拉肚子','空姐','飛行員','水龍頭','鬥牛','相撲','拔河','抬槓','騎馬打仗','口試'
,'法式接吻','理髮','馬殺雞','比手畫腳','導盲犬','打網球','協力車','抓小偷','躲迷藏','接力賽跑','兔子舞','探戈','疊羅漢','黑白猜','兩人三腳','老漢推車','斷背山','你丟我撿'
,'啦啦隊','馬戲表演','跳火圈','橄欖球','殺價','超車','划拳','偷窺','潑冷水','碰釘子','吃閉門羹','婚禮','人體彩繪','阿魯巴','仰臥起坐','蹺蹺板','龜兔賽跑','合唱團',
'英雄救美','落井下石','波浪舞','袋鼠','鐵達尼號','雙胞胎','腳底按摩','人工呼吸','出人頭地','圓頂方踵','斬草除根','過眼雲煙','哄堂大笑','放下屠刀立地成佛','昏天黑地',
'飲水思源','胸懷千里','白馬王子','垂涎三尺','百折不撓','擎天憾地','海闊天空','愚公移山','才高八斗','雞飛狗跳','嘔心絞腦','萬紫千紅','張牙舞爪','一暴十寒','手不釋卷',
'眼波如水','圓通大師','隨風轉舵','望洋興嘆','無懈可擊','花枝招展','鳶飛魚躍','一絲不苟','搔首弄姿','羊入虎口','黑白分明'
,'三頭六臂','雨過天青','三緘其口','半斤八兩','畫餅充飢','怒髮衝冠','鳥語花香','一石二鳥','環肥燕瘦','上下其手','一波三折','有口難言','身懷六甲','十全十美呼風喚雨']
num = int(input('有多少組玩家\n'))
guessword = []
correct = []
for i in range(0,num ):
    guessword.append([])
    correct.append(0)
wordnum=int(input('要幾道題目\n'))
gametime=int(input('要計時多少秒\n'))
for i in range(0,num):
    for k in range(0,wordnum):
        word=random.randint(0,108)
        guessword[i].append(allwords[word])
for i in range(0,num):
    start = time.time()
    for k in range(0,wordnum):
        print (('%d.%s')%(k+1,guessword[i][k]))
        end = time.time()
        sec = end-start
        if (gametime-10<=sec<=gametime):
            print ('還有10秒鐘')
        flag = input('請答題,答對請輸入y,跳過請輸入任意鍵')
        if (gametime-10<=sec<=gametime):
            print ('還有10秒鐘')
        if (sec>=gametime):
            print ('時間到！遊戲結束')
            break
        if (flag=='y'):
            correct[i]=correct[i]+1
            continue
        else:
            continue
    str_temp=('第%d組答對數目:%d') % (i+1,correct[i])	
    print (str_temp)
