from libs.ACB_Biped_Robot import *
# Define the GPIO pin numbers connected to different parts of the Biped robot
Left_thigh = 5     
Left_calf = 16   
Right_thigh = 18  
Right_calf = 19

# Initialize the Biped robot with the specified pins
servo_init(Left_thigh, Left_calf, Right_thigh, Right_calf)

Servo_PROGRAM_Zero() # 90 90 90 90


Dance1 = [
    # GPIO5,GPIO16,GPIO18,GPIO17,time
    [50,90,80,90, 300],  #Left thigh to the lateral rotation
    [50,130,80,100, 300],#Left calf to the inward rotation
    [80,130,80,100, 300],#Left thigh to the inward rotation
    [60,130,80,100, 300],#Left thigh to the lateral rotation
    [80,130,80,100, 300],#Left thigh to the inward rotation

    [60,130,80,100, 300],#Left thigh to the lateral rotation
    [80,130,80,100, 300],#Left thigh to the inward rotation
    [60,130,80,100, 300],#Left thigh to the lateral rotation
    [80,130,80,100, 300],#Left thigh to the inward rotation
    [60,110,80,105, 300],#Left thigh to the lateral rotation，Left calf to the inward rotation

    [90,90,90,90, 300],  #Action initialization of biped robot
    [100,90,125,90, 300],#Right thigh to the lateral rotation
    [100,75,125,50, 300],#Right calf to the inward rotation
    [100,75,100,50, 300],#Right thigh to the inward rotation
    [100,75,120,50, 300],#Right thigh to the lateral rotation
    [100,75,100,50, 300],#Right thigh to the inward rotation

    [100,75,120,50, 300],#Right thigh to the lateral rotation
    [100,75,100,50, 300],#Right thigh to the inward rotation
    [100,75,120,50, 300],#Right thigh to the lateral rotation
    [100,75,100,50, 300],#Right thigh to the inward rotation

    [100,90,120,70, 300],#Right thigh to the lateral rotation，Right calf to the lateral rotation
    [90,90,90,90, 300],  #Action initialization of biped robot
]


while True:  
    Servo_PROGRAM_Run(Dance1, len(Dance1))
