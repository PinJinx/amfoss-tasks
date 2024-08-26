use std::fs;
use std::path::PathBuf;

fn main() {
    let script_dir = PathBuf::from(std::env::current_dir().unwrap());
    let input_path = script_dir.join("input.txt");
    let output_path = script_dir.join("output.txt");
    let content = match fs::read_to_string(&input_path) {
        Ok(content) => content,
        Err(err) => {
            eprintln!("Error reading input file: {}", err);
            return;
        }
    };
    match fs::write(&output_path, content.as_bytes()) {
        Ok(_) => println!("File copied successfully!"),
        Err(err) => eprintln!("Error writing output file: {}", err),
    }
}