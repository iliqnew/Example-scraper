# Example-scraper
A scrapy/selenium scraper of https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99

# build
python -m venv venv\
.\venv\Scripts\activate\
pip install requirements.txt\
cd .\mango_shop\\

# crawl
scrapy crawl midi_satin_skirt -o product.json