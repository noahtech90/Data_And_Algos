
/*Sorting Algorithm, not used much in the real world

search through all possible pairs and swap 

if value to the right is less than

*/
let bubbleSort = (inputArr) => {
    let len = inputArr.length;
    for (let i = 0; i < len; i++) {
        for (let j = 0; j < len; j++) {
            if (inputArr[j] > inputArr[j + 1]) {
                let tmp = inputArr[j];
                inputArr[j] = inputArr[j + 1];
                inputArr[j + 1] = tmp;
            }
        }
    }
    return inputArr;
};


testArr = [22,5,62,300,5,84,7,999];
console.log(bubbleSort(testArr))






