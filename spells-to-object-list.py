import json

try:
    with open("spells.json", 'r') as file:
        content = json.load(file)
        finished = {};
        finished['spells'] = [];
        for key in content.keys():
            data = content[key];
            data['name'] = key;
            finished['spells'].append(data);

    with open("converted-spells.json", 'w') as file:
        json.dump(finished, file)

except IOError as e:
    print "Error reading spells ({0}): {1}".format(e.errno, e.strerror)
