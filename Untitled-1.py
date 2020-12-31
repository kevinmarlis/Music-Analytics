from lxml import etree
import pandas as pd

xml_path = '/Users/kevinmarlis/Developer/Music Analytics/Library.xml'
tracks = []
track_dicts = []

for event, element in etree.iterparse(xml_path):
    if element.text == 'Tracks':
        results = element.getnext()

for element in results:
    if element.tag == 'dict':
        tracks.append(element)

for item in tracks:
    track = {}
    for element in item:
        if element.tag == 'key':
            track[element.text] = element.getnext().text
    track_dicts.append(track)

df = pd.DataFrame(track_dicts)
print(df.head)
# print(len(track_dicts))
