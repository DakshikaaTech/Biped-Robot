from machine import Pin, PWM
import time

# 1. Map out the pins directly
pin_lt = Pin(5, Pin.OUT) # Left Thigh
pin_lc = Pin(16, Pin.OUT) # Left Calf/Ankle
pin_rt = Pin(18, Pin.OUT) # Right Thigh
pin_rc = Pin(17, Pin.OUT) # Right Calf/Ankle

# 2. Initialize PWM streams at standard servo frequency (50Hz)
pwm_lt = PWM(pin_lt, freq=50)
pwm_lc = PWM(pin_lc, freq=50)
pwm_rt = PWM(pin_rt, freq=50)
pwm_rc = PWM(pin_rc, freq=50)

def set_servo_angle(pwm_channel, angle):
    """
    Converts an angle (0 to 180) into the exact hardware duty cycle 
    the ESP32 microcontroller needs to send down the wire.
    """
    # Standard duty mapping: 0 deg ~ duty 40, 180 deg ~ duty 115
    duty = int(40 + (angle / 180) * 75)
    pwm_channel.duty(duty)

def stand_straight():
    """Sets all motors to their exact 90-degree center baseline."""
    set_servo_angle(pwm_lt, 90)
    set_servo_angle(pwm_lc, 90)
    set_servo_angle(pwm_rt, 90)
    set_servo_angle(pwm_rc, 90)

# --- Main Program Execution ---

print("Initializing standing posture...")
stand_straight()
time.sleep(2.0) # Safe delay to place the robot down on its feet

print("Starting direct PWM walking loop... Press Ctrl+C to abort.")

try:
    while True:
        # --- STEP 1: Shift Weight Left & Lean ---
        # Ankle angles change to lean the torso over the left foot
        set_servo_angle(pwm_lc, 70)   
        set_servo_angle(pwm_rc, 70)   
        time.sleep(0.3)
        
        # --- STEP 2: Step Right Foot Forward ---
        # Right thigh swings forward, left thigh pushes backward
        set_servo_angle(pwm_rt, 110)  
        set_servo_angle(pwm_lt, 110)  
        time.sleep(0.3)
        
        # --- STEP 3: Shift Weight Right & Lean ---
        # Ankle angles invert to lean the torso over the right foot
        set_servo_angle(pwm_lc, 110)  
        set_servo_angle(pwm_rc, 110)  
        time.sleep(0.3)
        
        # --- STEP 4: Step Left Foot Forward ---
        # Left thigh swings forward, right thigh pushes backward
        set_servo_angle(pwm_lt, 70)   
        set_servo_angle(pwm_rt, 70)   
        time.sleep(0.3)

except KeyboardInterrupt:
    # When you interrupt the loop, clean up the pins and stand up straight
    print("\nResetting robot safely...")
    stand_straight()
    time.sleep(0.5)
    
    # Shut down the PWM timers safely
    pwm_lt.deinit()
    pwm_lc.deinit()
    pwm_rt.deinit()
    pwm_rc.deinit()
    print("PWM engines deactivated.")
