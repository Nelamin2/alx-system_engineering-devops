#!/usr/bin/env ruby

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end
input_string = ARGV[0]
regex = /School/
match_result = input_string.match(regex)
if match_result
  puts "#{match_result[0]}$"
else
  puts "No match found"
end
