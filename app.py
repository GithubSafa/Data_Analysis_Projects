from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Safa Jazi"
PAGE_ICON = ":wave:"
NAME = "Safa Jazi"
DESCRIPTION = """
Data Analyst | Data Detective | Data Scrubber | Data Visionist.
"""
EMAIL = "safadataanalyst@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/safa-jazi-4a80b5203/",
    "GitHub": "https://github.com/GithubSafa",
    "Tableau": "https://public.tableau.com/app/profile/safa8111",
}
PROJECTS = {
    "🏆 Airbnb Dashboard ": "https://public.tableau.com/app/profile/safa8111/viz/Airbnb_16647150027990/Tableaudebord1",
    "🏆 Web Scraping -Using Python": "https://github.com/GithubSafa/Web_Scraping_Project",
    "🏆 Desktop Application - Face recognition attendance app-Using OpenCv": "https://github.com/GithubSafa/final_year_project",
    "🏆 Netflix Dashboard": "https://github.com/GithubSafa/Data_Analysis_Projects",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Good knowledge of data visualization tools
- ✔️ Good knowledge of data analysis tools
- ✔️ Good understanding of machine leraning concepts and their respective applications 
- ✔️ Certified HCIA IA
- ✔️ Good team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, R
- 📊 Data Visulization: MS Excel, Tableau, Panel, Hvplot
- 📚 Modeling: Logistic regression, linear regression, Random Forest, CNN
- 🗄️ Languages: Arabic(Native Speaker) | French(B2,fluent=True) | English(B2,Fluent=True)
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", " Data Analyst | CloudiaSys")
st.write("04/2022 - Present")
st.write(
    """
- ► Used Excel and SQL to interpret complex and large data sets and blend disparate data sets into digestible formats to answer key business questions
- ► Collect, track and mine data from multiple sources and identify outliers and anomalies in contrived data sets.
- ► Used Tableau to support my organization's lines of business to deliver valuable insights from data
- ► Collaborate with key partners to understand requirements and improve opportunities to drive knowledge into action
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "Machine Learning specialist | TiM")
st.write("07/2021 - 09/2021")
st.write(
    """
- ► Explore the data and choose the type of algorithm
- ► Prepare and clean the dataset.
- ► Perform machine learning optimisation
- ► Deploy the model |the chatbot application
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "Web Developer | INNIR")
st.write("07/2020 - 09/2020")
st.write(
    """
- ► Create and improve web-based systems
- ► Discover "Angular" and "Laravel" frameworks
- ► Concept and realise a hiking website
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")