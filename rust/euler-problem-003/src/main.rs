fn main() {
    println!("Hello, world!");
    let x: i64 = 600851475143;
    let midpoint: i64 = x / 2;

    for k in (3..midpoint) {

        if (x % k == 0) & (is_prime(k)) {
            println!("{k} is a prime factor of 600,851,475,143"); 
        }
    }
    println!("No prime factor found");
}

fn is_prime(num:i64) -> bool {
    let midpoint = num / 2;

    for k in 2..midpoint { 
        if num % k == 0 {
            return false;
        }
    }
    true
}
