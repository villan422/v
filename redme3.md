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
        



######################################################################################################################

Step-by-Step Guide: Connect Windows to Ubuntu Using FileZilla (SFTP)
1) VirtualBox – Configure Network Adapters
•	Shutdown the VM completely.
•	Open VirtualBox → Select Ubuntu VM → Settings → Network.
•	Adapter 1 → Enable Adapter → Attached to: NAT (provides internet).
•	Adapter 2 → Enable Adapter → Attached to: Host-only Adapter (for Windows ↔ Ubuntu communication).
•	Ensure Host-Only adapter exists via: File → Host Network Manager → Create if missing.
2) Verify Host-Only Adapter Exists on Windows
•	Open Control Panel → Network and Internet → Network Connections.
•	Confirm ‘VirtualBox Host-Only Network’ appears.
•	If missing → create via VirtualBox Host Network Manager.
3) Start Ubuntu and Identify Network Interface
•	Run: ip addr
•	Find the Host-Only interface (usually enp0s8 or eth1).
4) Assign Temporary IP to Ubuntu (works until reboot)
•	sudo ip addr add 192.168.56.11/24 dev enp0s8
•	sudo ip link set enp0s8 up
•	Check with: ip addr show enp0s8
5) Assign Permanent Static IP (Netplan)
•	Check files: ls /etc/netplan
•	Edit file: sudo nano /etc/netplan/01-netcfg.yaml
•	Example configuration:
•	network:
•	  version: 2
•	  renderer: NetworkManager
•	  ethernets:
•	    enp0s8:
•	      dhcp4: no
•	      addresses: [192.168.56.11/24]
•	      gateway4: 192.168.56.1
•	      nameservers:
•	        addresses: [8.8.8.8, 8.8.4.4]
•	Apply config: sudo netplan apply
•	Verify IP: ip addr show enp0s8
6) Install & Enable SSH on Ubuntu
•	sudo apt update
•	sudo apt install -y openssh-server
•	sudo systemctl start ssh
•	sudo systemctl enable ssh
•	sudo systemctl status ssh
7) Firewall Rules (If UFW is enabled)
•	sudo ufw allow ssh
•	sudo ufw enable
•	sudo ufw status
8) Windows – Verify Windows IP
•	Open CMD: ipconfig
•	Check IPv4 Address on VirtualBox Host-Only Adapter (e.g., 192.168.56.1).
9) Test Connection Between Windows & Ubuntu
•	From Windows CMD: ping 192.168.56.11
•	From Ubuntu Terminal: ping 192.168.56.1
10) Optional: Test SSH from Windows
•	ssh <ubuntu-username>@192.168.56.11
•	If works, FileZilla will work too.
11) Connect Using FileZilla (Windows → Ubuntu)
•	Open FileZilla.
•	Host: sftp://192.168.56.11
•	Username: <your ubuntu username>
•	Password: <your ubuntu password>
•	Port: 22
•	Click Quickconnect.
•	Left Pane = Windows files, Right Pane = Ubuntu files.
12) Transfer Files
•	Drag files from left (Windows) → right (Ubuntu).
•	Or right-click → Upload.
13) Troubleshooting
•	Check SSH: sudo systemctl status ssh
•	Check IP: ip addr
•	Check open port: sudo netstat -tulpn | grep :22
•	Disable firewall if needed: sudo ufw disable
•	Ensure Host-Only adapter enabled in VirtualBox.



#################################################################################################

Ruby (Ruby on Rails) Deployment & Migration Guide (Windows → Ubuntu)
1. Download & Setup Ruby/Rails Project (Windows)
•	Install RubyInstaller from rubyinstaller.org.
•	Enable MSYS2 toolchain during installation.
•	Install Rails: gem install rails.
•	Clone project: git clone <repo-url>.
•	Run: bundle install.
•	Run server: rails server → http://localhost:3000.
2. Configure Database on Windows
•	Edit config/database.yml.
•	For SQLite: adapter=sqlite3, database=db/development.sqlite3.
•	For MySQL: adapter=mysql2, host=localhost, username=root, password= , database=myapp_db.
•	For PostgreSQL: adapter=postgresql, host=localhost, username=postgres.
3. Migrate Project from Windows to Ubuntu
•	Find Ubuntu IP: ip addr.
•	Open FileZilla → Quickconnect.
•	Host: sftp://<Ubuntu-IP>, port 22.
•	Upload project to /home/<ubuntu-user>/<project>.
4. Install Ruby, Rails, Database on Ubuntu
•	sudo apt update
•	sudo apt install ruby-full build-essential
•	sudo gem install rails
•	SQLite: sudo apt install sqlite3 libsqlite3-dev
•	MySQL: sudo apt install mysql-server libmysqlclient-dev
•	PostgreSQL: sudo apt install postgresql postgresql-contrib libpq-dev
5. Install Gems on Ubuntu
•	cd /home/<ubuntu-user>/<project>
•	bundle install
•	If errors: sudo apt install zlib1g-dev libssl-dev libreadline-dev
6. Configure Database on Ubuntu
•	Start MySQL: sudo systemctl start mysql
•	Open MySQL: sudo mysql
•	CREATE DATABASE myapp_db;
•	CREATE USER 'admin'@'%' IDENTIFIED BY 'admin123';
•	GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%';
•	FLUSH PRIVILEGES;
•	Edit config/database.yml with new user credentials.
7. Run Rails Server on Ubuntu
•	rails server -b 0.0.0.0
•	Open http://Ubuntu-IP:3000
8. Verify Installation
•	Check Ruby: ruby -v
•	Check Rails: rails -v
•	Check MySQL: sudo systemctl status mysql
•	Check PostgreSQL: sudo systemctl status postgresql


