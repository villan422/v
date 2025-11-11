--------------Set C-----------------
--Test Case Plan:
   1.Test Plan Identifier=University_Result_TestPlan_V1
   2.References=
            - Requirement Document
            - IEEE Test Plan Format
            - User Manual
   3.Introduction=
          This system helps students to see their results semester-wise or year-wise. It also allows them to apply for rechecking or re-evaluation by paying online.
   4.Features to be Tested=
            Student Login
            - View Result (Semester/Year wise)
            - Rechecking Form
            - Online Payment
            - Admin Login and Result Update
   5.Approach=
            - Functional Testing: Check all functions work properly.
            - UI Testing: Check if pages look and work nicely.
            - Database Testing: Check data is saved correctly.
            - Integration Testing: Check if modules connect correctly (Login → Result → Payment).
   6.Environmental Needs=
            - Hardware: Computer/Laptop
            - Software: Windows 10, Chrome Browser
            - Server: MySQL Database, Apache/Tomcat Server
            - Network: Internet Connection
   7.Staffing & Training Needs=
           - 1 Test Lead
            - 2 Testers
            - Testers should know basic SQL and how to report bugs using Excel or Jira.
   8.Responsibilities=
            - Test Lead: Prepare plan and assign work
            - Tester 1: Test Login and Result module
            - Tester 2: Test Payment and Rechecking module
            - Developer: Fix bugs found during testing 

   9.Schedule=
           Plan Preparation: 2 Days
            - Test Case Writing: 3 Days
            - Testing: 5 Days
            - Bug Fix & Retesting: 2 Days
            - Final Report: 1 Day
   10.Approval=
            Prepared by: Kartik
            Reviewed by: Project Manager
            Approved by: QA Lead

Project Name:University Result Declaration System
Module Name:Result Viewing and Rechecking Module
Tester Name:Shreyas Jadhav
Manager Name:Project Manager
Reviewed By:QA Lead
Date Created:11-Nov-2025
Date Reviewed:12-Nov-2025
Test Data:	Student login details, Result records, Rechecking form data, Payment information

*********************Test Cases********************
1.Login with correct username and password->Username: 12345, Password: abcd@123 ->User should log in and go to dashboard->As expected->pass
2.Try login with wrong password->Username: 12345, Password: wrong@123->System should show “Invalid Username or Password”->''->''
3.Check if student can view result semester-wise->Semester: 5->Semester 5 result should appear->As expected->''
4.Check if student can view result year-wise->year:2024->Year 2024 result should appear->''->''
5.Check if rechecking form opens->Click “Apply for Rechecking”->Rechecking form should open->''->''
6.Submit form with correct data->All fields filled properly->Message “Application submitted successfully” should show->''->''
8.Click Pay Now and check payment page->Click Pay Now->Payment page should open->''->''
9.Test successful payment->UPI, ₹500->“Payment Successful” message should show->''->
10.Test failed payment->Wrong OTP->“Payment Failed” message should show->''->''
11.Check if confirmation email is received->Email: user@gmail.com->Confirmation email/SMS should be received->''->''
12.Check if admin can see rechecking applications->Admin login->Admin can view student rechecking requests->''->''


--------------Set B------------------------------------------------

**Test Case Plan
1.Test Plan Identifier=OARS_TestPlan_V1.0
2.References=
        - Software Requirement Specification (SRS) for OARS
        - IEEE 829 Test Plan Format
        - User Manual and Design Documents
3.Introduction=
       The Online Admission and Registration System (OARS) allows students from around the world to apply for admission online. The system includes account creation, form filling, document uploads, admission status checking, and final payment if accepted. This test plan ensures that all these functions work properly, safely, and smoothly.
4.Features to be Tested=
      - User Registration and Login
    - User Registration and Login
    - Application Form Filling
    - Document Upload and Attachment
    - Admission Status Checking
    - Display of Final Decision (Accepted/Rejected/On Hold)
    - Online Payment through Card or Net Banking
