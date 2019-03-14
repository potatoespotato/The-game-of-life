import random
import time

from PIL import Image


fld = [[' ' for i in range(100)] for i in range(100)]


'''добавить новое поколение'''
# x - rows, y - column
class Field_and_first_genetation():
	def __init__(self):
		self.first_block = [0, 0]

	def first_block_generate(self):
		x = int(random.uniform(0, 101))
		y = int(random.uniform(0, 101))
		self.first_block[0] = x
		self.first_block[1] = y

	def I_type_generation(self):
		x = self.first_block[0]
		y = self.first_block[1]
		x_or_y = int(random.uniform(0, 2))
		if x_or_y == 0:
			for i in range(3):
				x += 1
				self.first_block.append(x)
				self.first_block.append(y)
		else:
			for i in range(3):
				y += 1
				self.first_block.append(x)
				self.first_block.append(y)

	def L_type_generation(self):
		x = self.first_block[0]
		y = self.first_block[1]
		up_down_left_right = int(random.uniform(0, 2))
		if up_down_left_right == 0:
			up_or_down = int(random.uniform(0, 2))
			if up_or_down == 0:
				y1 = y - 1
				y2 = y - 2
				left_or_right = int(random.uniform(0, 2))
				if left_or_right == 0:
					x1 = x - 1
				else:
					x1 = x + 1
			else:
				y1 = y + 1
				y2 = y + 2
				left_or_right = int(random.uniform(0, 2))
				if left_or_right == 0:
					x1 = x - 1
				else:
					x1 = x + 1
				self.first_block.append(x)
				self.first_block.append(y1)
				self.first_block.append(x1)
				self.first_block.append(y2)
		elif up_down_left_right == 1:
			left_or_right = int(random.uniform(0, 2))
			if left_or_right == 0:
				x1 = x - 1
				x2 = x - 2
				left_or_right = int(random.uniform(0, 2))
				if left_or_right == 0:
					y1 = x - 1
				else:
					y1 = x + 1
			else:
				x1 = x + 1
				x2 = x + 2
				left_or_right = int(random.uniform(0, 2))
				if left_or_right == 0:
					y1 = x - 1
				else:
					y1 = x + 1
			self.first_block.append(x1)
			self.first_block.append(y)
			self.first_block.append(x2)
			self.first_block.append(y1)

	def Z_type_generation(self):
		x = self.first_block[0]
		y = self.first_block[1]
		vertical_or_horizontal = int(random.uniform(0, 4))
		if vertical_or_horizontal == 0:  # vertical z
			x1 = x + 1
			y1 = y + 1
			y2 = y - 1
			self.first_block.append(x1)
			self.first_block.append(y)
			self.first_block.append(x1)
			self.first_block.append(y2)
			self.first_block.append(x)
			self.first_block.append(y1)

		elif vertical_or_horizontal == 1:  # vertical z
			x1 = x + 1
			y1 = y + 1
			y2 = y - 1
			self.first_block.append(x1)
			self.first_block.append(y)
			self.first_block.append(x1)
			self.first_block.append(y2)
			self.first_block.append(x)
			self.first_block.append(y1)

		elif vertical_or_horizontal == 2:  # horizontal z
			y1 = y + 1
			x1 = x + 1
			x2 = x - 1
			self.first_block.append(x)
			self.first_block.append(y1)
			self.first_block.append(x2)
			self.first_block.append(y1)
			self.first_block.append(x2)
			self.first_block.append(y)
		elif vertical_or_horizontal == 3:  # horizontal z
			y1 = y - 1
			x1 = x + 1
			x2 = x - 1
			self.first_block.append(x)
			self.first_block.append(y1)
			self.first_block.append(x2)
			self.first_block.append(y1)
			self.first_block.append(x2)
			self.first_block.append(y)

	def add_first_generation_on_field(self):
		global n_generation, fld
		s = (len(self.first_block))
		i = 0
		try:
			while i < s:
				x = self.first_block[i]
				y = self.first_block[(i+1)]
				fld[x][y] = '+'
				i = i + 2
			n_generation = n_generation - 1
		except:
			print('pass')


class life():
	def new_life():
		global fld
		for y in range(len(fld)):
			for x in range(len(fld[y])):
				if fld[y][x] == ' ':
					live_blocks = 0
					for i in range(-1, 2):
						for j in range(-1, 2):
							try:
								if fld[y+i][x+j] == '+':
									live_blocks += 1
							except:
								pass
					if live_blocks == 3:
						fld[y][x] = '+'
	def die():
		global fld
		for y in range(len(fld)):
			for x in range(len(fld[y])):
				if fld[y][x] == '+':
					live_blocks = -1
					for i in (-1, 0, 1):
						for j in (-1, 0, 1):
							try:
								if fld[y+i][x+j] == '+':
									live_blocks += 1
							except IndexError:
								live_blocks += 1
					if live_blocks == 2 or live_blocks == 3:
						fld[y][x] = "+"
					else:
						fld[y][x] = ' '



def create_img(i):
	global fld
	im = Image.new("RGB", (100, 100))
	pix = im.load()
	for y in range(len(fld)):
		for x in range(len(fld[y])):
			if fld[y][x] == ' ':
				pix[x, y] = (255, 255, 255)
			else:
				pix[x, y] = (0, 0, 0)
	im.save(r"C:\Users\Potato\Documents\GitHub\The game of life\for gif\{}.png".format(i))
	time.sleep(0.05)


	# imgfld = np.array(fld)
	# im = Image.fromarray(imgfld.astype('uint8')*255)
	# im.save(r"C:\Users\Potato\Documents\GitHub\The game of life\for gif\{}.png".format(i))


st = str('Amy normally hated Monday mornings but this year was different Kamal wasin her art class and she liked Kama she was waiting outside the classroom when her friend Tara arrived')
gen = st.split(' ')
n_generation = int(input('how mach first generation do?'))


for i in gen:
	i = Field_and_first_genetation()
	i.first_block_generate()
	choice_generation_type = int(random.uniform(0, 3))
	if choice_generation_type == 0:
		i.I_type_generation()
	elif choice_generation_type == 1:
		i.L_type_generation()
	elif choice_generation_type == 2:
		i.Z_type_generation()
	i.add_first_generation_on_field()
	if n_generation == 0:
		lucky_first_generation = i
		break
for row in fld:
	print(*row)
s = int(input('how mach img do?  '))
print('Life existed')
print(10*'-')
for i in range(s):
	life.new_life()
	life.die()
	create_img(i)
	if i == 10:
		input('If you want to continue. Press Enter')
	if i == s//10:
		print('['+1*'#' + 9*'-'+']')
	if i == 2*s//10:
		print('['+2*'#' + 8*'-'+']')
	if i == 3*s//10:
		print('['+3*'#' + 7*'-'+']')
	if i == 4*s//10:
		print('['+4*'#' + 6*'-'+']')
	if i == 5*s//10:
		print('['+5*'#' + 5*'-'+']')
	if i == 6*s//10:
		print('['+6*'#' + 4*'-'+']')
	if i == 7*s//10:
		print('['+7*'#' + 3*'-'+']')
	if i == 8*s//10:
		print('['+8*'#' + 2*'-'+']')
	if i == 9*s//10:
		print('['+9*'#' + 1*'-'+']')
	if i == s:
		print('['+10*'#'+']')
print('done')
