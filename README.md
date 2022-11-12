# Palgorithm-Fall-2022
## Project Architecture
Pull Requests for minigames must have a structured minigame class.
The PyGame game loop includes two main components, event processing and updating. Each minigame must have the following two methods included with the class which correspond to this paradigm.
```
def event(event) -> none:
def update(screen) -> bool:
```
Event takes the pygame event object as a parameter to allow programmer to be free to handle events in any way they want, this includes mouse and keyboard presses and releases for movement or commands.

The update method takes the screen object and is responsible for drawing things on the screen. You do not need to call update to the screen yourself as the main loop does that for you but you will need use ```blit``` to render viewable components. This method typically also contains the object movement and collision code. This method will return false for every update where the game doesn't end. If it returns true it means that the game is over. The code will no longer call your event, update functions and move on to the next minigame.
## Example
Below I've included code for a main menu that implements the event and update functions which moves the game forward when you press the button. The button component was taken from <a href='https://github.com/Mekire/pygame-button'>pygame button</a>. You are welcome to do the same to make it easier to develop the game (pygame might not have a component you want but don't want to write).
# Learn a Bit About Git
<a href='https://www.w3schools.com/git/git_intro.asp'>W3 Schools git guide</a>

# How to Contribute
<a href='https://docs.github.com/en/get-started/quickstart/contributing-to-projects'>Github Contribution Guide</a>
