from selenium import webdriver
import requests
import sys
import os


def goFetch(q):
    chrome_path = os.path.realpath('chromedriver')
    print(chrome_path)
    driver = webdriver.Chrome(executable_path=chrome_path)
    driver.get('https://imgur.com/search?q=' + q)
    images = driver.find_elements_by_tag_name('img')
    i = 1
    for image in images:
        src = image.get_attribute("src")
        if src:
            img_data = requests.get(src)
            with open('./1PGZ/image' + str(i) + '.png', 'wb') as handler:
                handler.write(img_data.content)
            i += 1
            print(src)
        if i > 8:
            break
    driver.close()

if __name__ ==  "__main__":
    if len(sys.argv) > 1:
        goFetch(sys.argv[1])
