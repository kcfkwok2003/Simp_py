# Simp-py 例子說明

## 標記說明:
* [M]: 只適用於 M5stack
* [W]: 只適用於 Wifikit32

## 例子簡要說明

### ex001_hello
在顯示器上印出hello world

### ex002_random
    在顯示器上隨機劃出點

### ex003_remote_songs
    等待遙距命令，如果收到相符合的曲名，便奏出樂曲。

* ex004_fix_me 練習用監察頁找出程式的錯誤。
* ex005_pwm_led [W] 用pwm 模式使8只led 輪流閃亮。
* ex006_kung_hei 用字節數組(byte array)砌出中文字“恭喜發財”。

ex007_birthday_song 奏生日歌，是根據網上的arduino 的代碼改寫為python的。
ex008_christmas 用字節數組(byte array)砌出英文草體“Merry Christmas”。
ex009_christmas_pwm [W]  在ex008 christmas 的基礎加上 ex005 的pwm led 走燈效果。
ex010_christmas_mix2 在 ex008 christmas 的基礎上加上 jingle bells 樂曲。
ex011_christmas_mix3 [W] 在 ex008 christmas 的基礎上加上 jingle bells 樂曲和pwm led 走燈效果。
ex012_hello 能被匯入到其他程式的hello (ex001) 版本。
ex013_kung_hei 能被匯入到其他程式的“恭喜發財”(ex006) 版本。
ex014_random2 能被匯入到其他程式的random (ex002) 版本。
ex015_sin 在顯示器上描出正弦函數。
ex016_intro simp-py簡介文字，引用了字體庫的幫助。
ex017_xled_kung_hei 用軟件方式實現spi 總線驅動多塊led 顯示“福、恭喜發財、新春大吉”。
ex018_xled_kung_hei 用硬件方式實現spi 總線驅動多塊led 顯示“福、恭喜發財、新春大吉”。
ex019_intro simp-py簡介文字， 用framebuffer實現螢幕滾動。
ex020_demo_loop 匯入前面多個例子順序運行。
ex021_demo_loop 匯入前面多個例子運行同時增加一線程(thread) 運行ex018 xled_kung_hei。
ex022_random3 [W] 在顯示器上隨機劃出點，並在隨機地用pwm 方式驅動8只led。
ex023_ntptime 連接internet 上的NTP 服務器取得當前時間。
ex024_scope 順時作模數(AD: analog to digital) 採集數據並繪出點圖及顯示輸入的數值和電位。
ex025_scope 以定時器回調(callback) 作模數(AD: analog to digital) 採集數據並繪出點圖及顯示輸入的數值和電位。
ex026_uresp 示範用監察頁的send 和MCU 進行遙距互動。
ex027_file_op 示範用監察頁的send 遙距進行MCU內的文件操作。
ex028_sd_op 示範用監察頁的send 遙距進行MCU內的SD 卡文件操作。
ex029_jpg [M] 在顯示器上顯示jpeg 相片


