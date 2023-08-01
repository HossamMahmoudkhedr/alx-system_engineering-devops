#!/usr/bin/env ruby
input = ARGV[0]
pattern = /School/
if input.match(pattern)
    puts "School"
else
    puts ""
