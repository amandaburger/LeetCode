import java.util.Stack;

public class simplifyUnixPath {

    public static String simplifyPath(String path) {
            String[] components = path.split("/");
            Stack<String> st = new Stack<>();
    
            for (String i: components){
                if( i.equals("")|| i.equals(".")){
                    continue;
                }
                if(i.equals("..")){
                    if(!st.isEmpty()){
                        st.pop();
                    }
                    
                }
                else{
                    st.push(i);
                }
            }
            StringBuilder result = new StringBuilder();
            while (!st.isEmpty()) {
                result.insert(0, "/" + st.pop());
            }
            if(result.length() == 0){
                return "/";
            }
            return result.toString();
        }
    
        public static void main(String[] args) {
            System.out.println(simplifyPath("/home/"));
            System.out.println(simplifyPath("/home//foo/"));
            System.out.println(simplifyPath("/home/user/Documents/../Pictures"));
            System.out.println(simplifyPath("/../"));
            System.out.println(simplifyPath("/.../a/../b/c/../d/./"));
 


}
    
}
