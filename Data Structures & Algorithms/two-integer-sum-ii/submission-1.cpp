class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        int x = 0;
        int y = numbers.size() - 1 ;

        while(x != y){
            if (numbers[x] + numbers[y] > target){
                y -= 1;
            } 
            else if (numbers[x] + numbers[y] < target){
                x += 1 ;
            }
            else{
                return {x + 1, y + 1};
            }
        } 




    }
};
