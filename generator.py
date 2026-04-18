import os

class SmartResponder:
    def __init__(self):
        self.name = "OmniVerse AI"

    def generate_answer(self, query, results):
        if not results:
            return "🤖 إبراهيم، مفيش ملفات في الـ 10 آلاف ملف بتوعي بتغطي النقطة دي. تحب أحللها من منطقي الخاص؟"

        # ترتيب الردود بناءً على القوة الرياضية
        best_match = results[0]
        score, content, path = best_match
        
        # لو التشابه قوي جداً، يبقى ده رد مباشر
        if score > 0.3:
            summary = "\n".join([line for line in content.split('\n') if len(line) > 30][:5])
            return f"🧠 **تحليل {self.name} (قوة الربط: {score:.2f}):**\n\n{summary}\n\n📚 المصدر: {os.path.basename(path)}"
        
        # لو التشابه ضعيف، يبدأ يدردش ويحاول يستنتج
        return f"🤖 كلامك عن '{query}' فيه لمحة من اللي قريته في {os.path.basename(path)}، بس محتاج توضيح أكتر عشان أربط لك الخيوط ببعض."
