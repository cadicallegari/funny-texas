# Why python is cossuming all my memory?


I faced a memory consumption issue loading csv files to memory using dicts.
Yes, I must use generators for that, but in that case I needed to know how much entries was read.
Yes, I could use something to count how much lines there is in the file, but the logic must be generic, in other cases the data could not be a csv file.

So, it was how it all began, how could a 250 MB csv file use more than 5 GB in memory?

My point here, is to understand why python is using all my memory


## Running

pip install -r requirements.txt

python3 -m memory_profiler test.py

## TODO

- [ ] Explan tests and results
- [ ] Same tests in ruby
- [ ] Same tests in Golang
