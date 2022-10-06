def read(path):
	with open(path, 'r') as file:
		return file.read().split('\n')

def write(path, arr):
	with open(path, 'w') as file:
		file.write('\n'.join(' '.join(row) for row in arr))

WORDS = read('words_alpha.txt')
segments = [set() for _ in range(15)]
words_lens = [[] for _ in range(14)]
for word in WORDS:
	if 16 >= len(word) >= 4:
		words_lens[len(word)-4] += [word]
		for i in range(2,len(word)+1):
			segments[i-2] |= {word[:i]}

write('words.csv', words_lens)
write('segments.csv', segments)