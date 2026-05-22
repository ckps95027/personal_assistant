import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. 載入 .env 檔案中的環境變數
load_dotenv()

# 2. 從環境變數中取得 API Key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key or "在這裡貼上" in api_key:
    print("❌ 錯誤：請先在 .env 檔案中填寫您的 GEMINI_API_KEY！")
    exit(1)

# 3. 設定 Gemini API
genai.configure(api_key=api_key)

# 4. 選擇模型 (我們使用最新的 gemini-1.5-flash，反應快且便宜/免費額度高)
model = genai.GenerativeModel('gemini-1.5-flash')

def main():
    print("🤖 您的個人生活助理已連線！")
    print("請輸入您想對我說的話 (輸入 'quit' 或 'exit' 離開)：")
    
    # 開始無限對話迴圈
    chat = model.start_chat(history=[])
    
    while True:
        user_input = input("\n您: ")
        
        if user_input.lower() in ['quit', 'exit']:
            print("👋 助理已斷線，期待下次為您服務！")
            break
            
        try:
            # 呼叫 Gemini 取得回應
            response = chat.send_message(user_input)
            print(f"助理: {response.text}")
        except Exception as e:
            print(f"❌ 發生錯誤: {e}")

if __name__ == "__main__":
    main()
