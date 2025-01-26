
import java.util.ArrayList;
import java.util.Random;
class RandomizedSet {
    private final ArrayList<Integer> listt;

    public RandomizedSet() {
         listt = new ArrayList<>();
        
    }
    
    public boolean insert(int val) {
        if(listt.contains(val)== true){
            return false;
        }
        listt.add(val);
        return true;
    }
    
    public boolean remove(int val) {
        if(listt.contains(val)== false){
            return false;
        }
         listt.remove(Integer.valueOf(val));
         return true;
    }
    
    public int getRandom() {
        Random random = new Random();
        int randomNumber = random.nextInt(listt.size());
        return listt.get(randomNumber);
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

