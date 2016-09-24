# Why python is cossuming all my memory?


I faced a memory consumption issue loading csv files to memory using dicts.
Yes, I must use generators for that, but in that case I needed to know how much entries was read.
Yes, I could use something to count how much lines there is in the file, but the logic must be generic, in other cases the data could not be a csv file.

So, it was how it all began, how could a 250 MB csv file use more than 5 GB in memory?

My point here is to understand why python is using all my memory


Some tests results can be found [here](results.md)



## Running

If you want to tests with same files you can download:

- [Small](https://www.dropbox.com/s/za7cj025seknafh/small.txt.zip?dl=0)
- [Medium](https://www.dropbox.com/s/awf5vqa89o7erv4/medium.txt.zip?dl=0)
- [Large](https://www.dropbox.com/s/51gkyvgf16xpn4k/large.txt.zip?dl=0)



## TODO

- [ ] Explan tests and results
- [ ] Same tests in Golang
- [ ] Same tests in ruby
