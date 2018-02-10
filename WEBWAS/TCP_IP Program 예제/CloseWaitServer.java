import java.io.*;
import java.net.*;

public class CloseWaitServer {   
	public static void main(String[] args) {      
		ServerSocket ss;      
		Socket sc;      
		BufferedReader in;      
		PrintWriter out; 
		String clientIP;
		
		try {              
		

			ss = new ServerSocket(4444,50);			            			
			
			sc = ss.accept();         
			clientIP=sc.getInetAddress().getHostAddress();
			
			System.out.println(clientIP+" connected");             
			
			in = new BufferedReader(new InputStreamReader(sc.getInputStream()));          
			out = new PrintWriter(sc.getOutputStream(), true);          
			
			String inLine;
			while((inLine = in.readLine()) != null) {           
				System.out.println("Receive from Client: " + inLine);         
			  out.println(inLine);         
				System.out.println("Send to [ " + clientIP+" ] :" + inLine);                 
			}
			Thread.sleep(20000);
			in.close();         
			out.close();         
			sc.close();     
			
			
			    
			ss.close();      
		} catch(Exception ex) {         
			ex.printStackTrace();      
		}   
	}
}