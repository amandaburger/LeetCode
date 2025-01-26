import java.util.Arrays;

public class validAnagram {
    public static boolean isAnagram(String s, String t) {
            char[] k = s.toCharArray();
            char[] n = t.toCharArray();
            Arrays.sort(k);
            Arrays.sort(n);
            return Arrays.equals(k,n);
            
        }
        public static void main(String[] args) {
            System.out.println(isAnagram("anagram", "nagaram"));
    }
}
