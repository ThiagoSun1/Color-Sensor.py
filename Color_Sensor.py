import color_sensor
import motor_pair
from hub import port
import color, runloop
from time import sleep

def detected_color():
    return color_sensor.color(port.B) == color.BLACK

async def main():

    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    motor_pair.move(motor_pair.PAIR_1, 0)

    await runloop.until(detected_color)
    if detected_color:
        # motor_pair.PAIR_1 is the pair, 180 turns 90 degrees, 100 is 100% speed
        motor_pair.move_for_degrees(motor_pair.PAIR_1, 180, 100)
        
runloop.run(main())
