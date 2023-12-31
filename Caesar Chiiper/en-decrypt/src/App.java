import java.io.*;
import java.util.*;
public class Solution { //to keep track of index
  public static final String alpha = "abcdefghijklmnopqrstuvwxyz";

  public static String encrypt(String message, int shiftKey) {
    message = message.toLowerCase();
    String cipherText = "";
    for (int ii = 0; ii < message.length(); ii++) {
      int charPosition = aplha.indexOf(message.charAt(ii));
      int keyVal = (shiftKey + charPosition) % 26;
      char replaceVal = aplha.charAt(keyVal);
      cipherText += replaceVal;
    }
    return cipherText;
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String message = new String();
    int key = 0;
    System.out.print("Enter the String for Encryption:");
    message = sc.next();

    System.out.println("\n\nEnter Shift Key:");
    key = sc.nextInt();
    System.out.println("\nEncrpyted msg:" + encrypt(message, key));
  } //main method ends
} //Solution Class End


age_modus = data['Age'].mode()[0]
print('Modus dari Age: ', age_modus)

inc_modus = data['Income'].mode()[0]
print('Modus dari Income: ', inc_modus)

credit_score_modus = data['Credit Score'].mode()[0]
print('Modus dari Credit Score: ', credit_score_modus)

chl_modus = data['Credit History Length'].mode()[0]
print('Modus dari Credit History Length: ', chl_modus)

loansamt_modus = data['Loan Amount'].mode()[0]
print('Modus dari Loan Amount: ', loansamt_modus)

loantenure_modus = data['Loan Tenure'].mode()[0]
print('Modus dari Loan Tenure: ', loantenure_modus)

profile_modus = data['Profile Score'].mode()[0]
print('Modus dari Profile Score: ', profile_modus)