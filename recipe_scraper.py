from flask import Flask, request
from recipe_scrapers import scrape_me

app = Flask(__name__)

def bulletize(data, numbered=False):
    data_to_format = data
    formatted_list = ''
    list_type = 'ul'

    if numbered:
        list_type = 'ol'

    if isinstance(data, str):
        data_to_format = data.split('\n')

    for item in data_to_format:
        list_item = '''\
            <li>
            {}
            </li>
        '''.format(item)

        formatted_list += list_item

    return '''\
        <{}>
        {}
        </{}>
    '''.format(list_type, formatted_list, list_type)

@app.route('/')
def hello_world():
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
        <H1>{}</>
        <p>Yields: {} </p>
        <p>Total Time: {} minutes</p>
        <H2>Ingredients</H2>
        {}
        <H2>Instructions</H2>
        {}
    '''.format(title, yields, total_time, formatted_ingredients, formatted_instructions)

