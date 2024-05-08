fn main() {
    let mut total = 0; // Initialize a variable to track the sum

    for n in 1..1000 {
        // For each n, check divisibility

        let truly_three: bool = divisible_by_three(n);
        let truly_five: bool = divisible_by_five(n);
        
        // Add to total if divisible by 3 or 5. Print the values
        // as well as the added value if there was one
        
        if truly_three | truly_five {
            total += n;
            println!("{total} (Added {n})");
        } else {
            println!("{total}");
        }
    }
}

// Functions to determine divisibility by three and five


fn divisible_by_three(number: u32) -> bool {
    // Return true if number is divisible by 3
    
    if number % 3 == 0 {
        true
    } else {
        false
    }
}

fn divisible_by_five(number: u32) -> bool {
    // Return true if number is divisible by 5
    
    if number % 5 == 0 {
        true
    } else {
        false
    }
}
