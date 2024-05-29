# festago-locust

페스타고 어플리케이션의 부하 테스트를 위한 저장소

## Setup

1. `python -3.11 -m venv .venv` (최소 3.9 이상 사용할 것)
2. `source ./.venv/bin/activate`
3. `pip install -r requirements.txt`

## How to run

1. `locust -f ./locustfiles/school/school_festivals_test.py`


## Option (but recommend)

1. `vi ./locust.conf`
2. 
```
host = https://yourdomain.com
users = 500
spawn-rate = 100
autostart = false 
run-time = 60s
```
