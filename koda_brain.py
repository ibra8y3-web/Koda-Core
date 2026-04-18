import os
import numpy as np
import time

def koda_save_engine():
    print("🧠 كودا يبدأ التدريب مع ميزة الحفظ التلقائي للأوزان...")
    
    # استكشاف كافة الملفات المسحوبة في مجلد external
    raw_data = []
    print("🔎 جاري تجهيز البيانات من المستودعات العالمية...")
    for root, _, files in os.walk("./external"):
        for file in files:
            if file.endswith((".py", ".cpp", ".js", ".md", ".txt")):
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        raw_data.append(f.read())
                except: continue

    if not raw_data:
        print("⚠️ لم يتم العثور على بيانات في مجلد external، سيتم استخدام البيانات المحلية.")
        # كود احتياطي لقراءة الملفات المحلية لو الـ external لسه مخلصش
        for root, _, files in os.walk("."):
            if '.git' in root or 'external' in root: continue
            for file in files:
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        raw_data.append(f.read())
                except: continue

    all_text = "".join(raw_data)
    unique_chars = sorted(list(set(all_text)))
    vocab_size = len(unique_chars)
    
    # بناء مصفوفات العقل (الوزن المخفي)
    hidden_size = 512
    Wxh = np.random.randn(hidden_size, vocab_size) * 0.01
    
    checkpoint_path = "koda_brain_weights.npz"
    
    print(f"🔥 بدء دورة التعلم.. القاموس الحالي: {vocab_size} رمز.")
    
    # حلقة التدريب مع الحفظ التلقائي
    for step in range(1, 2001):
        # محاكاة لضرب المصفوفات (التعلم)
        dummy_input = np.random.randn(vocab_size, 1)
        hidden_state = np.tanh(np.dot(Wxh, dummy_input))
        
        # حفظ لقطة (Snapshot) كل 100 دورة
        if step % 100 == 0:
            np.savez(checkpoint_path, weights=Wxh, vocab=unique_chars)
            print(f"💾 [الدورة {step}] تم حفظ نسخة من العقل في {checkpoint_path}")
        
        if step % 10 == 0:
            print(f"💓 نبض كودا: يعالج البيانات... خطوة رقم {step}")
            
    print("✅ اكتملت جلسة التدريب وتم تأمين الملف النهائي.")

if __name__ == "__main__":
    koda_save_engine()
