# Running the ex020_demo_loop.py or ex021_demo_loop.py on M5Stack

## Install instruction:

### Install firmware to M5Stack
```
  Download url https://github.com/kcfkwok2003/Simp_py/tree/master/dist
  Choose the updated version from m5stack-x.y.z
  refer to erflash.sh to erase flash
  refer to wrflash.sh to write firmware to MCU
```
### Install simp-py on android
  Search simp-py in google play store and install
  
## Connect wifi
  1. power up the M5Stack, it will show the essid and ip address
     ```
     Essid: e.g SIMP_PY-XXXX 
     IP:     e.g. 192.168.4.1
     ```
  2. In android, connect the wifi to SIMP_PY-XXXX
     ```
     in Simp-py on android,
     press [Set..] to enter settings screen,
     change the Device IP to the IP shown on M5Stack.
     press [Save] and [Ping], if the you see something response ok. It works
     ```
     
## If you have no led matrix (drive with Max7219), you can try ex020_demo_loop.py
  1. Upload following files: (When open file select "Open data/simp_py_ex", then select files in m5stack folder. When upload, select "upload only" option)
  ```
   ex011_christmas_mix2.py 
   ex012_hello.py 
   ex013_kung_hei.py
   ex014_random2.py
   ex015_sin.py
   ex019_intro.py
   ch_intro_font.py   
   ch_intro.txt
  ```
  
  2. Upload following file (When open file select "Open data/simp_py_ex", then select files in m5stack folder. When upload, select "upload as test.py" option)
  ```
   ex020_demo_loop.py
  ```
  
  3. press [Rst] to send reset to the mcu

## If you have led matrix (drive with Max7219), you can try ex021_demo_loop.py 
  1. Upload following files: (When open file select "Open data/simp_py_ex", then select files in m5stack folder. When upload, select "upload only" option)
  ```
   ex011_christmas_mix2.py 
   ex012_hello.py 
   ex013_kung_hei.py
   ex014_random2.py   
   ex015_sin.py
   ex018_xled_kung_hei.py
   ex019_intro.py
   ch_intro_font.py   
   ch_intro.txt
   ch_kung_hei_font.py
   ```
   
  2. Upload following file (When open file select "Open data/simp_py_ex", then select files in m5stack folder. When upload, select "upload as test.py" option)
```
   ex021_demo_loop.py
```
  3. press [Rst] to send reset to the mcu