5.Approach=
    Functional Testing: Verify all main functions like registration, login, and payment work as expected.
    UI Testing: Ensure all pages are user-friendly, properly aligned, and responsive.
    Database Testing: Verify that user details, documents, and payment records are correctly stored in the database.
    Integration Testing: Check the smooth flow between modules (e.g., Registration → Application → Payment).
    Security Testing: Confirm that login and payment details are securely handled.
6.Environmental Needs
    Hardware: Computer/Laptop with minimum 8GB RAM
    Software: Windows 10 or higher, Chrome/Firefox Browser
    Server: MySQL Database, Apache/Tomcat Server
    Network: Stable Internet Connection
7.Staffing & Training Needs
    1 Test Lead
    2 Testers
    Testers should have basic knowledge of SQL, web testing, and reporting bugs using Excel or Jira.
8.Responsibilities
    Test Lead: Prepare test plan, assign tasks, review test cases.
    Tester 1: Test Registration, Login, and Application Form modules.
    Tester 2: Test Document Upload, Status Check, and Payment modules.
    Developer: Fix bugs found during testing and retest the fixes.
10.Schedule
   Activity	           Duration
    Plan Preparation	2 Days
    Test Case Writing	3 Days
    Testing Execution	5 Days
    Bug Fix & Retesting	2 Days
    Final Report Preparation	1 Day

----
Project Name:	Online Admission and Registration System (OARS)
Module Name:	Admission Form, Document Upload, and Payment Module
Tester Name:	Kartik
Manager Name:	Project Manager
Reviewed By:	QA Lead
Date Created:	11-Nov-2025
Date Reviewed:	12-Nov-2025
Test Data:	Applicant login details, Admission form data, Uploaded documents, Payment details (Card/Net Banking)
-------Test Cases--------
1.Verify new user registration->Go to “Register”, fill required fields, and submit->Account should be created successfully->as Expected->pass
2.Verify login with valid credentials->Enter correct username and password->User should be redirected to the dashboard->''->''
3.Verify login with invalid credentials->->Enter wrong username/password->System should show an error message “Invalid login details”
4.Check that the admission form opens after login->Click on “Apply for Admission”->Admission form page should open properly
5.Verify that all required fields in the admission form are validated->Leave required fields empty and submit->System should show      “Please fill required fields”
6.Verify document upload feature->Upload files in the “Upload Documents” section->Files should upload successfully and show in the list
7.Verify invalid file upload->Try uploading a file with unsupported format or size->System should show “Invalid file format or file too large”
8.Verify status checking feature->After submitting the form, go to “Check Status”->System should show the current application status (Accepted/Rejected/On Hold)
9.Verify payment through card->Select “Card Payment” and enter valid details->Payment should be successful and confirmation message should appear
10.Verify payment through net-banking->Select “Net Banking” option and complete payment->Payment should be successful and receipt should be generated
11.Verify that accepted applicants get final confirmation->Check status after admin approval->System should show “Congratulations, you are accepted”
12.Verify logout function->Click on “Logout” button->System should log out and redirect to login page	

********************Set A********************

--Test Case Plan
1.Test Plan Identifier=CloudKitchen_TestPlan_V1.0
2.References=
    Software Requirement Specification (SRS) for Cloud Kitchen Aggregator App
    IEEE 829 Test Plan Format
    User Manual and Design Documents
3.Introduction
    The Cloud Kitchen Aggregator App connects users with multiple cloud kitchens for online food ordering.
    It allows users to browse menus, place orders, make online payments, and track deliveries.
    Kitchens can manage their menus, promotions, and orders through the app.
    The app also integrates with third-party delivery and payment partners.
    This test plan ensures that all modules work properly, securely, and give a smooth user experience.
