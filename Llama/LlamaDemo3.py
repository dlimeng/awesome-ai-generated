import os
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer, util
import torch

# 加载预训练模型的分词器和模型
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-chat-hf",
    device_map='auto')

# 加载HuggingFace的Embeddings模型
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# 指定知识库文件目录
knowledge_base_dir = "path/to/your/knowledge/base"

# 读取目录中的所有文件，并将其内容作为知识库条目
knowledge_base = []
for filename in os.listdir(knowledge_base_dir):
    filepath = os.path.join(knowledge_base_dir, filename)
    if os.path.isfile(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            knowledge_base.append(file.read())

# 将知识库文本转换为embeddings
knowledge_embeddings = embedder.encode(knowledge_base, convert_to_tensor=True)

# 定义一个用户的问题或提示
prompt = "请给我讲个玫瑰的爱情故事?"

# 将用户的问题转换为embedding
question_embedding = embedder.encode(prompt, convert_to_tensor=True)

# 在知识库中寻找最相似的文本
cos_scores = util.pytorch_cos_sim(question_embedding, knowledge_embeddings)[0]
top_result = torch.topk(cos_scores, k=1)

# 使用找到的最相关的文本作为模型的输入
input_text = knowledge_base[top_result.indices[0]]

# 使用分词器将找到的最相关的文本转化为模型可以理解的格式
inputs = tokenizer(input_text, return_tensors="pt").to("cuda")

# 使用模型生成文本
outputs = model.generate(inputs["input_ids"], max_new_tokens=2000)

# 将生成的令牌解码成文本
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# 打印生成的响应
print(response)
