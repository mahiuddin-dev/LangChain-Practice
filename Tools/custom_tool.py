from langchain_core.tools import tool


@tool
def multiply(a: int, b:int) -> int:
    """Multiply two numbers"""
    return a*b

result = multiply.invoke({"a":3, "b":5})
print(result)

print(multiply.args_schema.model_json_schema())
