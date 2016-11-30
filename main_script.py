from flask import Flask
import os
from selenium import webdriver

#import google_test
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/auth')
def auth():
    return 'The username is: ' + os.environ['AZN_AUTH1']

@app.route('/selenium')
def test():
    driver = webdriver.Chrome()
    driver.get("http://www.youtube.com/results?search_query=" + "guitar+lessons")

    results = driver.find_elements_by_xpath('//div[@class="yt-lockup-content"]')

    print(len(results))

    for result in results:
        video = result.find_element_by_xpath('.//h3/a')
        title = video.get_attribute('title')
        url = video.get_attribute('href')
        print("{} ({})".format(title, url))
    driver.quit()


if __name__ == '__main__':
    app.run()
