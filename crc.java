import java.util.*;

class crc{
  public static String msg;
  public static String genp = "10001000000100001";
  public static String csum;
  public static int totallen;
  public static int genplen;
  public static int msglen;
  public static String xor(String csum,String genp){
    int gen = Integer.parseInt(genp,2);
    int csum1 = Integer.parseInt(csum,2);
    int result = gen^csum1;
    return Integer.toBinaryString(result);
  }
  public static String crcgen(){
    int i = genplen;
    csum = msg.substring(0,genplen);
    do {
      if(csum.charAt(0)!='1'){
        csum = csum.substring(1,csum.length());
      }
      if(csum.length()==genplen){
        csum = xor(csum,genp);
      }
      csum = csum+msg.charAt(i++);
    } while (i<totallen);
    if(csum.length()==genplen){
      csum = xor(csum,genp);
    }
    return csum;
  }
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    System.out.println("enter the data");
    msg = s.nextLine();
    System.out.println("generating polynomial is"+genp);
    msglen = msg.length();
    genplen = genp.length();
    totallen = msglen+genplen-1;
    for(int i = msglen;i<totallen;i++){
      msg+= 0;
    }
    System.out.println("msg after modification"+msg);
    crcgen();
    msg = xor(msg,csum);
    System.out.println("generated message"+msg);
    int newLen = msg.length();
    System.out.println("enter receive data");
    msg = s.nextLine();
    if(msg.length()!= newLen){
      System.out.println("error");
    }
    else{
      crcgen();
      if(csum.contains("1")){
        System.out.println("error");
      }
      else{
        System.out.println("no error  ");
      }
    }
  }
}
