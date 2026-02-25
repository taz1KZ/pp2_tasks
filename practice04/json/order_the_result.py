import json
x = {
  "name": "KBTU",
  "city": "Almaty",
  "courses": ["Python", "JS", "C++"]
}
#Use the sort_keys parameter to specify if the result should be sorted or not:
json.dumps(x, indent=4, sort_keys=True)
print(data)