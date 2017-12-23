def talking_clock(time):
	number_to_word = {
		0: " twelve",
		1: " one",
		2: " two",
		3: " three",
		4: " four",
		5: " five",
		6: " six",
		7: " seven",
		8: " eight",
		9: " nine",
		10: " ten",
		11: " eleven",
		12: " twelve",
		13: " thirteen",
		14: " fourteen",
		15: " fifteen",
		16: " sixteen",
		17: " seventeen",
		18: " eighteen",
		19: " nineteen",
		20: " twenty",
		30: " thirty",
		40: " fourty",
		50: " fifty",
	}

	tens_to_word = {
		2: " twenty",
		3: " thirty",
		4: " fourty",
		5: " fifty",
	}

	try:
		hour, minutes = [int(x) for x in time.split(":")]
	except ValueError: 
		raise ValueError("Time not in format 'HH:MM'")

	output = "It's"
	output += number_to_word[hour % 12]

	period = " am" if (hour % 24 < 12) else " pm"
	minutes = minutes % 60

	if minutes == 0:
		pass
	elif minutes < 20:
		output += (" oh" if minutes < 10 else "") + number_to_word[minutes]
	else:
		tens, ones = divmod(minutes, 10)
		output += tens_to_word[tens]

		if minutes % 10:
			output += number_to_word[ones]

	return output + period 


if __name__ == '__main__':
	time = "1:59"
	print talking_clock(time)