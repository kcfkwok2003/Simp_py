# 在 Wifi Kit 32 上運行  ex020_demo_loop.py 或 ex021_demo_loop.py
## 安裝指示
### 安裝simp-py 固件到M5tack
```
 下載網址 https://github.com/kcfkwok2003/Simp_py/tree/master/dist
 選擇最迎新版本文件夾 m5stack-x.y.z
 下載後下列腳本寫入固件: erflash.sh, wrflash.sh
```

### 在android 手機上安裝 simp-py 編程應用程式
在google play store 搜尋simp-py 並安裝，或在github 下載安裝。

## 連接無線(Wifi)
 1. 供電 M5Stack, 它會顯示 essid 和 ip 地址
    ```
    Essid: 例如 SIMP_PY-XXXX
    IP:     例如 192.168.4.1
    ```
 2. 在 android 手機連上以上無線網 (即 SIMP_PY-XXXX) 密碼預設為12345678
    ```
    在android 上運行 Simp-py 後
    按 [Set..] 進入 settings 頁面
    更改Device IP 和 M5Stack 顯示的 ip 一致
    按 [Save] 儲存。
    按 [DevInfo], 如果收到回應就表示ok
    ```
    
## 如果沒有帶 led matrix (Max7219 驅動), 你可嘗試運行ex020_demo_loop.py
 1. 上載下列文件 (安 [File] 然後選 "Open data/simp_py_ex", 再進 m5stack 文件夾，開啟 ex020_demo_loop.py 後，按[Upld] 選Upload 後按 [ok]. )
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
 2. 上載以下文件為測試程式(如上一步驟開啟文件，上載時選“Upload as test.py”)
 ```
  ex020_demo_loop.py
 ```
 3. 按[Rst] 重啟MCU，MCU重啟後便會運行上述演示程式。

## 如果你有 led matrix (Max7219 驅動), 你可嘗試運行 ex021_demo_loop.py
 1. 上載下列文件 (安 [File] 然後選 "Open data/simp_py_ex", 再進 m5stack 文件夾，開啟 ex020_demo_loop.py 後，按[Upld] 選Upload 後按 [ok]. )
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
  2. 上載以下文件為測試程式(如上一步驟開啟文件，上載時選“Upload as test.py”)
```
  ex021_demo_loop.py
```
 3. 按[Rst] 重啟MCU，MCU重啟後便會運行上述演示程式。


