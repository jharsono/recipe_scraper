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

def create_shopping_list(list):
	shopping_list = ''

	for item in list:
		list_item = '''\
			<p>
			<input type="checkbox" value={}>{}
			</p>
		'''.format(item, item)

		shopping_list += list_item

	return shopping_list
