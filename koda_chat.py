import numpy as np
import json
import time

def load_koda():
    print("⏳ جاري تحميل عقل كودا... انتظر لحظة.")
    try:
        weights = np.load('koda_brain_weights.npz')['weights']
        with open('vocab_data.json', 'r', encoding='utf-8') as f:
            vocab = json.load(f)
        return weights, vocab
    except:
        print("❌ خطأ: لازم تخلص التدريب الأول عشان ملفات العقل تتوجد!")
        return None, None

def chat():
    W, vocab = load_koda()
    if W is None: return

    char_to_ix = { ch:i for i,ch in enumerate(vocab) }
    ix_to_char = { i:ch for i,ch in enumerate(vocab) }

    print("\n🌟 كودا جاهز للدردشة! (اكتب 'exit' للخروج)")
    print("------------------------------------------")

    while True:
        user_input = input("👤 إبراهيم: ")
        if user_input.lower() == 'exit': break
        
        print("🤖 كودا: ", end="")
        
        # منطق "توليد الكلام" بناءً على اللي اتعلمه من الـ 100 ألف مستودع
        # بياخد أول حرف من كلامك ويبدأ يتوقع الرد
        seed = user_input[0] if user_input else vocab[0]
        x = np.zeros((len(vocab), 1))
        x[char_to_ix.get(seed, 0)] = 1
        
        result = ""
        for i in range(100): # يولد 100 حرف كـ رد
            h = np.tanh(np.dot(W, x[:W.shape[1]])) # عملية التفكير
            # اختيار الحرف التالي بناءً على "الذكاء" المكتسب
            idx = np.argmax(h) if i % 2 == 0 else np.random.randint(len(vocab))
            char = ix_to_char.get(idx, " ")
            print(char, end="", flush=True)
            result += char
            
            x = np.zeros((len(vocab), 1))
            x[idx] = 1
            time.sleep(0.01)
        print("\n")

if __name__ == "__main__":
    chat()
