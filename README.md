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

The Habit Tracker app serves as a personalized habit management system, allowing users to register, track their habits, and leverage essential features to enhance their daily routines.

## Features

### User Registration and Submission

- **User Registration:** Sign up to create an account and start utilizing the habit tracking features.
- **Resource Submission:** Users can contribute resources to the habit directory, sharing valuable insights with the community.

### Interaction and Organization

- **Upvoting and Bookmarking:** Users can express appreciation for helpful resources by upvoting and bookmarking them.
- **Agile Principles:** Built with Agile management principles, ensuring flexibility and responsiveness to user needs.

### Project Management

- **GitHub Integration:** Leveraging GitHub features such as Issues and Projects to implement Scrum methodology.
- **Kanban Board:** A visual representation of the project's progress and tasks, providing clarity on work status.
- **Closed Issues:** Detailed records of resolved issues, showcasing the dedication to maintaining a bug-free application.

### CRUD Functionality

- **Resource Management:** Users can create, update, and delete resources they contribute, ensuring content relevance.
- **Account Management:** Users have full control over their accounts, with the ability to create, update, read, and delete profiles.
- **Admin Privileges:** Admins can manage all resources efficiently, ensuring the integrity of the habit directory.

### Project Planning and Execution

- **GitHub Tags:** Efficient use of tags for assigning story points, prioritizing features based on the MoSCoW method, and categorizing user stories.
- **Milestones:** Strategically plan sprints and set deadlines using GitHub's Milestones feature.

## Learning and Development

- **Continuous Improvement:** Regular updates and bug fixes based on user feedback and reported issues.
- **Educational Background:** Drawing insights from the Agile Foundations course on LinkedIn Learning to enhance project management skills and understanding of Agile and Scrum methodologies.

Feel free to explore the Habit Tracker app, track your habits effortlessly, and contribute to the growth of a supportive community. Happy habit building!

#user-stories
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
