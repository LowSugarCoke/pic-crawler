import google_catch_image


if __name__ == '__main__':   

    keywordlist=['Abyssinian','American Shorthair','Burmilla','Black cat','Cats in ancient Egypt','Turkish Van','Korat']
    crawler_lib = google_catch_image.GoogleCatchImage()

    for keyword in keywordlist:   
            url = 'https://www.google.com.hk/search?q='+keyword+'&tbm=isch'
            crawler_lib.run(url,keyword,headless=True,round=70)