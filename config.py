# إعدادات النظام الأساسية
MODEL_NAME = 'all-MiniLM-L6-v2'  # المحرك الرياضي
SOURCE_DIR = "knowledge_source"  # مصدر البيانات
STORAGE_DIR = "brain_storage"    # مكان حفظ الذاكرة

# ملفات الذاكرة
INDEX_FILE = f"{STORAGE_DIR}/vector_brain.index"
TEXT_DATA_FILE = f"{STORAGE_DIR}/knowledge.pkl"

# إعدادات المعالجة
CHUNK_SIZE = 500  # طول قطعة النص الواحدة
TOP_K_RESULTS = 3 # عدد الإجابات التي يستخرجها الذكاء

