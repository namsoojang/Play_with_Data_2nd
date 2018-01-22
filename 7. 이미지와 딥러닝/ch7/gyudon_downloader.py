import sys, os, re, time
import urllib.request as req
import urllib.parse as parse
import json
# API의 URL 지정하기
PHOTOZOU_API = "https://api.photozou.jp/rest/search_public.json"
CACHE_DIR = "./image/cache"
# 포토주 API로 이미지 검색하기 --- (※1)
def search_photo(keyword, offset=0, limit=100):
    # API 쿼리 조합하기
    keyword_enc = parse.quote_plus(keyword)
    q = "keyword={0}&offset={1}&limit={2}".format(keyword_enc, offset, limit)
    url = PHOTOZOU_API + "?" + q
    # 캐시 전용 폴더 만들기
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
    cache = CACHE_DIR + "/" + re.sub(r'[^a-zA-Z0-9\%\#]+', '_', url)
    if os.path.exists(cache):
        return json.load(open(cache, "r", encoding="utf-8"))
    print("[API] " + url)
    req.urlretrieve(url, cache)
    time.sleep(1) # --- 1초 쉬기
    return json.load(open(cache, "r", encoding="utf-8"))
# 이미지 다운로드하기 --- (※2)
def download_thumb(info, save_dir):
    if not os.path.exists(save_dir): os.makedirs(save_dir)
    if info is None: return
    if not "photo" in info["info"]:
        print("[ERROR] broken info")
        return
    photolist = info["info"]["photo"]
    for photo in photolist:
        title = photo["photo_title"]
        photo_id = photo["photo_id"]
        url = photo["thumbnail_image_url"]
        path = save_dir + "/" + str(photo_id) + "_thumb.jpg"
        if os.path.exists(path): continue
        try:
            print("[download]", title, photo_id)
            req.urlretrieve(url, path)
            time.sleep(1) # --- 1초 쉬기
        except Exception as e:
            print("[ERROR] failed to downlaod url=", url)
# 모두 검색하고 다운로드하기 --- (※3)
def download_all(keyword, save_dir, maxphoto = 1000):
    offset = 0
    limit = 100
    while True:
        # API 호출
        info = search_photo(keyword, offset=offset, limit=limit)
        if info is None:
            print("[ERROR] no result"); return
        if (not "info" in info) or (not "photo_num" in info["info"]):
            print("[ERROR] broken data"); return
        photo_num = info["info"]["photo_num"]
        if photo_num == 0:
            print("photo_num = 0, offset=", offset)
            return
        # 사진 정보가 포함돼 있으면 다운받기
        print("*** download offset=", offset)
        download_thumb(info, save_dir)
        offset += limit
        if offset >= maxphoto: break
if __name__ == '__main__':
    # 모듈로 사용할 수 있게 설정
    download_all(" ", "./image/gyudon") # --- (※4)