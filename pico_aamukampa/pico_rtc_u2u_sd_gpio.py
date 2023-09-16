'''
Pico U2U RTC SD  GPIO
'''
'''
import time
import board
import busio
import terminalio
import displayio
import digitalio
import microcontroller
'''
TX0_PIN      = board.GP0
RX0_PIN      = board.GP1
TX1_PIN      = board.GP8
RX1_PIN      = board.GP9
EN_I2C_PIN   = board.GP2
I2C0_SDA_PIN = board.GP4
I2C0_SCL_PIN = board.GP5
I2C1_SDA_PIN = board.GP6
I2C1_SCL_PIN = board.GP7
PWM7A_PIN    = board.GP14
PWM7B_PIN    = board.GP15
SD_CS_PIN    = board.GP17
SD_MOSI_PIN  = board.GP18
SD_CLK_PIN   = board.GP19
SD_MISO_PIN  = board.GP16
RTC_CLK_PIN  = board.GP21
RGB1_PIN     = board.GP20
RGB2_PIN     = board.GP22



'''
# pwma = digitalio.DigitalInOut(PWM7A_PIN)
sd_cs = digitalio.DigitalInOut(SD_CS_PIN)
sd_cs.direction = digitalio.Direction.OUTPUT
sd_mosi = digitalio.DigitalInOut(SD_MOSI_PIN)
sd_mosi.direction = digitalio.Direction.OUTPUT
sd_clk = digitalio.DigitalInOut(SD_CLK_PIN)
sd_clk.direction = digitalio.Direction.OUTPUT
tx0 = digitalio.DigitalInOut(TX0_PIN)
tx0.direction = digitalio.Direction.OUTPUT
tx1 = digitalio.DigitalInOut(TX1_PIN)
tx1.direction = digitalio.Direction.OUTPUT

i2c0_sda = digitalio.DigitalInOut(I2C0_SDA_PIN)
i2c0_sda.direction = digitalio.Direction.OUTPUT
i2c0_scl = digitalio.DigitalInOut(I2C0_SCL_PIN)
i2c0_scl.direction = digitalio.Direction.OUTPUT

i2c1_sda = digitalio.DigitalInOut(I2C1_SDA_PIN)
i2c1_sda.direction = digitalio.Direction.OUTPUT
i2c1_scl = digitalio.DigitalInOut(I2C1_SCL_PIN)
i2c1_scl.direction = digitalio.Direction.OUTPUT

pwm7a = digitalio.DigitalInOut(PWM7A_PIN)
pwm7a.direction = digitalio.Direction.OUTPUT
'''

# yellow_button.switch_to_input(pull=digitalio.Pull.UP)


'''
test = pwm7a
while 1:
    test.value = not test.value
    print(test.value)
    time.sleep(2.0)
 '''
