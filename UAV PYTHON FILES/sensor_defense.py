import time
import math

class FlightControllerDefense:
    def __init__(self, frequency_threshold=20.0, amplitude_limit=250):
        self.frequency_threshold = frequency_threshold
        self.amplitude_limit = amplitude_limit
        self.is_locked_down = False

    def monitor_and_filter(self, current_pwm, base_pwm):
        delta = abs(current_pwm - base_pwm)
        
        # Detect abnormal high-amplitude oscillation signatures
        if delta > self.amplitude_limit:
            if not self.is_locked_down:
                print("[WARNING] Anomaly detected: High-frequency actuator variance exceeds safety limits!")
                print("[DEFENSE] Engaging software notch filter and clamping motor mixing matrix.")
                self.is_locked_down = True
            
            # Clamp the PWM to safe baseline hover limits to neutralize the attack vector
            return base_pwm
        
        if self.is_locked_down and delta <= self.amplitude_limit:
            print("[INFO] Telemetry normalized. Restoring full manual control channels.")
            self.is_locked_down = False
            
        return current_pwm

# Testing the defense filter logic against our attack profile
if __name__ == '__main__':
    defense = FlightControllerDefense()
    base_pwm = 1500
    
    # Simulate receiving normal vs malicious attack signals
    test_signals = [1510, 1520, 1800, 1850, 1490, 1500]
    
    print("Running defense filter simulation...")
    for sig in test_signals:
        filtered_pwm = defense.monitor_and_filter(sig, base_pwm)
        print(f"Input PWM: {sig} ---> Filtered Active PWM: {filtered_pwm}")
        time.sleep(0.1)