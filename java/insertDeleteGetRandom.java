
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;
class RandomizedSet {
    
    // private final ArrayList<Integer> listt;

    // public RandomizedSet() {
    //      listt = new ArrayList<>();
        
    // }
    
    // public boolean insert(int val) {
    //     if(listt.contains(val)== true){
    //         return false;
    //     }
    //     listt.add(val);
    //     return true;
    // }
    
    // public boolean remove(int val) {
    //     if(listt.contains(val)== false){
    //         return false;
    //     }
    //      listt.remove(Integer.valueOf(val));
    //      return true;
    // }
    
    // public int getRandom() {
    //     Random random = new Random();
    //     int randomNumber = random.nextInt(listt.size());
    //     return listt.get(randomNumber);
    // }
    //--------------------------FASTER----------------------------
    private Map<Integer, Integer> map;
    private ArrayList<Integer> listt;

    public RandomizedSet() {
        listt = new ArrayList<>();
        map = new HashMap<>();
    }

    public boolean search(int val) {
        return map.containsKey(val);
    }

    public boolean insert(int val) {
        if (search(val)) return false;

        listt.add(val);
        map.put(val, listt.size() - 1);
        return true;
    }

    public boolean remove(int val) {
        if (!search(val)) return false;

        int index = map.get(val);
        listt.set(index, listt.get(listt.size() - 1));
        map.put(listt.get(index), index);
        listt.remove(listt.size() - 1);
        map.remove(val);

        return true;
    }

    public int getRandom() {
        Random rand = new Random();
        return listt.get(rand.nextInt(listt.size()));
    }


    public static void main(String[] args) {
        RandomizedSet hi = new RandomizedSet();
        System.out.println(hi.insert(1));
        System.out.println(hi.remove(2));
        System.out.println(hi.insert(2));
        System.out.println(hi.getRandom());
        System.out.println(hi.remove(1));
        System.out.println(hi.getRandom());



    }
}

