def evaluate_relevance(question, answer, model, tokenizer):
    eval_prompt = f"""以下はユーザーからの質問と、その質問に対するAIの回答です。

[質問]
{question}

[回答]
{answer}

この回答は、質問に対してどれくらい関連性がありますか？  
また、回答内容が事実に基づいて正確であるかも踏まえて、以下の5段階で評価してください。

- 5点：質問に完全に的確かつ、内容も正確
- 4点：質問には合っているが、一部に誤解や曖昧な表現がある
- 3点：質問にはやや関連があるが、要点がずれているか、内容があいまい
- 2点：質問とはほとんど関係がなく、内容も不正確
- 1点：まったく関係がなく、事実としても誤っている

点数とその理由を、できるだけ具体的に述べてください。
"""

    messages = [{"role": "user", "content": eval_prompt}]
    input_ids = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_tensors="pt"
    ).to(model.device)

    outputs = model.generate(
        input_ids,
        max_new_tokens=300,
        do_sample=False,
        eos_token_id=tokenizer.eos_token_id,
    )

    response = outputs[0][input_ids.shape[-1]:]
    return tokenizer.decode(response, skip_special_tokens=True)
