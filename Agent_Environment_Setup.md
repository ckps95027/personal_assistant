# Antigravity (Gemini) Agent 開發環境與中文設定指南

這份文件記錄了在另一台電腦上接續開發 `X2-agent` 與 `personal_assistant` 時，需要為 Agent (AI 助手) 設定的「個人偏好 (User Rules)」以及專案安裝的核心套件。

## 1. Agent 核心中文外掛與行為設定 (個人偏好)

這是在另一台電腦上，讓 Agent (Antigravity) 保持相同語氣與工作模式的最重要設定！

👉 **請將以下內容，完整複製並貼上到另一台電腦 Agent 的「User Rules (個人規則 / Global Instructions)」設定框中**：

```text
<RULE[user_global]>
# 個人偏好（全域設定）
預設使用「繁體中文（台灣用語）」回應所有自然語言與文件內容。
包括你自己的思考過程 (thinking process)，也請使用繁體中文與自己交談。
所有產出的 Artifacts (如 README.md, implementation.plan, task.md) 一律使用繁體中文。
程式碼本體保持英文，但註解、說明與 docstring 必須使用繁體中文。
若需要輸出英文，請顯式回覆「請用英文」
自動產生 git commit messages/comments時，一律使用繁體中文台灣用語
Agent 產生的 implementation.plan*, task.md*, walkthrought.md*，全部用繁體中文台灣用語
如果要使用python開發程式，一定要使用 uv, .venv 建立環境，千萬不要用到base及單獨使用pip，不要弄髒我的環境
</RULE[user_global]>
```

## 2. 檢查 API Quota (配額與連線) 的工具

我們已在此專案新增了一支用來檢查配額與連線狀態的工具：`check_quota.py`。
在另一台電腦上，您可以透過以下指令執行，確認 API 金鑰是否正常以及可以使用的模型：

```cmd
uv run python check_quota.py
```
*(請確保您已在專案根目錄建立 `.env` 檔案並填妥 `GEMINI_API_KEY`)*

> 註：由於 Google 官方目前未開放透過 API 直接取得「剩餘 Token 額度」，若需查看當日配額使用量，仍需前往 [Google AI Studio 控制台](https://aistudio.google.com/) 查看 Dashboard。

## 3. X2-agent 專案套件安裝 (uv)

如果您在另一台電腦也需要執行 `X2-agent` 專案，請在該專案目錄執行以下指令來重建虛擬環境：

### 安裝 uv (如果該電腦尚未安裝)
```cmd
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 初始化環境並安裝所有依賴套件
```cmd
cd X2-agent
uv venv
uv pip install fastapi uvicorn jinja2 python-multipart pydantic docxtpl docx2pdf pywin32 xlsxwriter
```

> **注意**：如果在另一台電腦上無法執行 `uv`，請確認安裝完成後是否已經重啟終端機 (關掉黑色視窗重開)。

## 4. 啟動 X2-agent 伺服器
完成安裝後，即可啟動後端伺服器：
```cmd
uv run python src/main.py
```
