[![homepage][1]][2]

[1]:  static/images/siterender.png
[2]:  https://wild-camping.herokuapp.com/ "Redirect to homepage"



**WildCamping Website**
==================
Table of contents:
-----------------


 - [Description](#description)
 - [User Experience](#user-experience)
     - User Stories
     - Strategy
     - Scope
     - Structure
     - Skeleton
     - Surface
 - [Technologies](#technologies)
 - [Testing](#testing)
     - Acceptance Criteria
     - Browser Compatibility
     - OS Compatibility
     - Devices Compatibility
     - W3 HTML Validation
     - W3 CSS Validation 
     - CSS Lint Validation 
     - JSHint Validation
     - Python PEP8 Validation
     - Lightspeed Performance Test
     - Regression Testing
     - User Testing
     - Bugs
 - [Deployment](#deployment)
 - [Credits](#credits)
     - Code Used
     - Content
     - Acknowledgements


Description
-----------

WildCamping is a camp search website allowing users to search, create accounts, add locations and favourite their own spots

The live site can be viewed [here](https://wild-camping.herokuapp.com/).

User Experience
--------------------

----------

**USER STORIES**

----------

**External User Goal:  (In order of priority):**

 1. As an external user I want to find good camping locations.
 2. As an external user I want to share information on a good camping location.
 3. As an external user I create a collection of my favourite camping locations.

 Users make use of the site to share their own data with the community, and benefit from having convenient access to the data provided by all other members.
The site owner advances their own goals by providing this functionality, potentially by being a regular user themselves. The site owner might also benefit from the collection of the dataset as a whole.


**Site Owner Goal:**

 1. As a site owner I want create a knowledge bank of good camping locations

The mockup for this site was done on Balsamiq Wireframes 
and can be viewed below 

- [Desktop Homepage](static/images/wireframes/index_page.png).  
- [Profile_Page](static/images/wireframes/profile_page.png).  
- [Add_Location Page](static/images/wireframes/user_location.png).  
- [Search_Results_Page](static/images/wireframes/add_location_mobile.png).  
- [Search_Results_Page](static/images/wireframes/add_location_tablet.png). 

The full selection of wireframes can be viewed in PDF for [here](static/images/wireframes/wild_camping_wireframes)



----------

**STRATEGY**

--------

 - **Focus:**  
    The focus of this project will the search functionality, creating a simple and intuitive way to find, store and share camping locations. 

 - **Definition:**  
    The site will user populated database of camping locations with descriptions and ratings. 

 - **Value:**   
    This site allows users to explore new opportunities in wild camping, share their own camping knowledge and procure their own list of favourite locations.

----------

**SCOPE**

----------

**Features:** 


- **Navigation menu** – The navigation menu will offer users a number of site locations depending on their user access. 

- **Search Bar** – Search bar to query the database on camping locations.

- **Profile Page** – Displays user profile bio and saved locations.


**STRUCTURE**

----------

1.	The spash page of Wild Camping will disiplay a random card selection of some of the locations in the database. Scrolling down will review a map with markers to these locations. There will be a selection 6 cards below this with location pictures and previews of the descriptions. The search bar will be at the top of the page and a search button
    - As an external user I want to find good camping locations.
    - As an external user I want to share information on a good camping location.

2. The Menu will display if not logged in "Home", "Login" and "SignUp" and if logged in will display "Add Location", "Profile" "Home and "Logout"


3. The Profile page will Be broken into three sections. A profile card with some stats about the users activity. A section for posts that the user has created and section with posts that the user has liked. 
    - As an external user I create a collection of my favourite camping locations.

4. The View location page will be a simple card displaying the Name, Description, Rating, Location and Picture of the campsite. This card will display a like button to logged in users and edit or delete to the user who created the post.

5. The Add Location page will have a simple form with fields for Name and Description, a star rating selection area, a map to search for the location and drop a pin, a button to upload a photo and a submit button. 
    - As a site owner I want create a knowledge bank of good camping locations


----------

**SURFACE**

----------


**Colours:** 
    - I have got gone for muted colours with this site. I used the nighttime image of the campsite used in the background for inspiration. The dark blue or navy colours evoke the atmospheric feeling of being under the night sky. 
**Typography:** 

    - I chose the 'Baloo Tammudu 2' as the main font for its soft lines. 'Roboto' is the backup font, not so soft but similar in structure. 

**Effects:**

 -  Materialize button effects seen mouse is over the element. The navbar is transparent and become opaque as the user scrolls ensuring lighter coloured elements scrolling behind the menu will not create a contrasting issue. 

**Imagery:** 

 - The imagery on the site is quite simple, using the nighttime image of campsite as the background reinforcing the sites function.

**Deviations from design:**

- There were minor layout deviations from the original design and the homepage was redesigned to include more information for the user. 


Technologies
----------------

 - [**HTML5**](https://en.wikipedia.org/wiki/HTML5) –  to create the websites main structures
 - [**CSS3**](https://en.wikipedia.org/wiki/CSS) – to style the components created with HTML and
   create the desired effects described in the ‘Surface’ section.
 - [**Python**](https://www.python.org/download/releases/3.0/)
 - [**Materialize**](https://materializecss.com/) – to create responsive elements on the page.
 - [**FontAwesome**](https://fontawesome.com/)  - icons used throughout the site.
 - [**Google Fonts**](https://fonts.google.com/) – Imported fonts.
 - [**GitPod**](https://gitpod.io/) – IDE used for working on my code
 - [**GitHub**](https://github.com/) – Used for hosting the files used for the website.
 - [**Git**](https://git-scm.com/) – Version control used to track changes, commit and push code to
   Github.
 - [**Javascript**](https://www.javascript.com/)
 - [**Flask**](https://flask.palletsprojects.com/en/2.0.x/)
 - [**Lightspeed**](https://developers.google.com/speed/pagespeed/insights/) - Website performance testing utility
 - [**DevTools**](https://developers.google.com/web/tools/chrome-devtools) - I used Chrome DevTools throughout the development of the site to modify elements on the screen live, testing screen responsiveness and debugging code.
 - [**W3 HTML Validation**](https://validator.w3.org/) - Online HTML validation tool. 
 - [**W3 CSS Validation**](https://jigsaw.w3.org/css-validator/) - Online CSS validation tool.
 - **Gitpod extensions:**
     - Auto Close Tag
     - Bracket Pair Colorizer
     - Code Spellchecker
     - Prettier - Code Formatter
     - Indent-Rainbow
 - [**Techsini**](http://techsini.com/multi-mockup/index.php) - I used this website to create a multi mockup of the live website display at the head of my Readme file. 
 - [**Brackets**](http://brackets.io/) - Local IDE.
 - [**Autoprefixer**](https://autoprefixer.github.io/) - Parses CSS and adds vendor prefixes.
 - [**Google mobile-friendly Test**](https://search.google.com/test/mobile-friendly?id=PM7sy6dG9tEXLsvHooNW6Q) - Tests for mobile compatibility. 
 - [**Xcode simulator**](https://developer.apple.com/documentation/xcode) - suite of tools used for build or testing apps for Apple platform.
 - [**BeautifyTools Javascript Validator**](https://beautifytools.com/javascript-validator.php) - Online Javascript validation tool. 
 - [**JSHint Validation**](https://jshint.com/) - Online Javascript validation tool. 
 - [**JSON Valdiation**](https://jsonlint.com/) - Debug JSON object structure used in MongoDB and Javascript


Testing
-------

----
**Acceptance Criteria:**

1. All links on the website must connect to the correct location.
2. All images and elements on website must load correctly.
3. All fallback fonts must work visually should the first choice fonts be unavailable.
4. All elements on the website must be responsive, resizing for different screen sizes and maintaining their integrity with no overlapping.
5. All external links direct to the correct website.
6. The website loads correctly and functions on Chrome, Internet Explorer, Safari and Firefox browsers.
7. The website performs as required as outlined in User Stories for external users and the site owner.

All testing is documented and can be viewed in the following formats. [Mac Numbers](atesting/wildcampingtesting.numbers), [Excel](testing/wildcampingtesting.xlsx) and [PDF](testing/wildcampingtesting.pdf).

----
**Browser Compatibility**


| Screen Size/Browser  | Chrome  | Internet Explorer  | Safari  |  Firefox |
|---|---|---|---|---|
|  Mobile |✅   | ✅  | ✅| ✅ |
|  Desktop | ✅  | ✅  | ✅  | ✅  | 
|  Tablet | ✅  | ✅  | ✅  |  ✅ | 


**OS Compatibility** 


The OS used during testing were: 
The OS used during testing were: 
- Mac OS 11.0.1 
- Windows 10
- Android (OxygenOS Version 9.0.6)
- iOS 14.4.1
- Xcode Simulator - iPhone 12 Pro Max, iPad Pro 12.9inch
- Chrome OS (release 89.0.4389.95)

Further testing yet to be carried out on Linux and Unix.

----
**Device Compatibility** 


The devices used during testing were: 
- MacBook Air 13inch 2017
- Acer Chromebook cb3-431
- OnePlus 3T 
- OnePlus 5T
- Pixel 4a
- iPhone X 
- iPhone SE 
- HP Elitebook G5 
- iPad 10.2
- Dell OptiPlex 7480 
- Samsung Galaxy s20


----
**W3 HTML Validation** 

HTML Validation with [https://validator.w3.org/](https://validator.w3.org/).

I recieved the following erros which could not be resolved.

Error: Element link is missing one or more of the following attributes: href, resource.

<link type="text/css" rel="stylesheet" id="dark-mode-custom-link"><link 

Error: Start tag head seen but an element of the same type was already open.

</style><head><style

Error: Bad value https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Google+Sans:400,500,700|Google+Sans+Text:400 for attribute href on element link: Illegal character in query: | is not allowed.


Error: Attribute controlheight not allowed on element div at this point.


/div><div><div class="gmnoprint gm-bundled-control gm-bundled-control-on-bottom" draggable="false" controlwidt…tyle="margin: 10px; user-select: none; position: absolute; display: none; bottom: 26px; left: 0px;"><div c

----
**W3C CSS Validation** 


CSS validation with [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)

<****>

----
**CSS Lint Validation**


CSS also validated via http://csslint.net/

<****>

----
**BeautifyTools Javascript Validation** 

https://beautifytools.com/javascript-validator.php

No major javascript errors found 

----
**Lightspeed Performance Test** 

The performance of the site on Lighthouse can be viewed [here](testing/lightspeedtest.pdf)

----
**Regression Testing**

Any new features and bug fixes were submitted to regression testing of all functional and non functional aspects of the project to ensure that previously developed and tested software still performed following changes.

----
**User Testing**

I used most of my family and friends for this section of the testing, the only instructions given were to be brutal with their use of the site and unforgiving with their criticisms. The testers ranged in age from 8 to 76.

I was lucky enough to have one user who was familiar with testing procedures and recieved a comprehensive report on her findings. This can be viewed here on [PDF](testing/usertest.pdf) or here as [.docx](testing/usertest.docx)

----
**Bugs**

+ **Bug:** Editing url allowed unauthorised user access to edit any location.     
**Fix:** Put an authorisation check in the flask routing for edit_location.

+ **Bug:** Username allowing nonregex chars throws error when using .lower().   
**Fix:** Input validation script. 

+ **Bug:** Heart icon not rendering correct in safari.  
**Fix:**  Replaced with Font Awesomoe icon.   

+ **Bug:** Users adding no text for username signup were allowed to, this in turn caused erros when reading an empty string as a username.    
**Fix:** Validation to prevent empty profile username or passwords. 

+ **Bug:** Profile image wasn't automatically submitting when user selected photo.   
**Fix:** Used onchange instead of onsubmit to submit the img.   

+ **Bug:** Eventlistener throwing error when reading null elements.  
**Fix:** Add if statement to catch property of Null for eventlistener. 

+ **Bug:** Extra spaces entered by user can cause JSON validation error.  
**Fix:** Script to remove extra spaces from user input. 

+ **Bug:** API error when accessing google maps.  
**Fix:** Edit callback in google api links to fix loading issue, wrong callback intially entered.  


Deployment
----------

**Local Deployment**

 
1. Create a GitHub account at [https://www.github.com](https://www.github.com). Locate the WildCamping repository for the website. The link is here. [https://github.com/raymondkeogh/wildcamping](https://github.com/raymondkeogh/wildcamping) 
2. Click on the setting "Code" button and click download. 
3. Scroll down to the section that says GitHub Pages. 
4. Unzip the files into the directory you will be working from. 
5. Open the files in your local IDE. VScode was the one I chose. 
6. Setup your IDE to run with Python

***
Prequisites 
-(Source: [visualstudio.com](https://code.visualstudio.com/docs/python/tutorial-flask))

- Install the Python extension.

- Install a version of Python 3 (for which this project is written). Options include:

- (All operating systems) A download from [python.org](python.org) typically use the Download Python 3.9.1 button that appears first on the page (or whatever is the latest version).
(Linux) The built-in Python 3 installation works well, but to install other Python packages you must run sudo apt install python3-pip in the terminal.
(macOS) An installation through Homebrew on macOS using brew install python3 (the system install of Python on macOS is not supported).
(All operating systems) A download from Anaconda (for data science purposes).
On Windows, make sure the location of your Python interpreter is included in your PATH environment variable. You can check the location by running path at the command prompt. If the Python interpreter's folder isn't included, open Windows Settings, search for "environment", select Edit environment variables for your account, then edit the Path variable to include that folder.

7. Create a requirements.txt file for the environment.

On your file system, create a project folder for this project, e.g wildcamping.

In that folder, use the following command (as appropriate to your computer) to create a virtual environment named env based on your current interpreter:

- Linux

            sudo apt-get install python3-venv

If needed

            python3 -m venv env

- macOS

            python3 -m venv env

 - Windows


            python -m venv env

Note: Use a stock Python installation when running the above commands. If you use python.exe from an Anaconda installation, you see an error because the ensurepip module isn't available, and the environment is left in an unfinished state.

Open the project folder in VS Code by running code ., or by running VS Code and using the File > Open Folder command.

In VS Code, open the Command Palette (View > Command Palette or (⇧⌘P)). Then select the Python: Select Interpreter command:


The command presents a list of available interpreters that VS Code can locate automatically (your list will vary; if you don't see the desired interpreter, see Configuring Python environments). From the list, select the virtual environment in your project folder that starts with ./env or .\env:


Run Terminal: Create New Integrated Terminal (⌃⇧`)) from the Command Palette, which creates a terminal and automatically activates the virtual environment by running its activation script.

Note: On Windows, if your default terminal type is PowerShell, you may see an error that it cannot run activate.ps1 because running scripts is disabled on the system. The error provides a link for information on how to allow scripts. Otherwise, use Terminal: Select Default Shell to set "Command Prompt" or "Git Bash" as your default instead.

The selected environment appears on the left side of the VS Code status bar, and notice the "(venv)" indicator that tells you that you're using a virtual environment:

Update pip in the virtual environment by running the following command in the VS Code Terminal:

        python -m pip install --upgrade pip
Install Flask in the virtual environment by running the following command in the VS Code Terminal:

        python -m pip install flask
You now have a self-contained environment ready for writing Flask code. VS Code activates the environment automatically when you use Terminal: Create New Integrated Terminal. If you open a separate command prompt or terminal, activate the environment by running source env/bin/activate (Linux/macOS) or env\Scripts\Activate.ps1 (Windows). You know the environment is activated when the command prompt shows (env) at the beginning.


**Remote**


1. Create an acount with [https://www.heroku.com/](https://www.heroku.com/)
2. Click on the button in the top right that says "New"
3. Select "Create new app"
4. Name the app, select your region and click 'Create app'
5. In the deploy section select "Github"
6. Search for your repository ('eg. WildCampng'). 
7. Click Connect. 
8. Click "Enable Automatic Deploys.
9. Click "Deploy Branch"
10. You will need to configure your Environment Variables by going to 'Setting' and selecting 'Config Variable'
[More info here](https://devcenter.heroku.com/articles/config-vars)



Credits
-------

**Code used**

Https error fix:

https://stackoverflow.com/questions/35178135/how-to-fix-insecure-content-was-loaded-over-https-but-requested-an-insecure-re/35178323

Star Rating function:

https://bbbootstrap.com/snippets/star-rating-pure-css-19646372 

Scrolling navbar changes:

https://stackoverflow.com/questions/23706003/changing-nav-bar-color-after-scrolling

Fix for 'null found' error:

https://stackoverflow.com/questions/26107125/cannot-read-property-addeventlistener-of-null

File size validation:

https://www.encodedna.com/jquery/get-file-size-before-uploading-using-javascript-and-jquery.html

Increment variable in jinja loop:

https://stackoverflow.com/questions/7537439/how-to-increment-a-variable-on-a-for-loop-in-jinja-template 

Code for Like button logic:

https://github.com/LigaMoon/swap-clothes-app/ 

Code used to get coordinates from search address:

https://developer.here.com/documentation/geocoding-search-api/dev_guide/topics/endpoint-geocode-brief.html

Render JSON data of locations from database:

https://stackoverflow.com/questions/49718569/multiple-markers-in-flask-google-map-api


Take location_id and action from location cards and add like/unlike to db:

https://github.com/LigaMoon/swap-clothes-app/blob/main/app.py


404 Page 
https://stackoverflow.com/questions/29516093/how-to-redirect-to-a-external-404-page-python-flask



<****>

**Content**

https://racemph.com/people/person-1/profile-image-placeholder/

https://unsplash.com/photos/_94HLr_QXo8

https://www.clipartkey.com/view/bowTb_magnifying-glass-detective-with-clipart-transparent-clip-art/

https://en.wikipedia.org/wiki/Montpelier_Hill#/media/File:Hell_Fire_Club_Dublin_at_Dawn.jpg


**Acknowledgements**

I would like to thank,
Andy, Pamela,and Gary for running user tests on the site.
Maranatha for his awesome guidance.
The Code Institute tutors Sheryl, Michael, Kohn, Jo, Stephen for all their help.
Jack for reviewing my code in peer-review on Slack and his tip on guarding my session. 


