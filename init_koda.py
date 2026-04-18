import os, subprocess
def fast_clone():
    os.makedirs('external', exist_ok=True)
    os.chdir('external')
    # مستودعات تقيلة ومفيدة
    repos = ["https://github.com/vinta/awesome-python", "https://github.com/josephmisiti/awesome-machine-learning"]
    for r in repos:
        subprocess.run(f"git clone --depth 1 {r} || true", shell=True)
    # مسح أي ملف مش كود أو نص فوراً
    subprocess.run("find . -type f ! -name '*.py' ! -name '*.txt' ! -name '*.md' -delete", shell=True)
if __name__ == "__main__": fast_clone()
