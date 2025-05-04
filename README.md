# Aryan-Shanker-Final-Project
This is a new public repository for my OIM3640 Final Project. 

I will be working individually for this project. 
Team Members: Aryan Shanker (myself)

## Big Idea / Project Goal:
Evora is an AI-powered web application designed to help users make more sustainable transportation choices. The mission behind this project is to empower individuals to reduce their carbon footprint by providing real-time emissions calculations, coupled with actionable insights and recommendations for shifting to more eco-friendly commute routines. 

## Purpose:
Climate Change is one of the most monumental worldwide issues in the world today. Global temperatures have already surpassed the 1.5 degree celsius warming threshold, and the transportation sector alone accounts for 24% of global carbon dioxide emissions (with road travel alone making up 3/4 of the 24%). I feel that many people want to make greener choices, but lack the tools and  solutions to understand the impact of their daily travel. Thus, I thought Evora would be an interesting final project to pursue as an entrepreneurial, AI-focused initiative directly helping tp solve the pressing real-world problem of climate change. 

## User Instructions:
- Clone the repository on GitHub to VS Code,
- Once the repository is cloned to your laptop, and all files are accessible, in order to effectively run the code, and as well experience the web application, you need to download two APIs: Mapbox API and Climatiq API. Prior to doing so, create a .env file to securely store your API Keys. In your .env file, it should look like this:

MAPBOX_TOKEN=your_mapbox_token
CLIMATIQ_API_KEY=your_climatiq_api_key

Once that is done, in the .gitignore file, add .env to ensure that your API Keys are kept private, and are not pushed to a public GitHub repository.

- Moving onto the downloading process for the API Keys, the two links below will guide you to simply create a free account, and register for a key. Inputting instructions below as well.

To download the Climatiq API Key:
- Go to this link: https://www.climatiq.io/pricing
- Scroll down to the bottom, choose the community plan (ideal for getting started with carbon measurements), click the free signup button and create an account! You will get an email confirmation after all is done.
- Once your account is created and you log in, on your home page, click the Get API Keys button, and then on the top right hand side, there will be a purple button saying: Create API Key. Click it - label your API Key, then copy the key into your .env file - replacing your_climatiq_api_key with your actual Climatiq API Key. 

To download the Mapbox API Token:
- Go to this link: https://account.mapbox.com/auth/signin/?route-to=https%3A%2F%2Fconsole.mapbox.com%2F%3Fauth%3D1
- Create an account and sign into your account. Then on the left hand side of your home page, under the heading Admin, click Tokens, then click the round button saying: Create a token. Label your token, and then similar to as you did for Climatiq API Key process, copy the key into your .env file - replacing your_mapbox_token with your actual API token. 

- Now you are ready to go! You have securely created your own API Keys, stored them securely, and now can experiemtn with the code and run the web app! Run the app.py file, and in the terminal, visit the development server link that pops up in a new broswer tab. It will look like this: http://127.0.0.1:5000

- To stop experimenting with the web app, just press CTRL+C in the terminal to quit. 

- Enjoy and have fun! Enter your starting location, distance (in kilometres) travelled and mode of transport taken, click Calculate Emissions, view your carbon footprint on a trip by trip basis, and receive a greener travel recommendation!

## Implementation Information:

In terms of implementation, I thought it was first best to register for, download and securely store the API Keys I was going to use for this project. From Assignment 3, I knew that Geocoding would be a major part of the code for Evora's MVP, therefore I focused on using Mapbox. Afterwards, I researched for carbon emissions calculation APIs that could aid in helping to swiftly calculate user's carbon footprint, and found Climatiq to be the most encompassing. Once completing the process of choosing the best APIs for the scope of my project, and downloading both API Keys, I made sure to create a .env file to store the API Keys, a .gitignore file, writing .env in the .gitignore for greater security.

To organize my code for this project, creating seperate .py files was the most effective way to accurately see and structure my code easily. Immediately after storing my API Keys, I created config.py, to load the .env files (API Keys) utilizing the dotenv package. Thus, creating a very good start, and foundation to the completion of Evora' MVP. 

Once that was done, I focused on integrating the APIs in my code (api_integrations.py), creating two main functions calling the Mapbox API and the Climatiq API. Mapbox for geocoding requests - gaining the longitude and latitude of the user's inputted start location, and Climatiq API for carbon emission calculation. This helped to streamline the backend process of providing detailed carbon footprint analytics to users whilst utilizing the web app. 

Following that, to complete the backend development of the Evora MVP, I imported libraries that would help with the Machine Learning/AI aspect of my project and created functions integrating these libraries for better AI analytics for users - to help improve AI-powered recommendation logic (ml_functions.py), leveraging: pandas, numpy, scikit-learn libraries, matplotlib and TexBlob. By pursuing this project, I strecthed myself particularly in the usage of machine learning and data analysis methods - increasing my confidence and curiosity in diving deeper into it in the near future, and appying them to more of my personal projects. 

After combining all these ingredients, the backend was robustly designed, helping to ease the transition towards front-end web app development. To start, I created (app.py) - the Flask web server, combining backend code, taking in user input and helping to display user results effectively. On top of that, I worked on an index.html file, utilizing mainly HTML and aspects of CSS code to design a simple, effective, and pleasant design! 

### Use of AI In Development:
Throughout this project, AI was incredibly helpful not only with ensuring the functionality of the code at times where I was running into issues (for debugging purpose), but also in broadening my understanding and my experience with exploring new libraries (ex: especially in creating the latter machine learning functions for Evora in ml_functions.py). Thus, enhancing my awareness of the different avenues that can be taken to improve the feasability of a project (ex: helping me to enter into the realms of CSS, coupled with HTML code to finalze the Evora frontend web app design), bring multiple features to life, and aid in creating a foundational, solid MVP, ready for greater potental future development. 

## Results:
- Accurate Emissions Analytics: Providing real-world carbon footprint estimates for various transportation modes, for each user's trips.
- Personalized AI-based Recommendations: Greener alternatives based on user input.
- Friendly User Experience & Interface: Clean, simple to grasp, intuitive design for use. 

![Screenshot](screenshot.png) 
The screenshot of the result of the Evora AI Transportation Assistant is also uploaded to the GitHub repository for reference.

## Project Evolution/Narrative:
Evora's MVP development was very fun, and exciting! It was a learning journey of research, iteration and continuous improvement! First I focused on really ensuring the backend was working well and was coded up effectively - constantly checking that APIs were well integrated, stored securely, AI-powered recommendations and analytics for user's personalized feedback was well structured. Writing test functions at the end of code scripts to see how the code ran, and the results given based on sample data was really cool to see! Once all was done, then I moved onto frontend web app development, focusing on a visually appealing user interface, allowing for a simple user experience! My approach to the completion of the final project was via a step by step process, inputting checks and balances to confirm that all aspects of the code (backend and frontend) were combined and running smoothly together!

## Attribution:
- External APIs For This Project: [Mapbox](https://www.mapbox.com/) and [Climatiq](https://www.climatiq.io/).
- Python Libraries: Flask, pandas, numpy, scikit-learn, matplotlib, TextBlob.
- AI Assistance: Perplexity For Debugging Purposes & Code Review. 




