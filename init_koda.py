import os
import subprocess

# هنسحب أهم المستودعات بس ونبعد عن القواميس اللي بتملا المساحة
TARGETS = [
    "https://github.com/nltk/nltk_data",
    "https://github.com/vinta/awesome-python"
]

def clean_clone():
    if not os.path.exists('external'): os.makedirs('external')
    os.chdir('external')
    for url in TARGETS:
        # السر هنا في --depth 1 و --sparse عشان ميسحبش تاريخ الملفات
        subprocess.run(f"git clone --depth 1 {url} || true", shell=True)
    
    # أهم خطوة: مسح أي حاجة مش نصية فوراً لتوفير مساحة
    subprocess.run("find . -type f ! -name '*.txt' ! -name '*.py' ! -name '*.md' -delete", shell=True)

if __name__ == "__main__":
    clean_clone()
