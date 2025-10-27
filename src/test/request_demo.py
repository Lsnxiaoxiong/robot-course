import requests

payload = {
    "servo_id":2,
    "pulse":1600
}
r = requests.post('http://192.168.1.103:5000/robot/turn_head', json=payload, timeout=10)
print(r.json())