import json
with open(r'C:\Users\yaros\PycharmProjects\DJangoTestWorkProject\fixtures\product\categories.json', encoding='windows-1251') as f:
    data = json.load(f)
with open('1.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)