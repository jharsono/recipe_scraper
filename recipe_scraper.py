from flask import Flask, request
from recipe_scrapers import scrape_me
from utlities import bulletize
from utlities import create_shopping_list

app = Flask(__name__)

@app.route('/')
def home():
	return 'POST to /scrape with {url: "recipe_link.html"} in the request body.'

@app.route('/scrape', methods=['POST'])
def scrape_recipe():
	req_data = request.get_json()
	scraper = scrape_me(req_data['url'])

	title = scraper.title()
	yields = scraper.yields()
	total_time = scraper.total_time()
	ingredients = scraper.ingredients()
	instructions = scraper.instructions()

	formatted_ingredients = bulletize(ingredients)
	formatted_instructions = bulletize(instructions, numbered=True)

	return '''\
		<H1>{}</H1>
		<p>Yields: {}</p>
		<p>Total Time: {} minutes</p>
		<H2>Ingredients</H2>
		{}
		<H2>Instructions</H2>
		{}
	'''.format(title, yields, total_time, formatted_ingredients, formatted_instructions)


@app.route('/shopping-list', methods=['POST'])
def show_shopping_list():
	req_data = request.get_json()
	scraper = scrape_me(req_data['url'])

	title = scraper.title()
	ingredients = scraper.ingredients()

	return '''\
		{}
		<p>
		{}
		</p>
		'''.format(title, create_shopping_list(ingredients))

