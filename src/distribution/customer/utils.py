import csv 

def get_customer_data():
	""" Read the data from csv and return the data"""
	with open('customer_data.csv', 'r') as csvfile:
		data = csv.reader(csvfile)
		next(data)
		return get_details(data)
	# return order_count, amount, customer_order_count

def get_details(data):
	""" Count the number of times a customer ordered and its total,
		total orders and amount"""
	order_count = 0
	amount = 0
	customer_order_count = {}
	for each_row in data:
		if each_row:
			order_count +=1
			amount += int(each_row[3])
			if customer_order_count.has_key(each_row[2]):
				customer_order_count[each_row[2]]['count'] += 1
				customer_order_count[each_row[2]]['ordered_amount'] += int(each_row[3])
			else:
				customer_order_count[each_row[2]] = {'count':1, 'ordered_amount':int(each_row[3])}
	return order_count, amount, customer_order_count

def get_customer_order_count(customer_order_count):
	"""get the list of customer names by their total orders"""
	once = []
	twice = []
	thrice = []
	fourtimes = []
	higher = []
	for key, value in customer_order_count.items():
		if value['count'] == 1:
			once.append(key)
		if value['count'] == 2:
			twice.append(key)
		if value['count'] == 3:
			thrice.append(key)
		if value['count'] == 4:
			fourtimes.append(key)
		if value['count'] > 4:
			higher.append(key)
	return once, twice, thrice, fourtimes, higher