script_dir = File.dirname(__FILE__)
input_file = File.open(File.join(script_dir, "input.txt"), "r")
n = input_file.readline.chomp.to_i
input_file.close
output_file = File.open(File.join(script_dir, "output.txt"), "w")
n -= 1 if n.even?
k = (n + 1) - 2
(1..n).step(2) do |i|
  k -= 1
  output_file.write(" " * k + "*" * i + "\n")
end
(n - 2).step(1, -2) do |i|
  k += 1
  output_file.write(" " * k + "*" * i + "\n")
end
output_file.close
