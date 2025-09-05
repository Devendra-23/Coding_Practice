function secondLargest(nums) {
  let largest = -Infinity;
  let second = -Infinity;

  for (let n of nums) {
    if (n > largest) {
      second = largest;
      largest = n;
    } else if (n < largest && n > second) {
      second = n;
    }
  }

  return second === -Infinity ? null : second;
}
