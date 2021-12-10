import google_catch_image


if __name__ == '__main__':   
    keyword = 'cat'
    url = 'https://www.google.com.hk/search?q='+keyword+'&tbm=isch'

    crawler_lib = google_catch_image.GoogleCatchImage()
    crawler_lib.run(url,keyword)