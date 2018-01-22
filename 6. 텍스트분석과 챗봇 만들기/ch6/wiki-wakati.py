import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from gensim.models import word2vec
# 파일 열기
readFp = codecs.open("wiki.txt", "r", encoding="utf-8")
wakati_file = "wiki.wakati"
writeFp = open(wakati_file, "w", encoding="utf-8")
# 형태소 분석 --- (※2)
twitter = Twitter()
i = 0
# 텍스트를 한 줄씩 처리하기
while True:
    line = readFp.readline()
    if not line: break
    if i % 20000 == 0:
        print("current - " + str(i))
    i += 1
    # 형태소 분석
    malist = twitter.pos(line, norm=True, stem=True)
    # 필요한 어구만 대상으로 하기
    r = []
    for word in malist:
        # 어미/조사/구두점 등은 대상에서 제외 
        if not word[1] in ["Josa", "Eomi", "Punctuation"]:
            writeFp.write(word[0] + " ")
writeFp.close()