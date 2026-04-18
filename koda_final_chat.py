import numpy as np
import time

def start_koda():
    print("🚀 جاري استخراج الوعي وتصحيح المسارات العصبية...")
    try:
        data = np.load('koda_brain_weights.npz', allow_pickle=True)
        weights = data['weights']
        
        if 'vocab' in data:
            vocab = data['vocab'].tolist()
        else:
            vocab = [chr(i) for i in range(344)] # تثبيت الحجم على اللي اتدرب عليه
            
        char_to_ix = { ch:i for i,ch in enumerate(vocab) }
        ix_to_char = { i:ch for i,ch in enumerate(vocab) }
        
        print(f"✅ كودا جاهز وآمن الآن! (حجم الذاكرة: {len(vocab)} رمز)")
        print("------------------------------------------")
        
        while True:
            user_input = input("👤 إبراهيم: ")
            if user_input.lower() in ['exit', 'خروج']: break
            
            print("🤖 كودا: ", end="", flush=True)
            
            # تحديد أول حرف وبداية التفكير
            seed = user_input[-1] if user_input and user_input[-1] in char_to_ix else vocab[0]
            x = np.zeros((len(vocab), 1))
            x[char_to_ix[seed]] = 1
            
            for _ in range(100):
                # عملية التفكير الرياضي
                h = np.tanh(np.dot(weights, x[:weights.shape[1]]))
                
                # صمام الأمان: التأكد إن الاختيار جوه حدود القاموس (344)
                idx = np.argmax(h) % len(vocab) 
                
                char = ix_to_char.get(idx, " ")
                print(char, end="", flush=True)
                
                # تحضير الحرف اللي بعده
                x = np.zeros((len(vocab), 1))
                x[idx] = 1
                time.sleep(0.01)
            print("\n")
            
    except Exception as e:
        print(f"❌ خطأ غير متوقع: {e}")

if __name__ == "__main__":
    start_koda()
