import os
from processor import DataProcessor
from model_core import AIBrain
from generator import SmartResponder

def start():
    # 1. تحديد مكان المشروع الرئيسي
    base_path = "/data/data/com.termux/files/home/MyAI_Project/"
    
    brain = AIBrain()
    processor = DataProcessor()
    responder = SmartResponder()

    print("🚀 بدء فحص وتلقين كافة المستودعات...")
    
    all_docs = []
    # 2. المرور على كل المجلدات أوتوماتيكياً
    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)
        
        # التأكد إنه مجلد وليس ملف، وتجاهل المجلدات المخفية
        if os.path.isdir(folder_path) and not folder.startswith('.'):
            print(f"🔍 جاري معالجة مستودع: {folder}")
            # استدعاء دالة المعالجة لكل مجلد
            docs = processor.process_directory(folder_path)
            all_docs.extend(docs)

    # 3. تغذية المخ بكل البيانات المجمعة
    brain.train_in_batches(all_docs)
    
    print(f"\n✅ ذكاء إبراهيم الخاص جاهز (تم استيعاب {len(all_docs)} ملف من كافة المصادر)")

    while True:
        q = input("\n👤 أنت: ")
        if q.lower() in ['exit', 'quit', 'خروج']: break
        
        print("🧠 الذكاء يفكر...")
        # البحث في كل ما تم استيعابه
        raw_results = brain.search(q, k=3)
        final_answer = responder.generate_answer(q, raw_results)
        print(f"\n{final_answer}")

if __name__ == "__main__":
    start()

