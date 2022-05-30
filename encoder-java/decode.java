import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class decode {
    String encodedText;

decode(String encodedText){
    this.encodedText = encodedText;
}
public static Map<Integer, Character> mapencodeMap(){
    String characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()*+,-./";
    HashMap<Integer, Character> encodeMap = new HashMap<>();
    for (int i = 0; i < characters.length(); i++) {
        Character character = (characters.charAt(i));
        encodeMap.put(i, character);
    }
    return encodeMap;
}
public static Integer getKey(Character a){
    Map<Integer, Character> encodeMap = mapencodeMap();
    for(Entry<Integer, Character> entry: encodeMap.entrySet()) {
        if (entry.getValue() == a)
            return entry.getKey();
    }
    return null;
}
public String toDecode(){
    Map<Integer, Character> encodeMap = mapencodeMap();
    String plainText = "";
    Integer offsetInt = getKey(this.encodedText.charAt(0));
    encodedText = this.encodedText.substring(1);
    for (int i = 0; i < encodedText.length(); i++) {
        if ((encodedText.charAt(i)) == ' '){
            plainText += " ";
        }
        else{
            Integer index = getKey(encodedText.charAt(i)) + offsetInt;
            if (index > 43){
                index -= 44;
            }
                plainText += String.valueOf(encodeMap.get(index));
        }
    }
    return plainText;
}
}
