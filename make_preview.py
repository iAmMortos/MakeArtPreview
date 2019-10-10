from PIL import Image
import appex
import console
import sys

def scale_size_to_max(size, max_size):
	w,h = size
	return (max_size, round(max_size*h/w)) if w>h else (round(max_size*w/h), max_size)

def watermark_with_transparency(img):
	base_image = img
	width, height = base_image.size
	watermark = Image.open('watermark.png')
	watermark = watermark.resize(base_image.size, Image.ANTIALIAS)

	transparent = Image.alpha_composite(base_image.convert('RGBA'), watermark.convert('RGBA'))
	return transparent

def main():
	img = None
	args = sys.argv
	if appex.is_running_extension():
		img = appex.get_image()
	else:
		print('running in Pythonista, using test image.')
		img = Image.open('test:Mandrill')
		
	if img != None:
		i0 = img.resize(scale_size_to_max(img.size, 400), Image.ANTIALIAS)
		preview = watermark_with_transparency(i0)
		preview.show()

if __name__ == '__main__':
	main()
