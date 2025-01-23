import re
import torch
import tkinter as tk
from transformers import MllamaForConditionalGeneration, MllamaProcessor

model = MllamaForConditionalGeneration.from_pretrained(
    'Bllossom/llama-3.2-Korean-Bllossom-AICA-5B',
    torch_dtype=torch.bfloat16,
    device_map='auto'
)
processor = MllamaProcessor.from_pretrained('Bllossom/llama-3.2-Korean-Bllossom-AICA-5B')

def generate(mode, text):
    if mode == "summary":
        prompt = "다음 텍스트를 요약해줘: "
    elif mode == "quiz":
        prompt = "다음 텍스트로 문제와 정답을 1개만 만들어줘: "
    
    messages = [{'role': 'user',
                 'content': [{'type': 'text',
                              'text': prompt+text}]}]

    input_text = processor.apply_chat_template(messages,
                                               tokenize=False,
                                               add_generation_prompt=True)

    inputs = processor(text=input_text,
                       add_special_tokens=False,
                       return_tensors="pt").to(model.device)

    output = model.generate(**inputs,
                            max_new_tokens=256,
                            temperature=0.1,
                            eos_token_id=processor.tokenizer.convert_tokens_to_ids('<|eot_id|>'),
                            use_cache=False)
    
    output_text = processor.decode(output[0])

    match = re.search(r'<\|start_header_id\|>assistant<\|end_header_id\|>(.*?)<\|eot_id\|>',
                      output_text,
                      re.DOTALL)
    
    return match.group(1)

def process_0():
    input_text = entry.get()
    summary = generate("summary", input_text)
    output_label_0.config(text=summary)

def process_1():
    summary = entry.get()
    quiz = generate("quiz", summary)
    output_label_1.config(text=quiz)

root = tk.Tk()
root.title("텍스트 요약 및 퀴즈 생성")

entry_label = tk.Label(root, text="요약할 텍스트를 입력하세요:")
entry_label.pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button_0 = tk.Button(root, text="1. 요약 생성", command=process_0)
button_0.pack(pady=10)

output_label_0 = tk.Label(root, text="", fg="blue")
output_label_0.pack(pady=5)

button_1 = tk.Button(root, text="2. 문제 생성", command=process_1)
button_1.pack(pady=10)

output_label_1 = tk.Label(root, text="", fg="blue")
output_label_1.pack(pady=5)

root.mainloop()