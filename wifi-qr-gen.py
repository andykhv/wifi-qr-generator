import sys
import qrcode

#string to encode
ssid = sys.argv[1]
password = sys.argv[2]
string = "WIFI:T:WPA;S:" + ssid + ";P:" + password + ";;"

#generate image
img = qrcode.make(string)
img.save(ssid + "-QRCode.png")
