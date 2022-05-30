public class Main {
    public static void main(String[]args){
        encode e1 = new encode("HELLO WORLD", 'B');
        encode e2 = new encode("HELLO WORLD", 'F');
        encode e3 = new encode("HELLO WORLD", 'X');
        System.out.println(e1.toEncode());
        System.out.println(e2.toEncode());
        System.out.println(e3.toEncode());
        decode d1 = new decode("BGDKKN VNQKC");
        decode d2 = new decode("FC/GGJ RJMG.");
        decode d3 = new decode("X2Z669 /9*6Y");
        System.out.println(d1.toDecode());
        System.out.println(d2.toDecode());
        System.out.println(d3.toDecode());
    }
}
