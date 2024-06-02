# Track the duration of the alarm trigger
alarm_start_time = None

while True:
    distance = get_distance()
    print("Measured Distance = %.1f cm" % distance)
    if distance < 20:
        pi.write(BUZZER, 1)
        pi.write(LED, 1)
        if alarm_start_time is None:
            alarm_start_time = time.time()
        elif time.time() - alarm_start_time > 3:  # Check if the alarm has been triggered for more than 3 seconds
            # Send a message to the trigger website server
            try:
                # Replace "xxx.xx.xx" with the actual server address
                server_address = "http://xxx.xx.xx"
                response = requests.get(server_address)
                print("Message sent to trigger server:", response.text)
            except Exception as e:
                print("Failed to send message to trigger server:", e)
        time.sleep(1)
    else:
        alarm_start_time = None  # Reset the alarm start time if the distance is above the threshold
        pi.write(BUZZER, 0)
        pi.write(LED, 0)
    time.sleep(1)
