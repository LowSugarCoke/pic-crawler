

# Pic-Crawler

Pic-Crawler is a Python program for crawling images from the web.

## Install


1. create a Python virtual environment
```
python -m venv pic-crawler-env
```
2. activate this environment, on Linux or MacOS
```
source pic-crawler-env/bin/activate
```
or on Windows
```
.\pic-crawler-env\Scripts\activate
```
3. install the project dependencies
```
pip install -r requirements.txt
```

## Usage

1. Run this script from command line without arguments to use the default keywords:
```
python pic-crawler.py
```
2. To use custom keywords, pass them as command line arguments, separated by spaces:
```  
python pic-crawler.py custom_keyword1 custom_keyword2
```
3. To specify the number of rounds, use the --num_rounds argument:
```
python pic-crawler.py --num_rounds 50 custom_keyword1 custom_keyword2
```

## Contributing

PRs accepted.

## License

This project is licensed under LowSugarCoke