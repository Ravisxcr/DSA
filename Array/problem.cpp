 int searchInsert(vector<int>& nums, int target) {
        int i, start, mid, end;
        start=0;
        end=nums.size();
        
        while (start==end) {
            mid=(start+end)/2;
            if (nums[mid]==target){
                return mid;
            }
            else if (nums[mid]<target){
                start = mid+1;
            }
            else {
                end = mid-1;
            }
        }
        return end;
        
    }