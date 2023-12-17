![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for Codeanywhere. If you are using Gitpod then you need [this template](https://github.com/Code-Institute-Org/gitpod-full-template) instead.  We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **August 30th, 2023**

## Codeanywhere Reminders

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

Happy coding!

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [User Experience Design (UX)](#user-experience-design-ux)
    + [Typography](#typography)
    + [Wireframes](#wireframes)
- [Accessibility]('accessibility)
- [Database Desgign](#database-design)
- [The Strategy Plane](#the-strategy-plane)
  - [Site Goals](#site-goals)
  - [User Stories](#user-stories)
- [The Scope Plane](#the-scope-plane)
- [The Structure Plane](#the-structure-plane)
  - [Main Structure](#main-menu)
- [The Skeleton Plane](#the-skeleton-plane)
  - [Design Flow](#Design Flow)
- [The Surface Plane](#the-surface-plane)
  - [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
- [Features](#features)
  - [Existing Features](#existing-features)
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

#### Typography
A display font called  was used for the logo as it fitted the neubrutalist theme of the site.


#### Wireframe
![Alt text](/static/readme_images/Screenshot%20(774).png>)
![Alt text](</static/readme_images/Screenshot (775).png>)

## Database Design
Certainly! Here's a concise and formatted version for your README:

# Habit Tracker Django App - Database Design

## Title:
Habit Tracker Django App Database Flow Diagram

## Models:

### 1. `Item` Model
   - **Fields:**
     - `name`: CharField
     - `done`: BooleanField
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

### 5. `toggle_habit` Function
   - **Input:** Habit ID
   - **Output:** Redirect to `get_habits` view
   - **Description:** Toggles the status (done/not done) of a habit in the database.

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


#### User-stories
1. Create User Account  
    As a new user, I want to create a personalized account by providing my email and a secure password, so I can start tracking my habits.

2. User Login  
    As a registered user, I want to log in with my email and password to access my habit tracking dashboard.

3. Remember Frequent Users  
    As a frequent user, I want the application to remember my login credentials, so I can quickly access my habit tracker without entering my details each time.

4. Reset Forgotten Password  
    As a user who forgets my password, I want the option to reset it by receiving a password reset link via email, ensuring I can regain access to my account.

5. Social Media Login  
    As a user, I want the ability to sign in using my Google or Facebook account, simplifying the login process and enhancing security.

6. View Personalized Dashboard  
    As a user, I want to see a personalized dashboard upon logging in, displaying my habit categories, tracking streaks, and progress.

7. Set and Update Goals  
    As a user, I want to set, edit, and update my habit goals within my account settings, helping me focus on specific targets.

8. Track Habit History  
    As a user, I want to view a history of my habit completion, enabling me to review past performance and identify patterns.

9. Edit User Profile  
    As a user, I want to edit my profile details, including my name, profile picture, and email, ensuring accurate representation.

10. Logout Functionality  
     As a user, I want a secure way to log out of the application, ensuring my account remains private when using shared devices.

11. Sync Data Across Devices  
     As a user, I want my habit tracking data to sync seamlessly across different devices, ensuring consistency and accessibility.

12. Receive Email Notifications  
     As a user, I want to receive email notifications for important updates, such as habit reminders, achievements, and account changes.

13. Log Daily Habits  
    As a user, I want to log my daily habits, prompted by the app, so I can keep track of my progress and maintain consistency.

14. View Habit Streaks  
    As a user, I want to see my habit streaks and visualize my consistent performance over time, motivating me to maintain positive habits.

15. Customize Habit Reminders  
    As a user, I want to customize the time and frequency of habit reminders, ensuring that I receive prompts at times that suit my routine.

16. Edit Habit Details  
    As a user, I want the ability to edit habit details, such as the habit's name, category, and reminder settings, to reflect changes in my routine.

17. Set Long-Term Goals  
    As a user, I want to set long-term goals related to my habits, so I can work towards achieving larger milestones over time.

18. View Habit Analytics  
    As a user, I want to view analytics that display trends in my habits' performance, helping me identify areas for improvement and growth.

19. Share Habit Achievements  
    As a user, I want to share my habit achievements on social media or with friends, celebrating my progress and encouraging others.

20. User-Specific Habit Tracking  
    As a user, I want to ensure that my habit tracking is personalized, only allowing me to view and manage my own habits.

21. Responsive Design for Mobile  
    As a user, I want the habit tracker application to be responsive on mobile devices, ensuring that I can conveniently track habits on the go.


# Deployment
Heroku is a platform that allows you to deploy and host your applications, which is what I used for this expense tracker and these are the following steps I took:

I logged in to my Heroku account at https://www.heroku.com/.

I installed the Heroku Command Line Interface (CLI) on your system. This CLI tool lets you manage and deploy your Heroku apps from the command line.

I ensured my project is in a Git repository, copying and pasting the name to connect Heroku to GitHub successfully.

A requirements.txt file and a Procfile was added from Code Institute's template so the project would deploy successfully.

I created a new Heroku app using the Heroku CLI after I logged into my account and made sure my Git repository was connected. I also enabled the automatic deployment.

Before creating the app, I added two buildpacks from the Settings tab making sure to add heroku/python first, followed by heroku/nodejs.

I deployed my project to Heroku by pushing your Git repository to Heroku's remote, that will update with every git push, as chosen by me in the settings, successfully integrating and deploying my project for use through the Heroku URL.


## Media-and-credits
Bootstrap was used extensively in the project.
Code Institute's To-Do list walk through project was a big help setting the base of this project.


## Thanks-to
I would like to express my gratitude to Code Institute and my mentor for their exceptional web development curriculum and to my mentor for their invaluable guidance and support throughout this project. Thank you for providing the resources and expertise that have helped me grow as a developer.