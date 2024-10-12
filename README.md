# VoteQuote - Cyber security project
Link to this repository: https://github.com/leinson/csbproject

This is an extremely simple app, that lets you vote on different quotes. 
The app was created as a cyber security project for Cyber Security Base, Project I. 
It has many intended vulnerabilities and security issues – 
please be mindful of this if you test or use the app. 
The project is done with Python and Django.  

## Instructions 

Download the project from GitHub in a way that suits you.  

Navigate in the terminal to the outmost folder ``/cbproject``. 

**Run following commands** 
``pip install Jinja2==3.0.0`` 

Start app: ``python3 manage.py runserver`` at address http://127.0.0.1:8000/ 

**Test User**  
username: test, password: cybersec1  
**Test Admin**  
username: admin, password: cybersec1  

### FLAW 1: CSRF, Cross Site Request Forgery 
Link to vulnerability in OWASP: https://owasp.org/www-community/attacks/csrf  
**Source link:**    
**Description of flaw:**   
Protection against Cross Site Request Forgery (CSRF) is missing from the application. Django provides inbuilt CSRF-protection, but the developer has disabled this feature by adding @csrf_exempt as a decorator in front of the different page views. This makes the app vulnerable for CSRF-attacks.  

**How to fix it:**  
Remove all ``@csrf_exempt`` decorators from ``views.py`` to enable Django’s built-in CSRF-attack protection. This causes a CSRF-token to be generated along with the other data in a POST-request, which the site uses to make sure the POST-request is really coming from the logged in user.  


### FLAW 2: Vulnerable and Outdated components 
Link to vulnerability in OWASP: https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/ 

**Source link:**    
**Description of flaw:**  
A component can bring in a security flaw to an app. I chose to add Jinja2 to the project, which is a templating engine. It is used in this project to render the free text comment. Other than being useless in this app, Jinja2 has known vulnerabilities in older versions – for example XSS and Denial of service (DoS). You should always be mindful of what packages and dependencies you install to a project, since the more of them you have, the greater is the risk of one being outdated or prone to a vulnerability. 
 
**How to fix it:**  
Either update the package to ``3.1.4.`` or higher version to eliminate the vulnerability or remove Jinja2 from the project entirely since it is not necessary for the execution of the project. You should run ``pip uninstall Jinja2`` and remove the lines of code that uses it. 

 
### FLAW 3: Broken access control 
Link to vulnerability in OWASP: https://owasp.org/Top10/A01_2021-Broken_Access_Control/ 



**Source link:**    

**Description of flaw:**  
The only page that requires the end-user to login is the front page of the app. If you enter the address by yourself to, for example, http://127.0.0.1:8000/1/vote/ , you will bypass the login to immediately be able to cast a vote. This is a security flaw of broken access control. The site’s access control is clearly broken, as a malicious user who is not logged in can view all pages meant only for logged in users, as well as cast votes! 


**How to fix it:**  
Add Django’s ``@login_required`` to ``views.py`` in front of all views as a decorator. This will redirect the user to the login page when needed. 


### FLAW 4: Injection (XSS) 
Link to vulnerability in OWASP:  https://owasp.org/Top10/A03_2021-Injection/ 


**Source link:**   

**Description of flaw:**  
An XSS flaw leaves the app vulnerable to malicious users, who can enter for example raw HTML to the page to be executed when other users use the app.  

In this app the flaw is in the free comment field, where a safe filter is applied. This filter disables Django’s own protections against XSS injections. The textfield causes unsanitized data to be stored through the POST request in the database and the potentially malicious entered string will pass again through the backend to other end users every time the page is loaded. As an example, you can try to enter ``<script>alert('YOU’VE BEEN HACKED');</script>`` as a comment, which will then pop up as an alert box on the page. (If you do it, please log in as the admin user and remove the comment from the admin page afterwards or alternatively contact me to do so). 

**How to fix it:**  
Remove ``|safe`` from the text-field comment line to enable Django’s own protection against XSS injections.    


### FLAW 5: Security misconfiguration 
Link to vulnerability in OWASP: https://owasp.org/Top10/A05_2021-Security_Misconfiguration/ 

 
**Source link:**   

**Description of flaw:**  
The admin username and password meant for development only are still shown on the page, only changed to a white color to not be obvious. There is also a link that guides users to the admin page. The admin password is the same as the test-user's password. These can be considered as security misconfigurations. There is no need for a straight link to the admin site from the front page for end users to access. The site has not been properly cleaned up from the development process, and since this admin account is still in use it provides an unnecessary and dangerous feature that a malicious user can cause huge damage through. 

**How to fix it:**  
Remove the unnecessary features: the link to the admin page, as well as the white-outed text that provides the login credentials for an admin. This early on created admin account with the same easy password should also be deleted or changed to something less guessable.
