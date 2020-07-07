#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:)[a-zA-Z0-9+]+|(?<=to:)[a-z0-9+]+|(?<=flags:)[a-z0-9+-:]+/).join(",")
