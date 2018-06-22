# Returns the first word in a given text.
lambda text: ''.join(x for x in text if not x in ',.').split()[0]

# Returns a corrected sentence which starts with a capital letter and ends with a dot.
correct_sentence = lambda t: t[0].upper() + t[1:] + '.'*(t[-1] != '.')

# Returns the second index of a symbol in a given text
second_index = lambda text, symbol: (lambda x: x[1] if len(x)>1 else None)([x[0] for x in enumerate(text) if symbol in x]
second_index = lambda text, symbol: None if text.count(symbol) < 2 else [x[0] for x in enumerate(text) if symbol in x][1]i

#  Returns substring between two given markers
between_markers = lambda text, begin, end: text[text.index(begin)+len(begin) if begin in text else 0: text.index(end) if end in text else None]

# You are given the current stock prices. You have to find out which stocks cost more.
best_stock = lambda data: max([[data[x],x] for x in data])[1]
best_stock = lambda data: max(data, key=lambda x: data[x])

# Determine the popularity of certain words in the text.
popular_words = lambda text,words: (lambda text: {x:text.count(x) for x in words})(text.lower().split())

# Find the TOP most expensive things in a dictionary
bigger_price = lambda limit, data: sorted(data, key=lambda x: x['price'], reverse=True)[:limit]


# You should write a function that will receive a positive integer and return:
# "Fizz Buzz" if the number is divisible by 3 and by 5;
# "Fizz" if the number is divisible by 3;
# "Buzz" if the number is divisible by 5; 
# The number as a string for other cases.
checkio = lambda number: 'Fizz Buzz'if(not number%5 and not number %3) else ('Fizz'  if(not number%3) else ('Buzz' if(not number%5) else str(number)))


checkio = lambda *args: (lambda difference: round(difference, 3) if type(difference)==float else difference)(max(args) - min(args)) if len(args) else 0
checkio = lambda numbers: sum(numbers[::2])*numbers[-1] if len(numbers) else 0
checkio = lambda words: 3 in (lambda is_word: [sum(is_word[x:x+3]) for x in range(len(is_word)-3 or True)])([x.isalpha()*1 for x in words.split()])


# Find Nth power of the element with index N.
index_power = lambda number_array, power_value: number_array[power_value]**power_value if len(number_array) >  power_value else -1


# Join strings and replace "right" to "left"
left_join = lambda phrases: ', '.join(x for x in phrases).replace('right', 'left')
