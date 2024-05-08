fn main() {
    let x = fibonacci(1000);
    
    for num in &x {
        println!("{num}")
    }
}

// Function to generate a Fibonacci sequence up to a max value
//
//

fn fibonacci(n: u32) -> Vec<u32> {
    let mut fib = vec![0, 1];

    while fib[fib.len() - 1] < n {
        fib.push(fib.iter().rev().take(2).sum());
    }

    fib 
}


