import java.io.*;
import java.net.*;

public class CloseWaitClient {   
	public static void main(String[] args) {     
		if(args.length!=3){
			System.out.println("Usage > Client [IP] [Port] [message]\n");
			System.exit(0);
		}

		Socket sc;      
		
		BufferedReader in,stdin;     
		PrintWriter out;     
		
		String outLine ;      
		String inLine = null;      
		
		String host,msg;     
		int port;
		

		host=args[0];
		port=new Integer(args[1]).intValue();
		msg=args[2];

		System.out.println("Binding : "+host+":"+port);
		
		try {    
			sc = new Socket(host, port);       
			out = new PrintWriter(sc.getOutputStream(), true);          
			in = new BufferedReader(new InputStreamReader(sc.getInputStream()));          
			stdin = new BufferedReader(new InputStreamReader(System.in));         
			
			System.out.println("\nSend to Server: " + msg);         
				
			out.println(msg);      
				
			inLine = in.readLine();      
				
			System.out.println("Receive from Server: " + inLine);         		
		  
		  
			in.close();         
			out.close();         
			sc.close();
			
		  Thread.sleep(30000);
		} catch(Exception ex) {         
			ex.printStackTrace();       
		}   
	}
}