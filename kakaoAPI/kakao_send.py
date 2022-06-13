import requests
import json

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers = {
    "Authorization": "Bearer " + "H362fSYveMY8jeuy5tSMBmri1jHx1yhN_8QrGsISCj102QAAAYFYzrIw"
}


data = {
    "template_object" : json.dumps({ "object_type" : "text",
                                     "text" : "오늘의 급식: 냠냠",
                                     "link" : {
                                                 "web_url" : "https://blog.daum.net/geoscience/1624"
                                              }
    })
}

response = requests.post(url, headers=headers, data=data)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
