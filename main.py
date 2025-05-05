from huggingface_hub import notebook_login
from config import device
from model_loader import model, tokenizer
from generate import generate_output

# Hugging Face Login（初回のみ必要）
notebook_login()

question = "磯村拓哉ユニットリーダーの論文「脳知能の三大理論を統合する三重等価性」の要約をしてください"
response = generate_output(question, model, tokenizer)
print(response)
