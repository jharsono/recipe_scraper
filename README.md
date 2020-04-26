# Recipe Scraper

This is a small webapp hosted on pythonanywhere.com that will scrape recipes from websites, returning only the recipe text and skipping all the ads and unnecessary content. Uses the recipe-scrapers Python package: https://github.com/hhursev/recipe-scrapers

See recipe-scrapers repo for list of supported sites.

## How to use
Make a `POST` request to `'/scrape'` with a request body like this:

```
{
	"url": "recipe-site.com/the-best-fried-chicken"
}
```

## How I use it
Since I'm in my kitchen I'll have my phone and not a computer, so I use iOS Shortcuts to make the request and return the recipe data.

1. Find recipe
2. Copy url
3. Open Shortcut (shortcut automatically takes url from clipboard)

## TO DO
* Provide more info on ios shortcut

