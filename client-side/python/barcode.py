import cv2
from pyzbar import pyzbar
 
bardet = cv2.barcode_BarcodeDetector()
img = cv2.imread("assets/barcode.jpg")
ok, decoded_info, decoded_type, corners = bardet.detectAndDecode(img)
img = cv2.imshow(ok)