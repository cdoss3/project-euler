fn main() {
    /// A script to solve project Euler problem 6
    
    println!("Hello, world!");

    // Mutable variables to track our sums
    let mut naturals_sum:i64 = 0;
    let mut sum_of_squares:i64 = 0;
    
    println!("Start loop through k");

    for i in 1..101 {
        // Add our counter number to the naturals, square it then add it to the sum of squares
        naturals_sum += i;
        sum_of_squares += i64::pow(i, 2);

        // Print results to check accuracy
        println!("Added {i} -- Total naturals_sum = {naturals_sum} -- Total sum_of_squares = {sum_of_squares}")
    };

    // Square the sum of the natural numbers
    let squared_sum:i64 = i64::pow(naturals_sum, 2);
    println!("Squared sum is {squared_sum}");

    let difference:i64 = squared_sum - sum_of_squares;
    println!("The answer is {difference}")
}
