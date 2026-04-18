import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# إعدادات المسارات داخل المجلد الجديد
SOURCE_DIR = "knowledge_source"
STORAGE_DIR = "brain_storage"
INDEX_FILE = os.path.join(STORAGE_DIR, "vector_brain.index")
PKL_FILE = os.path.join(STORAGE_DIR, "text_data.pkl")
MODEL_NAME = 'all-MiniLM-L6-v2'

print("--- نظام ذكاء إبراهيم: المحرك قيد التشغيل ---")
model = SentenceTransformer(MODEL_NAME)

def train_brain():
    content = []
    print(f"جاري قراءة الملفات من {SOURCE_DIR}...")
    
    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    # تقسيم النص لقطع ذكية (Chunks) لزيادة دقة الفهم
                    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
                    for chunk in chunks:
                        content.append(f"موقع المعلومة ({file}):\n {chunk.strip()}")
            except: continue

    if not content:
        print("المجلد فارغ! ضع ملفاتك في knowledge_source أولاً.")
        return None, None

    print(f"تم العثور على {len(content)} وحدة معرفية. جاري بناء المخ الرياضي...")
    embeddings = model.encode(content, show_progress_bar=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    
    # حفظ الذاكرة
    faiss.write_index(index, INDEX_FILE)
    with open(PKL_FILE, 'wb') as f:
        pickle.dump(content, f)
    
    return index, content

def load_brain():
    if os.path.exists(INDEX_FILE) and os.path.exists(PKL_FILE):
        print("تم العثور على ذاكرة سابقة، جاري التحميل...")
        index = faiss.read_index(INDEX_FILE)
        with open(PKL_FILE, 'rb') as f:
            content = pickle.load(f)
        return index, content
    return None, None

# المنطق التشغيلي
index, knowledge = load_brain()

if not index:
    index, knowledge = train_brain()

if index:
    print("\n✅ الذكاء جاهز الآن. اسأل عن أي شيء داخل ملفاتك.")
    while True:
        query = input("\n🤔 سؤالك: ")
        if query.lower() in ['exit', 'خروج']: break
        
        q_emb = model.encode([query])
        D, I = index.search(np.array(q_emb), k=2) # جلب أفضل نتيجتين
        
        print("\n--- النتائج المستخرجة من ذاكرتك الخاصة ---")
        for i in I[0]:
            print(f"💡 {knowledge[i]}\n" + "-"*30)

