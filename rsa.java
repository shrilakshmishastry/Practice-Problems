// rsa algorithm for data encryption and decryption
import java.util.*;

class rsa{
  public static int gcd(int m,int n){
    if(n==0){
      return m;
    }
    else{
      return gcd(n,m%n);
    }
  }
  public static int mult(int msg,int e,int n){
    int k =1;
    for(int j =1;j<=e;j++){
      k = (k*msg)%n;
    }
    return k;
  }
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int msg,cyper,d=0,n,p,q,z,e;
    System.out.println("enter two prime number p and q");
    p = s.nextInt();
    q = s.nextInt();
    n = p*q;
    z = (p-1)*(q-1);
    System.out.println("enter the message such that is less than (p*q)-2");
    msg = s.nextInt();
    System.out.println("enter the value for e such that gcd(z,e)==1");
    do{
      e = s.nextInt();
    }while(gcd(z,e)!=1);
    int i=2;
    while(((i*e)%z)!=1){
      i++;
      d=i;
    }
    System.out.println("the public key pair is "+e+" "+n);
    System.out.println("enterprivate key pair is"+d+" "+n);
    cyper = mult(msg,e,n);
    System.out.println("cyper text is"+cyper);

    int plainmsg = mult(cyper,d,n);
    System.out.println("normal text"+plainmsg);
  }
}
