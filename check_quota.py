import os
import google.generativeai as genai
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ 錯誤：請先在 .env 檔案中填寫 GEMINI_API_KEY！")
    exit(1)

genai.configure(api_key=api_key)

try:
    print("正在查詢模型列表與配額...")
    models = genai.list_models()
    for m in models:
        if 'generateContent' in m.supported_generation_methods:
            print(f"✔️ 可用模型: {m.name}")
    print("\n✅ 您的 API 金鑰目前狀態正常，可成功連線至 Google 伺服器！")
    print("💡 備註：Google 目前尚未提供直接查詢剩餘 token 額度的 API，若要確認免費配額用量，請至 Google AI Studio 網頁控制台 (https://aistudio.google.com/) 查看 Dashboard。")
except Exception as e:
    print(f"❌ 查詢失敗，可能金鑰無效或網路異常: {e}")
