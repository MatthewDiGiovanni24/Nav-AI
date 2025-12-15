from action import actionOriented
from analysis import analysisOriented
from categorization import categorizeQuery
from task import taskOriented

# NavAI

# Setup:
# Set screenshot bounds with bounds.py and place region variable
# Set goal in goal variable
# Place api key in api_key.txt

# goal = ""
# region = (x1, y1, width, height)
# goal = "Get to the yellow bus and avoid hitting other cars, go around them. You can stop when you are near it."
# goal = "Where am I?"
# goal = "Walk forward for three seconds, turn to the left for one second, and walk right for two seconds."
goal = "Walk through the doorway on the left walk into the bedroom."
region = (1397, 358, 1008, 562)

category = categorizeQuery(goal)

if category == 0:
    actionOriented(goal, region)
elif category == 1:
    analysisOriented(goal, region)
elif category == 2:
    taskOriented(goal, region)