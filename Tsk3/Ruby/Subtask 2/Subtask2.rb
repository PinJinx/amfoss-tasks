script_dir = File.dirname(__FILE__)
input_file = File.open(File.join(script_dir, "input.txt"), "r")
content = input_file.read
output_file = File.open(File.join(script_dir, "output.txt"), "w")
output_file.write(content)

input_file.close
output_file.close