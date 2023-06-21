"""
@author: Jack Lee

This script uses the GoogleCatchImage library to crawl Google Images based on given keywords. 
If no keywords are provided via command line, it will use the default keywords "cat" and "dog".

How to use:
1. Run this script from command line without arguments to use the default keywords:
    python script.py
2. To use custom keywords, pass them as command line arguments, separated by spaces:
    python script.py custom_keyword1 custom_keyword2

"""

import argparse
import google_catch_image


def main(keywords):
    crawler_lib = google_catch_image.GoogleCatchImage()

    for keyword in keywords:
        url = 'https://www.google.com.hk/search?q=' + keyword + '&tbm=isch'
        crawler_lib.run(url, keyword, headless=True, round=100)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Crawl Google Images based on keywords.')
    parser.add_argument('keywords', metavar='K', type=str, nargs='*',
                        help='keywords to search for')

    args = parser.parse_args()
    if not args.keywords:
        args.keywords = ["cat", "dog"]
    main(args.keywords)
