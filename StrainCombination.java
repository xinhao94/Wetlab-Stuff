import java.util.*;

class StrainCombination {
  
  private int nStrain;
  List<Character> strains;
  
  public StrainCombination(int nStrain) {
    this.nStrain = nStrain;
    this.strains = new ArrayList<>();
    for (int i=0; i<this.nStrain; i++) {
      char strain = (char) ('A' + i);
      this.strains.add(strain);
    }
    System.out.print("Strains: ");
    System.out.print(this.strains);
    System.out.print('\n');
  }

  public int getCombinationCount() {
    int[] combinationCount = {0};
    int[] counter = {0};
    dfs(0, counter, combinationCount);
    return combinationCount[0];
  }

  private void dfs(int idx, int[] counter, int[] combinationCount) {
    // Base case
    if (counter[0] > this.nStrain) {
      return;
    }
    if (counter[0] == this.nStrain || idx == this.nStrain-1) {
      combinationCount[0] ++;
      if (combinationCount[0] % 5000 == 0) {
        System.out.println(combinationCount[0]);
      }
      return;
    }
    // Recursion rule
    for (int i=0; i<=nStrain; i++) {
      counter[0] += i;
      dfs(idx+1, counter, combinationCount);
      counter[0] -= i;
    }
  }
}
