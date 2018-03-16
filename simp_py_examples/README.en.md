# Simp-py examples description

## remarks:
* [M]: available for M5stack only
* [W]: available for Wifikit32 only

## brief description fro each example

### ex001_hello
Show "hello world" on screen

### ex002_random
Show random points on screen

### ex003_remote_songs
Wait remote command. When received name match, play the melody

### ex004_fix_me
Bugs are included, try to find all out using the monitor page function.

### ex005_pwm_led [W]
Use PWM mode to drive 8 led to flash

### ex006_kung_hei
Use byte array to show chinese “恭喜發財”。

### ex007_birthday_song
Play a birthday song. It is rewrite to python code from arduino code on a web site

### ex008_christmas
Use byte array to draw English hand writing letter “Merry Christmas”。 

### ex009_christmas_pwm [W]
Base on codes from ex008 christmas and add ex005 pwm led effect. 

### ex010_christmas_mix2
Base on ex008 christmas and add jingle bells song. 

### ex011_christmas_mix3 [W]
Base on ex008 christmas, add jingle bells song and pwm led effect  

### ex012_hello
Rewrite ex001 hello that can be imported to other program

### ex013_kung_hei
Rewrite ex006 “恭喜發財 that can be imported to other program

### ex014_random2
Rewrite ex002 random that can be imported to other program

### ex015_sin
Show mathematical sin curve on screen

### ex016_intro
Show chinese simp-py introduction, with the help of font library. 

### ex017_xled_kung_hei
Use software spi bus to drive matrix led to show “福、恭喜發財、新春大吉”。

### ex018_xled_kung_hei
Use hardware spi bus to drive matrix led to show “福、恭喜發財、新春大吉”。

### ex019_intro
As ex016_intro, but use framebuffer to scroll the screen

### ex020_demo_loop
A demo loop to sequentially import other examples and execute them.

### ex021_demo_loop
A demo loop as ex020, at the same time to run ex018 xled_kung_hei on another thread.

### ex022_random3 [W]
Show random points on screen at the same time randomly flash 8 led by pwm

### ex023_ntptime
Connect to internet to get current date time from NTP server.

### ex024_scope
Use AD(Analog to digital) input to collect data and plot the curve and value

### ex025_scope
Same as ex024 but using timer callback to collect data

### ex026_uresp
Demonstrate to use monitor page to send command to MCU to do remote interaction.

### ex027_file_op
Demonstrate to use monitor page to do remote file operation on MCU 

### ex028_sd_op [M]
Demonstrate to use monitor page to do remote SD card file operation on MCU

### ex029_jpg [M]
Show a jpeg photograph on screen

### ex030_mpu9250 [M]
MPU-9250 test, MPU-9250 contains MPU-6500 (3-axis gyroscope and 3-axis accelerometer) and an AK8963 (3-axis digital compass)

### ex031_mqtt [M]
Mqtt IOT (internet of thing) protocol test
