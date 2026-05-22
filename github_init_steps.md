# 個人助理專案：GitHub 初始化與上傳步驟

這份文件記錄了如何將本機的「個人助理」專案上傳至 GitHub。

## 步驟一：在 GitHub 上建立新的 Repository

1. 開啟瀏覽器並登入 [GitHub](https://github.com/)。
2. 點擊右上角的 **+** 號，選擇 **New repository**（或直接前往 [此連結](https://github.com/new)）。
3. 在 **Repository name** 欄位中，輸入您想要的專案名稱（建議填寫 `personal_assistant`）。
4. **不要**勾選「Add a README file」、「Add .gitignore」或「Choose a license」，保持空白的專案狀態。
5. 點擊最下方的 **Create repository** 按鈕。

## 步驟二：取得專案的遠端網址 (URL)

建立成功後，GitHub 會顯示一個畫面，告訴您如何上傳現有的 Repository。
請找到類似下方的網址並將其複製：
```text
https://github.com/您的帳號/personal_assistant.git
```

## 步驟三：將本機程式碼推播 (Push) 到 GitHub

取得網址後，請在終端機（或提供給 AI 助理），執行以下指令來完成推播：

1. **加入遠端網址 (Remote)**：
   ```bash
   git remote add origin https://github.com/您的帳號/personal_assistant.git
   ```

2. **重新命名預設分支為 main**（現今 GitHub 預設使用 main）：
   ```bash
   git branch -M main
   ```

3. **推播 (Push) 到 GitHub**：
   ```bash
   git push -u origin main
   ```

完成以上步驟後，您的程式碼就會成功備份到 GitHub 上了！
