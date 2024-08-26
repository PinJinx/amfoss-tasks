IO.puts("Enter a value: ")
n = IO.gets("") |> String.trim() |> String.to_integer()

n = if rem(n, 2) == 0, do: n - 1, else: n
k = 5
for i <- Enum.filter(1..n, fn x -> rem(x, 2) == 1 end) do
  k= trunc((n - i)/2)
  IO.puts String.duplicate(" ", k) <> String.duplicate("*", i)
end
for i <- Enum.reverse(Enum.filter(1..(n - 2), fn x -> rem(x, 2) == 1 end)) do
  k= trunc((n - i)/2)
  IO.puts String.duplicate(" ", k) <> String.duplicate("*", i)
end