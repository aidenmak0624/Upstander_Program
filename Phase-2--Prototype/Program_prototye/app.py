import streamlit as st
import requests
import sqlite3
from datetime import datetime
import google.generativeai as genai



    
def init_db():
    # Initialize user_data.db
    conn = sqlite3.connect("user_data.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS interactions 
                 (user_id TEXT, message TEXT, response TEXT, timestamp DATETIME)''')
    conn.commit()
    conn.close()
    
    conn = sqlite3.connect("upstander_stories.db")
    c = conn.cursor()
    #c.execute('''CREATE TABLE IF NOT EXISTS upstander_stories 
    #             (title TEXT, category TEXT, emotion_tags TEXT, story TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS stories 
                 (title TEXT,  story TEXT)''')
    c.execute("DELETE FROM stories")
    
    c = conn.execute("INSERT INTO stories (title, story) VALUES ('Tyler Clementis Story', 'Tyler Clementi was an 18-year-old freshman at Rutgers University in 2010. Eager to embrace his identity as a gay man, Tyler faced a tragic invasion of his privacy when his roommate secretly streamed his intimate moments online without his consent. This act of cyberbullying led to immense humiliation and emotional distress for Tyler. The lack of intervention from those who witnessed the harassment highlighted the profound impact of bystander apathy. Devastated by the ordeal, Tylers story ended in tragedy, but it ignited a global movement advocating for the end of bullying and the promotion of empathy and respect. Today, the Tyler Clementi Foundation continues to inspire individuals worldwide to become Upstanders, standing against bullying and supporting those affected. The foundation can be visited at: https://tylerclementi.org/tylers-story-tcf/?utm_source=chatgpt.com')")
    
    conn.commit()
    conn.close()
    
def clear_database():
      
    conn = sqlite3.connect("upstander_stories.db")
    c = conn.cursor()
    
    # Clear existing data
    c.execute("DELETE FROM stories")
    
    # Save and close connection
    conn.commit()
    conn.close()

    print("Database cleared.")




    
genai.configure(api_key="API_KEY)  # Replace with your API key

def get_ai_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")  # Using Gemini Pro model
        response = model.generate_content(user_input)

        if response and hasattr(response, "text"):  
            return response.text  # Extract text from response
        else:
            return "Error: No valid response from AI."

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Store user interaction
def store_interaction(user_id, message, response):
    conn = sqlite3.connect("user_data.db")
    c = conn.cursor()
    c.execute("INSERT INTO interactions (user_id, message, response, timestamp) VALUES (?, ?, ?, ?)", 
              (user_id, message, response, datetime.now()))
    conn.commit()
    conn.close()

# Streamlit UI with multiple pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Introduction", "Upstander Project", "Real Stories", "Strength Survey", "Personal Memories", "Scenario Generation", "Events & Resources"])

    # Page 0: Introduction
    if page == "Introduction":
        st.title("Welcome to the Upstander Program")
        #st.image("images/banner.jpg", use_column_width=True)  # Add a banner image
        st.markdown('<div class="text-container">', unsafe_allow_html=True)
        st.write("Learn how to respond to social situations with AI-driven stories and suggestions. Here we will display Universal Declaration of Human Right...")
        st.write("### Get Started:")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Randmoly Chooseing An Article from UDHM"):
                st.write("Article 1: All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.")
                st.write("Article 2: Everyone is entitled to all the rights and freedoms set forth in this Declaration, without distinction of any kind")
        with col2:
            if st.button("Select the topic of Human Rights you interested in!"):
                st.write("Article 3: Everyone has the right to life, liberty and security of person.")
                st.write("Article 4: No one shall be held")
               
        st.markdown('</div>', unsafe_allow_html=True)

    # Page 1: Upstander Project
    elif page == "Upstander Project":
        st.title("Upstander Project")
        st.markdown('<div class="text-container">', unsafe_allow_html=True)
        st.write("Learn about the history and importance of upstanders.")
        
        with st.expander("What is an Upstander?"):
            st.write("An upstander is someone who takes action to support others in difficult situations.")
        
        with st.expander("Take the Upstander Quiz"):
            st.write("Test your knowledge of upstanders!")
            question = st.radio("What does it mean to be an upstander?", ["Someone who ignores problems", "Someone who takes action to help others", "Someone who causes problems"])
            if st.button("Submit Quiz"):
                if question == "Someone who takes action to help others":
                    st.success("Correct! An upstander takes action to help others.")
                else:
                    st.error("Incorrect. Try again!")
        st.markdown('</div>', unsafe_allow_html=True)

    # Page 2: Real Stories
    elif page == "Real Stories":
        st.title("Real Stories")
        st.markdown('<div class="text-container">', unsafe_allow_html=True)
        st.write("Read real stories from the Human Rights Museum.")
        
        # Fetch stories from the database
        conn = sqlite3.connect("upstander_stories.db")
        c = conn.cursor()
        c.execute("SELECT title, story FROM stories")
        stories = c.fetchall()
        conn.close()
        
        for title, story in stories:
            with st.expander(title):
                st.write(story)
        st.markdown('</div>', unsafe_allow_html=True)

    # Page 3: Strength Survey
    elif page == "Strength Survey":
        st.title("Personal Strength Survey")
        st.markdown('<div class="text-container">', unsafe_allow_html=True)
        st.write("Discover your strengths and how to use them.")
        
        with st.form("strength_survey"):
            st.write("How do you react in stressful situations?")
            reaction = st.radio("Choose one:", ["Calmly", "Anxiously", "With anger"])
            submitted = st.form_submit_button("Submit")
            
            if submitted:
                st.write(f"Your reaction: {reaction}")
                st.write("**Your top strength:** Empathy")  # Example result
        st.markdown('</div>', unsafe_allow_html=True)

    # Page 4: Personal Memories
    elif page == "Personal Memories":
        st.title("Personal Memories")
        st.markdown('<div class="text-container">', unsafe_allow_html=True)
        st.write("Reflect on your own experiences and share your stories.")
        
        with st.form("share_story"):
            user_id = st.text_input("Enter your User ID:")
            story = st.text_area("Share your story:")
            submitted = st.form_submit_button("Submit")
            
            if submitted:
                conn = sqlite3.connect("user_data.db")
                c = conn.cursor()
                c.execute("INSERT INTO interactions (user_id, message, response, timestamp) VALUES (?, ?, ?, ?)", 
                          (user_id, story, "N/A", datetime.now()))
                conn.commit()
                conn.close()
                st.success("Thank you for sharing your story!")
        
        st.subheader("Community Stories")
        conn = sqlite3.connect("user_data.db")
        c = conn.cursor()
        c.execute("SELECT user_id, message FROM interactions WHERE response = 'N/A'")
        user_stories = c.fetchall()
        conn.close()
        
        for user_id, story in user_stories:
            st.write(f"**User {user_id}:** {story}")
        st.markdown('</div>', unsafe_allow_html=True)

    # Page 5: Scenario Generation
    elif page == "Scenario Generation":
        st.title("Scenario Generation")
        st.markdown('<div class="text-container">', unsafe_allow_html=True)
        st.write("Get actionable steps for specific situations.")
        
        scenario = st.selectbox("Choose a scenario:", ["Bullying", "Workplace Harassment", "Public Discrimination"])
        if st.button("Get Advice"):
            with st.spinner("Generating advice..."):
                advice = get_ai_response(f"How to handle {scenario}?")
                st.write("**AI Advice:**", advice)
        st.markdown('</div>', unsafe_allow_html=True)

    # Page 6: Events & Resources
    elif page == "Events & Resources":
        st.title("Events & Resources")
        st.markdown('<div class="text-container">', unsafe_allow_html=True)
        st.write("Find upcoming events and emotional support resources.")
        
        st.subheader("Upcoming Events")
        st.write("1. Upstander Workshop - October 15, 2023")
        st.write("2. Human Rights Seminar - November 1, 2023")
        
        st.subheader("Resources")
        st.write("[Mental Health Hotline](https://example.com)")
        st.write("[Anti-Bullying Organization](https://example.com)")
        st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        © 2023 Upstander Program. All rights reserved. | 
        <a href="mailto:info@upstanderprogram.com" style="color: white;">Contact Us</a> | 
        <a href="https://example.com" style="color: white;">Privacy Policy</a>
    </div>
    """, unsafe_allow_html=True)

# Initialize database
clear_database()
init_db()

if __name__ == "__main__":
    main()
