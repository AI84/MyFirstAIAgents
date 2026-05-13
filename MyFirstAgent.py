
from strands import Agent
from strands.models.bedrock import BedrockModel

model = BedrockModel(
    model_id="amazon.nova-micro-v1:0",
    region_name="eu-west-2"
)

agent  = Agent(model = model)
print("The model  within strands invocation is ", agent.model)
print(vars(agent.model))

# response = agent("what is the current date and time?")

# print(response)
