import java.io.*;
import java.util.*;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Pattern pattern = Pattern.compile("^(\\2tic|(tac))+$");
        Matcher matcher = pattern.matcher(scanner.nextLine());
        System.out.println(matcher.find());
    }
}