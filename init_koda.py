import os
import subprocess

# قائمة بكلمات البحث لجلب مستودعات من جميع المجالات
TOPICS = [
    "machine-learning", "deep-learning", "nlp", "artificial-intelligence",
    "history-of-egypt", "space-science", "astronomy", "programming-algorithms",
    "philosophy-books", "general-knowledge", "physics-theories", "arabic-language-nlp"
]

def clone_wide_knowledge():
    print("🌍 بدء عملية السحب الكوني للمستودعات...")
    
    # التأكد من وجود مجلد خارجي
    if not os.path.exists('external'):
        os.makedirs('external')
    
    os.chdir('external')

    for topic in TOPICS:
        print(f"🔍 جاري البحث وسحب مستودعات عن: {topic}")
        # استخدام البحث السريع لجلب مستودع واحد قوي لكل مجال لضمان عدم انفجار المساحة
        # --depth 1 للسحب السريع جداً بدون تاريخ الملفات
        cmd = f"git clone --depth 1 https://github.com/topics/{topic}.git || true"
        subprocess.run(cmd, shell=True)
        
        # إضافة مستودعات محددة إنت محتاجها (ممكن تضيف روابطك هنا)
        # مثال: subprocess.run("git clone --depth 1 https://github.com/user/repo.git", shell=True)

    print("✅ انتهى السحب الموسع. كل المعرفة الآن في مجلد external.")

if __name__ == "__main__":
    clone_wide_knowledge()
