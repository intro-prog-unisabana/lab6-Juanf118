def trigger_alarm(temperatures, threshold=80):
    """
    Filtra sensores que superan estrictamente el límite.
    """
    alarm_sensors = []
    
    for sensor, temp in temperatures.items():
        if temp > threshold:
            alarm_sensors.append(sensor)
            
    return alarm_sensors
if __name__ == "__main__":
    t1 = {"sensor_1": 85.5, "sensor_2": 90.2, "sensor_3": 78.8, "sensor_4": 92.3}
    print(trigger_alarm(t1, 88)) # Salida: ['sensor_2', 'sensor_4']
    
    #t2 = {"sensor_A": 79.0, "sensor_B": 81.2, "sensor_C": 75.4, "sensor_D": 85.7}
    #print(trigger_alarm(t2))     # Salida: ['sensor_B', 'sensor_D']

