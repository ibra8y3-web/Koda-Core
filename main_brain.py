import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling

# تجميع المعرفة
with open('koda_data.txt', 'w', encoding='utf-8') as f:
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith(('.py', '.txt', '.md')):
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as src:
                        f.write(src.read() + "\n")
                except: continue

# تحميل النموذج والتدريب
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
dataset = TextDataset(tokenizer=tokenizer, file_path="koda_data.txt", block_size=128)
args = TrainingArguments(output_dir="./koda_final", num_train_epochs=1, per_device_train_batch_size=4, save_steps=100)
trainer = Trainer(model=model, args=args, data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False), train_dataset=dataset)

print("🧠 كودا بدأ يتعلم لغة البشر والأكواد...")
trainer.train()
model.save_pretrained("./Koda_LLM")
tokenizer.save_pretrained("./Koda_LLM")
