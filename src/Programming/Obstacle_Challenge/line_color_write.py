#Import the required modules
from vehicle_function import*
#Control the LED using the methods and attributes defined within the LED_control class
LED = LED_control()

#Utilize the methods and properties defined within the button_control class to read the button
button = button_control()

#Using methods and attributes defined within the dc_motor class to control a DC motor
motor = dc_motor()

#Utilize the methods and attributes defined within the servo_motor class to control the servo motor
servo = servo_motor()

#Utilize the methods and attributes defined within the TCS34725 class to read the color sensor
color_sensor = TCS34725()

#Utilize the methods and attributes defined within the 'Tools' class
mapping = tools()

white_color = -1
orange_color = -1
blue_color = -1

#The function for reading the value of the white area
def white_area_read():
    global white_color
    print('=======white area=======')
    print('wait button')
    button.wait_press_release()
    print('start white area\n')
    state = 1
    low_color = 100
    while state == 1:
        state = button.raw_value()
        color = color_sensor.readluminance()['c']
        if color < low_color:
            low_color = color
            print('  white:' + str(low_color))
        time.sleep(0.01)
    button.wait_release()
    white_color = low_color

#The function for reading the value of the orange line
def orange_line_read():
    print('\n=======orange line=======')
    print('wait button')
    button.wait_press_release()
    print('start orange line\n')
    state = 1
    low_color = 100
    while state == 1:
        state = button.raw_value()
        color = color_sensor.readluminance()['c']
        if color < low_color:
            low_color = color
            print('  Orange:' + str(low_color))
        time.sleep(0.01)
    button.wait_release()
    orange_color = low_color

#The function for reading the value of the blue line
def blue_line_read():
    print('\n=======blue line=======')
    print('wait button')
    button.wait_press_release()
    print('start blue line\n')
    state = 1
    low_color = 100
    while state == 1:
        state = button.raw_value()
        color = color_sensor.readluminance()['c']
        if color < low_color:
            low_color = color
            print('  Blue:' + str(low_color))
        time.sleep(0.01)
    button.wait_release()
    blue_color = low_color

#Record the values to the color_sensor.p file
def file_write():
    print('\n=======file write down=======')
    print('Orange:' + str(orange_color))
    print('Blue:' + str(blue_color))
    print('white:' + str(white_color))
    value = {}
    value['Blue'] = blue_color
    value['Orange'] = orange_color
    value['white'] = white_color
    print('Write Finish')
    pickle.dump(value, open('save_file/color_sensor.p', 'wb') )

white_area_read()
orange_line_read()
blue_line_read()
