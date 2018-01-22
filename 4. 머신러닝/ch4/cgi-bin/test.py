#!/usr/bin/env python3

# 라이브러리를 읽어 들입니다. --- (※1)
import sys
import urllib.request as req
import urllib.parse as parse

# 명령 라인 매개 변수 추출 --- (※2)
if len(sys.argv) <= 1:
    print("USAGE: download-forecast-argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]

# 매개 변수를 URL 인코드합니다. --- (※3)
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId': regionNumber
}
params = parse.urlencode(values)
url = API + "?" + params
print("url=", url)

# 다운로드합니다. --- (※3)
data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)
