use std::io::{self, Write};

fn main() {
    print!("Enter a value: ");
    io::stdout().flush().unwrap();
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let mut n: i32 = input.trim().parse().expect("Please enter a valid number");
    if n % 2 == 0 {
        n -= 1;
    }
    let mut k = (n + 1) - 2;
    for i in (1..=n).step_by(2) {
        k -= 1;
        println!("{:width$}{}", "", "*".repeat(i as usize), width = k as usize);
    }
    for i in (1..=(n-2)).rev().step_by(2) {
        k += 1;
        println!("{:width$}{}", "", "*".repeat(i as usize), width = k as usize);
    }
}
