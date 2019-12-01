// program for belmanford algorithm
import java.util.*;

class belmanford{
  public static void bellmanFord(int vertexnum,int edgenum,int src,int [][]edgematrix){
    int sourcedist[] = new int[vertexnum+1];
    int prevnode[]= new int[vertexnum+1];
    for (int i=1;i<=vertexnum;i++){
      sourcedist[i]=9999;
      prevnode[i]=-1;
    }
    sourcedist[src]=0;
    prevnode[src]=src;

    for(int i=1;i<=edgenum;i++){
      for(int j=1;j<=vertexnum;j++){
      int  v = edgematrix[j][1];
      int   u = edgematrix[j][0];
        int w = edgematrix[j][2];

      if(sourcedist[v]>(sourcedist[u]+w)){
        sourcedist[v]=sourcedist[u]+w;
        prevnode[v]=u;
      }}
    }

    for(int i=1;i<=edgenum;i++){
      for(int j=1;j<=vertexnum;j++){
        int v = edgematrix[j][1];
        int u = edgematrix[j][0];
        int w = edgematrix[j][2];

      if(sourcedist[v]>(sourcedist[u]+w)){
      System.out.println("negitive edge");
        return;
      }}
    }
    for(int i=1;i<=vertexnum;i++){
      System.out.println("distance from "+src+"to node"+i+"is"+sourcedist[i]+"from node"+prevnode[i]);
    }
  }
  public static void main(String arg[]){
    int vertexnum,edgenum;
    Scanner s = new Scanner(System.in);
    System.out.println("enter the number of vertex");
    vertexnum = s.nextInt();
    System.out.println("enter the number of edges");
    edgenum = s.nextInt();
    System.out.println("enter the source");
    int src  = s.nextInt();
    int [][]edgematrix = new int[edgenum+1][3];
    System.out.println("enter the matrix in from  to distance format");
    for (int i=1;i<=edgenum;i++){
      edgematrix[i][0]=s.nextInt();
      edgematrix[i][1]=s.nextInt();
      edgematrix[i][2]=s.nextInt();
    }
    bellmanFord(vertexnum,edgenum,src,edgematrix);
    // for(int i=1;i<=edgenum;i++){
    //   System.out.println(edgematrix[i][0]+" "+edgematrix[i][1]+" "+edgematrix[i][2]);
    // }
  }
}
