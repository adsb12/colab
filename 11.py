import cv2
from google.colab.patches import cv2_imshow
import numpy as np
import urllib.request

def url_to_image(url):
  resp = urllib.request.urlopen(url)
  image = np.asarray(bytearray(resp.read()), dtype='uint8')
  image = cv2.imdecode(image, cv2.IMREAD_COLOR)

  return image

tiger_image = url_to_image('https://bananabearbooks.com/wp-content/uploads/2018/04/tiger-illustration-bananabeabooks.jpg')

cv2_imshow(tiger_image)