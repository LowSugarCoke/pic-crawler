"""
@author: Jack Lee

This script uses the GoogleCatchImage library to crawl Google Images based on given keywords. 
If no keywords are provided via command line, it will use the default keywords "cat" and "dog".
The number of rounds can also be specified. If not provided, it defaults to 100.

How to use:
1. Run this script from command line without arguments to use the default keywords and default number of rounds:
    python pic-crawler.py
2. To use custom keywords, pass them as command line arguments, separated by spaces:
    python pic-crawler.py custom_keyword1 custom_keyword2
3. To specify the number of rounds, use the --num_rounds argument:
    python pic-crawler.py --num_rounds 50 custom_keyword1 custom_keyword2

"""

import argparse
import google_catch_image


def main(keywords, num_rounds):
    crawler_lib = google_catch_image.GoogleCatchImage()

    for keyword in keywords:
        url = 'https://www.google.com.hk/search?q=' + keyword + '&tbm=isch'
        crawler_lib.run(url, keyword, headless=True, round=num_rounds)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Crawl Google Images based on keywords.')
    parser.add_argument('keywords', metavar='K', type=str, nargs='*',
                        help='keywords to search for')
    parser.add_argument('--num_rounds', metavar='N', type=int, default=45,
                        help='number of rounds to perform for each keyword')

    args = parser.parse_args()
    if not args.keywords:
        args.keywords = ["cat", "dog"]
    main(args.keywords, args.num_rounds)
