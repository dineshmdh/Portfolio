import json
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie_animation(file_path: str):
    """Load a Lottie animation from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)


network_animation = load_lottie_animation("Lottie files/NetworkBubble.json")

st.set_page_config(page_title="My Portfolio", page_icon="💼", layout="wide")

st_lottie = st_lottie(
    network_animation,
    speed=0.05,
    reverse=False,
    loop=True,
    quality="low",
    height=100, 
    width=100, 
    key=None,
)

st.subheader("Welcome to Dinesh's Portfolio!")

st.write("""
         Hi, I'm Dinesh. 👋
        
         I am a Bioinformatics and Computational Biology Scientist with a passion for leveraging data to drive insights in biomedical research.
         I enjoy tackling challenges at the forefront of biomedical research and driving innovation through integrative, 
         state-of-the-art analytical approaches. I have over 12 years of research experience, including close to 7 years of 
         post-PhD industry experience engaging across numerous cross-functional collaborations - particularly within 
         immuno-oncology drug development space in the last 4 years. In this time, I have contributed across numerous projects 
         both as an individual contributor but also as a lead in silico scientist. 

         My expertise lies in the integration of multi-omics data, statistical modeling, and machine learning to identify and validate novel therapeutic targets, biomarkers, and drug indications. My projects have spanned multiple facets 
         of drug development lifecycle, including target discovery, triaging and validation efforts, deep dives on mechanistic 
         understanding of drugs and drug associated safety landscape, as well as translational investigation, including 
         biomarker discovery, and drug indication expansion analyses. In process, I have garnered expertise and mentorship 
         experience in investigating genomic, transcriptomic, epigenomic data probing target-drug-indication associations 
         and drug treatment effects using state of the art methods, statistical modeling and machine learning applications.

        * NGS or other data experience and expertise: Bulk / sc-RNA-seq, CITE-seq, bulk/sc-ATAC-seq, VDJ-seq, spectral-flow cytometry data, Flurospot, DNA-methylation, multi-modal integrative analysis. 
        * Programming expertise: Python (Pandas, TensorFlow), R, Bash, SLURM, AWS, DNA-Nexus, SQL
        * [Google Scholar Page >] (https://scholar.google.com/citations?user=0gJS7AMAAAAJ&hl=en&authuser=1)
        * [Example Project >] (https://github.com/dineshmdh/predicting_gene_expression)
         """)
st.write("---")

# --- PROJECTS--- 
with st.container():
    st.subheader("Projects")
    st.write("""
        Some of my recent project involvements include: 
        - Enhancing T cell therapy with functional genomics screen (Patent Pending)
        - De novo Tumor Myeloid Surface Target Discovery
        - M. Tb. mRNA vaccine epitope assessment (Patent Published)
        - Building Single-cell Atlas and Cell type Deconvolution Tools
        - Integrative omics in Myogenic Cellular Remodeling and Statistical Modeling of Longitudinal Transcriptomics data (Published)
        I will go through these in detail in the projects section below.
             """)
    # --- PROJECT 1: Predicting Gene Expression ---
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("Images/methods_protocol_and_NNframework.png")
    with text_column:
        st.subheader("Project 1: Predicting Gene Expression across cell types based on GRN and cis-chromatin landscape ")
        st.write(
            """
            - Developed a deep learning model using TensorFlow to predict gene expression levels based on 
            Gene-regulatory network (GRN) and cis-chromatin accessibility data across multiple cell types.
            - Achieved high accuracy in predictions, demonstrating the potential of deep learning in genomics.
            - Published findings in a conference and shared the code on GitHub for community use.
            """
        )
        st.markdown("[View Project on GitHub >](https://github.com/dineshmdh/predicting_gene_expression/tree/master)")


st.write("---")
# --- SKILLS ---
st.subheader("Technical Skills")
st.write("""
        - Python (Pandas, TensorFlow, Streamlit & Bioinformatics libraries)
        - R (tidyverse, ggplot2, Shiny)
        - Bash and SLURM for high-performance computing
        - AWS and DNA-Nexus for cloud computing
        - SQL for database management
        - Data visualization and reporting (Seaborn, Matplotlib, Plotly)
        - Machine learning and statistical modeling (Gaussian Processes, Random Forests, Neural Networks, Regression Models)
         """)

st.subheader("Contact")
st.write("Email: dinesh.mdh01@gmail.com")
st.markdown("[LinkedIn >] (https://www.linkedin.com/in/dinesh-manandhar/)")
