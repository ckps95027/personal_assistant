# Antigravity (Gemini) Agent 開發環境與中文設定指南

這份文件記錄了在另一台電腦上接續開發 `X2-agent` (或其他專案) 時，需要為 Agent (AI 助手) 設定的「個人偏好 (User Rules)」以及專案安裝的核心套件。

## 1. Agent 中文外掛 (個人偏好設定)

為了讓 Agent 能夠完全使用繁體中文（台灣用語）進行思考、回答與撰寫註解，並且嚴格遵守使用 `uv` 建立虛擬環境的規則，請在另一台電腦的 Agent 設定 (User Rules / Global Instructions) 中貼上以下內容：

```text
# 個人偏好（全域設定）
預設使用「繁體中文（台灣用語）」回應所有自然語言與文件內容。
包括你自己的思考過程 (thinking process)，也請使用繁體中文與自己交談。
所有產出的 Artifacts (如 README.md, implementation.plan, task.md) 一律使用繁體中文。
程式碼本體保持英文，但註解、說明與 docstring 必須使用繁體中文。
若需要輸出英文，請顯式回覆「請用英文」
自動產生 git commit messages/comments時，一律使用繁體中文台灣用語
Agent 產生的 implementation.plan*, task.md*, walkthrought.md*，全部用繁體中文台灣用語
如果要使用python開發程式，一定要使用 uv, .venv 建立環境，千萬不要用到base及單獨使用pip，不要弄髒我的環境
```

## 2. X2-agent 專案套件安裝 (uv)

在另一台電腦拉取 (git clone) `X2-agent` 專案後，因為您有設定不要弄髒本機環境，請在終端機執行以下指令來重建虛擬環境：

### 安裝 uv (如果還沒安裝)
```cmd
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 初始化環境並安裝所有依賴套件
進入專案資料夾後，執行以下指令：
```cmd
uv venv
uv pip install fastapi uvicorn jinja2 python-multipart pydantic docxtpl docx2pdf pywin32 xlsxwriter
```

> **注意**：如果在另一台電腦上無法執行 `uv`，請確認安裝完成後是否已經重啟終端機。

## 3. 啟動伺服器
完成安裝後，即可使用以下指令啟動 X2-agent 的後端伺服器：
```cmd
uv run python src/main.py
```
