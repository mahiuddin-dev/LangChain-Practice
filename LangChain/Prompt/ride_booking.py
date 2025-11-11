from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4o", temperature=1.5, max_completion_tokens=100)
# load template from json
template = load_prompt("./Prompt/template/template_json/ride-booking_template.json")
# prompt
# prompt = template.invoke({
#     "pickup_location": "Vodra hojer Mor",
#     "destination_location": "Padma Park",
#     "pickup_time": "9 pm"
# })

# # model
# response = model.invoke(prompt)
# print(response.content)


# Chain 
chain = template | model
response = chain.invoke({
    "pickup_location": "Vodra hojer Mor",
    "destination_location": "Padma Park",
    "pickup_time": "9 pm"
})
print(response.content)
