/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
// var twoSum = function(nums, target) {
//     let map = {}
//     for (const i in nums){
//         const subtractedValue = target - nums[i]
//         if(map[subtractedValue]){
//             return [map[subtractedValue], i]
//         }
//         map[nums[i]] = i
//     }
// };

// let solution = twoSum([3,3], 6);
// console.log(solution)

// This solution works well and passes, but maybe we can try using an actual map since object only compares with the tostring

// var twoSum = function(nums, target) {
//     let map = new Map()
//     for (const i in nums){
//         const subtractedValue = target - nums[i]
//         if(map.has(subtractedValue)){
//             return [map.get(subtractedValue), i]
//         }
//         map.set(nums[i], i)
//     }
// };

// let solution = twoSum([3,5, 8], 13);
// console.log(solution)

// Lets try one more time but with the simple object and simplified code

var twoSum = function(nums, target) {
    let map = {}
    for (const i in nums){
        if(target - nums[i] in map){
            return [map[target - nums[i]], i]
        }
        map[nums[i]] = i
    }
};

let solution = twoSum([3,3], 6);
console.log(solution)

// This was the fastest solution, but worst with space