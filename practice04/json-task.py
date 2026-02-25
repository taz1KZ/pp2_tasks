import json
print("Interface status")
print("=" * 50)
print("DN                         Description       Speed  MTU") # DO NOT KNOW how to position
print("-" * 60)
with open('sample-data.json', 'r') as file:
    data = json.load(file)
for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]
    print(attr["dn"], attr["descr"], attr["speed"], attr["mtu"])