4.Features to be Tested
    User Registration and Login
    Browse Cloud Kitchens and Menus
    Add to Cart and Place Order
    Apply Offers and Promotions
    Online Payment (Card/UPI/Net Banking)
    Order Tracking and Delivery Partner Integration
    Kitchen Partner Login and Menu Management
    Admin Dashboard for Managing Users, Kitchens, and Promotions
5.Approach
    Functional Testing:
        Check all major functions (login, menu, order, payment, delivery) work correctly.
    UI Testing:
        Ensure screens are user-friendly, properly aligned, and responsive on mobile and desktop.
    Database Testing:
        Verify that user data, orders, and payments are saved correctly in the database.
    Integration Testing:
        Check the smooth flow between modules (e.g., Menu → Cart → Payment → Delivery).
    Security Testing:
        Ensure user login, payment, and personal data are securely handled.
    Performance Testing:
        Test system speed and stability under high load (many users ordering at once).
6.Environmental Needs
    Hardware: Computer/Laptop with at least 8GB RAM
    Software: Windows 10 or higher, Chrome/Firefox Browser
    Server: MySQL Database, Apache/Tomcat Server
    Network: Stable Internet Connection
7.Staffing & Training Needs
    1 Test Lead
    2 Testers
    Testers should have knowledge of web testing, SQL, API testing (for integrations), and bug tracking using Excel or Jira.
8.Responsibilities
    Test Lead: Prepare test plan, assign tasks, review test cases, and summarize results.
    Tester 1: Test User Registration, Login, Menu Browsing, and Order Placement.
    Tester 2: Test Offers, Payment, Delivery Integration, and Admin Functions.
    Developer: Fix bugs and recheck after retesting.
9.Schedule
    Activity	       Duration
    Plan Preparation	2 Days
    Test Case Writing	3 Days
    Test Execution	5 Days
    Bug Fix & Retesting	2 Days
    Final Report Preparation	1 Day
10. Approval
    Prepared by: Kartik
    Reviewed by: Project Manager
    Approved by: QA Lead
--
Project Name:	Cloud Kitchen Aggregator App
Module Name:	Food Ordering, Menu Management, and Payment Module
Tester Name:	Shreyas Jadhav
Manager Name:	Project Manager
Reviewed By:	QA Lead
Date Created:	11-Nov-2025
Date Reviewed:	12-Nov-2025
Test Data:	User login details, Restaurant partner details, Menu items, Order data, Offer codes, Payment details (Card/UPI/Net Banking)

--Test Cases--
1.Verify user registration==>Open app → Click “Sign Up” → Enter details → Submit==>User account should be created successfully==>As Expected==>Pass
2.Verify user login with valid credentials==>Enter valid username and password → Click “Login”==>User should be redirected to the home/dashboard page
3.Verify user login with invalid credentials==>Enter wrong username/password → Click “Login”==>System should display “Invalid login details” message
4.Verify browsing available cloud kitchens==>Login → Go to “Browse Kitchens”==>List of nearby kitchens should appear
5.Verify viewing and selecting items from a menu==>Open any kitchen → View menu → Add items to cart==>Items should be added to cart 
correctly
6.Verify applying a valid offer code==>Add items to cart → Apply valid promo code==>Discount should be applied and total amount should update
7.Verify applying an invalid offer code==>Apply invalid/expired promo code==>System should show “Invalid or expired code”
8.Verify payment through card==>Proceed to checkout → Select card option → Enter valid card details → Pay==>Payment should be successful and confirmation message should appear
9.Verify payment through UPI or net banking==>Proceed to checkout → Select UPI/Net Banking option → Complete payment==>Payment should succeed and order confirmation should be displayed
10.Verify order tracking feature==>After placing an order → Open “Track Order”==>Order status should update (Confirmed, Preparing, Out for Delivery, Delivered)
11.Verify restaurant partner login and menu update==>Login as restaurant → Go to “Menu Management” → Add or update items==>
Menu should update successfully and visible to customers
12.Verify admin dashboard access==>Login as Admin → Open Dashboard==>Admin should be able to view and manage users, restaurants, and orders

