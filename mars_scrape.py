import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
executable_path = {'executable_path': ChromeDriverManager().install()}

def scrape():
    browser = Browser('chrome', **executable_path, headless=False)

    data = {}

    browser.visit('https://redplanetscience.com/')
    data['title'] = browser.find_by_css('div.content_title').text
    data['paragraph'] = browser.find_by_css('div.article_teaser_body').text

    browser.visit('https://spaceimages-mars.com')
    browser.find_link_by_partial_text('FULL IMAGE').click()
    data['image'] = browser.find_by_css('img.fancybox-image')['src']

    data['table'] = pd.read_html('https://galaxyfacts-mars.com')[1].to_html()

    browser.visit('https://marshemispheres.com/')

    hemispheres = []
    for i in range(4):
        hemisphere = {}
        hemisphere['title'] = browser.find_by_css('a.itemLink h3')[i].text
        browser.find_by_css('a.itemLink h3')[i].click()
        hemisphere['url'] = browser.find_by_text('Sample')['href']
        browser.back()
        hemispheres.append(hemisphere)
    browser.quit()
    data['hemispheres'] = hemispheres  

    return data
