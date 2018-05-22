# Returns the first word in a given text.
lambda text: ''.join(x for x in text if not x in ',.').split()[0]

# Returns a corrected sentence which starts with a capital letter and ends with a dot.
correct_sentence = lambda t: t[0].upper() + t[1:] + '.'*(t[-1] != '.')

# Returns the second index of a symbol in a given text
second_index = lambda text, symbol: (lambda x: x[1] if len(x)>1 else None)([x[0] for x in enumerate(text) if symbol in x]
second_index = lambda text, symbol: None if text.count(symbol) < 2 else [x[0] for x in enumerate(text) if symbol in x][1]i)

#  Returns substring between two given markers
between_markers = lambda text, begin, end: text[text.index(begin)+len(begin) if begin in text else 0: text.index(end) if end in text else None]

# You are given the current stock prices. You have to find out which stocks cost more.
best_stock = lambda data: max([[data[x],x] for x in data])[1]
best_stock = lambda data: max(data, key=lambda x: data[x])


