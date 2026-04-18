import os, subprocess, shutil

def smart_stream_clone():
    repos = [
        "https://github.com/vinta/awesome-python",
        "https://github.com/josephmisiti/awesome-machine-learning",
        "https://github.com/lucidrains/vit-pytorch",
        "https://github.com/karpathy/char-rnn" # أمثلة لمستودعات عبقرية
    ]
    
    os.makedirs('knowledge_vault', exist_ok=True)
    master_file = 'koda_data.txt'
    
    for url in repos:
        repo_name = url.split('/')[-1]
        print(f"📥 سحب ومعالجة: {repo_name}")
        
        # سحب المستودع بعمق 1 فقط لتوفير الوقت والمساحة
        subprocess.run(f"git clone --depth 1 {url} temp_repo || true", shell=True)
        
        # استخراج النصوص والأكواد ووضعها في ملف واحد
        with open(master_file, 'a', encoding='utf-8') as f_out:
            for root, _, files in os.walk('temp_repo'):
                for file in files:
                    if file.endswith(('.py', '.txt', '.md', '.c', '.cpp', '.math')):
                        try:
                            with open(os.path.join(root, file), 'r', encoding='utf-8') as f_in:
                                f_out.write(f"\n--- Source: {repo_name}/{file} ---\n")
                                f_out.write(f_in.read() + "\n")
                        except: continue
        
        # 🔥 الحركة السحرية: مسح المستودع فوراً بعد شفط المعلومات منه
        if os.path.exists('temp_repo'):
            shutil.rmtree('temp_repo')
            print(f"🧹 تم مسح {repo_name}.. المساحة الآن آمنة.")

if __name__ == "__main__": smart_stream_clone()
