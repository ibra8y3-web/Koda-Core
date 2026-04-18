import os

class DataProcessor:
    def __init__(self):
        # وسعنا القائمة لتشمل كل شيء نصي أو برميجي
        self.supported_extensions = [
            '.py', '.cpp', '.h', '.hpp', '.c', '.cc', '.md', '.txt', 
            '.java', '.js', '.ts', '.html', '.css', '.sql', '.pdf',
            '.json', '.rst', '.sh', '.rb', '.go', '.rs'
        ]

    def process_directory(self, directory_path):
        documents = []
        # استخدام os.walk للغوص في المجلدات الفرعية لآخر مستوى
        for root, dirs, files in os.walk(directory_path):
            # تجاهل مجلدات النظام والملفات المخفية
            if any(ignore in root for ignore in ['__pycache__', '.git', '.github', 'node_modules']):
                continue
                
            for file in files:
                if any(file.endswith(ext) for ext in self.supported_extensions):
                    file_path = os.path.join(root, file)
                    try:
                        # القراءة بترميز لاتيني لو الـ utf-8 فشل عشان نسحب كل الملفات
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            if len(content.strip()) > 10:
                                documents.append({
                                    'file_path': file_path,
                                    'content': content
                                })
                    except:
                        # لو فشل في ملف واحد يكمل اللي بعده ميفصلش
                        continue
        return documents
