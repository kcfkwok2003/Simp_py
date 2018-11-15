V1.2 host todo: (simp-py windows and android)
  a1 fix about wrongly clearing edit area during 1st time upload (simp_py-android v1.1.14) (android changed)
  a2 fix scaled.jpg recursive problem (win done) (android changed) 
  a3 show path in title  (win done)  (android changed)
  a4 only AP mode can upload WIFI config and host code (win done) (android changed) 
  a5 add host code for matching host and device, device will only accept host with same host code can write program (win done) (android changed)
  a6 device will send uid to host. host should check again it to avoid connected to a wrong device. (win done) (android changed)
  a7 host can connect to device port other than 8080, specified by ip:port (win done) 
  a8 add reload option in File menu to reload file edited by external editor (win done) (android changed)
  a9 add new and open prj file (win done)
  a10 add upload "files in prj" (win done)
  a11 save prj from course folder ask for copy files in prj (win done)
  
V1.2 device todo:
  * when startup in AP mode, test.py will not be run (dev done)
  * in startup info, show also host code (dev done)
  * only AP mode can change WIFI config and host code (dev done)
  * device will sent uid in each message. (dev done)
  * device can use port other than 8080 according to host_code with ':[port]'
  * when startup in AP mode, press A to run test.py

working for host android:
  1. a2 fix scaled.jpg recursive problem (changed)
  2. a3 show path in title (changed)
  3. a4 only ap mode can upload wifi config (changed)
  4. add host code and connected device in settings screen (changed)
  5. upload wifi config with host_code (changed)
  6. ping with host (changed)
  7. set uid with devinfo (changed)
  8. no more ping before upload (changed)
  9. add reload in file operation (changed)
  10. upload with host code (changed)
  11. rst with host code (changed)
  12. mon with host code (Changed)
  13. a6 host check uid not match with message show (changed)
  14. a7 use port other than 8080
  
  
working:
  * refer to protocol.txt 1.12
  1. add host code and connected device info in set page
  2. host should record and set the uid of the target device in set page
  3. only allow upload wifi config when ip is 192.168.4.1 otherwise host_r='reject'
  4. implement protocol 1.12 host code of ping in host side
  5. device: when start, show HOST_CODE
  6. device: when receive HOST_CODE not matched, set host_r to 'chk host', otherwise 'ok'
     device: resp with host_r when ping
  7. host: host should send host code before any action except in ap mode
  8. device: when start up in AP mode, test.py will not be run
  - device: when start in ap, not run test.py until b pressed  