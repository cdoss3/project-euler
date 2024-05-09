fn main() {

    let x = fibonacci(4000000);
    let mut total = 0;
    
    for num in &x {
        
        if num % 2 == 0 {
            total += num;
        }
    }

    println!("The sum of all even Fibonacci numbers < 4,000,000 is {total}");
}

// Function to generate a Fibonacci sequence up to a max value
//
//
// We are going to ignore that a number is still generated which is over 4000000 since
// that number is odd, and won't be added to our total anyway
//

fn fibonacci(n: u32) -> Vec<u32> {
    let mut fib = vec![0, 1];

    while fib[fib.len() - 1] < n {
        fib.push(fib.iter().rev().take(2).sum());
    }

    fib 
}


