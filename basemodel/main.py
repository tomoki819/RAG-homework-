from model_loader import model, tokenizer
from generate import generate_output
from evaluate_relevance import evaluate_relevance
import torch
import random

# シード固定
random.seed(0)

# CUDA or CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

question = "磯村拓哉ユニットリーダーの論文「脳知能の三大理論を統合する三重等価性」の要約をしてください"

response = generate_output(question, model, tokenizer)
print("🗣️ 回答:\n", response)

evaluation = evaluate_relevance(question, response, model, tokenizer)
print("📊 回答の関連性評価:\n", evaluation)
