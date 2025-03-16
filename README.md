# SectionChanger
METU Register Section Changer

IN ORDER TO MAKE USE OF THIS, ONE NEEDS A COURSE SELECTED IN AN UNDESIRED SECTION. THIS IS *JUST* FOR SECTION CHANGES.

Open the file using any Python IDE.

As in described in .py file, one needs Selenium package, chromedriver, and all set values in order for this script to work out.


## SELENIUM
About Selenium, it's easy to install selenium with the help of a python console. Just insert the following code in your console:
pip install selenium

---------------------------------

## CHROMEDRIVER
About chromedriver, https://chromedriver.chromium.org/ is the link to go. Most of the time, stable release corresponds your needs.

--------------------------------

## VARIABLES
In .py file, I briefly tried to explain the credential and variable stuff. About to check them one by one here:

>course_indice: This one indicates the course indice IN your logged in register.metu.edu.tr interface. Say you have 5 courses, sorted down as 5 rows.
The first row corresponds to '1', second row does to '2' and so on.

>desired_section: This one is quite straightforward. It is the section you want to change to.

>username: Your username in 'eXXXXXX' format

>password: Your login password

>course_category: The items in Course Category dropdown menu. As mentioned in .py script, Following are valid: 'MUST', 'RESTRICTED ELECTIVE', 'FREE ELECTIVE', 'TECHNICAL ELECTIVE', 'NONTECHNICAL ELECTIVE', 'NOT INCLUDED'.

>driver: This one is crucially important. You need to locate the chromedriver item you downloaded. For the sake of simplicity, you can put it right under the C:\ directory, which yields the following:
>  driver = webdriver.Chrome('C:/chromedriver') 
>  and you're done. Otherwise you got to locate it manually.


