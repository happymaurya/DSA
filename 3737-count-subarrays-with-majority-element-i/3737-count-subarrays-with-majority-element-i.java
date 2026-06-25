class Solution{
    public int countMajoritySubarrays(int[] nums,int target){
        int totalLength=nums.length;
        int validSubarrayCount=0;
        for(int startIndex=0;startIndex<totalLength;startIndex++){
            int targetCount=0;
            int otherCount=0;
            for(int endIndex=startIndex;endIndex<totalLength;endIndex++){
                if(nums[endIndex]==target){
                    targetCount++;
                }else{
                    otherCount++;
                }
                if(targetCount>otherCount){
                    validSubarrayCount++;
                }
            }
        }
        return validSubarrayCount;
    }
}