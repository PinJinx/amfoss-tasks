print "Enter a value: "
n = gets.chomp.to_i

n -= 1 if n.even?

k = (n + 1) - 2
(1..n).step(2) do |i|
  k -= 1
  puts " " * k + "*" * i
end

(n - 2).step(1, -2) do |i|
  k += 1
  puts " " * k + "*" * i
end