#!/usr/bin/env ruby
# This is ruby script that accept argument and pass it to a reqular expression
argument = ARGV[0]
matches = argument.scan(/^h[a-zA-Z0-9]{1}n$/)
matches.each do |match|
  print match
end
puts
