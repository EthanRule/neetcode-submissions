class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    #res = []
    permuteUnique(nums) {
          const result = [];

  // Base case: if array is empty, return an empty array inside a container
  if (nums.length === 0) return [[]];

  for (let i = 0; i < nums.length; i++) {
    const currentNum = nums[i];
    
    // Create an array of the remaining elements
    const remainingNums = nums.slice(0, i).concat(nums.slice(i + 1));
    
    // Recursively get permutations of the remaining elements
    const remainingPermutations = getPermutations(remainingNums);
    
    // Prepend the current number to each sub-permutation
    for (let j = 0; j < remainingPermutations.length; j++) {
      result.push([currentNum, ...remainingPermutations[j]]);
    }
  }

  return result;
    }
}
