package stack_and_queue;
import java.util.*;

class RecentCounter {

    List<Integer> pingList;
    int curInd;

    public RecentCounter() {
        this.pingList = new ArrayList<Integer>();
        this.curInd = 0;
    }
    
    public int ping(int t) {
        this.pingList.add(t);
        int lowerVal = t - 3000;
        while (this.pingList.get(this.curInd) < lowerVal){
            this.curInd += 1;
        }
        return this.pingList.size() - this.curInd;
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */
