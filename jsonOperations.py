import json

def operateFileToJson(path_to_file='artists.jsonl'):
    with open(path_to_file, 'r') as json_file:
        json_list = list(json_file)
    return json_list

def getObjectsFromJson(path_to_file='artists.jsonl'):
    json_list = operateFileToJson(path_to_file)
    objects = []
    for json_str in json_list:
        result = json.loads(json_str)
        objects.append(result)
    return objects

def writeToNewJsonFile(dictionary, path_to_file='artists_modified.jsonl'):
    with open(path_to_file, 'w') as outfile:
        json.dump(dictionary, outfile)

def writeToNewJsonFile2(dictionary, path_to_file='artists_modified.jsonl'):
    with open(path_to_file, 'w') as outfile:
        for item in dictionary:
            json.dump(item, outfile)
            outfile.write('\n')