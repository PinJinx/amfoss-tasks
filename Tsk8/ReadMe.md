# Hero Dex Project: Creating an Android App with Flutter

## Introduction

One of the most challenging yet fascinating tasks I encountered was the Hero Dex project. The main objective of this task was to create an Android app using Flutter that reads data from a JSON file and displays each hero along with their descriptions. I experimented with both VS Code and Android Studio and managed to get Flutter working only inside Android Studio. I completed the task in about 3-4 days, with the last two days being the most interesting.

## Basic Structure

```
Main Branch
|
--lib
|  |
|  ---Pages
|      |
|      ---Dart files(I placed my dart files for each page in this)
|
--Assets
   |
   ---- Icons(this Stored pictures)
   |
   ---- Json(data for heros)
```

## Technical Details

I began the task by following a YouTube tutorial that was partially related to my topic, which helped me get a grasp on Flutter. As a result, I organized my codebase into different files. The program executes from the `main.dart` file, which fetches the JSON file and calls another file named `HomePage.dart`. This file manages the UI and backend of the application.

Once the data is fetched from the JSON file, this file draws the UI and initializes the name and icon of each hero, stored inside a container within a grid view. Each container also contains a button with a heart icon that tracks and stores a list of favorite heroes whenever the user interacts with it. The user can then display all of their favorite heroes by clicking the heart icon inside the search bar. Additionally, there is another button in the search bar with a moon icon that toggles between Dark and Light mode.

## My Experience with the Task

When I first started the task, I decided to work in VS Code. To do so, I searched for instructions and found that I needed to install and extract some JDKs and SDKs. On my first attempt, I encountered an error saying the SDK was not found. After resolving that issue, a new problem arose, indicating that some other module was not installed. I kept running into issues, and every time I fixed a bug related to installing or configuring a module, a new one popped up.

Eventually, I got so fed up that I decided to switch to Android Studio. Setting up Android Studio for Flutter was a much easier task. Once everything was set up, I started on my project. For the basics, I followed a YouTube video that helped me create a framework and complete the basic front end, like the search bar and buttons. The remaining tasks, such as fetching data from the JSON file and displaying the information, were completed with the help of Google.

Once I got started, it was really fun figuring things out, and it gave me a sense of accomplishment as every piece of the puzzle started coming together.

## My Thoughts on the Task

This task was really interesting. It felt similar to working with a modern game engine, and since I have experience with Unity, I had no trouble adapting. In my opinion, this task was well-designed, with plenty of guides and tutorials available for Flutter. Any beginner could pick it up; although it might look like a mountain at first, once you grasp the basics, the rest is smooth sailing.

