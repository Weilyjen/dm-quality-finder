# 🩸 全台糖尿病院所品質查詢與比對器 (115年第1季)

> **零伺服器成本 · 100% 純靜態單頁應用 (SPA) · 手機/平板/電腦即開即用**  
> 資料來源：衛生福利部中央健康保險署公開品質資訊（共收錄全台 7,765 家院所）

---

## 🌟 核心特色

1. **雙模式切換**：
   * 🟢 **民眾模式（單選複製 · LINE查品質）**：卡片式大字體呈現，依縣市/鄉鎮篩選、照護率排序。每張卡片皆提供 **「LINE 查品質」**、**「複製代碼」** 與 **「健保官方明細」** 一鍵按鈕（完全隱藏 Telegram，保障診所伺服器資源與社群安全）。
   * 👨‍⚕️ **醫師模式（最多10家多選比對 · 專屬AI服務）**：專業同儕表格檢視，提供 Checkbox 多選（上限 10 家）。底部常駐懸浮抽屜，一鍵生成並複製 `/quality 代碼1 代碼2...` 指令，並彈出「加入【診所醫師AI服務】Telegram 私密群組」審核須知（**提醒必須透過 FB 或 LINE 告知鄭院長真實服務醫院與醫師身分，經審核確認後才會核准入群**）。
2. **極速篩選與流暢操作**：
   * 7,765 筆資料本地端毫秒級即時搜尋、縣市連動、指標排序。
   * 自適應深色/淺色主題（Dark/Light Mode）。
3. **100% 永久免費託管相容**：
   * 無需任何資料庫或 Python 後端，可免費放在 GitHub Pages、Cloudflare Pages、Netlify 等任何靜態空間。

---

## 📂 檔案架構

| 檔案名稱 | 用途說明 | 檔案大小 |
| :--- | :--- | :--- |
| `index.html` | 響應式單頁應用程式主程式（含現代化 CSS 與完整互動邏輯） | ~52 KB |
| `county_stats.html` | 📊 **115Q1 各縣市糖尿病在全部醫院與全部診所人數及品質均值全覽** | ~28 KB |
| `champions.html` | 🏆 **115Q1 台灣各縣市糖尿病收案冠軍診所專題頁**（落實分級醫療、在地就醫） | ~164 KB |
| `county_dm_data.js` | 22 縣市醫院與診所人數及品質均值結構化資料庫 (JS) | ~58 KB |
| `county_dm_data.json` | 22 縣市醫院與診所人數及品質均值結構化資料庫 (JSON) | ~58 KB |
| `champions_full_data.json` | 22 縣市冠軍診所與 20 項健保品質指標完整結構化資料庫 | ~35 KB |
| `dm_clinics_data.js` | 結構化院所資料（讓本機直接雙擊開啟，免架 Web Server） | ~739 KB |
| `dm_clinics_115q1.json` | 輕量化 JSON 資料檔（供 API / Fetch 使用） | ~738 KB |


---

## 🚀 3 分鐘免費發布上線教學

### 方案 A：發布到 GitHub Pages（最推薦 · 永久免費 · 穩定）

1. 登入您的 [GitHub](https://github.com/) 帳號，點擊 **New Repository** 建立一個新的公開儲存庫（例如命名為 `dm-quality-finder`）。
2. 將本資料夾內的 `index.html`、`dm_clinics_data.js`、`dm_clinics_115q1.json` 上傳到倉庫根目錄。
3. 進入該儲存庫的 **Settings** ➔ 點擊左側 **Pages**。
4. 在 **Branch** 選擇 `main`（或 `master`），資料夾選擇 `/ (root)`，點擊 **Save**。
5. 等候 1~2 分鐘，即可獲得免費的全球訪問網址：
   ```text
   https://<您的GitHub使用者名稱>.github.io/dm-quality-finder/
   ```

---

### 方案 B：發布到 Cloudflare Pages（拖拉即上線 · 速度極快）

1. 登入 [Cloudflare Dashboard](https://dash.cloudflare.com/) ➔ 點擊 **Workers & Pages** ➔ **Create Application** ➔ 選擇 **Pages**。
2. 選擇 **Upload Assets (直接上傳資產)**。
3. 將本資料夾（`web_dm_quality`）整個拖拉放進網頁上傳區。
4. 點擊 **Deploy**，30 秒內即可獲得全球 CDN 免費網址（例如 `https://dm-quality-finder.pages.dev`），還可直接免費綁定您的自訂網域！

---

### 方案 C：本機離線直接開啟

* 無需安裝任何伺服器軟體，直接以滑鼠雙擊 `index.html`，即可在 Chrome、Safari、Edge 瀏覽器中完全離線順暢使用！

---

## 🔗 與 Line Bot 及 Telegram Bot 連動語法

* **Telegram Bot (`@WellcomeClinic_bot`)**：
  * 指令語法：`/quality <機構代碼1> <機構代碼2> ...`（最多 10 家）
  * 範例：`/quality 3534021927 3512011276 3501195270`
* **LINE 官方帳號 (`line.23092807.com`)**：
  * 民眾查詢語法：`查品質 3534021927` 或直接傳送 `3534021927`
