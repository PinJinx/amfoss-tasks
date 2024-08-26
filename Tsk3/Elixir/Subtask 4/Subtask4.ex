def get_script_dir do
    Path.dirname(__FILE__)
  end
input_path = Path.join(get_script_dir(),"input.txt")
output_path = Path.join(get_script_dir(),"output.txt")
{:ok, input_file} = File.open(input_path, [:read])
n = String.trim(IO.read(input_file)) |> String.to_integer()
File.close(input_file)
{:ok, output_file} = File.open(output_path, [:write])

try do
  n = if rem(n, 2) == 0, do: n - 1, else: n
  k = 5
  for i <- Enum.filter(1..n, fn x -> rem(x, 2) == 1 end) do
    k= trunc((n - i)/2)
    IO.write(output_file,String.duplicate(" ", k) <> String.duplicate("*", i)<> "\n")
  end
  for i <- Enum.reverse(Enum.filter(1..(n - 2), fn x -> rem(x, 2) == 1 end)) do
    k= trunc((n - i)/2)
    IO.write(output_file, String.duplicate(" ", k) <> String.duplicate("*", i)<> "\n")
  end
  File.close(output_file)
end