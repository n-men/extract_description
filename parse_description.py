from collections import OrderedDict


def get_description(text):
	"""Split item description to parts"""
	
	# set names and titles of parts
	names = ['description', 'materials', 'features', 'advantages']
	titles = ['', 'Материалы изготовления', 'Особенности', 'Преимущества']
	
	# remove newlines from text
	content = text.replace("\n", "")
	
	# define start position of each part
	starts = [content.find(title) for title in titles]
	# append the last symbol position
	starts.append(len(content))

	# initialise ordered dictionary for results storage
	result_dict = OrderedDict((key, '') for key in names)
	
	# get content for each part
	for i in range(len(names)):
		
		part_start = starts[i]
		
		# check if part title was found in content
		if part_start >= 0:
		
			part_name = names[i]
			
			# define the next part start which means the end of the current part
			next_parts = starts[i+1:]
			# only count parts that are in content
			next_parts = list(filter(lambda x: x > 0, next_parts))
			next_part_start = next_parts[0]
			
			# save part content
			result_dict[part_name] = content[part_start:next_part_start]

	return result_dict

	
text = """Электрическая сетевая дрель безударная 'Калибр' ДЭ-310Ш мощностью 310 Вт "
предназначена для использования в ремонтно-строительных работах.
Материалы изготовления Электропривод и органы управления помещены в ударопрочный 
пластиковый корпус.
Особенности "Безударная дрель-шуруповерт 'Калибр' ДЭ-310Ш характеризуется компактной"
конструкцией и небольшим весом. 
Преимущества Основные преимущества использования сетевой дрели-шуруповерта: 1 2 3"""
	
description = get_description(text=text)
for name, content in description.items():
	print('{}: {}'.format(name, content))