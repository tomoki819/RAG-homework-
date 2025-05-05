import torch
import random

# シード固定
random.seed(0)

# CUDA or CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Hugging Face Login（初回のみ必要）
notebook_login()
