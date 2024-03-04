# file : p56.slackMsg.py
# desc : 슬랙으로 스마트폰 메시지 보내기
'''순서
1. https://api.slack.com/ 에서 your apps > Creat your first app
2. From Scratch 클릭 > 앱 이름은 "영
3. 워크스페이스 선택
4. Incomming Webhooks > On > Add new Webhook to Workspace 클릭 > 채널선택 > 허용
'''

# https://hooks.slack.com/services/T**/B0**

import requests
import json

slack_url = 'https://hooks.slack.com/services/T**/B0**' # 깃헙 업로드전 삭제필요

headers = { 'Content-type':'application/json'}
data = { 'text':'Python에서 보내는 메시지!!'}

res = requests.post(slack_url, headers=headers, data=json.dumps(data))
if res.status_code == 200:
    print('메시지 전송 성공!')
else:
    print('메시지 전송 실패')



