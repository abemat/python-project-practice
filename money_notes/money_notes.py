def notes50(amount):
	return_notes = []
	if amount >= 5000:
		return_note50, change50 = divmod(amount,5000)
		return_note10 = notes10(change50)
		return_notes.append(return_note50)
		return_notes.append(return_note10)
	else:
		return_note10 = notes10(amount)
		return_notes.append(0)
		return_notes.append(return_note10)
	return return_notes

def notes10(amount):
	return_notes = []
	if amount >= 1000:
		return_note10, change10 = divmod(amount,1000)
		return_note5 = notes5(change10)
		return_notes.append(return_note10)
		return_notes.append(return_note5)
	else:
		return_note5 = notes5(amount)
		return_notes.append(0)
		return_notes.append(return_note5)
	return return_notes

def notes5(amount):
	return_notes = []
	if amount >= 500:
		return_note5, change5 = divmod(amount,500)
		return_note1 = notes1(change5)
		return_notes.append(return_note5)
		return_notes.append(return_note1)
	else:
		return_note1 = notes1(amount)
		return_notes.append(0)
		return_notes.append(return_note1)
	return return_notes

def notes1(amount):
	return_notes = []
	if amount >= 100:
		return_note1, change1 = divmod(amount,100)
		return_note01 = change1
		return_notes.append(return_note1)
		return_notes.append(return_note01)
	else:
		return_note01 = amount
		return_notes.append(0)
		return_notes.append(return_note01)
	return return_notes

def nest_breaker(nested_list):
	temp_list = []
	for item in nested_list:
		if type(item) is not list:
			temp_list.append(item)
		else:
			temp_list.extend(nest_breaker(item))
	return temp_list

if __name__ == "__main__":
	price = float(raw_input("Enter price: "))
	money = float(raw_input("Pay here: "))

	while money < price : 
		print "Money not enough\n"
		money = float(raw_input("Pay here: "))

	change = money - price
	print "Your change: ", change
	change_100 = change*100

	nested_notes = notes50(int(change_100))
	#print nested_notes
	return_notes = nest_breaker(nested_notes)

	print "50 notes :", return_notes[0]
	print "10 notes :", return_notes[1]
	print "5 notes :", return_notes[2]
	print "1 notes :", return_notes[3]
	print "cents :", return_notes[4]

