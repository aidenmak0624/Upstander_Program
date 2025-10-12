
from utils.conversation_stages import conversation_stages
from utils.upstander_stories import upstander_stories
from utils.get_response import *
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_session import Session 
import pandas as pd
import os
import re
import random
import requests
from dotenv import load_dotenv

app = Flask(__name__, static_folder='static')
CORS(app)

# Configure server-side session storage
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "supersecretkey"
Session(app)

# Load environment variables
load_dotenv()


def main():
    # Main application logic goes here
     app.run(debug=True, port=5002)
     
     
#Function to send User input to get resoonse function
@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message', '')
        session_data = request.json.get('session_data', None)
        print(f"User input: {user_input}")
        print(f"Session data before: {session_data}")
        
        if not user_input:
            return jsonify({"response": "Please provide a message."})
        
        if not session_data:
            session_data = {
                'current_stage': 'basic_information',
                'progress': 0,
                'responses': [],
                'selected_options': [],
                'user_data': {},
                'selected_characteristic': None
            }
            
        # Update session data with the user's input
        session_data['responses'].append(user_input)

        current_stage = session_data.get('current_stage', 'basic_information')

        if current_stage not in conversation_stages:
            return jsonify({"response": f"Error: '{current_stage}' stage not found in conversation_stages."}), 400
        
        # Handle Next Stage Button Click
        if user_input == "[NEXT_STAGE]":
            stages = list(conversation_stages.keys())
            current_stage = session_data.get('current_stage', 'basic_information')

            try:
                current_index = stages.index(current_stage)
                if current_index < len(stages) - 1:
                    next_stage = stages[current_index + 1]
                    session_data['current_stage'] = next_stage
                    session_data['progress'] = min(100, (current_index + 1) * (100 // len(stages)))
                    # Get the actual message for the next stage
                    response = conversation_stages[next_stage]["message"]
                else:
                    response = "You've completed all stages!"
            
            except ValueError:
                response = "Invalid conversation stage."
            
            return jsonify({
                "response": response,
                "session_data": session_data,
                "current_stage": session_data['current_stage'],
                "options": conversation_stages[session_data['current_stage']].get("options", []),
                "progress": session_data['progress']
            })

        selected_characteristic = session_data.get("selected_characteristic", "")

        # Handle `explain_upstander` stage
        if session_data.get("current_stage") == "explain_upstander" and user_input in upstander_stories.keys() and selected_characteristic is None:
            upstander_names = [story["name"] for story in upstander_stories[user_input]]
            response_text = f"Here are some upstanders who exhibit {user_input}: {', '.join(upstander_names)}"
            options = upstander_names

            session_data["selected_characteristic"] = user_input
            #session_data["current_stage"] = "identify_upstander" # TODO

            return jsonify({
                "response": response_text,
                "session_data": session_data,
                "current_stage": session_data['current_stage'],
                "options": options,
                "progress": session_data['progress']
            })

       
        elif session_data.get("current_stage") == "explain_upstander" and selected_characteristic in upstander_stories.keys():
            for story in upstander_stories[selected_characteristic]:
                if user_input.lower() == story["name"].lower():
                    response_text = f"{story['name']} was an upstander because: {story['story']} \nImpact: {story['impact']}"
                    
                    return jsonify({
                        "response": response_text,
                        "session_data": session_data,
                        "current_stage": session_data['current_stage'],
                        "options": [s["name"] for s in upstander_stories[selected_characteristic]],
                        "progress": session_data['progress']
                    })

        
            # Handle `identify_upstander` stage without needing selected_characteristic
        elif session_data.get("current_stage") == "identify_upstander":
            found_story = None
            matched_characteristic = None
            
            for characteristic, stories in upstander_stories.items():
                for story in stories:
                    if user_input.lower() == story["name"].lower():
                        found_story = story
                        matched_characteristic = characteristic
                        break
                if found_story:
                    break

            if found_story:
                response_text = f"{found_story['name']} was an upstander because: {found_story['story']} \nImpact: {found_story['impact']}"
                options = [s["name"] for s in upstander_stories[matched_characteristic]]

                return jsonify({
                    "response": response_text,
                    "session_data": session_data,
                    "current_stage": session_data['current_stage'],
                    "options": options,
                    "progress": session_data['progress']
                })


        print(user_input)
        # Get response from the AI model
        result = get_response(user_input, session_data)
        print(user_input)
        print(result)
        # Clean up the response by removing template variables
        response = result["response"]
        if response:
            # Remove template variables like {stage_message}
            response = re.sub(r'\{[^}]+\}', '', response).strip()
            # Remove any extra whitespace
            response = ' '.join(response.split())
        
        return jsonify({
            "response": response,
            "session_data": session_data,
            "current_stage": session_data['current_stage'],
            "options": [],
            "progress": session_data['progress']
        })
    
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        return jsonify({"response": "An error occurred while processing your request. Please try again."})


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


if __name__ == "__main__":
    main()
