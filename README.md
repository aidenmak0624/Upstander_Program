# AI-Driven Personalized Journey for the Upstander Program

## Overview

This project enhances the **Canadian Museum for Human Rights (CMHR)** Upstander Program by integrating **AI-driven personalization** to create a tailored, interactive experience for users. The goal is to deepen users' connection with human rights issues, inspire them to recognize injustices, identify their strengths, and take action through three transformative phases:

1. **Recognizing Injustice**: Help users identify and understand social issues such as bullying, discrimination, and harassment.
2. **Discovering Personal Strengths**: Provide tools for users to reflect on their unique talents and capabilities through self-assessment exercises.
3. **Applying Strengths for Change**: Offer actionable advice, scenarios, and resources to help users apply their personal strengths in real-world situations.

By tailoring content to each user's background, interests, and needs, this program transforms human rights education into a deeply personal and empowering experience, inspiring users to become active advocates for social change.

## Project Goals

- **Enhance User Engagement**: Create a personalized journey through the Upstander Program using AI to tailor content based on user interests and strengths.
- **Interactive Experience**: Develop an AI-driven chatbot that guides users through the program, offering educational content and interactive elements.
- **Empower Users**: Encourage users to take action on human rights issues by providing them with relevant, personalized content and calls to action.

## Key Features

- **AI-Driven Chatbot**: A conversational AI chatbot powered by system prompts that educates and guides students through the program, offering personalized interactions and information delivery.
- **Personalized Recommendations**: Tailored content based on user inputs, such as interests, strengths, and preferred learning styles.
- **Interactive Learning Modules**: Engage with quizzes, games, and multimedia content that explore the history and impact of upstanders.
- **Personal Strength Survey**: A self-assessment tool that helps users discover their strengths and how to leverage them in social situations.
- **AI-Powered Scenario Generation**: Get personalized advice and role-playing simulations for handling real-world situations.
- **Community Story Sharing**: A space for users to share their personal stories, experiences, and insights, while reading and commenting on others' contributions.
- **Event and Resource Hub**: Stay informed with a calendar of upcoming events, workshops, and access to important resources.

## Chatbot Design Principles

The AI chatbot leverages system prompts to act as an educational agent, providing structured guidance while maintaining conversational fluency:

- **Defined Persona**: Establishing a specific attitude and communication style for the chatbot that aligns with educational goals.
- **Operational Rules**: Implementing clear guidelines the chatbot must follow to ensure appropriate and effective interactions.
- **Adaptive Prompting**: Using selective and multi-stage prompts, where the instructions given to the AI change based on the user's choices or the current stage of the conversation.
- **Guided Interaction**: Providing users with options or suggestions to steer the conversation effectively.
- **Hybrid Response Strategy**: Combining pre-defined answers for guaranteed accuracy on specific topics with AI-generated responses to maintain a natural and appropriate conversational tone.

## Technologies Used

- **Natural Language Processing (NLP)**: For building the conversational AI chatbot and educational agent.
- **Google's Gemini flash2.0 API**: To power the chatbot interactions and enable intelligent responses.
- **Pandas**: For processing and analyzing user activity and program data.
- **Flask/Streamlit**: For building the backend server and user interface.
- **Other Libraries**: Additional Python libraries for data processing, recommendation systems, and user interface development.

## Installation

To get a local copy of the repository up and running on your machine, follow these simple steps:

### 1. Clone the repository
```bash
git clone https://github.com/aidenmak0624/Upstander_Program.git
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

## Project Development Phases

1. **Research and Planning (Completed February 20)**:
   - Analyzed the existing Upstander Program and identified key requirements.
   - Conducted stakeholder interviews to understand user needs.
   - Researched AI techniques suitable for personalization.
   - Developed detailed project specifications and a timeline.

2. **Initial Development and Prototyping (Completed March 18)**:
   - Implemented foundational features, such as data processing and content integration.
   - Developed a basic chatbot for testing AI feasibility.
   - Created a prototype for user feedback.

3. **Refinement and Feature Expansion**:
   - Refined the prototype based on user feedback.
   - Added advanced features like personalized recommendations and multi-platform compatibility.
   - Implemented interactions tailored for different contexts (online, classrooms).

4. **Testing and Finalization**:
   - Iterated on the design and implementation to address issues.
   - Tested the final product for stability and usability.
   - Finalized features for the final presentation.

5. **Combined Version Development**:
   - Integrated individual team member contributions into a unified solution.
   - **Note**: This repository represents a collaborative effort. An earlier version with a different workflow approach was developed independently but was later merged with teammate contributions to create the final combined version presented here.

## Deliverables

- **AI-Driven Personalized Journey**: A functional AI system that tailors the user's journey through the Upstander Program.
- **User Interface (UI)**: An intuitive interface for users to engage with the program online or in classrooms.
- **Final Presentation**: A comprehensive presentation showcasing the AI journey, key learnings, and outcomes.

## Future Development Roadmap

Our plans for enhancing the chatbot and platform include:

- **Database Enhancement**: Improving the accuracy and expanding the scope of the underlying knowledge base.
- **Efficient Information Retrieval**: Implementing a database-selective prompt structure, allowing the chatbot to draw information only from relevant parts of the database for a given query.
- **Personalization**: Introducing an initial stage to identify user characteristics (like age or occupation) to tailor the conversation for a more personalized experience.
- **Multilingual Support**: Implementing features to make the program accessible to a wider audience.
- **Integration with Other Educational Tools**: Developing compatibility with other platforms used by museums and educational institutions.

## Acknowledgments

We would like to thank the **Canadian Museum for Human Rights (CMHR)** for their guidance and support throughout this project. This project is part of an educational initiative, credited by the Upstander Program from the Manitoba Human Rights Museum.

## Contributors

- **Rafia Rafa Islam**
- **Chin Wei Mak**

Special thanks to all team members for their contributions to this collaborative project.

## Project Timeline Notes

The project timeline experienced some delays due to a postponed kick-off meeting and delays in receiving necessary data. As a result, planned phases were adjusted. We worked diligently to catch up and ensure that all tasks were completed according to the revised timeline. The final deliverable represents a combined effort integrating multiple workflow approaches into a cohesive solution.

---
