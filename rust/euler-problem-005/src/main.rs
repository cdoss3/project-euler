fn main() {
    /// Solve Euler problem 5. Leave Hello World in for a laugh

    println!("Hello, world!");

    // Set our initial conditions here. found_it will refer to whether we've
    // found our answer. When we find the answer, set found_it = true

    let mut num = 2520;
    let mut found_it = false;

    // Start our loop. While we don't have the answer, keep going

    while !found_it {

        // Incriment by 2520, a number we know already to be divisible up to 10

        num += 2520;

        // Assume our number is good, if it's not, then set this to false

        let mut num_is_good = true;

        /* We already know our number is divisible up to 10. Check divisibility up to 20 now */

        for k in 11..21 {

            // Check individually whether k divides num

            if !check_divisible(num, k) {

                /* If we're here, we found num not to be divisible by k. Output for progress checker, disinclude num, break loop */

                println!("{num} not divisible by {k}. Moving on.");
                num_is_good = false;
                break
            }
        }

        /* If we're here, our number was divisible by everything. Output the answer to the console, tell the program we found it, */

        if num_is_good {
            println!("Found it! Your answer is {num}");
            found_it = true
        }
    }
}

fn check_divisible(a: i64, b: i64) -> bool {
    /// A simple function to test divisibility between two integers

    if a % b == 0 {
        true
    } else {
        false
    }
}
