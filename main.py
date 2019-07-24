import random
import time
import os

from PIL import Image


fld = [[' ' for i in range(100)] for i in range(100)]


'''добавить новое поколение'''
# x - rows, y - column
class Field_and_first_genetation():
	"""
	[Field_and_first_genetation] - генерация первой популяции
	"""
	def __init__(self, field, n_generation):
		self.first_block = [0, 0]
		self.field = field
		self.n_generation = n_generation
	


	def first_block_generate(self):
		x = int(random.uniform(0, 101))
		y = int(random.uniform(0, 101))
		self.first_block[0] = x
		self.first_block[1] = y
	
	def add(self, params):
		for i in params:
			self.first_block.append(i)
	
	def give_first_cordination(self, x = 0, y = 1):
		"""
		[give_first_cordination] - возвращает начальные координаты
		
		Returns:
			[int] -- [начальные координаты x и y]
		"""
		return self.first_block[x], self.first_block[y]

	def I_type_generation(self):
		"""
		[I_type_generation] - генерация | образной популяции
		"""

		x, y = self.give_first_cordination()


		x_or_y = int(random.uniform(0, 2))
		
		if x_or_y == 0:
			for i in range(3):
				x += 1
				self.add([x,y])

		else:

			for i in range(3):
				y += 1
				self.add([x,y])


	def L_type_generation(self):
		"""
		[L_type_generation] - генерации L образной популяции
		"""
		
		x, y = self.give_first_cordination()


		up_down_left_right = int(random.uniform(0, 2))

		if up_down_left_right == 0:
			up_or_down = int(random.uniform(0, 2))
			if up_or_down == 0: # популяция растет вниз
				y1 = y - 1
				y2 = y - 2
				left_or_right = int(random.uniform(0, 2))
				if left_or_right == 0: # популяция растет влево
					x1 = x - 1
				else:                  # популяция растет вправо
					x1 = x + 1
			else:
				y1 = y + 1
				y2 = y + 2
				left_or_right = int(random.uniform(0, 2))
				if left_or_right == 0: # популяция растет вверх
					x1 = x - 1
				else:
					x1 = x + 1

				self.add([x, y1, x1, y2])

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
			
			self.add([x1, y, x2, y1])

	def Z_type_generation(self):
		"""
		[Z_type_generation] - генерация Z образной популяции
		"""
		x, y = self.give_first_cordination()

		vertical_or_horizontal = int(random.uniform(0, 4))
		
		if vertical_or_horizontal == 0:  # vertical z
			
			x1 = x + 1
			y1 = y + 1
			y2 = y - 1

			self.add([x1, y, x1, y2, x ,y1])

		if vertical_or_horizontal == 1:  # vertical z
			
			x1 = x + 1
			y1 = y + 1
			y2 = y - 1

			self.add([x1, y, x1, y2, x ,y1])

		if vertical_or_horizontal == 2:  # horizontal z
			
			y1 = y + 1
			x1 = x + 1
			x2 = x - 1

			self.add([x, y1, x2, y1, x2 ,y])

		if vertical_or_horizontal == 3:  # horizontal z
			y1 = y - 1
			x1 = x + 1
			x2 = x - 1

			self.add([x, y1, x2, y1, x2 ,y])

	def add_first_generation_on_field(self):
		"""
		[add_first_generation_on_field] - добавляет первую популяцию на поле
		"""
		
		s = (len(self.first_block))
		i = 0
		try:

			while i < s:
				x, y = self.give_first_cordination(i, i+1)
				self.field[x][y] = '+'
				i = i + 2
			
			self.n_generation = n_generation - 1

		except:
			print('pass')
		global fld
		fld = self.field


class Life():

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
	directory = os.path.dirname(os.path.abspath(__file__)) + '/for_gif/{}.png'.format(i)
	print(directory)
	im.save(directory)
	time.sleep(0.05)


	# imgfld = np.array(fld)
	# im = Image.fromarray(imgfld.astype('uint8')*255)
	# im.save(r"C:\Users\Potato\Documents\GitHub\The game of life\for gif\{}.png".format(i))


st = str('Amy normally hated Monday mornings' +
' but this year was different Kamal wasin her art class and she liked' +
 ' Kama she was waiting outside the classroom when her friend Tara arrived'
 		)
gen = st.split(' ')

n_generation = int(input('how mach first generation do? \n'))


for i in gen:
	i = Field_and_first_genetation(fld, n_generation)
	i.first_block_generate()
	choice_generation_type = int(random.uniform(0, 3))
	if choice_generation_type == 0:
		i.I_type_generation()
	if choice_generation_type == 1:
		i.L_type_generation()
	if choice_generation_type == 2:
		i.Z_type_generation()
	i.add_first_generation_on_field()
	
	if n_generation == 0:
		lucky_first_generation = i
		break

for row in fld:
	print(*row)

s = int(input('how mach img do?\n'))
print('Life existed')
print(10*'-')
for i in range(s):

	Life.new_life()
	Life.die()

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
