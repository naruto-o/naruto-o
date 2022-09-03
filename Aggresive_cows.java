https://www.spoj.com/problems/AGGRCOW/
class solution{
  static boolean isPossible(int a[],int cows,int n ,int mindist){
    int cntcows = 1;
    int lastplacedcow = a[0];
    for(int i =1;i<n;i++){
      if(a[i]-lastplacedcow>=mindist){
        cnt cows++;
        lastPlacedcow =a[i];
      }
    }
    if(cntcows>=cows)return true;
    return false;
  }
  public static void main(String[] args){
    int n =5,cows = 3;
    int a[] = {1,2,4,8,9};
    Arrays.sort(a);
    int low = 1;int high= a[n-1]-a[0];
    while(low<=high){
        int mid = (low + high)>>1;
      if(isPossible(a,n,cows,mid)){
  lowm = mid+1;
        else{
          high = mid-1;
        }
       System.out.println(high);
      }
    }
  
