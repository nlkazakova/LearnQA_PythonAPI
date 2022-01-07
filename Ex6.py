import requests

responses = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
i=0
if responses.history:
    print("Request was redirected")
    for resp in responses.history:
        i=i+1
        print(resp.status_code, resp.url)
    print("Final destination:")
    print(responses.status_code, responses.url)
    print(f"Количество редиректов - {i}")
else:
    print("Request was not redirected")

