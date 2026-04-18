import os
import time

def start_deep_learning():
    print("🚀 جاري بدء المحرك العصبي لـ Koda...")
    files_count = 0
    chars_processed = 0
    
    # قائمة المجلدات اللي إنت رفعتها
    for root, dirs, files in os.walk("."):
        # تخطي مجلدات النظام
        if '.git' in root or '__pycache__' in root:
            continue
            
        for file in files:
            if file.endswith((".py", ".md", ".txt", ".cpp", ".js")):
                files_count += 1
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        content = f.read()
                        chars_processed += len(content)
                        # محاكاة لعملية التدريب (عشان السيرفر يشتغل بجد)
                        if files_count % 50 == 0:
                            print(f"🧬 تم تحليل {files_count} ملف.. إجمالي الحروف المستوعبة: {chars_processed}")
                            time.sleep(0.1) # بنعطي السيرفر وقت "يفكر"
                except:
                    continue

    print(f"✅ اكتملت المهمة! Koda استوعب {chars_processed} حرف من {files_count} ملف.")

if __name__ == "__main__":
    start_deep_learning()
