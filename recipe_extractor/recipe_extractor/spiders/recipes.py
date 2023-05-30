import scrapy


class RecipesSpider(scrapy.Spider):
    name = "recipes"
    allowed_domains = ["bbcgoodfood.com"]
    start_urls = [
        "https://www.bbcgoodfood.com/recipes/padron-peppers",
        "https://www.bbcgoodfood.com/recipes/vegetable-bean-chilli",
    ]

    def parse(self, response):
        yield {
            "name": response.css(".heading-1::text").get(),
            "author": response.css("a[rel=author]::text").get(),
            "description": response.css(".editor-content > p::text").get(),
            "rating_count": int(
                response.css(".rating__count-text::text").re(r"[0-9]+")[0]
            ),
            "rating_value": float(response.css(".sr-only::text").re(r"[0-9\.]+")[0]),
            "rating_value_max": float(
                response.css(".sr-only::text").re(r"[0-9\.]+")[1]
            ),
        }
