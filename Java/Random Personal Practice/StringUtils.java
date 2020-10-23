public class StringUtils {
    public static void genGauge(String currentString) {
        System.out.println(currentString);
        int c = 0;
        int l = currentString.length();
        String genGauge = "";
        while(c < l) {
            genGauge = genGauge + c;
            if (c < 9) {c++;}
            else {c = 0; l = l - 10;}
        }
        System.out.println(genGauge);
    }

    public static String copy(String currentString, int startPosition, int onePastLastPosition) {
        return currentString.substring(startPosition, onePastLastPosition);
    }


    public static String cut(String currentString, int startPosition, int onePastLastPosition) {
        String temp1 = currentString.substring(0, (startPosition));
        String temp2 = currentString.substring(onePastLastPosition);
        return temp1 + temp2;
    }

    public static String paste(String currentString, int insertBefore, String stringToInsert) {
        String start = currentString.substring(0, insertBefore);
        String end = currentString.substring(insertBefore);
        return start + stringToInsert + end;
    }

}