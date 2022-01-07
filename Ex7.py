import requests
import json

# response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
# print(response.status_code)
# print(response.text)
# response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
# print(response.status_code)
# print(response.text)
# response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
# print(response.status_code)
# print(response.text)
# response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")
# print(response.status_code)
# print(response.text)
#
# response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
# print(response.text)
# print(response.status_code)

# response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
# print(response.status_code)
# print(response.text)
#
# response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"POST"})
# print(response.status_code)
# print(response.text)
#
# response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"PUT"})
# print(response.status_code)
# print(response.text)
#
# response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"DELETE"})
# print(response.status_code)
# print(response.text)

methods=["GET", "POST", "PUT", "DELETE"]

for m in methods:
    m_param = '{"method":"' + m + '"}'
    obj = json.loads(m_param)
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=obj)
    if (m == 'GET' and response.text != '{"success":"!"}') or (m != 'GET' and response.text == '{"success":"!"}'):
        print("GET")
        print(m_param)

    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=obj)
    if (m == 'POST' and response.text != '{"success":"!"}') or (m != 'POST' and response.text == '{"success":"!"}'):
        print("POST")
        print(m_param)
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=obj)
    if (m == 'PUT' and response.text != '{"success":"!"}') or (m != 'PUT' and response.text == '{"success":"!"}'):
        print("PUT")
        print(m_param)
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=obj)
    if (m == 'DELETE' and response.text != '{"success":"!"}') or (m != 'DELETE' and response.text == '{"success":"!"}'):
        print("DELETE")
        print(m_param)
