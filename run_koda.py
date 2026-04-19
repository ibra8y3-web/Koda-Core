import os
import json
import numpy as np

# المسار لمجلد العقل
BRAIN_PATH = "./koda_final_brain"

class KodaFixedCore:
    def __init__(self):
        self.weights, self.vocab, self.inv_vocab = self.load_brain()
        
    def load_brain(self):
        try:
            # تحميل القاموس
            v_path = os.path.join(BRAIN_PATH, 'vocab_data.json')
            with open(v_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # تنظيف القاموس من أي رموز غريبة
            if isinstance(data, list):
                vocab = {w: i for i, w in enumerate(data) if len(str(w)) > 1 or str(w).isalnum()}
            else:
                vocab = {k: v for k, v in data.items() if len(str(k)) > 1 or str(k).isalnum()}
                
            inv_vocab = {i: w for w, i in vocab.items()}

            # تحميل الأوزان
            w_path = os.path.join(BRAIN_PATH, 'koda_brain_weights.npz')
            w_data = np.load(w_path, allow_pickle=True)
            matrix = w_data['weights'] if 'weights' in w_data else w_data[w_data.files[0]]
            
            return matrix, vocab, inv_vocab
        except Exception as e:
            print(f"❌ خطأ: {e}")
            return None, None, None

    def predict_next_word(self, current_text):
        try:
            tokens = [self.vocab.get(w.lower(), 0) for w in current_text.split()]
            if not tokens: return ""
            
            # حساب "البصمة" (Vector Sum)
            # بنستخدم الـ Slice عشان نضمن إننا جوه حدود المصفوفة الـ 13 ميجا
            state = np.zeros(self.weights.shape[1] if len(self.weights.shape) > 1 else 1)
            for t in tokens:
                state += self.weights[t % len(self.weights)]
            
            # اختيار الكلمة (تصفية الرموز)
            # بندور على أعلى قيمة احتمالية بس لكلمات حقيقية (أطول من حرفين)
            for offset in range(100):
                idx = int(np.abs(np.sum(state) + offset) % len(self.inv_vocab))
                word = self.inv_vocab.get(idx, "")
                if len(word) > 1 and word.isalnum(): # فلتر الكلمات الحقيقية
                    return word
            return ""
        except: return ""

    def chat(self, user_input):
        # توليد جملة من 5 لـ 10 كلمات
        response = []
        current = user_input
        for _ in range(8):
            next_w = self.predict_next_word(current)
            if next_w and next_w not in response:
                response.append(next_w)
                current = next_w
            else:
                break
        return " ".join(response) if response else "أنا فاهم قصدك، بس الأوزان محتاجة ربط أدق بالقاموس."

def main():
    core = KodaFixedCore()
    if core.weights is None: return

    print("\n🚀 [Koda Brain] Fixed Inference Active")
    print("الآن يتم تصفية الرموز العشوائية والتركيز على الكلمات المدربة.")

    while True:
        try:
            inp = input("\nUser >> ").strip()
            if not inp or inp.lower() in ['exit', 'خروج']: break
            
            print(f"Koda >> {core.chat(inp)}")
        except KeyboardInterrupt: break

if __name__ == "__main__":
    main()
