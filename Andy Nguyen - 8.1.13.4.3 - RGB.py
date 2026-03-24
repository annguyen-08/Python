from gpiozero import RGBLED
from time import sleep

right_eye_led = RGBLED(red="BOARD3", green="BOARD5", blue="BOARD7")
left_eye_led = RGBLED(red="BOARD8", green="BOARD10", blue="BOARD12")

def rgb_255_to_1(a,b,c):
    r = int(a)/255
    g = int(b)/255
    b = int(c)/255
    return (r,g,b)

def main():
    print("Starting Program")
    left_eye_command = {"set_left_rgb_eye_color": [30, 17, 55]}
    right_eye_command = {"set_left_rgb_eye_color": [30, 17, 55]}

    print(left_eye_command)

    eye_rgb = rgb_255_to_1 (left_eye_command["set_left_rgb_eye_color"][0], 
                            left_eye_command["set_left_rgb_eye_color"][1],
                            left_eye_command["set_left_rgb_eye_color"][2])
    
    eye_rgb = rgb_255_to_1 (right_eye_command["set_left_rgb_eye_color"][0], 
                            right_eye_command["set_left_rgb_eye_color"][1],
                            right_eye_command["set_left_rgb_eye_color"][2])

    #eye_rgb = [.5,0,.4]  edit this line to get the normalized RGB values
    for i in range(20):
        left_eye_led.color = eye_rgb
        sleep(50)
        eye_rgb = [.1,0,.9]
        left_eye_led.color = eye_rgb
        sleep(50)
        left_eye_led.color = (0,0,0)
        right_eye_led.color = eye_rgb
        sleep(50)
        eye_rgb = [.1,0,.9]
        right_eye_led.color = eye_rgb
        sleep(50)
        right_eye_led.color = (0,0,0)
    print("Ending Program")

main()
