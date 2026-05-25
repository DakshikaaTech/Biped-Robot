from machine import Pin, PWM
import time

# Initialize all 4 pins
pwm_lt = PWM(Pin(5, Pin.OUT), freq=50)  # Left Thigh
pwm_lc = PWM(Pin(16, Pin.OUT), freq=50) # Left Calf/Ankle
pwm_rt = PWM(Pin(18, Pin.OUT), freq=50) # Right Thigh
pwm_rc = PWM(Pin(17, Pin.OUT), freq=50) # Right Calf/Ankle

def set_angle(pwm_channel, angle):
    """Converts degrees (0-180) to hardware duty cycle."""
    duty = int(40 + (angle / 180) * 75)
    pwm_channel.duty(duty)

def stand_straight():
    """Quickly resets all joints to the 90-degree default baseline."""
    set_angle(pwm_lt, 90); set_angle(pwm_lc, 90)
    set_angle(pwm_rt, 90); set_angle(pwm_rc, 90)

print("Initializing... Setting robot straight.")
stand_straight()
time.sleep(2.0)  # 2-second delay to place the robot down safely

try:
    print("🚶 Walking Backward continuously...")
    while True:
        # --- STEP 1: Shift weight to the Left foot ---
        set_angle(pwm_lc, 80)
        set_angle(pwm_rc, 80)
        time.sleep(0.2)
        
        # --- STEP 2: Swing the Right leg backward ---
        # (Angles < 90 pull the leg back relative to the chassis alignment)
        set_angle(pwm_rt, 75)
        set_angle(pwm_lt, 75)
        time.sleep(0.3)
        
        # --- STEP 3: Shift weight to the Right foot ---
        set_angle(pwm_lc, 100)
        set_angle(pwm_rc, 100)
        time.sleep(0.2)
        
        # --- STEP 4: Swing the Left leg backward ---
        # (Angles > 90 pull the opposite side back)
        set_angle(pwm_lt, 105)
        set_angle(pwm_rt, 105)
        time.sleep(0.3)

except KeyboardInterrupt:
    # Safe exit when you click Stop in Thonny
    print("\nStopping...")
    stand_straight()
    time.sleep(0.2)
    pwm_lt.deinit(); pwm_lc.deinit(); pwm_rt.deinit(); pwm_rc.deinit()
    print("PWM streams disconnected.")