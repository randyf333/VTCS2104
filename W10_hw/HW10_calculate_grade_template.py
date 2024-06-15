'''
HW10: work with Canvas API
@Date Created:
@pid:
@author: your name
'''

import requests
import json

# Set variables that we need for checking whether the config file has the 
# environment variable that we want
has_access_token = False # Check if the config file has the access token
has_api_version = False # Check if the config file has the API version
has_base_url = False # Check if the config file has the base url
has_course_id = False # Check if the config file has the course id

env_config = {} # Store the config variables

# Check if `config.json` contains the environment variable that we need
try:
    with open('config.json', 'r') as config_json:
        config = json.load(config_json)
        if 'ACCESS_TOKEN' in config:
            env_config['ACCESS_TOKEN'] = config['ACCESS_TOKEN']
            has_access_token = True
        if 'BASE_URL' in config:
            env_config['BASE_URL'] = config['BASE_URL']
            has_base_url = True
        if 'COURSE_ID' in config:
            env_config['COURSE_ID'] = config['COURSE_ID']
            has_course_id = True
        if "API_VERSION" in config:
            env_config['API_VERSION'] = config['API_VERSION']
            has_api_version = True
except FileNotFoundError: # Case if the config file do not exist, go to the input section
    pass
except json.decoder.JSONDecodeError: # Case if the config file is not a valid json file(eg. empty file, corrupted file)
    pass

# Input section, do this step if user do not have the config file or file do
# not have the environment variable that we needed
if not has_access_token:
    env_config['ACCESS_TOKEN'] = input('Please input your access token: ')
    has_access_token = True
if not has_base_url:
    env_config['BASE_URL'] = input('Please input your canvas base url: ')
    has_base_url = True
if not has_api_version:
    env_config['API_VERSION'] = input('Please input the API version of Canvas: ')
    has_api_version = True
while not has_course_id: # Loop until user input a valid course id
    env_config['COURSE_ID'] = input('Please input your course id: ')
    if env_config['COURSE_ID'].isdigit():
        env_config['COURSE_ID'] = int(env_config['COURSE_ID'])
        has_course_id = True
    else:
        print("Error! The course ID should be an integer.")

# Here we define some variables to make it easier for you to access those
ACCESS_TOKEN = env_config['ACCESS_TOKEN']
BASE_URL = env_config['BASE_URL']
API_VERSION = env_config['API_VERSION']
COURSE_ID = env_config['COURSE_ID']


# Here is a helper function that may help you resolve the pagination process
def get_paginated_list(url, header=None, params=None):
    response = requests.get(url, headers=header, params=params)
    data = response.json()
    while 'next' in response.links:
        response = requests.get(response.links['next']['url'], headers=header)
        data += response.json()
    return data


"""
You can use the following variables that we defined above. However,
to make sure your code can run properly, DO NOT change the above code.

Try to resolve all the TODOs below, and you can delete TODOs if you want
to during the submission.
"""

# Define you Header here (Hint: You should include your Access Token here)
header = {
    # TODO 1: Add Header that is necessary for complete this assignment
    'Authorization':ACCESS_TOKEN,
}

# List all assignments and their groups
# TODO 2: Replace <LINK> to the API endpoints of the Assignment Groups Endpoint
ASSIGNMENT_GROUPS_URL = BASE_URL + '/' + API_VERSION + '/' + 'courses/' + COURSE_ID + '/assignment_groups?include[]=assignments&include[]=submission'

params = {
    # TODO 3: Define parameters that you need to pass to the API
    'include[]':'assignments',
    'include[]':'submissions'
}

# TODO 4: Get all of your assignment group list based on the ASSIGNMENT_GROUPS_URL, 
# save the result in assignments_by_group
#assignments_by_group = requests.get(ASSIGNMENT_GROUPS_URL,headers=header,params=params)
assignments_by_group = get_paginated_list(ASSIGNMENT_GROUPS_URL,header=header,params=params)
# Print the assignment detail and calculate the score, you can define some variable 
# that help you with the calculation
total_weight = 0 # Store the total weight of all assignment group
percentage_earned_current = 0 # Store the current percentage earned
percentage_earned_final = 0 # Store the final percentage earned
points_earned = 0
total_points = 0
total_scored_weights = 0
hasGradedAssignment = False

for group in assignments_by_group:
    print("Assignment Group: ",group["name"]," (Assignment Group ID:", str(group["position"])+")","- Weight: ",group["group_weight"])
    total_weight += group["group_weight"]
    for assignment in group["assignments"]:
        submission = assignment["submission"]
        scoreEarned = "None"
        if("score" in submission):
            hasGradedAssignment = True
            scoreEarned = submission["score"]
            if(scoreEarned != None):
                points_earned += scoreEarned
            total_points += assignment["points_possible"]
        print("Assignment: ",assignment["name"], " Grade Possible: ",assignment["points_possible"], " Points Earned: ",scoreEarned)
    if hasGradedAssignment:
        total_scored_weights += group["group_weight"]
    percentage_earned_current += (points_earned/total_points) * group["group_weight"]
    percentage_earned_final += (points_earned/total_points) * group["group_weight"] 
    print("\n")
    # TODO 5: 
    # 1. Print the assignment in the group,
    # 2. Show the grade for each assignm,ent,
    # 3. Calculate the overall score for this course. 
    # 
    # Once you finish this part, you can delete the pass keyword

# TODO 6: Print out the overall score for the course
print("Current Grade: ",(percentage_earned_current/total_scored_weights)*100)
print("Final Grade: ", (percentage_earned_final/total_weight)*100)
