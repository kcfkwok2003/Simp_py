
# 1. 安裝固件遇到的問題

## 1.1 安裝固件後, MCU 開機顯示:
```
No valid passkey
Wait 10s
..........ok
```
passkey 是什麼?

答:
  passkey 是根據 MCU 的 unique ID 而生成, 因此每塊MCU 的passkey 都不同, 加入這功能是為了方便用戶做知識產權審計及交易用途.
  
  經分銷或培訓班取的 MCU 會預先安裝了passkey, 為免MCU 內的passkey 意外丟失,用戶可在Android Simp-py Apps 上備份passkey. 步驟: [Set..] -> [Passkey] -> []Backup passkey to file -> [OK]
  
  在沒有passkey情況, MCU 仍然是可以進行實驗的, 大部分例子仍可以運行.只是有以下兩點要注意:
  * 無綫設定 WIFI configuration 沒有作用, MCU 會連上路由器.
  * MCU 仍然可以作為無綫接入點(Wifi access point)使用, 但密碼不能更改.(預設為12345678)

  要取得 passkey, 用戶需提供 MCU 的 unique ID. 可按後述步驟讀取 MCU 的 unique ID: [Set..] -> [DevInfo], "UID:" 後的數字即為 MCU 的 unique ID.
  
  
  取得passkey 文件名會是 pass_xxxxxx.key, 其中xxxxxx 對應 MCU 的 unique ID. 將文件放入 sdcard/data/simp_py_dat 內, 在Android Simp-py Apps 內按後述步驟完成: [Set..] -> [Passkey] -> [] Upload passkey from file -> [OK]


  

