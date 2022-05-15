import imageio
from wand.image import Image
from pygifsicle import optimize

filenames = []

with Image(filename="base.jpg") as img:
  for i in range(1, 150):
    img.swirl(degree = -10)
    img.save(filename="frame_swirl/swirl_{}.jpg".format(i))
    filenames.append("frame_swirl/swirl_{}.jpg".format(i))

images = []

for filename in filenames:
  images.append(imageio.imread(filename))

for filename in reversed(filenames):
  images.append(imageio.imread(filename))

output_name = 'swirled.gif'

imageio.mimsave(output_name, images, fps=60)

optimize(output_name, 'optimized.gif')
optimize(output_name)