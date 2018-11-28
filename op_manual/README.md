Simp-py 操作摘要 (v1.2.1)

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
<td><p><img src=".//media/image19.png" style="width:2.5in;height:2.5in" /></p>
<p>圖1</p></td>
<td><p>按一下M5Stack側面的紅色按鍵,約3秒後</p>
<p>LCD 亮起. 出現左圖畫面. 信息包括:</p>
<p>SIMP_PY 板本，例如 1.2</p>
<p>Wifi 接入點的名稱 (SSID) 例如 SIMP_PY-3640</p>
<p>網絡地址(IP address)，例如 192.168.4.1</p>
<ul>
<li><blockquote>
<p>如果test.py存在, 有可能因 test.py 的運行而看不到上述畫面, 請參照12.1 (1) 使test.py不運行.</p>
</blockquote></li>
<li><blockquote>
<p>如果SSID不是SIMP_PY-.. 和 IP 不是192.168.4.1, 請參照12.1 (2) 回复到初始狀態.</p>
</blockquote></li>
<li><blockquote>
<p>當M5Stack 在AP模式,IP 定是192.168.4.1, 此時不會運行test.py, 按下A鍵才會運行.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

M5Stack 側面的紅色按鍵是開關. 按一下開機, 連按兩下關機.

前面3個按鍵由左至右為A,B,C 按鍵.

4\. 經Wi-Fi連接M5Stack 的 AP 模式 (見附錄A1)

<table>
<tbody>
<tr class="odd">
<td><p><img src=".//media/image13.png" style="width:1.9375in;height:1.375in" /></p>
<p>圖2</p></td>
<td><p><img src=".//media/image1.png" style="width:1.9375in;height:3.05556in" /></p>
<p>圖3</p></td>
<td><p>在手機開啟Wi-Fi 連接到M5Stack.</p>
<p>進入Simp-py Apps, 按[Set..] 進入設定頁.(參考附錄B)</p>
<p>在Device IP欄輸入對應的ip 地址</p></td>
</tr>
</tbody>
</table>

5\. 取得器件資訊

<table>
<tbody>
<tr class="odd">
<td><p><img src=".//media/image14.png" style="width:2.97917in;height:3.08333in" /></p>
<p>圖4</p></td>
<td><p>在設定頁面按下[DevInfo] 便能經Wi-Fi 讀取器件資訊</p>
<p>顯示Device not match, set it? 表示Connected Device 內容不配合.</p>
<p>Passkey: ??? 表示passkey 未設定.</p>
<p>按[OK]設定Connected Device 內容.</p>
<p>要取得passkey, 記下Device info 內的資料, 到下列網站登記便可:</p>
<p><a href="http://simp-py.appspot.com/"><span class="underline">http://simp-py.appspot.com/</span></a></p></td>
</tr>
</tbody>
</table>

6\. 設定passkey

<table>
<thead>
<tr class="header">
<th><img src=".//media/image10.png" style="width:1.76339in;height:1.95313in" /></th>
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
<td><img src=".//media/image16.png" style="width:1.80208in;height:1.76389in" /></td>
<td><p><img src=".//media/image9.png" style="width:1.72917in;height:1.30556in" /></p>
<p>圖5</p></td>
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

8\. 下載課程例子

<table>
<tbody>
<tr class="odd">
<td><p><img src=".//media/image11.png" style="width:1.9375in;height:1.34722in" /></p>
<p>圖6</p></td>
<td><p><img src=".//media/image7.png" style="width:1.9375in;height:2.02778in" /></p>
<p>圖7</p></td>
<td>先到設定頁輸入正確課程編號 (Course code). 然按[help] 選 Download Course. 按 [ok] 便下載課程例子. 例子會放在/data/simp_py/simp_py_ex/course 內.</td>
</tr>
</tbody>
</table>

9\. 運行課程 例子

<table>
<tbody>
<tr class="odd">
<td><p><img src=".//media/image15.png" style="width:1.9375in;height:3.06944in" /></p>
<p>圖8</p></td>
<td><p><img src=".//media/image2.png" style="width:1.91421in;height:3.04688in" /></p>
<p>圖9</p></td>
<td><p>在主頁按[File], 選Open Examples</p>
<p>選t101.py</p>
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
<p>請嘗試用前述方法運行不同例子. 或嘗試修改部分內容.</p>
<p>Open : 打開存放在data/simp_py_dat內的文件. 可打開的文件後綴包括 py, txt, jpg, prj</p>
<p>如果是jpg 文件, 會進入Photo operator 頁, 可下調相片,生成程式和 prj 文件</p>
<p>New file: 清除編輯區, 輸入新文件名稱.</p>
<p>Font py : 如果當前文件後綴為txt, 會進入字體數據生成頁, 生成數據,程式和 prj 文件.</p>
<p>Reload : 如果使用外置的編輯工具修改了文件, 可在此按Reload 重新載入文件.</p></td>
</tr>
</tbody>
</table>

11\. 監測頁

在主頁按 \[Mon\] 便進入監測頁

11.1 監測運行

<table>
<tbody>
<tr class="odd">
<td><p><img src=".//media/image17.png" style="width:2.52515in;height:2.57813in" /></p>
<p>圖10</p></td>
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
<td><p><img src=".//media/image5.png" style="width:2.399in;height:4.2982in" /></p>
<p>圖11</p></td>
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

13\. Host code 和Connected Device

由於M5Stack 的IP 地址分配有可能因改變了而使手機和M5Stack 出現錯誤配搭.

Simp-py r1.2 開始在設定頁增加了 Host code 和Connected Device.

