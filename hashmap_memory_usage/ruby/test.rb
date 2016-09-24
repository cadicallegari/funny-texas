require 'memory_profiler'
require 'json'

# FILE_NAME = "../resources/small.txt"
FILE_NAME = "../resources/medium.txt"
# FILE_NAME = "../resources/large.txt"


report = MemoryProfiler.report do

  list = []

  File.open(FILE_NAME) do |f|
    f.each_line do |line|
      list << JSON.parse(line)
    end
  end

end

report.pretty_print
