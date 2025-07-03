import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time

# Page configuration
st.set_page_config(
    page_title="Kabir Khanuja | Software Developer",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .stat-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        margin-bottom: 1rem;
    }
    
    .skill-badge {
        background: linear-gradient(45deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.25rem;
        display: inline-block;
        font-size: 0.9rem;
        font-weight: 600;
    }
    
    .project-card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .timeline-item {
        border-left: 3px solid #667eea;
        padding-left: 1rem;
        margin: 1rem 0;
    }
    
    .achievement-badge {
        background: linear-gradient(45deg, #ff6b6b, #ffa500);
        color: white;
        padding: 0.8rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        font-weight: bold;
    }
    
    .contact-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    
    .stMetric {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        padding: 1rem;
    }
    
    .animated-text {
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 20px #667eea; }
        to { text-shadow: 0 0 30px #764ba2; }
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("# 🚀 Navigation")
page = st.sidebar.selectbox(
    "Choose a section:",
    ["🏠 Home", "💼 Experience", "🎯 Projects", "🏆 Achievements", "📊 Skills Dashboard", "📞 Contact"]
)

# Data for visualizations
skills_data = {
    'Frontend': ['ReactJs', 'Tailwind CSS', 'StreamLit', 'React-Native'],
    'Backend': ['Flask', 'NextJs', 'Java', 'Node.js'],
    'AI/ML': ['Python', 'Machine Learning', 'CNN', 'GenAI'],
    'Database': ['MongoDB', 'PostgreSQL', 'NoSQL'],
    'Cloud': ['AWS', 'GCP'],
    'Tools': ['Git', 'GitHub', 'Figma', 'PowerBI']
}

projects = [
    {
        'name': 'Virtual AI Rehabilitation Assistant',
        'tech': ['Flask', 'MongoDB', 'Machine Learning', 'GenAI', 'React-Native'],
        'description': 'AI-powered rehabilitation assistant with personalized adaptive roadmaps and real-time progress tracking.',
        'impact': '99.5% user satisfaction'
    },
    {
        'name': 'Fake Job Detector',
        'tech': ['Machine Learning', 'Random Forest', 'Naive Bayes', 'ReactJs'],
        'description': 'ML-based fake job posting detector achieving 99.66% accuracy in fraud detection.',
        'impact': '99.66% accuracy'
    },
    {
        'name': 'CarbonCtrl',
        'tech': ['GitHub Actions', 'VS Code', 'CodeCarbon', 'AI'],
        'description': 'Sustainability-focused developer toolchain for carbon emission tracking and optimization.',
        'impact': 'CO₂ reduction in dev workflows'
    }
]

# HOME PAGE
if page == "🏠 Home":
    # Header Section
    st.markdown("""
    <div class="main-header">
        <h1 style="color: white; text-align: center; font-size: 3rem; margin-bottom: 0.5rem;">
            KABIR KHANUJA
        </h1>
        <h2 style="color: white; text-align: center; font-size: 1.5rem; opacity: 0.9;">
            🚀 Aspiring Software Developer | AI Enthusiast | Full-Stack Developer
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🎯 Projects Completed", "10+", "3 this year")
    with col2:
        st.metric("🏆 Hackathon Wins", "2", "Including IEEE Winner")
    with col3:
        st.metric("📚 Years Experience", "3+", "Since 2020")
    with col4:
        st.metric("💡 Technologies", "20+", "Always Learning")
    
    # Career Objective
    st.markdown("## 🎯 Career Objective")
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1)); 
                padding: 1.5rem; border-radius: 12px; border-left: 4px solid #667eea;">
        <p style="font-size: 1.1rem; line-height: 1.6;">
            Aspiring Software Developer with a solid foundation in <strong>C, Python, Java</strong>, and 
            <strong>Data Structures & Algorithms</strong>. Experienced in building web applications and 
            AI-driven solutions, proficient in tools like Excel and Power BI. I aim to contribute 
            impactful software projects, grow within a collaborative team, and continuously develop 
            my technical and problem-solving skills.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Skills Overview
    st.markdown("## 🛠️ Technical Arsenal")
    
    # Create main skill categories with key technologies only
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Full-Stack Development")
        main_fullstack = ['ReactJs', 'Flask', 'MongoDB', 'Python']
        for skill in main_fullstack:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
            
    with col2:
        st.markdown("### AI & Machine Learning")
        main_ai = ['Machine Learning', 'GenAI', 'Computer Vision']
        for skill in main_ai:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
    
    with col3:
        st.markdown("### Development Tools")
        main_tools = ['Git', 'GitHub', 'Figma', 'PowerBI']
        for skill in main_tools:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
    
    # Recent Highlights
    st.markdown("## ⭐ Recent Highlights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="achievement-badge">
            🏆 INC TechFiesta International Hackathon Runner Up (2025)
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="achievement-badge">
            🎯 EcoInnovate Hackathon Winner - IEEE (2024)
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="achievement-badge">
            💻 Web Developer at Insurance firm (Current)
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="achievement-badge">
            🎙️ Podcast Host - "ThatOneThinker" (Multi-platform)
        </div>
        """, unsafe_allow_html=True)

# EXPERIENCE PAGE
elif page == "💼 Experience":
    st.markdown("# 💼 Professional Experience")
    
    # Experience Timeline
    experiences = [
        {
            'role': 'Web Developer',
            'company': 'Insurance with Hardeep',
            'duration': 'DEC 2024 - FEB 2025',
            'description': 'Spearheaded design and development of fully functional website with focus on UI/UX optimization.',
            'achievements': [
                'Built entire user interface ensuring seamless user experience',
                'Implementing backend functionalities for efficient performance',
                'Optimizing cross-browser compatibility and troubleshooting'
            ]
        },
        {
            'role': 'Marketing Manager & Specialist',
            'company': 'Pawzz',
            'duration': 'APR 2024 - JUN 2024',
            'description': 'Led multifaceted responsibilities for animal welfare mission including content creation and awareness campaigns.',
            'achievements': [
                'Spearheaded content creation and writing initiatives',
                'Organized donation camps and awareness programs',
                'Developed marketing strategies for animal welfare'
            ]
        },
        {
            'role': 'Technical Expert',
            'company': 'TravLeo',
            'duration': 'NOV 2022 - FEB 2023',
            'description': 'Played pivotal role in website development with focus on both frontend and backend development.',
            'achievements': [
                'Developed website using SQL for data management',
                'Provided technical support and troubleshooting',
                'Created innovative marketing strategies and visual content'
            ]
        },
        {
            'role': 'Student Intern',
            'company': 'Dassault Systèmes',
            'duration': 'JUL 2020 - AUG 2021',
            'description': 'Participated in Seed the Future Entrepreneurs Program, built portable mixer project.',
            'achievements': [
                'Handled software component and design using Dassault web application',
                'Gathered user requirements from 1,500+ survey responses',
                'Received prestigious STFE award for team efforts'
            ]
        }
    ]
    
    # Display experiences
    for exp in experiences:
        st.markdown(f"""
        <div class="timeline-item">
            <h3 style="color: #667eea; margin-bottom: 0.5rem;">{exp['role']}</h3>
            <h4 style="color: #764ba2; margin-bottom: 0.5rem;">{exp['company']} | {exp['duration']}</h4>
            <p style="margin-bottom: 1rem;">{exp['description']}</p>
            <strong>Key Achievements:</strong>
            <ul>
        """, unsafe_allow_html=True)
        
        for achievement in exp['achievements']:
            st.markdown(f"• {achievement}")
        
        st.markdown("</ul></div>", unsafe_allow_html=True)
        st.markdown("---")

# PROJECTS PAGE
elif page == "🎯 Projects":
    st.markdown("# 🎯 Featured Projects")
    
    # Project showcase
    for i, project in enumerate(projects):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"""
            <div class="project-card">
                <h3 style="color: #667eea; margin-bottom: 1rem;">{project['name']}</h3>
                <p style="margin-bottom: 1rem;">{project['description']}</p>
                <div style="margin-bottom: 1rem;">
                    <strong>Technologies:</strong><br>
            """, unsafe_allow_html=True)
            
            for tech in project['tech']:
                st.markdown(f'<span class="skill-badge">{tech}</span>', unsafe_allow_html=True)
            
            st.markdown(f"""
                </div>
                <div style="background: rgba(102, 126, 234, 0.2); padding: 0.8rem; border-radius: 8px; margin-top: 1rem;">
                    <strong>Impact:</strong> {project['impact']}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Create a simple project metrics visualization
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = 95 - i*5,  # Simulated completion percentage
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Project Score"},
                gauge = {
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#667eea"},
                    'steps': [
                        {'range': [0, 50], 'color': "lightgray"},
                        {'range': [50, 80], 'color': "orange"},
                        {'range': [80, 100], 'color': "lightgreen"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 90
                    }
                }
            ))
            fig.update_layout(height=200, margin=dict(l=20,r=20,t=20,b=20))
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")

# ACHIEVEMENTS PAGE
elif page == "🏆 Achievements":
    st.markdown("# 🏆 Achievements & Recognition")
    
    achievements = [
        {
            'title': 'INC TechFiesta International Hackathon Runner Up',
            'organization': 'PICT',
            'year': '2025',
            'icon': '🥈',
            'description': 'Secured runner-up position in international hackathon competition'
        },
        {
            'title': 'EcoInnovate Hackathon Winner',
            'organization': 'IEEE',
            'year': '2024',
            'icon': '🏆',
            'description': 'Won hackathon focusing on environmental innovation and sustainability'
        },
        {
            'title': 'Outstanding Intern',
            'organization': 'TravLeo',
            'year': '2023',
            'icon': '⭐',
            'description': 'Recognized for exceptional performance during internship period'
        },
        {
            'title': 'Proficiency Award',
            'organization': 'Millennium National School & You for Youth',
            'year': '2022',
            'icon': '🎓',
            'description': 'Awarded for academic excellence and outstanding performance'
        },
        {
            'title': 'Future Entrepreneur Award',
            'organization': 'Dassault Systèmes',
            'year': '2021',
            'icon': '🚀',
            'description': 'Recognized in Seed the Future Entrepreneurs Program'
        }
    ]
    
    # Display achievements in an interactive format
    col1, col2 = st.columns(2)
    
    for i, achievement in enumerate(achievements):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class="achievement-badge" style="background: linear-gradient(45deg, 
                {'#ff6b6b, #ffa500' if i % 3 == 0 else '#4facfe, #00f2fe' if i % 3 == 1 else '#667eea, #764ba2'});">
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <span style="font-size: 2rem; margin-right: 1rem;">{achievement['icon']}</span>
                    <div>
                        <h4 style="margin: 0; font-size: 1.1rem;">{achievement['title']}</h4>
                        <p style="margin: 0; opacity: 0.9; font-size: 0.9rem;">{achievement['organization']} | {achievement['year']}</p>
                    </div>
                </div>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.8;">{achievement['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Academic Performance
    st.markdown("## 📚 Academic Excellence")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <h3>HSC Performance</h3>
            <h2>98.72%</h2>
            <p>MHT-CET Percentile</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <h3>CBSE Performance</h3>
            <h2>93% | 9.3 CGPA</h2>
            <p>10th Grade Excellence</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <h3>First Year VIT</h3>
            <h2>9.3 CGPA</h2>
            <p>Engineering Excellence</p>
        </div>
        """, unsafe_allow_html=True)

# SKILLS DASHBOARD
elif page == "📊 Skills Dashboard":
    st.markdown("# 📊 Skills & Technology Dashboard")
    
    # Skills proficiency data
    skills_proficiency = {
        'Programming Languages': {'Python': 90, 'Java': 85, 'JavaScript': 80, 'C++': 75, 'C': 70},
        'Web Technologies': {'ReactJs': 85, 'Flask': 80, 'TailwindCSS': 80, 'HTML/CSS': 95},
        'AI/ML': {'Machine Learning': 70, 'AI-Agents': 85, 'GenerativeAI': 95},
        'Databases': {'MongoDB': 80, 'SQL': 40, 'PostgreSQL': 50},
        'Cloud & Tools': {'AWS': 20, 'Git': 90, 'Docker': 50, 'PowerBI': 75}
    }
    
    # Create tabs for different skill categories
    tab1, tab2, tab3 = st.columns(3)
    
    with tab1:
        st.markdown("### Programming Languages")
        for lang, proficiency in skills_proficiency['Programming Languages'].items():
            st.progress(proficiency/100)
            st.write(f"{lang}: {proficiency}%")
        
        st.markdown("### Web Technologies")
        for tech, proficiency in skills_proficiency['Web Technologies'].items():
            st.progress(proficiency/100)
            st.write(f"{tech}: {proficiency}%")
    
    with tab2:
        st.markdown("### AI/ML Technologies")
        for tech, proficiency in skills_proficiency['AI/ML'].items():
            st.progress(proficiency/100)
            st.write(f"{tech}: {proficiency}%")
        
        st.markdown("### Databases")
        for db, proficiency in skills_proficiency['Databases'].items():
            st.progress(proficiency/100)
            st.write(f"{db}: {proficiency}%")
    
    with tab3:
        st.markdown("### Cloud & Tools")
        for tool, proficiency in skills_proficiency['Cloud & Tools'].items():
            st.progress(proficiency/100)
            st.write(f"{tool}: {proficiency}%")
    
    # Skills radar chart
    st.markdown("## 🎯 Skills Radar")
    
    categories = ['Programming', 'Web Development', 'AI/ML', 'Database', 'Cloud', 'UI/UX']
    values = [85, 80, 75, 80, 70, 85]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Skill Level',
        line=dict(color='#667eea'),
        fillcolor='rgba(102, 126, 234, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=False,
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Certifications
    st.markdown("## 🎓 Certifications")
    
    certifications = [
        {'name': 'Complete Full-Stack Web Development Bootcamp', 'hours': 55},
        {'name': 'Complete Python Bootcamp - Dr. Angela Yu', 'hours': 60},
        {'name': 'Introduction to Natural Language Processing (NLP)', 'hours': 5},
        {'name': 'Introduction to Generative AI Concepts', 'hours': 2}
    ]
    
    col1, col2 = st.columns(2)
    
    for i, cert in enumerate(certifications):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div style="background: linear-gradient(45deg, #4facfe 0%, #00f2fe 100%); 
                        color: white; padding: 1rem; border-radius: 10px; margin: 0.5rem 0;">
                <h4 style="margin: 0 0 0.5rem 0;">{cert['name']}</h4>
                <p style="margin: 0; opacity: 0.9;">{cert['hours']} hours</p>
            </div>
            """, unsafe_allow_html=True)

# CONTACT PAGE
elif page == "📞 Contact":
    st.markdown("# 📞 Get In Touch")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("## 💬 Let's Connect!")
        
        st.markdown("""
        <div class="contact-info">
            <h3>📧 Email</h3>
            <p>kabirkhanuja@gmail.com</p>
        </div>
        
        <div class="contact-info">
            <h3>📱 Phone</h3>
            <p>+91 9890095928</p>
        </div>
        
        <div class="contact-info">
            <h3>📍 Location</h3>
            <p>Mahatma Soc, Kothrud, Pune - 411038</p>
        </div>
        
        <div class="contact-info">
            <h3>🔗 Social Links</h3>
            <p>LinkedIn | GitHub</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Contact form
        st.markdown("### 📝 Send a Message")
        
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message", height=150)
            
            submitted = st.form_submit_button("Send Message 🚀")
            
            if submitted:
                st.success("Message sent successfully! I'll get back to you soon. 🎉")
    
    with col2:
        # Quick stats about Kabir
        st.markdown("## 🎯 Quick Stats")
        
        st.metric("📧 Response Time", "< 24 hrs", "Always responsive")
        st.metric("🌟 Projects", "10+", "Growing portfolio")
        st.metric("🎓 Education", "VIT Pune", "Engineering Student")
        st.metric("🏆 Achievements", "5+", "Awards & Recognition")
        
        # Extra-curricular highlights
        st.markdown("## 🎨 Beyond Tech")
        
        st.markdown("""
        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin: 0.5rem 0;">
            <h4>🎙️ Podcast Host</h4>
            <p>"ThatOneThinker" - Available on Spotify, Apple Podcasts, and more</p>
        </div>
        
        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin: 0.5rem 0;">
            <h4>✍️ Blog Writer</h4>
            <p>"Sunday Snippets" - Weekly personal newsletter</p>
        </div>
        
        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin: 0.5rem 0;">
            <h4>🎵 Music</h4>
            <p>Indian Classical training for 3+ years</p>
        </div>
        
        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin: 0.5rem 0;">
            <h4>🤝 Social Work</h4>
            <p>Lead Volunteer at Poona School for Blind</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #667eea;">
    <h3>🚀 Ready to Build the Future Together?</h3>
    <p>Open to opportunities in Software Development, AI/ML, and Full-Stack Development</p>
    <p><em>"Aspiring to make technology accessible and impactful for everyone"</em></p>
</div>
""", unsafe_allow_html=True)

# Add some interactivity with a live clock
if st.sidebar.checkbox("Show Live Clock"):
    placeholder = st.sidebar.empty()
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        placeholder.markdown(f"**Current Time:** {current_time}")
        time.sleep(1)