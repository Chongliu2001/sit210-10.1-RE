import time
import pigpio

# Initialize GPIO
pi = pigpio.pi()
TRIG = 17
ECHO = 27
BUZZER = 23
LED = 24

pi.set_mode(TRIG, pigpio.OUTPUT)
pi.set_mode(ECHO, pigpio.INPUT)
pi.set_mode(BUZZER, pigpio.OUTPUT)
pi.set_mode(LED, pigpio.OUTPUT)

pi.write(TRIG, 0)
time.sleep(2)  # Set time to stabilize the sensor


def get_distance():
    pi.write(TRIG, 1)
    time.sleep(0.00001)
    pi.write(TRIG, 0)

    start_time = time.time()
    stop_time = start_time  # Initialize stop_time here
    while pi.read(ECHO) == 0:
        start_time = time.time()

    while pi.read(ECHO) == 1:
        stop_time = time.time()

    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2

    return distance


try:
    while True:
        distance = get_distance()
        print("Measured Distance = %.1f cm" % distance)
        if distance < 20:
            pi.write(BUZZER, 1)
            pi.write(LED, 1)
            time.sleep(1)
            pi.write(BUZZER, 0)
            pi.write(LED, 0)
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    pi.stop()
