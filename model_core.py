import math
import re
from collections import Counter

class AIBrain:
    def __init__(self):
        self.docs = []
        self.idf = {}
        self.doc_vectors = []

    def train_in_batches(self, documents):
        self.docs = documents
        total_docs = len(documents)
        df = Counter()
        
        # 1. حساب تكرار الكلمات في كل الوثائق (Learning phase)
        for doc in documents:
            words = set(re.findall(r'\w+', doc['content'].lower()))
            for word in words:
                df[word] += 1
        
        # 2. حساب الوزن المنطقي لكل كلمة (IDF)
        for word, count in df.items():
            self.idf[word] = math.log(total_docs / (1 + count))
            
        # 3. بناء المتجهات لكل ملف
        for doc in documents:
            self.doc_vectors.append(self._get_vector(doc['content']))
        print(f"✅ تم بناء 'الوعي الإحصائي' لـ {total_docs} ملف باستقلال تام.")

    def _get_vector(self, text):
        words = re.findall(r'\w+', text.lower())
        counts = Counter(words)
        vector = {}
        for word, count in counts.items():
            if word in self.idf:
                vector[word] = count * self.idf[word]
        return vector

    def search(self, query, k=3):
        query_vector = self._get_vector(query)
        scores = []
        
        for i, doc_vec in enumerate(self.doc_vectors):
            # حساب التشابه الرياضي (Cosine Similarity)
            score = self._cosine_sim(query_vector, doc_vec)
            if score > 0:
                scores.append((score, self.docs[i]['content'], self.docs[i]['file_path']))
        
        return sorted(scores, key=lambda x: x[0], reverse=True)[:k]

    def _cosine_sim(self, vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum(vec1[x] * vec2[x] for x in intersection)
        sum1 = sum(v**2 for v in vec1.values())
        sum2 = sum(v**2 for v in vec2.values())
        if not sum1 or not sum2: return 0
        return numerator / (math.sqrt(sum1) * math.sqrt(sum2))
