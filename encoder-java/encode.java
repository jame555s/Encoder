import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class encode {
    String plainText;
    Character offsetChar;
    
encode(String plainText, Character OffsetChar){
    this.plainText = plainText;
    this.offsetChar = OffsetChar;
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
public String toEncode(){
    Map<Integer, Character> encodeMap = mapencodeMap();
    String encodedText = String.valueOf(this.offsetChar);
    for (int i = 0; i < this.plainText.length(); i++) {
        Character character = (this.plainText.charAt(i));
        if (character == ' '){
        encodedText += " ";
        }
        else {
            Integer encodedindex = getKey(character) - getKey(this.offsetChar);
            if (encodedindex < 0){
                encodedindex += 44;
            }
            encodedText += String.valueOf(encodeMap.get(encodedindex));
        }
    }
    return encodedText;
}
}
