package Java.twoSum;

import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(target-nums[i]))
            {
                return new int[]{map.get(target-nums[i]), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{};
    }
}


class Main {
    public static void main(String[] args)
    {
        Solution solution = new Solution();
        int[] result = solution.twoSum(new int[]{1,2,3}, 5);
        System.out.println(Arrays.toString(result));
    }
}


//Need to figure out how to instantiate inline a new arraylist, if possible
// Looks like we need to do new int[]{x,y,z,etc} to do an inline array
// HashMap is the data structure needed for hash maps in java
// This solution is faster than 99% of solutions in leetcode