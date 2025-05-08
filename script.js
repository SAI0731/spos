// Function to check if a number is prime
function isPrime(n) {
    if (n < 2n) return false;
    if (n === 2n || n === 3n) return true;
    if (n % 2n === 0n || n % 3n === 0n) return false;
    
    let i = 5n;
    while (i * i <= n) {
        if (n % i === 0n || n % (i + 2n) === 0n) return false;
        i += 6n;
    }
    return true;
}

// Function to compute GCD (Greatest Common Divisor)
function gcd(a, b) {
    while (b !== 0n) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Function for modular exponentiation: (base^exp) % mod
function modExp(base, exp, mod) {
    let result = 1n;
    base = BigInt(base) % BigInt(mod);
    while (exp > 0n) {
        if (exp % 2n === 1n) {
            result = (result * base) % BigInt(mod);
        }
        exp = exp / 2n;
        base = (base * base) % BigInt(mod);
    }
    return result;
}

// Function to perform the Diffie-Hellman Key Exchange
function calculateDH() {
    let p = BigInt(document.getElementById("prime").value);
    let g = BigInt(document.getElementById("generator").value);
    let xa = BigInt(document.getElementById("xa").value);
    let xb = BigInt(document.getElementById("xb").value);

    // Prime check for P
    if (!isPrime(p)) {
        alert("P must be a prime number!");
        return;
    }

    // Co-prime check for G and P
    if (gcd(g, p) !== 1n) {
        alert("G must be co-prime with P! Choose a different generator.");
        return;
    }

    // Compute public keys
    let ya = modExp(g, xa, p);
    let yb = modExp(g, xb, p);

    // Compute shared secret
    let sharedA = modExp(yb, xa, p);
    let sharedB = modExp(ya, xb, p);

    // Display results
    document.getElementById("ya").innerText = ya;
    document.getElementById("yb").innerText = yb;
    document.getElementById("sharedA").innerText = sharedA;
    document.getElementById("sharedB").innerText = sharedB;
     // Should match sharedB
}