##########################################################################

PHP Deployment & Migration Guide (Windows → Ubuntu)
1. Download & Setup PHP Project (Windows)
•	Download your PHP project ZIP or clone using: git clone <repo-url>
•	Install XAMPP on Windows (Apache + PHP + MySQL).
•	Copy your PHP project into C:\xampp\htdocs\<your-project>.
•	Start Apache and MySQL from XAMPP Control Panel.
•	Open http://localhost/<your-project>.
2. Configure MySQL Database in XAMPP (Windows)
•	Open phpMyAdmin: http://localhost/phpmyadmin.
•	Create database: CREATE DATABASE myapp_db;
•	Import SQL file if provided.
•	Open project config file (config.php/db.php).
•	Set DB configuration: host=localhost, user=root, pass='', db=myapp_db.
3. Test Application on Windows
•	Open browser: http://localhost/<your-project>.
•	If it loads properly, Windows setup is correct.
4. Migrate PHP Project from Windows to Ubuntu (FileZilla)
•	Find Ubuntu IP using: ip addr.
•	Open FileZilla → Quickconnect.
•	Host: sftp://<Ubuntu-IP>, Username, Password, Port: 22.
•	Upload project to /home/<ubuntu-user>/<your-project>.
5. Install Apache, PHP, MySQL on Ubuntu
•	sudo apt update
•	sudo apt install apache2
•	sudo apt install php libapache2-mod-php php-mysql php-cli php-xml php-mbstring php-curl php-zip
•	sudo apt install mysql-server
•	php -v
•	mysql --version
6. Configure MySQL on Ubuntu
•	sudo mysql
•	CREATE DATABASE myapp_db;
•	CREATE USER 'admin'@'%' IDENTIFIED BY 'admin123';
•	GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%';
•	FLUSH PRIVILEGES;
•	EXIT;
7. Copy Project to Apache Web Directory
•	sudo cp -r /home/<ubuntu-user>/<your-project> /var/www/html/
•	sudo chown -R www-data:www-data /var/www/html/<your-project>
•	sudo chmod -R 755 /var/www/html/<your-project>
•	sudo systemctl restart apache2
8. Update PHP DB Config on Ubuntu
•	sudo nano /var/www/html/<your-project>/config.php
•	Set DB credentials: host=localhost, user=admin, pass=admin123, db=myapp_db
9. Run PHP Application on Ubuntu
•	Open: http://<Ubuntu-IP>/<your-project>
•	If page loads, migration is successful.
10. Verify Apache, MySQL & PHP
•	sudo systemctl status apache2
•	sudo systemctl status mysql
•	php -v
•	Test from Windows browser: http://Ubuntu-IP/<your-project>


###############################################################################################

MERN Stack Deployment & Migration Guide (Windows → Linux)
1. Download & Setup Project (Windows)
•	Open the MERN project GitHub link or ZIP file.
•	Download or clone using: git clone <repo-url>
•	Open the project in VS Code.
•	Identify folders: backend/ (Node.js + Express), frontend/ (React).
2. Configure Backend (Node.js + Express + MongoDB)
•	Open backend/config/.env (or create .env).
•	Add the following variables:
•	MONGO_URI=mongodb://localhost:27017/your_db
•	PORT=5000
•	Install dependencies: npm install
•	Start backend: npm start
3. Configure Frontend (React)
•	Open frontend/.env or create it.
•	Add:
•	REACT_APP_API_URL=http://localhost:5000
•	Install dependencies: npm install
•	Start frontend: npm start
4. Install Node.js, MongoDB & Tools on Windows
•	Install Node.js from official website.
•	Install MongoDB Community Server.
•	Check versions:
•	node -v
•	npm -v
•	mongod --version
5. Run MERN App on Windows
•	Open two terminals:
•	Terminal 1 → cd backend → npm start
•	Terminal 2 → cd frontend → npm start
•	Open browser → http://localhost:3000
6. Migrate MERN Project from Windows to Linux (Ubuntu)
•	Install FileZilla on Windows.
•	Start Ubuntu in VirtualBox.
•	Find Ubuntu IP using: ip addr
•	Connect via FileZilla (SFTP):
•	Host: <ubuntu-ip> | Username: <ubuntu-user> | Password | Port: 22
•	Upload entire MERN project to Ubuntu home directory.
7. Install Node.js & MongoDB on Ubuntu
•	sudo apt update
•	sudo apt install nodejs npm
•	Install MongoDB:
•	sudo apt install mongodb
•	Start DB: sudo systemctl start mongodb
•	Check status: sudo systemctl status mongodb
8. Configure Backend on Ubuntu
•	cd backend
•	Create .env:
•	MONGO_URI=mongodb://localhost:27017/your_db
•	PORT=5000
•	Install dependencies: npm install
9. Configure Frontend on Ubuntu
•	cd frontend
•	Create .env:
•	REACT_APP_API_URL=http://Ubuntu_IP:5000
•	Install dependencies: npm install
10. Run Backend & Frontend on Ubuntu
•	Terminal 1 → cd backend → npm start
•	Terminal 2 → cd frontend → npm start
•	Open browser (in Windows):
•	http://Ubuntu_IP:3000
11. Test MERN App Across Windows → Ubuntu
•	Backend reachable at: http://Ubuntu_IP:5000
•	Frontend reachable at: http://Ubuntu_IP:3000
•	Ensure MongoDB is running and API calls succeed.





           









      







   



    




