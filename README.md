# recipevolution

Repo containing tools to find and plan recipes

This is for testing and learning purposes only.

## Running

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
cd recipe_extractor
scrapy crawl recipes -O recipes.json
```