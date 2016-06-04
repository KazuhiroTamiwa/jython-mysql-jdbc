from java.lang import Class
from java.sql import DriverManager

class classPathHacker:
    import java.net.URLClassLoader

    def addFile(self, s):
        sysloader = self.java.lang.ClassLoader.getSystemClassLoader()
        sysclass = self.java.net.URLClassLoader
        method = sysclass.getDeclaredMethod("addURL", [self.java.net.URL])
        method.setAccessible(1)
        f = self.java.io.File(s)
        method.invoke(sysloader, [f.toURL()])

c = classPathHacker()
c.addFile("mysql-connector-java-5.1.39-bin.jar")
driver = "com.mysql.jdbc.Driver"
Class.forName(driver).newInstance()

conn = DriverManager.getConnection("jdbc:mysql://hogehoge.com:3306/db_name", "username", "password")
conn.close()
