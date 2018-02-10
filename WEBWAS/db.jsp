html>
<head>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@page import="java.sql.*" %>
<%!
  String host="jdbc:mysql://localhost/mysql";
  String user="root";
  String pw="1";
  Connection conn;
  Statement stmt;
  String sql="select * from user";
  ResultSet rs;
  boolean ok=true;
%>
</head>

<body>
<h1> hello.db </h1>
<%
   try {
   Class.forName("com.mysql.jdbc.Driver");
   conn = DriverManager.getConnection(host,user,pw);
   stmt = conn.createStatement();
   rs= stmt.executeQuery(sql);

    while (rs.next()) {
    String f1 = rs.getString("host");
    String f2=  rs.getString("user");
    String f3=  rs.getString("password");
    out.println( f1 );
    out.println( f2 );
    out.println( f3 );

      }
      }  catch (Exception e) {
         out.println("ok");
         out.println(e.getMessage());
     }

%>
</body>
</html>



