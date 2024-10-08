from machine import Pin, I2C
import ssd1306
import utime
import urequests as uq
import network


# Display bitmap from file at custom position

station = network.WLAN(network.STA_IF)

def connect(id, pswd):
    ssid = id
    password = pswd
    if station.isconnected() == True:   
        print("Already connected")
        return
    station.active(True) 
    station.connect(ssid, password)
    while station.isconnected() == False:
        pass 
    print("Connection successful") 
    print(station.ifconfig())

connect("Enter wifi name","Enter wifi pass") #enter wifi details
feels= None
temp= None
feels= None
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:
    api = "https://api.tomorrow.io/v4/weather/realtime?location=mausam%20vihar&apikey=" # add your api key
    req = uq.get(api)  # Pass the headers to the request
    req = req.json()    
    feels = req['data']['values']['temperatureApparent']
    temp = req['data']['values']['temperature']
    humid = req['data']['values']['humidity']
    # Initialize the OLED display

    oled.rect(10, 10, 116, 43, 1)
    oled.text("Temp: ",16,15)
    oled.text(str(temp)+"C",55,15) # Ensure followers is converted to a string
    oled.text("Humid: ",16,26)
    oled.text(str(humid),64,26) # Ensure followers is converted to a string
    oled.text("Feels: ",16,38)
    oled.text(str(feels)+"C",64,38) # Ensure followers is converted to a string


    oled.show()
    utime.sleep(1800)
