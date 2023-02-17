from email import message
from selenium import webdriver
from urllib.parse import quote_plus
from urllib.request import urlopen
import os
from bs4 import BeautifulSoup
import time
import dload


def save_images(images, save_path, search_term):
    for index, image in enumerate(images[:500]):  # images[:크롤링하고 싶은 사진 개수]
        t = image.screenshot_as_base64
        file = open(os.path.join(save_path, search_term + str(index + 1) + ".jpg"), "wb")
        file.write(t)
        print("img save " + save_path + search_term + str(index + 1) + ".jpg")


def create_folder_if_not_exists(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def make_url(search_term):
    # 네이버 이미지 검색
    base_url = 'https://search.naver.com/search.naver?where=image&section=image&query='
    # CCL 상업적 이용 가능 옵션
    end_url = '&res_fr=0&res_to=0&sm=tab_opt&color=&ccl=2' \
              '&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&recent=0&datetype=0&startdate=0&enddate=0&gif=0&optStr=&nso_open=1'
    return base_url + quote_plus(search_term)


def crawl_images(search_term):
    # URL 생성
    url = make_url(search_term + " 사진")

    # chrome 브라우저 열기
    browser = webdriver.Chrome('./chromedriver.exe')
    browser.implicitly_wait(3)  # 브라우저를 오픈할 때 시간간격을 준다.
    browser.get(url)
     
    for _ in range(1000):
        # 가로 = 0, 세로 = 30000 픽셀 스크롤한다.
        browser.execute_script("window.scrollBy(0,30000)")

    # 이미지 긁어오기
    images = browser.find_elements_by_class_name("_listImage")

    # 저장 경로 설정
    save_path = "./사진/" + search_term + "/"
    create_folder_if_not_exists(save_path)

    # 이미지 저장
    req = browser.page_source
    soup = BeautifulSoup(req, 'html.parser')


    thumnails = soup.select('img._image._listImage')

    i = 1
    for thumnail in thumnails:
        img = thumnail['src']
        if "data:image" in str(img) :
            img = thumnail['data-lazy-src']
        print(img)
        try :
            dload.save(img, f'사진/' + search_term + '/' + search_term + str(i) + '.jpg')
        except :
            print("")
        i += 1

    # 마무리
    print(search_term + " 저장 성공")
    browser.close()


if __name__ == '__main__':
    list = ["무","비트","레몬","용과","생강","오렌지","잭푸르트","커스터드애플","배","오이","마늘","피방","바나나","양배추","할라페뇨","콩","키위","딸기","고구마","오크라","시금치","스타푸르트","가지","포도","상추","고추류","토마토","코코넛","파인애플","고추","감자","수박","당근","파파야","완두콩","포메그란테","대추","라임","순무","달걀","모란채","파프리카","사탕옥수수","사과","망고","양파","땅콩","옥수수","브로콜리","양송이버섯"]
    for food in list :
        crawl_images(food)