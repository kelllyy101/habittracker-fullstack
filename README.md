## Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [User Experience Design (UX)](#user-experience-design-ux)
    + [Typography](#typography)
    + [Wireframes](#wireframes)
- [Accessibility]('accessibility)
- [User Stories](#user-stories)
  - [Future Features](#future-features)
- [Technologies](#technologies)
-* [Testing](#testing)
    + [Browser Compatibility](#browser-compatibility)
    + [Responsiveness](#responsiveness)
    + [Performance Testing](#performance-testing)
    + [Accessibility Testing](#accessibility-testing)
    + [User Story Testing](#user-story-testing)
    + [Challenges Faced](#challenges-faced)
    + [Code Validation](#code-validation)
      - [HTML Validation](#html-validation)
      - [CSS Validation](#css-validation)
      - [Python Validation](#python-validation)
      - [JavaScript](#javascript)
  - [Deployment](#deployment)
    + [Local Deployment](#local-deployment)
    + [Heroku Deployment](#heroku-deployment)
  - [Project Creation](#project-creation)
  - [Software](#software)
  - [Media and Credits](#media-and-credits)
- [Thanks to](#thanks-to)



# Habit Tracker App - Django Readme

Welcome to the Habit Tracker app, a powerful tool designed to help users build and maintain healthy habits. This application is built using Django, offering a user-friendly interface to track and manage your daily routines.

## Overview

The Habit Tracker app serves as a personalised habit management system, allowing users to register, track their habits, and leverage essential features to enhance their daily routines.

## Features

### User Registration and Submission

- **User Registration:** Sign up to create an account and start utilising the habit tracking features.

### Interaction and Organization

- **Agile Principles:** Built with Agile management principles, ensuring flexibility and responsiveness to user needs.

### Project Management

- **GitHub Integration:** Leveraging GitHub features such as Issues and Projects to implement Agile methodology.
- **Heroku:** Deployed this app using Heroku.
- **Closed Issues:** Detailed records of resolved issues, showcasing the dedication to maintaining a bug-free application.

### CRUD Functionality

- **Resource Management:** Users can create, update, and delete habits they have created, ensuring content relevance.
- **Account Management:** Users have full control over their accounts, with the ability to create, update, read, and delete habits.
- **Admin Privileges:** Admins can manage all resources efficiently, ensuring the integrity of the habit directory.

### Project Planning and Execution

- **GitHub Tags:** Efficient use of tags for assigning story points, prioritizing features based on categorising user stories.
- **Milestones:** Strategically plan sprints and set deadlines using GitHub's Milestones feature.

## Learning and Development

- **Continuous Improvement:** Regular updates and bug fixes based on user feedback and reported issues that I found during manual testing.
- **Educational Background:** Drawing insights from the Agile Foundations course on Code Institute, while learning to enhance project management skills and understanding of Agile methodologies.

Feel free to explore the Habit Tracker app, track your habits effortlessly, and contribute to the growth of a supportive community. Happy habit building!

## User Experience
As the project is a directory of design resources, I wanted to try something fun and bold with the design and was inspired by the trend for neubrutalism web design, and websites such as

#### Typography and Colour
A basic font was used for the whole habit tracker as it fitted the simplistic theme of the site and helps with readability. Three basic colours, blue, black and white also contribute to the simplicity of this website so the focus is on the habits and the user achieving their goals.


#### Wireframe

These wireframes were created with Balsamiq Wireframes.
![Alt text](/static/readme_images/Screenshot%20(774).png>)
![Alt text](</static/readme_images/Screenshot (775).png>)

## Title:
Habit Tracker Django App Database Flow Diagram

## Models:

### 1. `Item` Model
   - **Fields:**
     - `name`: CharField
     - `monday` to `sunday`: BooleanFields
   - **Methods:**
     - `__str__`: Returns the name of the habit
   - **Description:** Represents a habit item with details such as name, completion status, and days of the week.

### 2. `HabitUsers` Model
   - **Fields:**
     - `first_name`: CharField
     - `last_name`: CharField
     - `email`: EmailField
     - `shared_users`: ManyToManyField to `Item`
   - **Methods:**
     - `__str__`: Returns the full name of the user
   - **Description:** Represents a user with personal details and habits shared with them.

## Views:

### 1. `home` Function
   - **Input:** None
   - **Output:** HTML page (`home.html`)
   - **Description:** Renders the home page for the application.

### 2. `get_habits` Function
   - **Input:** User session data
   - **Output:** HTML page (`habits.html`) with a list of habits
   - **Description:** Retrieves and displays a list of habits for the authenticated user.

### 3. `add_habit` Function
   - **Input:** Habit data from a form
   - **Output:** Redirect to `get_habits` view
   - **Description:** Adds a new habit to the database.

### 4. `edit_habit` Function
   - **Input:** Habit data from a form
   - **Output:** Redirect to `get_habits` view
   - **Description:** Edits an existing habit in the database.

### 6. `delete_habit` Function
   - **Input:** Habit ID
   - **Output:** Redirect to `get_habits` view
   - **Description:** Deletes a habit from the database.

### 7. `admin_view` Function
   - **Input:** None
   - **Output:** Redirect to the admin panel (`admin/`)
   - **Description:** Redirects the user to the Django admin panel.

### 8. `landing` Function
   - **Input:** None
   - **Output:** HTML page (`landing.html`)
   - **Description:** Renders the landing page for the application.

### 9. `register_user` Function
   - **Input:** User registration data from a form
   - **Output:** Redirect to `login` view
   - **Description:** Handles user registration and authentication.

### 10. `login_user` Function
   - **Input:** User login credentials
   - **Output:** Redirect to `get_habits` view or `login` view with an error message
   - **Description:** Handles user login and redirects accordingly.

### 11. `logout_user` Function
   - **Input:** None
   - **Output:** Redirect to `login` view
   - **Description:** Logs out the user and redirects to the login page.


## User-stories
1. Create User Account  
    As a new user, I want to create a personalised account by providing my email and a secure password, so I can start tracking my habits.

2. User Login  
    As a registered user, I want to log in with my email and password to access my habit tracking dashboard.

3. Remember Frequent Users  
    As a frequent user, I want the application to remember my login credentials, so I can quickly access my habit tracker without entering my details each time.

4. View Personalized Dashboard  
    As a user, I want to see a personalized dashboard upon logging in, displaying my habit categories, tracking streaks, and progress.

5. Set and Update Goals  
    As a user, I want to set, edit, and update my habit goals within my account settings, helping me focus on specific targets.

6. Logout Functionality  
     As a user, I want a secure way to log out of the application, ensuring my account remains private when using shared devices.

7. Edit Habit Details  
    As a user, I want the ability to edit habit details, such as the habit's name, category, and reminder settings, to reflect changes in my routine.

8. User-Specific Habit Tracking  
    As a user, I want to ensure that my habit tracking is personalized, only allowing me to view and manage my own habits.

9. Responsive Design for Mobile  
    As a user, I want the habit tracker application to be responsive on mobile devices, ensuring that I can conveniently track habits on the go.


#### Future Features
1. Reset Forgotten Password  
   As a user who forgets my password, I want the option to reset it by receiving a password reset link via email, ensuring I can regain access to my account.

2. Social Media Login  
    As a user, I want the ability to sign in using my Google or Facebook account, simplifying the login process and enhancing security.

3. Track Habit History  
    As a user, I want to view a history of my habit completion, enabling me to review past performance and identify patterns.

4. Edit User Profile  
    As a user, I want to edit my profile details, including my name, profile picture, and email, ensuring accurate representation.

5. Sync Data Across Devices  
     As a user, I want my habit tracking data to sync seamlessly across different devices, ensuring consistency and accessibility.

6. Receive Email Notifications  
     As a user, I want to receive email notifications for important updates, such as habit reminders, achievements, and account changes.

7. Log Daily Habits  
    As a user, I want to log my daily habits, prompted by the app, so I can keep track of my progress and maintain consistency.

8. View Habit Streaks  
    As a user, I want to see my habit streaks and visualize my consistent performance over time, motivating me to maintain positive habits.

9. Set Long-Term Goals  
    As a user, I want to set long-term goals related to my habits, so I can work towards achieving larger milestones over time.

10. View Habit Analytics  
    As a user, I want to view analytics that display trends in my habits' performance, helping me identify areas for improvement and growth.

11. Share Habit Achievements  
    As a user, I want to share my habit achievements on social media or with friends, celebrating my progress and encouraging others.

12. Customize Habit Reminders  
    As a user, I want to customize the time and frequency of habit reminders, ensuring that I receive prompts at times that suit my routine.




## Technologies


## Testing

#### Browser-Compatibility

#### Responsiveness

#### Performance Testing
Each function has their own test to ensure smooth funtionality and app usage. I ran a debug just before deploying as well as incuding error messages through out the functions created to test for functionality.

Code Structure and Style Testing (PEP8): I ran my code through a PEP8 linter to ensure it adhered to Python's style guidelines. I corrected any formatting issues or violations reported by the linter.

Functionality Testing with Print Statements: I inserted print statements at key points in my code to confirm the execution flow. For example, I added print statements at the beginning of each function to ensure they were being called. I ran the app and verified that the print statements showed up at the expected points
![Alt text](/static/readme_images/Screenshot%20(780).png)
![Alt text](/static/readme_images/Screenshot%20(773).png)

#### Accessibility Testing


#### User Story Testing
I manually tested the features by registering and logging in, then I set my own habits. I picked the days I wanted to do these habits and I edited habits that I wanted to change and I deleted habits that I did not want to keep. I then logged out. I returned to the login in page after a while and my username was there with the password saved so I was able to log back in and I could see the habits I had set and the days I want to do them.
![Alt text](/static/readme_images/Screenshot%20(792).png)


## Code Validation
#### HTML Validation
All Html codes was run through validators, warnings regarding the Django URL formatting.
#### CSS Validation
I ran the CSS through Jigsaw WC3 validator.

#### Python Validation
I ran my code through a PEP8 linter to ensure it adhered to Python's style guidelines. I corrected any formatting issues or violations reported by the linter.
#### JavaScript
I ran my code through JSLint and returns no errors.



# Deployment
Heroku is a platform that allows you to deploy and host your applications, which is what I used for this expense tracker and these are the following steps I took:

I logged in to my Heroku account at https://www.heroku.com/.

I installed the Heroku Command Line Interface (CLI) on your system. This CLI tool lets you manage and deploy your Heroku apps from the command line.

I ensured my project is in a Git repository, copying and pasting the name to connect Heroku to GitHub successfully.

A requirements.txt file and a Procfile was added from Code Institute's template so the project would deploy successfully as well as removing DEBUG for production.

I created a new Heroku app using the Heroku CLI after I logged into my account and made sure my Git repository was connected. I also enabled the automatic deployment.

Before creating the app, I added two buildpacks from the Settings tab making sure to add heroku/python first, followed by heroku/nodejs. For easier production, I also created: if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['fs-habit-tracker-786d6f38cbab.herokuapp.com'].

I deployed my project to Heroku by pushing your Git repository to Heroku's remote, that will update with every git push, as chosen by me in the settings, successfully integrating and deploying my project for use through the Heroku URL.


## Media-and-credits
Bootstrap was used extensively in the project.
Code Institute's To-Do list walk through project was a big help setting the base of this project and to be able to understand the basics.
Habit Tracker websites such as Habify and MyHabitTracker influenced the design.
Bootstrap documentation was thoroughly used throughout the design.
Stack Overflow provided much needed documentation when deploying this project.
Official Django Documentation was all thoroughly used throughout.


## Thanks-to
I would like to express my gratitude to Code Institute for their exceptional web development curriculum and to my mentor for their invaluable guidance and support throughout this project. Thank you for providing the resources and expertise that have helped me grow as a developer.