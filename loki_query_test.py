from loki import Loki
import json
from dotenv import load_dotenv
import os

load_dotenv()

username = os.environ.get("username")
password = os.environ.get("password")

loki = Loki(username = username, password = password, hosturl = "https://dev.saplingdata.com/covid19Dev/api/urn/com/loki/core/model/api/query/v/")

result = loki.data.query("urn:com:saplingdata:covid19:model:queries:covid_policy_areas", None)

if not result.is_success():
  raise Exception(result.get_error())

print(result.get_response().status_code)
print(result.get_response().content)
print(result.get_response().json())

for item in result.to_array():
  for value in item:
    print(value)