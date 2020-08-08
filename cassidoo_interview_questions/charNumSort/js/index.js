let myArray = ["Bananas", "do", "not", "grow", "in", "Mississippi"];

/**
 * Prints an array that has been sorted based on the number
 * of distinct characters that occur in the word
 * @param {string[]} arr
 * {@link https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort}
 */
const charNumSort = (arr) => {
  arr.sort((a, b) => {
    let a_len = distinctCharacters(a);
    let b_len = distinctCharacters(b);
    if (a_len === b_len) {
      return 0;
    } else if (a_len > b_len) {
      return 1;
    } else {
      return -1;
    }
  });

  arr.sort((a, b) => {
    if (a.length === b.length) {
      return 0;
    } else if (a.length > b.length) {
      return 1;
    } else {
      return -1;
    }
  });

  console.log(arr);
};

/**
 * Return number of distinct characters
 * @param {string} str
 * @returns {number}
 */
const distinctCharacters = (str) => {
  let characters = [];
  for (let i = 0; i < str.length; i++) {
    const character = str[i];
    if (!characters.includes(character)) {
      characters.push(character);
    }
  }
  return characters.length;
};

charNumSort(myArray);
