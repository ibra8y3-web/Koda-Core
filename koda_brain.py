import os
import numpy as np
import time

def build_unlimited_koda():
    print("🔓 فك القيود.. Koda يعمل الآن بنظام الاستيعاب المفتوح.")
    
    raw_data = []
    file_count = 0
    
    # البحث في كل مكان (بايثون، C++، علم بيانات، إلخ)
    print("🔎 جاري مسح كافة المجلدات والمستودعات المرفوعة...")
    for root, _, files in os.walk("."):
        if '.git' in root or '__pycache__' in root:
            continue
        for file in files:
            # استيعاب كافة أنواع ملفات الأكواد والنصوص
            if file.endswith((".py", ".cpp", ".js", ".md", ".txt", ".h", ".c")):
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        raw_data.append(f.read())
                        file_count += 1
                except:
                    continue

    combined_text = "".join(raw_data)
    total_chars = len(combined_text)
    
    # بناء القاموس بناءً على المكتشف فعلياً (مهما كان حجمه)
    unique_chars = sorted(list(set(combined_text)))
    vocab_size = len(unique_chars)

    print(f"📊 نتيجة المسح: استيعاب {file_count} ملف.")
    print(f"🌍 إجمالي الحروف: {total_chars} حرف.")
    print(f"🔢 حجم القاموس المكتشف: {vocab_size} رمز فريد.")
    
    # بناء الأوزان العصبية (عقل Koda)
    hidden_size = 512 
    print(f"🧠 بناء المصفوفات العصبية بحجم مخفي {hidden_size}...")
    Wxh = np.random.randn(hidden_size, vocab_size) * 0.01
    
    print("⚙️ المحرك يعمل الآن بأقصى طاقة.. Koda في حالة تعلم مستمر.")
    # محاكاة بسيطة للتدريب لضمان استمرار السيرفر
    for i in range(5):
        print(f"🔄 معالجة الحزمة رقم {i+1}...")
        time.sleep(1)

if __name__ == "__main__":
    build_unlimited_koda()
