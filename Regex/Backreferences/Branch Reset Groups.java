import java.io.*;
import java.util.*;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); //(---)|-|.|:
        Pattern pattern = Pattern.compile("^\\d{2}(---|-|\\.|:)(\\d{2}\\1){2}\\d{2}$");
        Matcher matcher = pattern.matcher(scanner.nextLine());
        System.out.println(matcher.find());
    }
}