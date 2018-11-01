V1.2 host todo: (simp-py windows and android)
  * fix about wrongly clearing edit area during 1st time upload (simp_py-android v1.1.14)
  * fix scaled.jpg recursive problem 
  * show path in title 
  * only AP mode can upload WIFI config and host code 
  * add host code for matching host and device, device will only accept host with same host code can write program 
  * device will send uid to host. host should check again it to avoid connected to a wrong device.
  
V1.2 device todo:
  * when startup in AP mode, test.py will not auto run, press B to run
  * in startup info, show also host code
  * when 3 button pressed, show startup info, 1st line of test.py
  * only AP mode can change WIFI config and host code
  * device will sent uid in each message.
  
working:
  * refer to protocol.txt 1.12
  1. add host code and connected device info in set page
  2. host should record and set the uid of the target device in set page
  3. only allow upload wifi config when ip is 192.168.4.1
  4. implement protocol 1.12 host code of ping in host side
  5. device: when start, show HOST_CODE
  6. device: when receive HOST_CODE not matched, set h_ip_f to false
     device: resp with '?h/ip' instead of ok 
  - device: when start in ap, not run test.py until b pressed  