用戶可自行設定Host Code並上傳至M5Stack. 設定好後M5Stack 只會接受來自相同Host code 的 手機的命令.(AP
模式則無此限制) 用戶會在狀態欄看到chk\_host 的信息.此時用戶應查看M5Stack 的IP 地址並修改手機上的設定.

用戶如果有多部M5Stack 並使用相同Host code 時. 由於每部M5Stack 都有獨立的ID. Connected Device
可儲存上次連接的的M5Stack, 如果連錯了另一部M5Stack, 用戶會在狀態欄看到 uid not match 等信息.
此時用戶應查看M5Stack 的IP 地址並修改手機上的設定.

14\. Host code 和 通訊口(port) 設定 (不熟識網絡用戶請不要作此部份嘗試)

M5Stack 的默認通訊口為8080

Host code 如果包含有":" , 例如"STEM-000:80”

如果上傳給M5Stack, M5Stack 重啟後會使用通訊口80, 手機應在Device IP 項加入":80", 例如:
"192.168.1.123:80" 才能和M5Stack 通訊.

**附錄A M5stack WIFI 連接方式**

A1. AP (Access Point) 接入點模式

<table>
<tbody>
<tr class="odd">
<td><p>IP: 固定為: 192.168.4.1</p>
<p>無互聯網連線</p></td>
<td><img src=".//media/image18.png" style="width:3.55208in;height:2.125in" /></td>
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
<td><img src=".//media/image4.png" style="width:3.76042in;height:2.13889in" /></td>
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
<td><img src=".//media/image12.png" style="width:2.97917in;height:1.93056in" /></td>
</tr>
</tbody>
</table>

**附錄B 主頁簡介**

<table>
<tbody>
<tr class="odd">
<td><img src=".//media/image8.png" style="width:2.60353in;height:3.14063in" /></td>
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

**附錄C 設定頁簡介**

<table>
<tbody>
<tr class="odd">
<td><img src=".//media/image6.png" style="width:2.6367in;height:4.13021in" /></td>
<td><p>從上而下:</p>
<p>Device IP: M5Stack 的IP 地址</p>
<p>Wifi Configuration 部份包括:</p>
<ul>
<li><blockquote>
<p>Station ESSID</p>
</blockquote></li>
<li><blockquote>
<p>Station password</p>
</blockquote></li>
<li><blockquote>
<p>AP Default</p>
</blockquote></li>
<li><blockquote>
<p>AP password</p>
</blockquote></li>
<li><blockquote>
<p>Host code</p>
</blockquote></li>
</ul>
<p>前四項設定參考7.1和7.2</p>
<p>Host code 用戶可自行設定.</p>
<p>按[Upload] 會上傳此部份資料到M5Stack.</p>
<p>Course code: 設定此部份可下載相關課程例子.</p>
<p>Connected Device: 按下[DevInfo] 取得 M5Stack 的資訊(見第5節)及更改.</p></td>
</tr>
</tbody>
</table>

\[\] View station password: 鈎選會顯示Station password 項目內容.

\[\] View ap password: 鈎選會顯示AP password 項目內容.

\[Save\] : 作任何修改後, 應按\[Save\] 儲存.

\[DevInfo\] : 按此鍵可讀取M5Stack 資訊.(見第5節)

\[Upload\] : 按此鍵上傳Wifi Configuration 資料到M5Stack.

\[Rst\] : 按此鍵令M5Stack 重啟.

\[Passkey\] : 按此鍵進行Passkey 操作.(見第6節)

\[Back\] : 返回主頁.

**附錄D \[help\] 簡介**

在主頁按下\[help\] 出現幫助選項

<table>
<tbody>
<tr class="odd">
<td><img src=".//media/image7.png" style="width:1.9375in;height:2.02778in" /></td>
<td><p>Help content : 進入幫助頁</p>
<p>Download GNUFont : 下載GNU 中文字庫</p>
<p>Download Course: 下載課程例子. Course code 要先在設定頁設好.</p>
<p>Clean course : 把先前下載的課程例子清除.</p>
<p>Download Simulator : 下載M5Stack 模擬器.</p></td>
</tr>
</tbody>
</table>

**附錄E M5Stack 模擬器 簡介(只適合用於教學示範或實驗性質)**

M5Stack 模擬器是用python 和py-game 寫成的.

在Android 上運行模擬器:

按裝pydroid3, 然後用 pip 安娤paho-mqtt 模組.

在pydroid3 內打開/data/simp\_py\_dat/simulator.py 然後運行.

Simulator.py 便會模擬M5Stack 環境打開/data/simp\_py\_dat/test.py 並運行.

可在Pydroid3 的編輯器修改test.py 或在simp\_py 內修改某文件, 然後儲存時選擇"Also save to
test.py” 便可.

如果用Pydroid3 修改了和Simp\_py 載入的相同文件. 在Simp\_py 中按\[File\] 然後選擇reload 重新載入.

**附錄F \[Upld\] 操作簡介**

<table>
<tbody>
<tr class="odd">
<td><img src=".//media/image20.png" style="width:1.78646in;height:1.51235in" /></td>
<td><p>Upload as test.py: 把文件上載至M5Stack 為test.py.</p>
<p>M5Stack 開機後只會運行test.py</p>
<p>Upload : 把文件上載至M5Stack (保留原文件名)</p>
<p>Upload binary: 上載 jpg (相片) 文件時要選這項</p>
<p>Upload files in prj : 把prj 文件中所列的文件上載至M5Stack. 上載時會自動選合適格式. Prj 文件最後一行如果有..&gt;test.py. 該文件會上載為test.py. 不需上載的文件名可在前面加上#.</p></td>
</tr>
</tbody>
</table>
