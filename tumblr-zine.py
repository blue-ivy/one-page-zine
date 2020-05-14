from selenium import webdriver
import requests
import sys
import os


def goFetch(q):
    chrome_path = os.path.realpath('chromedriver')
    print(chrome_path)
    driver = webdriver.Chrome(executable_path=chrome_path)
    driver.get('https://www.tumblr.com/search/' + q)
    images = driver.find_elements_by_css_selector('img.photo')
    i = 1
    for image in images:
        src = image.get_attribute("src")
        if "gif" not in src:
            img_data = requests.get(src)
            with open('./1PGZ/image' + str(i) + '.png', 'wb') as handler:
                handler.write(img_data.content)
            i += 1
            print(src)
        else:
            print('**SKIPPED gif: ' + src)
        if i > 8:
            break
    if i < 8:
        print("***DID NOT FIND 8 IMAGES***")
    driver.close()

if __name__ ==  "__main__":
    if len(sys.argv) > 1:
        goFetch(sys.argv[1])
