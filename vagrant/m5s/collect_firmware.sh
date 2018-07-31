# To make the firmware
# cp the simp_py/esp32_simp_py/m5s to d:/kcf_esp32/esp8266-micropython-vagrant/
# in vagrant vm
# cd /vagrant/m5s
# python sync_modules.py # cp the py to micropython directory
# cd ~/MicroPython_ESP32_psRAM_LoBo-master/MicroPython_BUILD
# ./BUILD.sh menuconfig
#  for 4M psram:
#    in Component config --> ESP32-specific --> [*] Support for external, SPI-connected RAM
#    otherwise, turn off [*] to  []
# ./BUILD.sh clean
# ./BUILD.sh all -v
# cd /vagrant/m5s
cp /home/vagrant/MicroPython_ESP32_psRAM_LoBo-master/MicroPython_BUILD/build/*.bin /vagrant/m5s/bin/
cp /home/vagrant/MicroPython_ESP32_psRAM_LoBo-master/MicroPython_BUILD/build/bootloader/*.bin /vagrant/m5s/bin/

