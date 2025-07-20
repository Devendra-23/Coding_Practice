function filter_even_numbers(numbers) {
  let evens = [];
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) {
      evens.push(numbers[i]);
    }
  }

  return evens;
}
