#!/usr/bin/env ruby
# This script accepts one argument and pass it to a regular expression matching method

def match_school(argument)
    regex = /School/
  
    if argument =~ regex
      puts "Match found: '#{argument}' contains 'School'."
    else
      puts "No match: '#{argument}' does not contain 'School'."
    end
  end
  
  if ARGV.empty?
    puts "Usage: ruby match_school.rb <argument>"
  else
    user_argument = ARGV[0]
  
    match_school(user_argument)
  end