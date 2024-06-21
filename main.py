import time
import random

# Function to read light sensor data (simulated for demonstration)
def read_light_sensor():
    # Simulated light intensity (replace with actual sensor reading)
    return random.randint(0, 100)

# Function to control street lights based on light intensity
def control_street_lights():
    while True:
        light_intensity = read_light_sensor()
        
        # Logic to decide when to turn street lights on or off
        if light_intensity < 50:
            print(f"Light intensity: {light_intensity}. Turning on street lights.")
            # Code to turn on street lights (simulated action)
        else:
            print(f"Light intensity: {light_intensity}. Turning off street lights.")
            # Code to turn off street lights (simulated action)
        
        # Adjust the time delay based on your requirements
        time.sleep(5)  # Check light intensity every 5 seconds

# Main function to start the monitoring system
if __name__ == "__main__":
    control_street_lights()
