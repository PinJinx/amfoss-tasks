defmodule FileCopy do
    def get_script_dir do
      Path.dirname(__FILE__)
    end
    def copy_file(input_filename, output_filename) do
      input_path = Path.join(get_script_dir(), input_filename)
      output_path = Path.join(get_script_dir(), output_filename)
      {:ok, input_file} = File.open(input_path, [:read])
      content = IO.read(input_file)
      {:ok, output_file} = File.open(output_path, [:write])
      File.write(output_file, content)
      File.close(input_file)
      File.close(output_file)
    end
  end

FileCopy.copy_file("input.txt", "output.txt")