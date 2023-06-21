import google_catch_image


if __name__ == '__main__':

    keywordlist = ['cat', 'pig']
    crawler_lib = google_catch_image.GoogleCatchImage()

    for keyword in keywordlist:
        url = 'https://www.google.com.hk/search?q='+keyword+'&tbm=isch'
        crawler_lib.run(url, keyword, headless=True, round=100)
