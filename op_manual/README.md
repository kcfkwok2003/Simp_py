Simp-py 操作摘要 (v1.2)

1\. 從google play(暫時只適用於香港) 安裝Simp-py app (Android 5.0 或以上)

Ref:
[<span class="underline">https://play.google.com/store/apps/details?id=com.tienlink.simp\_py</span>](https://play.google.com/store/apps/details?id=com.tienlink.simp_py)

2\. 如自行安裝M5Stack Simp-py 固件,
請到此下載:

[<span class="underline">https://github.com/kcfkwok2003/Simp\_py/tree/master/vagrant/m5s/bin</span>](https://github.com/kcfkwok2003/Simp_py/tree/master/vagrant/m5s/bin)

需要先安裝esptool, esptool
下載及安裝說明:

[<span class="underline">https://github.com/espressif/esptool</span>](https://github.com/espressif/esptool)

參考erflash.sh 及wrflash.sh 清除及寫入固件(需修改port 參數)

3\. 啓動M5Stack 並進入AP 模式 (見附錄A1)

<table>
<tbody>
<tr class="odd">
<td><img src=".//media/image18.png" style="width:2.39063in;height:2.39898in" /></td>
<td><p>按一下M5Stack側面的紅色按鍵,約3秒後</p>
<p>LCD 亮起. 出現左圖畫面. 信息包括:</p>
<p>SIMP_PY 板本，例如 1.0.9a</p>
<p>Wifi 接入點的名稱 (SSID) 例如 SIMP_PY-9EDC</p>
<p>網絡地址(IP address)，例如 192.168.4.1</p>
<ul>
<li><blockquote>
<p>如果test.py存在, 有可能因 test.py 的運行而看不到上述畫面, 請參照12.1 (1) 使test.py不運行.</p>
</blockquote></li>
<li><blockquote>
<p>如果SSID不是SIMP_PY-.. 和 IP 不是192.168.4.1, 請參照12.1 (2) 回复到初始狀態.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

4\. 經Wi-Fi連接M5Stack 的 AP 模式 (見附錄A1)

<table>
<tbody>
<tr class="odd">
<td><img src=".//media/image7.png" style="width:1.9375in;height:1.375in" /></td>
<td><img src=".//media/image16.png" style="width:1.9375in;height:3.06944in" /></td>
<td><p>在手機開啟Wi-Fi 連接到M5Stack.</p>
<p>進入Simp-py Apps, 按[Set..] 入設定頁.</p>
<p>在Device IP欄輸入對應的ip 地址</p></td>
</tr>
</tbody>
</table>

5\. 取得器件資訊

<table>
<tbody>
<tr class="odd">
<td><img src=".//media/image17.png" style="width:2.97917in;height:3.54167in" /></td>
<td><p>在設定頁面按下[DevInfo] 便能經Wi-Fi 讀取器件資訊</p>
<p>Passkey: ??? 表示passkey 未設定.</p>
<p>要取得passkey, 記下Device info 內的資料, 到下列網登記便可:</p>
<p><a href="http://simp-py.appspot.com/"><span class="underline">http://simp-py.appspot.com/</span></a></p></td>
</tr>
</tbody>
</table>

6\. 設定passkey

<table>
<thead>
<tr class="header">
<th><img src=".//media/image1.png" style="width:1.76339in;height:1.95313in" /></th>
<th><img src=".//media/image3.png" style="width:1.71542in;height:1.85938in" /></th>
<th><p>在設定頁按[Passkey], 然後選 Upload passkey by hand.</p>
<p>按[ok],</p>
<p>輸入passkey 再按[ok] 確定.</p>
<p>在收到resp ok 後, 按[Rst] 重啟M5Stack.</p>
<p>No valid passkey 不再出現</p>
<p>成功後,可選擇Backup passkey to file 把passkey 儲存在手機上.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src=".//media/image2.png" style="width:1.80208in;height:1.76389in" /></td>
<td><img src=".//media/image6.png" style="width:1.72917in;height:1.30556in" /></td>
<td><p>如果你因升級或重寫固件.而之前已備份了passkey 文件,可.</p>
<p>在設定頁按[Passkey], 然後選 Upload passkey from file.</p>
<p>按[ok], 看見右圖信息再按[ok] 確定.</p>
<p>在收到resp ok 後, 按[Rst] 重啟M5Stack.</p>
<p>No valid passkey 不再出現</p></td>
</tr>
</tbody>
</table>

7\. 更改M5Stack Wi-Fi 設定以接通互聯網

7.1 經內聯網接通互聯網 (見附錄 A2.工作站模式(在內聯網))

<table>
<tbody>
<tr class="odd">
<td><p>如要使M5Stack 經內聯網接通互聯網, 在設定頁設定如下信息:</p>
<p>Station ESSID: 輸入Wi-Fi路由器名稱</p>
<p>Station password: 輸入Wi-Fi路由器密碼</p>
<p>AP Default: 輸入0</p>
<p>AP Password: 在沒法連上路由器或AP Default 為1 時, 經Wi-Fi 連接M5Stack 的密碼. (不能少於8個字)</p>
<p>按[Save], 按[Upload], 見Upload Wifi config 提示後按ok</p>
<p>确定上載成功後可重啟M5Stack</p>
<p>M5Stack 重啟後連上Wi-Fi 路由器會顯示新的 IP 地址. 例如192.168.1.100</p>
<p>手機也要連上相同的Wi-Fi 路由器</p>
<p>在設定頁的Device IP欄輸入 M5Stack 的 IP 地址.</p>
<p>按[Save], 按[DevInfo], 如能顯示器件資訊, 表示連接成功.</p></td>
</tr>
</tbody>
</table>

7.2 經手機熱點接通互聯網 (見附錄 A3.工作站模式(手機熱點))

<table>
<tbody>
<tr class="odd">
<td><p>如要使M5Stack 經手機熱點接通互聯網, 在設定頁設定如下信息:</p>
<p>Station ESSID: 輸入手機熱點SSID名稱</p>
<p>Station password: 輸入手機熱點Wi-Fi密碼</p>
<p>AP Default: 輸入0</p>
<p>AP Password: 在沒法連上路由器或AP Default 為1 時, 經Wi-Fi 連接M5Stack 的密碼. (不能少於8個字)</p>
<p>按[Save], 按[Upload], 見Upload Wifi config 提示後按ok</p>
<p>确定上載成功後, 使手機切換到熱點模式.</p>
<p>當手機成功切換到熱點模式後, 才可重啟M5Stack</p>
<p>M5Stack 重啟後連上Wi-Fi 路由器會顯示新的 IP 地址. 例如192.168.43.10</p>
<p>在設定頁的Device IP欄輸入 M5Stack 的 IP 地址.</p>
<p>按[Save], 按[DevInfo], 如能顯示器件資訊, 表示連接成功.</p></td>
</tr>
</tbody>
</table>

8\.
下載課程例子

|                           |                          |                                                                                                                   |
| ------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| ![](.//media/image12.png) | ![](.//media/image9.png) | 先到設定頁輸入正確課程編號 (Course code). 然按\[help\] 選 Download Course. 按 \[ok\] 便下載課程例子. 例子會放在/data/simp\_py/simp\_py\_ex/ 內. |

9\. 運行課程 例子

<table>
<tbody>
<tr class="odd">
<td><img src=".//media/image10.png" style="width:1.9375in;height:3.45833in" /></td>
<td><img src=".//media/image8.png" style="width:1.9375in;height:3.5in" /></td>
<td><p>在主頁按[File], 選Open Examples</p>
<p>進入course 文件夾, 選t101.py</p>
<p>按[Ping]測試連接狀況。</p>
<p>按[upld] , 選Upload as test.py, 按[ok]</p>
<p>上載成功後會問是否”Reset the device?” 按[OK]</p>
<p>重啟M5Stack,</p>
<p>重啟後, M5Stack 顯示hello</p></td>
</tr>
</tbody>
</table>

10\. 修改程式

<table>
<tbody>
<tr class="odd">
<td><p>在主頁按[File], 選:</p>
<p>Save: 把文件以相同名稱存放入data/simp_py_dat 內. 儲存會問&quot;Also save to test.py”, 按 [OK] 便多存儲一份為 test.py</p>
<p>Save as : 把文件以不同名稱存放入data/simp_py_dat 內.</p>
<p>請嘗試用前述方法運行不同例子. 或嘗試修改部分內容.</p></td>
</tr>
</tbody>
</table>

11\. 監測頁

在主頁按 \[Mon\] 便進入監測頁

11.1 監測運行

<table>
<tbody>
<tr class="odd">
<td><img src=".//media/image4.png" style="width:2.52515in;height:2.57813in" /></td>
<td><p>按 [Start] 開始監測</p>
<p>按 [Stop] 結朿監測</p>
<p>如果程式有異常(Exception), 會看見如_exc:Traceback 等</p>
<p>按 [Clr] 清除頁面資料</p>
<p>按 [Back] 回到主頁面</p></td>
</tr>
</tbody>
</table>

11.2 即時命令或運行文件

<table>
<tbody>
<tr class="odd">
<td><img src=".//media/image11.png" style="width:2.399in;height:4.2982in" /></td>
<td><p>即時命令:</p>
<p>例如輸入tft.off() 按[Send] 可關 lcd 背光, 輸入 tft.on(), 按[Send] 可重開 lcd 背光.</p>
<p>運行文件:</p>
<p>開啟文件 t102.py</p>
<p>按[Ping]測試連接狀況。</p>
<p>按[upld] , 選Upload, 按[ok]</p>
<p>按[Mon], 進入測試頁, 輸入:</p>
<p>import t102</p>
<p>按[Send], 顯示器將劃出一個點.</p>
<p>注意: 如果文件再更改上傳後, 要運行下面幾句:</p>
<table>
<thead>
<tr class="header">
<th>import sys<br />
del sys.modules['t102']<br />
import t102</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>* 程式不能Loop 死, 否則不能接收下一命令</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

12\. 其他

需要直接連接, 但連不到, 或忘記密碼的處理

12.1 開啓M5Stack 時不運行test.py

1)  > 開啓M5Stack, 當背光亮起時按著A鍵不放, 直至出現ip地址後一秒才放A鍵. Test.py 不會運行.

此時營幕上會顯示press key again to clear wifi settings.

(2) 再下A鍵便清除現在的Wifi 設定, 回复到初始狀態.

12.2 如果手機開了Bluetooth, 便可能連接不上Ｍ5Stack, 請關上Bluetooth.

12.3 Android 7.0以上版本, 設定Wifi 直接連接Ｍ5Stack時（附錄A1) , 由於此路徑不接通Internet ,
會彈出確認框, 請進行確認, 在頂列也要出現wifi 符號, 否則會連接不上 M5Stack.

**附錄A M5stack WIFI 連接方式**

A1. AP (Access Point) 接入點模式

<table>
<tbody>
<tr class="odd">
<td><p>IP: 固定為: 192.168.4.1</p>
<p>無互聯網連線</p></td>
<td><img src=".//media/image13.png" style="width:3.55208in;height:2.125in" /></td>
</tr>
</tbody>
</table>

A2.工作站(Station)模式(在內聯網)

<table>
<tbody>
<tr class="odd">
<td><p>IP 由DHCP server 分配</p>
<p>經路由器連上互聯網</p>
<p>例如:</p>
<p>192.168.0.100</p>
<p>192.168.1.22</p></td>
<td><img src=".//media/image14.png" style="width:3.76042in;height:2.13889in" /></td>
</tr>
</tbody>
</table>

A3. 工作站(Station)模式(手機熱點)

<table>
<tbody>
<tr class="odd">
<td><p>IP 由手機熱點(Hot spot) 分配</p>
<p>經手機連上互聯網</p>
<p>例如:</p>
<p>192.168.43.100</p></td>
<td><img src=".//media/image15.png" style="width:2.97917in;height:1.93056in" /></td>
</tr>
</tbody>
</table>

**附錄B 主頁簡介**

<table>
<tbody>
<tr class="odd">
<td><img src=".//media/image5.png" style="width:2.97917in;height:3.59722in" /></td>
<td><p>從上而下:</p>
<p>標題欄: Simp-py 及檔名</p>
<p>編輯區: 程式文件在此顯示.</p>
<p>狀態區: 顯示操作結果</p>
<p>按鍵區: 按鍵說明如下</p>
<p>[File] : 文件操作</p>
<p>[Set..] : 進入設定頁</p>
<p>[Ping] : 測試和M5Stack 的連接.</p>
<p>[Upld] : 上載程式.</p>
<p>[Rst] : 重啟M5Stack</p>
<p>[Mon] : 進入監測頁</p>
<p>[Help] : 輔助操作</p></td>
</tr>
</tbody>
</table>
