public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int min = Integer.MAX_VALUE;
     
        for(int i=0; i<nums.length; i++){
            if(map.containsKey(nums[i])){
                int preIndex = map.get(nums[i]);
                int gap = i-preIndex;
                min = Math.min(min, gap);
            }
            map.put(nums[i], i);
        }
     
        if(min <= k){
            return true;
        }else{
            return false;
        }
    }
}