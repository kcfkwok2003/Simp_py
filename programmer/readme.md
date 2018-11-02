V1.2 host todo: (simp-py windows and android)
  * fix about wrongly clearing edit area during 1st time upload (simp_py-android v1.1.14)
  * fix scaled.jpg recursive problem (win done) 
  * show path in title  (win done)
  * only AP mode can upload WIFI config and host code (win done) 
  * add host code for matching host and device, device will only accept host with same host code can write program (win done)
  * device will send uid to host. host should check again it to avoid connected to a wrong device.
  
V1.2 device todo:
  * when startup in AP mode, test.py will not auto run, press B to run
  * in startup info, show also host code (dev done)
  * when 3 button pressed, show startup info, 1st line of test.py
  * only AP mode can change WIFI config and host code
  * device will sent uid in each message.
  
working:
  * refer to protocol.txt 1.12
  1. add host code and connected device info in set page
  2. host should record and set the uid of the target device in set page
  3. only allow upload wifi config when ip is 192.168.4.1 otherwise host_r='reject'
  4. implement protocol 1.12 host code of ping in host side
  5. device: when start, show HOST_CODE
  6. device: when receive HOST_CODE not matched, set host_r to 'chk host', otherwise 'ok'
     device: resp with host_r when ping
  7. device: old simp-py without HOST_CODE use connection to reject?
  - device: when start in ap, not run test.py until b pressed  