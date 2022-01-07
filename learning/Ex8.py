import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
parsed_response_text = response.json()
get_params={"token": parsed_response_text['token']}

response_with_token = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=get_params)
parsed_response_text_with_token=response_with_token.json()
if (parsed_response_text_with_token['status'] == "Job is NOT ready"):
    print(f"Получен правильный ответ: {parsed_response_text_with_token['status'] }")

time.sleep(parsed_response_text['seconds'])
response_with_token = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=get_params)
parsed_response_text_with_token=response_with_token.json()

if (parsed_response_text_with_token['status'] == "Job is ready" and "result" in parsed_response_text_with_token):
    print(f"Получен правильный ответ: {parsed_response_text_with_token['status']}, result={parsed_response_text_with_token['result']}")
