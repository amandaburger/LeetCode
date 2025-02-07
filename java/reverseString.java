public class reverseString {
    public static String reverseWords(String s) {
            String[] words = s.split("\s+");
            StringBuilder result = new StringBuilder();
            for (int i = words.length-1; i >=0; i--) {
                if(! words[i].isEmpty()){
                    //System.out.println(words[i]);
                    result.append(words[i]+" ");
                }
            }
        return result.toString().trim();
    }
    
    public static void main(String[] args) {
        System.out.println(reverseWords(" hello there bob "));
        System.out.println(reverseWords("hi there janet "));
    System.out.println(reverseWords("noah is a weird guy"));



}
}

