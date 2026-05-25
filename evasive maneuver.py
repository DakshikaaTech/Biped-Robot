from machine import Pin, PWM, time_pulse_us  # <-- Corrected import
import time

# 1. Setup ALL 4 Servos
pwm_lt = PWM(Pin(5, Pin.OUT), freq=50)
pwm_lc = PWM(Pin(16, Pin.OUT), freq=50)
pwm_rt = PWM(Pin(18, Pin.OUT), freq=50)
pwm_rc = PWM(Pin(19, Pin.OUT), freq=50)

# 2. Setup Ultrasonic Pins
trig = Pin(13, Pin.OUT)
echo = Pin(14, Pin.IN)

def set_angle(pwm_channel, angle):
    duty = int(40 + (angle / 180) * 75)
    pwm_channel.duty(duty)

def stand_straight():
    set_angle(pwm_lt, 90); set_angle(pwm_lc, 90)
    set_angle(pwm_rt, 90); set_angle(pwm_rc, 90)

def get_distance():
    trig.value(0)
    time.sleep_us(5)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    
    duration = time_pulse_us(echo, 1, 30000)
    if duration < 0: 
        return 999 
    return (duration * 0.0343) / 2

print("🚀 Running Final Autonomous Code! Get your camera ready!")
stand_straight()
time.sleep(2.0)

step_phase = 1

try:
    while True:
        distance = get_distance()
        print("Distance:", round(distance, 1), "cm")
        
        # Check if obstacle is closer than 20cm
        if distance < 20.0:
            print("🛑 Obstacle detected! Stopping robot.")
            stand_straight()
            # Do nothing else here - this effectively stops the robot
            time.sleep(0.5) 
            
        else:
            # --- NON-BLOCKING FORWARD WALK ---
            if step_phase == 1:
                set_angle(pwm_lc, 80); set_angle(pwm_rc, 80)
                step_phase = 2
            elif step_phase == 2:
                set_angle(pwm_rt, 105); set_angle(pwm_lt, 105)
                step_phase = 3
            elif step_phase == 3:
                set_angle(pwm_lc, 100); set_angle(pwm_rc, 100)
                step_phase = 4
            elif step_phase == 4:
                set_angle(pwm_lt, 75); set_angle(pwm_rt, 75)
                step_phase = 1
                
            time.sleep(0.3)
    
           

except KeyboardInterrupt:
    stand_straight()
    time.sleep(0.2)
    pwm_lt.deinit(); pwm_lc.deinit(); pwm_rt.deinit(); pwm_rc.deinit()
    print("Engines off safely.")
