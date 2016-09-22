# -*- coding: utf-8 -*-
import json
import pickle

@profile
def load_file_tojson(raw_file):
    results = []
    for line in raw_file:
        j = json.loads(line)
        results.append(j)
        # results.append(json.dumps(j))
        # results.append(line)
    return results

# denue_04_to_json.txt = 141M
# denue_02_to_json.txt = 25M
# denue_15_to_json.txt = 749M

if __name__ == '__main__':
    # with open("resources/denue_04_to_json.txt", "r") as raw_file:
    # with open("resources/denue_02_to_json.txt", "r") as raw_file:
    with open("resources/denue_15_to_json.txt", "r") as raw_file:
        l = load_file_tojson(raw_file)
    print(len(l))


# 04_to_json.txt = 141M
# Line #    Mem usage    Increment   Line Contents
# ================================================
#      5   14.652 MiB    0.000 MiB   @profile
#      6                             def load_file_tojson(raw_file):
#      7   14.652 MiB    0.000 MiB       results = []
#      8  846.102 MiB  831.449 MiB       for line in raw_file:
#      9  846.102 MiB    0.000 MiB           j = json.loads(line)
#     10  846.102 MiB    0.000 MiB           results.append(json.dumps(j))

#     12  846.102 MiB    0.000 MiB       return results


# 15_to_json.txt = 749M
# Line #    Mem usage    Increment   Line Contents
# ================================================
#      5   14.637 MiB    0.000 MiB   @profile
#      6                             def load_file_tojson(raw_file):
#      7   14.637 MiB    0.000 MiB       results = []
#      8 5378.891 MiB 5364.254 MiB       for line in raw_file:
#      9 5378.891 MiB    0.000 MiB           j = json.loads(line)
#     10 5378.891 MiB    0.000 MiB           results.append(j)
#     11                                     # results.append(json.dumps(j))
#     12                                     # results.append(line)
#     13 5378.891 MiB    0.000 MiB       return results
