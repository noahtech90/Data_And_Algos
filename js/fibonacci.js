function fib(num) {
    if (num <=2) {
        return num
    }


    return fib(num - 1) + fib(num - 2)
    
}

const fibSum = () => {
    let sum = 0;

    for (i = 1; i < 6; i++) {
        console.log(fib(i));
    }
}

fibSum()