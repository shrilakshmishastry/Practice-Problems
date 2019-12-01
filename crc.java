// program to check crc
import java.util.*;


class crc{
  public static String csum;
  public static String genep="10001000000100001";
  public static String msg;
  public static int totalLen;
  public static int genplen;
  public  static int msgLen;
  public static String xor(String csum, String genep ){
    int csumI = Integer.parseInt(csum,2);
    int genepI = Integer.parseInt(genep,2);
    int result = csumI ^ genepI;
    return  Integer.toBinaryString(result);
  }
  public static void crc(){
    System.out.println("hello");
    int i = genep.length();
    csum = msg.substring(0,genplen);
    do{
      if(csum.charAt(0)!='1'){
        csum =csum.substring(1,csum.length());
      }
      if(csum.length()== genep.length()){
      csum =  xor(csum,genep);
      }
      csum +=msg.charAt(i);
      i++;
    }while(i<totalLen);
    if(csum.length()== genep.length()){
    csum=  xor(csum,genep);
    }
  }
  public static void main(String[] args) {
    System.out.println("hello");
    System.out.println("result= "+xor("10001","10001"));
    System.out.println("enter the message");
    Scanner s = new Scanner(System.in);
    msg = s.next();
    System.out.println("entered message"+msg);
    msgLen = msg.length();
    System.out.println("entered message length"+msgLen);
    genplen = genep.length();
    totalLen = msgLen+genplen-1;
    for (int i=msgLen;i<totalLen;i++){
      msg+="0";
    }
    crc();
    msg = xor(msg,csum);
    System.out.println("entered message"+msg);
    System.out.println("csum"+csum);
    // System.out.println("csum"+csum);\
    int length = msg.length();
    System.out.println("enter message");
    msg = s.next();
    System.out.println("entered message"+msg);
    crc();
    if(length!=msg.length()){
      System.out.println("erroe");
    }

    if(csum.contains("1")){
      System.out.println("error");
    }
    else{
      System.out.println("no error");
    }

  }
}
