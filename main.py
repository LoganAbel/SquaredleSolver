def inp_list():
	while 1:
		i = input()
		if not i: return
		yield i

def inp_matrix():
	print('enter matrix:')
	return [[*i] for i in inp_list()]

def read(path):
	with open(path, 'r') as file:
		for row in file.read().split('\n'):
			yield row.split(' ')

WORDS = [{*words} for words in read(f'words.csv')]
SEGS = [{*segs} for segs in read('segments.csv')]
MATRIX = inp_matrix()

def next_trails(Is):
	for x in [-1,0,1]:
		for y in [-1,0,1]:
			nx = x + Is[-1][0]
			ny = y + Is[-1][1]
			if (nx,ny) not in Is and 0 <= nx < len(MATRIX[0]) and 0 <= ny < len(MATRIX):
				yield Is + [(nx, ny)]

def words_in_trail(Is):
	seg = ''.join([MATRIX[i[1]][i[0]] for i in Is])
	if len(seg) > 1 and seg not in SEGS[len(seg)-2]: return []
	return ([seg] if seg in WORDS[len(seg)-4] else []) + sum([words_in_trail(n_Is) for n_Is in next_trails(Is)], [])

def all_words():
	return {word for x in range(len(MATRIX[0])) for y in range(len(MATRIX)) for word in words_in_trail([(x,y)])}

def type(key):
	keyboard.press(key)
	keyboard.release(key)

word_lens = [set() for _ in range(len(WORDS))]
all_W = all_words()
for word in all_W:
	word_lens[len(word)-4] |= {word}

print('\n\n'.join(' '.join(sorted(words)) for words in word_lens if words))

print('press enter to type')
from pynput.keyboard import Key, Controller
import keyboard as key_get
keyboard = Controller()
for word in all_W:
	while not key_get.is_pressed('Enter'): pass
	while key_get.is_pressed('Enter'): pass
	for l in word:
		type(l)