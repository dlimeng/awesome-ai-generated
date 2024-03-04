
import os
os.environ["OPENAI_API_KEY"] = 'sk-tDHORTwNMfpIJGeeHNRpFx2CaiEKeqsoJH2cfncNyl67DWoU'
os.environ["SERPAPI_API_KEY"] = '1e112779a32325a9544c57c09642d4a26c72463f3732dc91be75040e67d9d1e2'

# 导入新的包和类
from langchain_openai import OpenAI
from langchain.agents import load_tools, AgentExecutor
# 使用新的代理构造方法（这里只是一个示例，根据你的需要选择正确的方法）
from langchain.agents import create_react_agent
from langchain import hub

prompt = hub.pull("hwchase17/react")

# 初始化LLM
llm = OpenAI(temperature=0)

# 加载工具
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# 使用新的方法创建代理
agent = create_react_agent(tools=tools, llm=llm, prompt=prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 使用invoke代替run（根据你选择的代理类型，这里的方法可能需要相应更改）
response = agent_executor.invoke({"input": "目前市场上python技术书的平均价格是多少？如果我在此基础上加价15%卖出，应该如何定价？"})

# 输出结果
print(response)



