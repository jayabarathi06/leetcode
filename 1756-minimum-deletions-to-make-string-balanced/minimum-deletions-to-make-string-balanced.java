class Solution {
    public int minimumDeletions(String s) {
       int before=0,deletion=0;
        for(char ch:s.toCharArray()){
            if(ch=='b') before+=1;
            else if(before>0){
                before-=1;
                deletion+=1;
            }
        }   
        return deletion;  
    }
}