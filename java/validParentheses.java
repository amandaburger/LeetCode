import java.util.Stack;

public class validParentheses {
    public static boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i=0;i<s.length();i++){
            if(!stack.isEmpty()){
                if(isPair(stack.peek(),s.charAt(i))){
                                    stack.pop();
                                    continue;
                                }
                            }
                            stack.push(s.charAt(i));
                            }
                            return stack.isEmpty();
                        }
                        
                        private static boolean isPair(char last, char cur) {
            return (last == '(' && cur == ')') ||
                   (last == '{' && cur == '}') ||
                   (last == '[' && cur == ']');
        }    
        
        public static void main(String[] args) {
            System.out.println(isValid("{[]()}"));
            System.out.println(isValid("{]"));
    }
}
