public class Solution {
   public void moveZeroes(int[] nums) {
       if(nums == null || nums.length <= 1) {
           return ;
       }
       int i = 0;
       int j = 0;
       while(j < nums.length) {
           if(nums[j] != 0) {
               nums[i]=nums[j];
               i++;
           }
           j++;
       }
       
       while(i < nums.length){
           nums[i]=0;
           i++;
       }
       return;
   }
}