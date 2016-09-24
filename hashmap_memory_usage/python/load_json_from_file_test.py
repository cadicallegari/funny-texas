# -*- coding: utf-8 -*-
import json
from memory_profiler import profile


@profile
def load_file_tojson(raw_file):
    results = []
    for line in raw_file:
        j = json.loads(line)
        results.append(j)
        # results.append(json.dumps(j))
        # results.append(line)
    return results

# small.txt = 25M
# medium.txt = 141M
# large.txt = 749M
if __name__ == '__main__':
    # with open("../resources/small.txt", "r") as raw_file:
    # with open("../resources/medium.txt", "r") as raw_file:
    with open("../resources/large.txt", "r") as raw_file:
        l = load_file_tojson(raw_file)
    print(len(l))
