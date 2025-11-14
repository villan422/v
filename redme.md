*Node js:
    1. Create folder & clone Node.js project
        mkdir C:\docker_app_lab1
        cd C:\docker_app_lab1
        git clone https://github.com/<repo-owner>/<project>.git
        cd <project>
    2.Install & run the Node.js application
        npm install
        npm start
          or
        node app.js
    3.Create folder in Linux
        mkdir -p /home/student/docker_app_lab1
        cd /home/student/docker_app_lab1
    4. Clone the same project
        git clone https://github.com/<repo-owner>/<project>.git
        cd <project>
    5. Install Node.js (if not installed)
        sudo apt update
        sudo apt install -y nodejs npm
    6.npm install
      npm start  or node app.js
    7.Take Screenshots
*php:
    1. Create folder & clone PHP project
        mkdir C:\docker_app_lab1
        cd C:\docker_app_lab1
        git clone https://github.com/<repo-owner>/<project>.git
        cd <project>
    2.Copy project into XAMPP htdocs
        Cut and paste into xampm/htdocs folder
    3.Restart the Xampp server
    4.Run PHP app in browser
        http://localhost/php_app_lab2
    In Linux Start:
    5.Create folder in Linux
        mkdir -p /home/student/php_app_lab2
        cd /home/student/php_app_lab2
    6.Clone same project
      git clone https://github.com/<repo-owner>/<project>.git
        cd <project>
    7.Install Apache, PHP, required extensions 
        sudo apt update
        sudo apt install -y apache2 php php-mysql php-cli php-xml php-zip php-curl libapache2-mod-php
    8.Move project to Apache directory
        sudo cp -r /home/student/php_app_lab2/<php-project> /var/www/html/php_app_lab2
    9.Set folder permissions
        sudo chmod -R 755 /var/www/html/php_app_lab2
        sudo chown -R www-data:www-data /var/www/html/php_app_lab2
    10.Restart Appache
       sudo systemctl restart apache2
    11.Run on browser
        http://localhost/php_app_lab2
    
*Python:
    1.Make Directory and clone project
    2.Build Docker image
       docker build -t python-docker-app .
    3.Run container
       docker run -d -p 5000:5000 python-docker-app
    4.run in browser
      http://localhost:5000
    5.Create folder in linux and clone same project
        mkdir -p /home/student/docker_lab6
        cd /home/student/docker_lab6
        git clone https://github.com/docker/labs.git
        cd labs/beginner/flask-app
    6.Install Docker
        sudo apt update
        sudo apt install -y docker.io
        sudo systemctl start docker
        sudo systemctl enable docker
    7.Build Docker image
       docker build -t python-docker-app .
    8.Run container
      docker run -d -p 5000:5000 python-docker-app
    9.open in browser
       https://localhost:5000
*Java
    1.Create Directory and clone the project:
        cd C:\
        mkdir java_lab14
        cd java_lab14
        git clone https://github.com/shreyansh-zak/Simple-Java-Maven-WebApp.git
        cd Simple-Java-Maven-WebApp
    2.Build the Maven project
        mvn clean install
    3. Deploy to Apache Tomcat
        1.Install Tomcat (if not installed).
        2.Go to:
            C:\tomcat\webapps\
        3.Copy the WAR file:
           C:\java_lab14\Simple-Java-Maven-WebApp\target\SimpleWebApp.war
            Paste into webapps folder.
        4.Start Tomcat
            cd C:\tomcat\bin
            startup.bat
        5.Open Browser and test
           http://localhost:8080/SimpleWebApp/
    4.For Linux:
        Create Directory and clone same project:
        mkdir -p /home/student/java_lab14
        cd /home/student/java_lab14
        git clone https://github.com/shreyansh-zak/Simple-Java-Maven-WebApp.git
        cd Simple-Java-Maven-WebApp
    5.Install Maven + Java (if not installed)
        sudo apt update
        sudo apt install default-jdk maven -y
    6.Build the project
        mvn clean install
    7.Install Tomcat 9 (if not installed)
        sudo apt install tomcat9 -y
    8.Deploy WAR to Linux Tomcat
        sudo cp target/SimpleWebApp.war /var/lib/tomcat9/webapps/
    9.Restart Tomcat:
        sudo systemctl restart tomcat9
    10.Test In Browser:
        http://localhost:8080/SimpleWebApp/
        






           









      







   



    




