temperatures = { "sensor_1": 85.5, "sensor_2": 90.2, "sensor_3": 78.8,
                "sensor_4": 92.3}
tlimit = 80.0
def trigger_alarm(temperatures, tlimit):
    exceeding_sensors = []
    for sensor, temp in temperatures.items():
        if temp > tlimit:
            exceeding_sensors.append(sensor)
    return exceeding_sensors
print(trigger_alarm(temperatures, tlimit))