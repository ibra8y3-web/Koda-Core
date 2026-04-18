import numpy as np
import os

# --- المرحلة 1: بناء هيكل الشبكة العصبية ---
class OmniNetwork:
    def __init__(self, vocab_size, hidden_size=128):
        self.hidden_size = hidden_size
        self.vocab_size = vocab_size
        # أوزان مخ الذكاء (تم توليدها من الصفر)
        self.Wxh = np.random.randn(hidden_size, vocab_size) * 0.01 
        self.Whh = np.random.randn(hidden_size, hidden_size) * 0.01 
        self.Why = np.random.randn(vocab_size, hidden_size) * 0.01 
        self.bh = np.zeros((hidden_size, 1)) 
        self.by = np.zeros((vocab_size, 1))
        # مصفوفات لتسريع التعلم (Adagrad)
        self.mWxh, self.mWhh, self.mWhy = np.zeros_like(self.Wxh), np.zeros_like(self.Whh), np.zeros_like(self.Why)
        self.mbh, self.mby = np.zeros_like(self.bh), np.zeros_like(self.by)

    def train(self, inputs, targets, hprev):
        xs, hs, ys, ps = {}, {}, {}, {}
        hs[-1] = np.copy(hprev)
        loss = 0
        # Forward Pass (التفكير للأمام)
        for t in range(len(inputs)):
            xs[t] = np.zeros((self.vocab_size, 1))
            xs[t][inputs[t]] = 1
            hs[t] = np.tanh(np.dot(self.Wxh, xs[t]) + np.dot(self.Whh, hs[t-1]) + self.bh)
            ys[t] = np.dot(self.Why, hs[t]) + self.by
            ps[t] = np.exp(ys[t]) / np.sum(np.exp(ys[t]))
            loss += -np.log(ps[t][targets[t], 0])
        
        # Backward Pass (تصحيح الأخطاء - التعلم)
        dWxh, dWhh, dWhy = np.zeros_like(self.Wxh), np.zeros_like(self.Whh), np.zeros_like(self.Why)
        dbh, dby = np.zeros_like(self.bh), np.zeros_like(self.by)
        dhnext = np.zeros_like(hs[0])
        for t in reversed(range(len(inputs))):
            dy = np.copy(ps[t])
            dy[targets[t]] -= 1
            dWhy += np.dot(dy, hs[t].T)
            dby += dy
            dh = np.dot(self.Why.T, dy) + dhnext
            dhraw = (1 - hs[t] * hs[t]) * dh
            dbh += dhraw
            dWxh += np.dot(dhraw, xs[t].T)
            dWhh += np.dot(dhraw, hs[t-1].T)
            dhnext = np.dot(self.Whh.T, dhraw)
        
        # تحديث الأوزان
        for param, dparam, mem in zip([self.Wxh, self.Whh, self.Why, self.bh, self.by], 
                                      [dWxh, dWhh, dWhy, dbh, dby], 
                                      [self.mWxh, self.mWhh, self.mWhy, self.mbh, self.mby]):
            mem += dparam * dparam
            param += -0.1 * dparam / np.sqrt(mem + 1e-8)
        
        return loss, hs[len(inputs)-1]

    def sample(self, h, seed_ix, n):
        x = np.zeros((self.vocab_size, 1))
        x[seed_ix] = 1
        ixes = []
        for t in range(n):
            h = np.tanh(np.dot(self.Wxh, x) + np.dot(self.Whh, h) + self.bh)
            y = np.dot(self.Why, h) + self.by
            p = np.exp(y) / np.sum(np.exp(y))
            ix = np.random.choice(range(self.vocab_size), p=p.ravel())
            x = np.zeros((self.vocab_size, 1))
            x[ix] = 1
            ixes.append(ix)
        return ixes

# --- المرحلة 2: تجميع المعرفة من كل الملفات بدون استثناء ---
def collect_knowledge():
    print("📂 جاري كشط كافة الملفات والمستودعات...")
    full_text = ""
    # بيلف على كل فولدر وكل ملف مهما كان عددهم
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(('.py', '.md', '.txt', '.cpp', '.h', '.js')):
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        full_text += f.read() + "\n"
                except: continue
    return full_text

# --- المرحلة 3: تشغيل التلقين (The Training Loop) ---
data = collect_knowledge()
chars = list(set(data))
data_size, vocab_size = len(data), len(chars)
char_to_ix = { ch:i for i,ch in enumerate(chars) }
ix_to_char = { i:ch for i,ch in enumerate(chars) }

print(f"🔥 تم استيعاب {data_size} حرف من كافة المصادر.")
model = OmniNetwork(vocab_size)

n, p = 0, 0
hprev = np.zeros((128, 1))

try:
    while True:
        if p + 25 + 1 >= len(data) or n == 0: 
            hprev = np.zeros((128, 1)) 
            p = 0 
        
        inputs = [char_to_ix[ch] for ch in data[p:p+25]]
        targets = [char_to_ix[ch] for ch in data[p+1:p+25+1]]
        
        loss, hprev = model.train(inputs, targets, hprev)
        
        if n % 1000 == 0:
            print(f'📊 دورة تدريبية رقم {n}, الخسارة (Loss): {loss}')
            sample_ix = model.sample(hprev, inputs[0], 200)
            txt = ''.join(ix_to_char[ix] for ix in sample_ix)
            print(f'----\n 🤖 OmniVerse يفكر الآن بـ: \n {txt} \n----')
        
        p += 25
        n += 1
except KeyboardInterrupt:
    print("\n🛑 تم إيقاف التدريب يدوياً.. OmniVerse احتفظ باللي اتعلمه.")

