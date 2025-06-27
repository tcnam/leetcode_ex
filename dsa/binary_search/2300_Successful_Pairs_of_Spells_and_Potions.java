package sorting;
import java.util.Arrays;

class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        Arrays.sort(potions);
        int nSpells = spells.length;
        int nPotions = potions.length; 
        int[] successfulPairs = new int[nSpells];

        for (int i = 0; i < nSpells; i++) {
            int left = 0;
            int right = nPotions - 1;

            while (left <= right) {
                int mid = left + (right - left) / 2;
                if ((long) spells[i] * potions[mid] >= success) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }

            successfulPairs[i] = nPotions - left;
        }
        return successfulPairs;
    }
}
