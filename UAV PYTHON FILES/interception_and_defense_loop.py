from pymavlink import mavutil
import time
import math

class MAVLinkDefenseProxy:
    def init(self, connection_string, amplitude_limit=250):
        self.connection_string = connection_string
        self.amplitude_limit = amplitude_limit
        self.base_pwm = 1500
        self.is_locked_down = False
        
        print(f"Connecting to target: {connection_string}...")
        self.master = mavutil.mavlink_connection(connection_string)
        self.master.wait_heartbeat()
        print("Heartbeat locked. Defense proxy active.")

    def run_proxy(self):
        try:
            while True:
                # Listen for incoming messages (like RC_CHANNELS_OVERRIDE)
                msg = self.master.recv_match(type=['RC_CHANNELS_OVERRIDE', 'COMMAND_LONG'], blocking=True, timeout=1.0)
                
                if msg and msg.get_type() == 'RC_CHANNELS_OVERRIDE':
                    # Extract channel 1 override value as a test vector
                    chan1 = msg.chan1_raw
                    
                    if chan1 > 0: # If an override is active
                        delta = abs(chan1 - self.base_pwm)
                        
                        if delta > self.amplitude_limit:
                            print(f"[SECURITY ALERT] Malicious frequency spike detected! PWM: {chan1}. Neutralizing...")
                            
                            # Counter-action: Send neutralizing baseline command override
                            self.master.mav.rc_channels_override_send(
                                self.master.target_system,
                                self.master.target_component,
                                self.base_pwm, self.base_pwm, self.base_pwm, self.base_pwm,
                                0, 0, 0, 0
                            )
                        else:
                            print(f"[INFO] Telemetry nominal. Channel 1 PWM: {chan1}")
                            
                time.sleep(0.01)
        except KeyboardInterrupt:
            print("\nProxy terminated by user. Releasing control.")

if __name__ == '__main__':
    # Point this to your SITL TCP endpoint
    proxy = MAVLinkDefenseProxy('tcp:127.0.0.1:5762')
    proxy.run_proxy()