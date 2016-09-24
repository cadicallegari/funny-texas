# Loading file a list of dicts

### Small file

```
Filename: load_json_from_file_test.py

Line #    Mem usage    Increment   Line Contents
================================================
     6     14.2 MiB      0.0 MiB   @profile
     7                             def load_file_tojson(raw_file):
     8     14.2 MiB      0.0 MiB       results = []
     9    198.1 MiB    183.9 MiB       for line in raw_file:
    10    198.1 MiB      0.0 MiB           j = json.loads(line)
    11    198.1 MiB      0.0 MiB           results.append(j)
    12                                     # results.append(json.dumps(j))
    13                                     # results.append(line)
    14    198.1 MiB      0.0 MiB       return results
```

small.txt = 25M
memory usage = 183.9 M


### Medium fi

```
Filename: load_json_from_file_test.py

Line #    Mem usage    Increment   Line Contents
================================================
     6     14.2 MiB      0.0 MiB   @profile
     7                             def load_file_tojson(raw_file):
     8     14.2 MiB      0.0 MiB       results = []
     9   1021.2 MiB   1006.9 MiB       for line in raw_file:
    10   1021.2 MiB      0.0 MiB           j = json.loads(line)
    11   1021.2 MiB      0.0 MiB           results.append(j)
    12                                     # results.append(json.dumps(j))
    13                                     # results.append(line)
    14   1021.2 MiB      0.0 MiB       return results

```

medium.txt = 141M
memory usage =  1G

### Large file


```
Line #    Mem usage    Increment   Line Contents
================================================
     5   14.637 MiB    0.000 MiB   @profile
     6                             def load_file_tojson(raw_file):
     7   14.637 MiB    0.000 MiB       results = []
     8 5378.891 MiB 5364.254 MiB       for line in raw_file:
     9 5378.891 MiB    0.000 MiB           j = json.loads(line)
    10 5378.891 MiB    0.000 MiB           results.append(j)
    11                                     # results.append(json.dumps(j))
    12                                     # results.append(line)
    13 5378.891 MiB    0.000 MiB       return results
```

large.txt = 749M
memory usage =  5.3G




# Creating dicts

size = 700000
Filename: test.py
```
Line #    Mem usage    Increment   Line Contents
================================================
    50 3123.121 MiB    0.000 MiB   @profile
    51                             def _create_random_string(size):
    52 3123.121 MiB    0.000 MiB       return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))


Filename: test.py

Line #    Mem usage    Increment   Line Contents
================================================
    55 3123.121 MiB    0.000 MiB   @profile
    56                             def create_random_json(fields, field_value_size=20):
    57 3123.121 MiB    0.000 MiB       result = {}
    58 3123.121 MiB    0.000 MiB       for field in fields:
    59 3123.121 MiB    0.000 MiB           result[field] = _create_random_string(field_value_size)
    60 3123.121 MiB    0.000 MiB       return result


Filename: test.py

Line #    Mem usage    Increment   Line Contents
================================================
    63   16.215 MiB    0.000 MiB   @profile
    64                             def create_random_json_list(size):
    65   16.215 MiB    0.000 MiB       results = []
    66 3123.121 MiB 3106.906 MiB       for i in range(size):
    67 3123.121 MiB    0.000 MiB           results.appe
```
