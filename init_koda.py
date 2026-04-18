import os, requests, subprocess, shutil

# هنا مفيش توكن مكتوب صراحة عشان الحماية
TOKEN = os.getenv("MY_GH_TOKEN")
REPO_NAME = "Koda-Core"

def run_command(command):
    subprocess.run(command, shell=True)

def setup():
    if not TOKEN:
        print("❌ يا هيما اكتب التوكن الأول في الترمكس!")
        return

    # إنشاء ملف العقل
    with open("koda_brain.py", "w") as f:
        f.write("# Koda Brain Core\nprint('Koda is learning from 62M characters...')")

    # إنشاء workflow
    os.makedirs(".github/workflows", exist_ok=True)
    with open(".github/workflows/train.yml", "w") as f:
        f.write("name: Koda Training\non: [push]\njobs:\n  train:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v3\n      - run: python koda_brain.py")

    # رفع لـ GitHub
    if os.path.exists(".git"): shutil.rmtree(".git")
    run_command("git init")
    run_command("git add .")
    run_command('git commit -m "Secure launch of Koda"')
    run_command("git branch -M main")

    # استخراج اليوزر ورفع الكود
    user_data = requests.get("https://api.github.com/user", headers={"Authorization": f"token {TOKEN}"}).json()
    user_login = user_data['login']
    remote_url = f"https://{TOKEN}@github.com/{user_login}/{REPO_NAME}.git"

    run_command(f"git remote add origin {remote_url}")
    run_command("git push -u origin main --force")
    print(f"✅ مبروك! Koda اتفك عنه الحظر واترفع.")

if __name__ == "__main__":
    setup()
