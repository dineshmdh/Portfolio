import json
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie_animation(file_path: str):
    """Load a Lottie animation from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)
    
# use local css
def local_css(file_path: str):
    """Load local CSS file."""
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)    

local_css("style/style.css")

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
st.write("[Google Scholar](https://scholar.google.com/citations?user=0gJS7AMAAAAJ&hl=en&authuser=1) | [LinkedIn](https://www.linkedin.com/in/dinesh-manandhar/)")

# Display highlighted intro text with custom CSS
intro_text = '''
Hi, I'm Dinesh. 👋<br><br>
I am a <b> Bioinformatics and Computational Biology Scientist </b> with a passion for leveraging data to drive insights in biomedical research.
I enjoy tackling challenges at the forefront of biomedical research and driving innovation through integrative, 
state-of-the-art analytical approaches. I have over 12 years of research experience, including close to 7 years of 
post-PhD industry experience engaging across numerous cross-functional collaborations - particularly within 
immuno-oncology drug development space in the last 4 years. In this time, I have contributed across numerous projects 
both as an individual contributor but also as an <b> in silico lead scientist</b>.<br><br>
My expertise lies in the integration of <b>multi-omics data, statistical modeling, and machine learning to identify and validate novel 
therapeutic targets, biomarkers, and drug indications</b>. My projects have spanned multiple facets 
of <b> drug development lifecycle, including target discovery, triaging and validation efforts, deep dives on mechanistic 
understanding of drugs and drug associated safety landscape</b>, as well as translational investigation, including 
<b>biomarker discovery, and drug indication mapping</b> analyses. In process, I have garnered expertise and mentorship 
experience in investigating genomic, transcriptomic, epigenomic data probing target-drug-indication associations 
and drug treatment effects using state of the art methods, statistical modeling and machine learning applications. 
I also enjoy mentoring students and peers in analytical techniques and deliverables.<br><br>
Below, I have highlighted some of my projects I led and technical skills. For more details, please connect with me directly.<br><br>
Thank you.
'''
st.markdown(f'<div class="highlighted-intro">{intro_text}</div>', unsafe_allow_html=True)

st.write("---")

# --- PROJECTS--- 
# st.write("""
#     Some of my recent project involvements include: 
#     - Enhancing T cell therapy with functional genomics screen (Patent Pending)
#     - De novo Tumor Myeloid Surface Target Discovery
#     - M. Tb. mRNA vaccine epitope assessment (Patent Published)
#     - Building Single-cell Atlas and Cell type Deconvolution Tools
#     I will go through these in detail in the projects section below.
#          """)



with st.container():
    st.subheader("Project 1: CRISPR-Guided Discovery of Knockouts Enhancing T Cell Persistence and Functionality (Patent and Publication Pending)")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("Images/genhancer_image_bing.jpeg")
    with text_column:
        project1_desc = '''
        <div class="projectx-box">
        <h4>Rationale</h4>
        <p>Adoptive T cell therapies are transforming oncology, but their success against solid tumors is limited by poor persistence, exhaustion, and a hostile tumor microenvironment. To systematically identify genetic barriers to durable T cell function, we implemented a high-throughput CRISPR-based loss-of-function screening platform across multiple model systems.</p>
        <h4>Screening & Analytics</h4>
        <p>Using pooled CRISPR/Cas9 knockout libraries curated for relevance to T cell biology, we screened both CD3/CD28-stimulated primary T cells and tumor antigen specific TCR-T cells. Phenotypic readouts included proliferation, stemness, and durability. In silico analysis with MAGeCK quantified guide enrichment and identified candidate hits across donors and models.</p>
        <h4>Key Discoveries</h4>
        <ul>
        <li>Gene target aliased as <b> GenT01</b> emerged as the strongest enhancer of stemness, expansion, and memory-like phenotypes when inactivated.</li>
        <li><b>GenT07</b> and <b>GenT10</b> promoted metabolic fitness, cytokine secretion, and sustained tumor-killing capacity.</li>
        </ul>
        <h4>🌟 Novelty of Dual Editing</h4>
        <p>Dual knockouts (<b>GenT01/GenT07</b> or <b>GenT01/GenT10</b>) synergized by retaining the stemness benefit of GenT01 loss while incorporating the functional/metabolic gains of GenT07 or GenT10. This combinatorial editing markedly improved expansion, cytokine polyfunctionality, and tumor control in vitro and in vivo.</p>
        <h4>Translational Impact</h4>
        <p>In xenograft and syngeneic models, GenT01/GenT10 dual knockout T cells exhibited superior peripheral persistence, enhanced tumor infiltration, and significantly improved tumor control compared to unedited or single KO cells.</p>
        <h4>Significance</h4>
        <p>This work establishes a scalable screening and computational analysis pipeline for rationally prioritizing genetic modifications that enhance T cell therapies. The combination of functional genomics, in silico target discovery, and rigorous in vivo validation paves the way for integrating multiplex knockout strategies into next-generation adoptive T cell platforms.</p>
        </div>
        '''
        st.markdown(project1_desc, unsafe_allow_html=True)


st.write("---")




with st.container():
    st.subheader("Project 2: Measuring Epigenetic Barriers: Chromatin Reprogramming Levels in MyoD activation induced myogenic conversion")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("Images/myod_CRL.jpeg")
    with text_column:
        project2_desc = '''
        <div class="projectx-box">
        <h4>Problem & Setup</h4>
        <p>Human dermal fibroblasts were transdifferentiated by inducible MyoD. Genome-wide RNA-seq, DNase-seq, and MyoD ChIP-seq were generated in fibroblast, fibro-control, fibro-MyoD, and primary myoblasts to quantify how closely reprogrammed cells approach bona fide myoblasts.</p>
        <h4>Quantifying Chromatin Reprogramming (CRL)</h4>
        <p>The study introduces a chromatin reprogramming level (CRL) per differentially accessible DHS: the fraction of the fibroblast→myoblast accessibility difference achieved after MyoD induction (0 = not reprogrammed, 1 = fully reprogrammed). Distributions reveal a continuum, with higher median CRL for closing fibroblast-specific sites than for opening myoblast-specific sites.</p>
        <h4>Gene Expression Coupling (GRL)</h4>
        <p>An analogous gene reprogramming level (GRL) shows that promoter-proximal accessibility remodeling explains substantial variation in expression reprogramming (e.g., PCC ≈ 0.6 at TSS ±2 kb for myoblast-specific genes).</p>
        <h4>Epigenetic Memory</h4>
        <p>Fibroblast identity features persist in both chromatin accessibility and transcriptome of fibro-MyoD, consistent with partial reprogramming and lineage memory.</p>
        <h4>MyoD Binding Predicts Chromatin Opening</h4>
        <p>MyoD binds both pre-open and previously closed regions; MyoD occupancy in fibro-MyoD correlates with CRL at myoblast-specific DHS (Spearman 0.66) and classifies reprogrammed vs non-reprogrammed sites with AUC ≈ 0.96. Binding weakly predicts closing of fibroblast-specific sites.</p>
        <h4>Feature-Based Classification</h4>
        <p>Random Forest/Elastic Net models discriminate reprogrammed vs non-reprogrammed DHS using: (i) TF-motif features from PBM data (clustered over 140 TF families), (ii) pre-existing histone marks/CTCF/EZH2 in fibroblasts, and (iii) local DNase signal. Accuracies ≈81% (myoblast-specific) and ≈69% (fibroblast-specific).</p>
        <h4>Novel Predicted Drivers</h4>
        <p>Predictive features highlight MyoD/MRF E-box recognition plus cofactors (TCF3/E2A, MEIS1/PKNOX1) and SAND-domain factors (e.g., GMEB1/2, SP100/AIRE) at sites resistant to opening—suggesting candidate factors to boost conversion efficiency.</p>
        <h4>Marker Dynamics</h4>
        <p>Early myogenic markers reprogram robustly, whereas intermediate/late muscle genes and many myoblast-specific enhancers remain suboptimally remodeled.</p>
        <h4>Use Cases for Reprogramming & Epigenetics</h4>
        <ol>
        <li>Rational cocktail design: add MyoD cofactors/SAND proteins to target non-reprogrammed enhancers.</li>
        <li>CRISPRa/epigenome editing targeting: prioritize enhancers with low CRL near non-reprogrammed genes.</li>
        <li>QC/benchmarking: report CRL/GRL to quantify “distance to target fate.”</li>
        <li>Generalizable framework: apply CRL/GRL and feature-based classifiers to other conversions (e.g., fibroblast→neuron/hepatocyte) to diagnose chromatin bottlenecks.</li>
        </ol>
        </div>
        '''
        st.markdown(project2_desc, unsafe_allow_html=True)

# <h4>Statistical Rigor/QC</h4>
# <p>Peak calling via MACS2/IDR; GC-matched negatives mitigate motif GC-bias; null CRL from fibro-control supports significance (Wilcoxon P &lt; 10⁻²⁹³).</p>
        


st.write("---")






with st.container():
    st.subheader("Project 3: Clustering Temporal Transcriptomics - A Nonparametric Bayesian Approach")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("Images/DPGP_image_cropped.png")
    with text_column:
        project2_desc = '''
        <div class="projectx-box">
        <h4>Problem & Framing</h4>
        <p>Time-series transcriptomics needs clustering that (i) doesn’t pre-specify the expected cluster number <b>K</b> and (ii) respects temporal correlation. The paper introduces <b>DPGP</b>—a Dirichlet-process Gaussian-process mixture that jointly infers the number of clusters and smooth trajectory structure.</p>
        <h4>Generative Model</h4>
        <p>Each cluster is a GP over time with cluster-specific mean and covariance. A Dirichlet process prior (default <b>𝛼=1</b>) governs mixture weights, yielding variable-size clusters and automatic complexity control. Missing or irregularly spaced time points are naturally handled.</p>
        <h4>Inference & Summarization</h4>
        <p>Posterior sampling uses Neal’s Algorithm 8 (Gibbs for DP mixtures). Kernel hyperparameters are updated by Type-II ML (marginal likelihood maximization via L-BFGS) with burn-in and thinning. Results are summarized by a MAP partition and a posterior similarity matrix (PSM) to quantify cluster-membership uncertainty and enable stability-aware downstream analysis.</p>
        <h4>Validation on Simulations</h4>
        <p>Across &gt;1,100 simulated datasets spanning diverse <b>K</b>, length scales, signal/marginal variances, and even t-distributed noise, DPGP/fDPGP achieved higher ARI than hierarchical, k-means, BHC, Mclust, GIMM, and SplineCluster baselines.</p>
        <h4>Software & Reproducibility</h4>
        <p>Open-source implementation is available (<a href="https://github.com/PrincetonUniversity/DP_GP_cluster" target="_blank">GitHub</a>), facilitating adoption in routine RNA-seq/microarray time-course workflows.</p>
        <h4>🌟 Novelty (Why This Matters)</h4>
        <ul>
        <li>Unified nonparametric, time-aware clustering; no need to pre-set K.</li>
        <li>Uncertainty-aware outputs (PSM, credible bands) for robust biological interpretation.</li>
        <li>Kernelized flexibility to match biological dynamics; extensible to non-Gaussian processes.</li>
        <li>Practical scalability (fDPGP) without discarding temporal structure.</li>
        </ul>
        </div>
        '''
        st.markdown(project2_desc, unsafe_allow_html=True)
# <h4>Scalability Variant</h4>
# <p>A marginalized implementation (<b>fDPGP</b>) swaps cluster-level for gene-level marginal likelihoods, reducing matrix-inversion cost and enabling larger studies; it was used for real-data applications in the paper.</p>
        

st.write("---")



with st.container():
    st.subheader("Project 4: In silico epitope selection for M. tuberculosis mRNA vaccine (Patent: WO 2024/216214)")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("Images/ppe18_patent_rotated.png")
    with text_column:
        project4_desc = '''
        <div class="projectx-box">
        <h4>Key Offering</h4>
        <p>RNA constructs encoding chimeric proteins composed of multiple antigens, immunogenic variants, or selected fragments from <b>Mycobacterium tuberculosis</b>, designed for in vivo expression to stimulate protective immunity.</p>
        <h4>Vaccine Design & Epitope Strategy</h4>
        <p>While the publicly available abstract provides only the high-level notion of chimeric antigen-encoding RNA, the inventive leap inherent in the patent lies in how these antigenic components are chosen and arranged—especially through novel in silico workflows. These computational steps likely include:</p>
        <ul>
        <li><b>Epitope prediction:</b> Identifying both T-cell (CTL, HTL) and potentially B-cell epitopes derived from key Mtb proteins using immunoinformatic pipelines.</li>
        <li><b>Immunogenicity filtering:</b> Prioritizing epitopes for high-binding affinity to relevant human MHC alleles and minimal cross-reactivity or allergenicity.</li>
        <li><b>Chimeric design:</b> Algorithmically combining multiple epitope fragments—possibly linked with rational linkers and optimized order—for maximal antigen presentation.</li>
        <li><b>RNA sequence optimization:</b> Codon and RNA structural optimization for enhanced stability, translational efficiency, and expression in host cells.</li>
        <li><b>In silico validation:</b> Computational assessment of multi-epitope immunogenic potential and modeling of antigen presentation pathways or predicted immune responses.</li>
        </ul>
        <p>These computational components represent the core novelty—not merely a mix of antigens, but an in silico–driven rational design of an RNA vaccine specific for tuberculosis.</p>
        <h4>🌟 Novelty & Significance for Immunologists</h4>
        <ul>
        <li><b>Multi-antigen, epitope-level granularity:</b> By breaking down Mtb proteins into individual epitopes, the design ensures focused, relevant immune targeting rather than broad-spectrum antigenic noise.</li>
        <li><b>In silico groundwork:</b> The application of predictive bioinformatic tools to guide epitope selection and vaccine configuration reduces empirical trial-and-error—accelerating development and potentially improving effectiveness and safety.</li>
        <li><b>RNA platform advantage:</b> Leveraging RNA for intracellular expression allows proper antigen processing through both MHC-I and MHC-II pathways, enhancing both cytotoxic and helper T-cell responses.</li>
        <li><b>Immune-tailored design:</b> The patent presumably considers human immunogenetic diversity, using computational MHC-binding predictions to include epitopes with broad HLA coverage.</li>
        </ul>
        </div>
        '''
        st.markdown(project4_desc, unsafe_allow_html=True)


st.write("---")



with st.container():
    st.subheader("Project 5: Predicting Gene Expression across cell types based on GRN and cis-chromatin landscape")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("Images/methods_protocol_and_NNframework.png")
    with text_column:
        project5_desc = '''
        <div class="projectx-box">
        <h4>CPGex: Cross-Cell Type Gene Expression Prediction Framework</h4>
        <p>The computational framework, <b>CPGex</b>, is designed to predict gene expression across different cell and tissue types. This approach leverages chromatin accessibility data and transcription factor-target gene (TF-TG) interactions, providing a novel method for gene expression prediction without relying on gene expression data from the target cell type.</p>
        <h4>🔬 Computational Approach</h4>
        <ul>
            <li><b>Chromatin Accessibility:</b> Data from cis-regulatory regions near the transcription start site (TSS) of genes.</li>
            <li><b>Transcription Factor Expression:</b> Expression levels of transcription factors predicted to regulate the gene of interest.</li>
        </ul>
        <p>The model is trained using data from a diverse set of cell and tissue types, allowing it to generalize predictions to unseen cell types. This methodology is particularly advantageous when gene expression data for the target cell type is unavailable.</p>
        <h4>🌟 Novelty</h4>
        <p>The novelty of CPGex lies in its ability to predict gene expression across cell types using only chromatin accessibility and transcription factor expression data. This approach addresses the challenge of limited gene expression data in certain cell types, enabling researchers to infer gene activity in these contexts. By focusing on regulatory mechanisms, CPGex provides insights into gene regulation that are not solely dependent on gene expression levels.</p>
        <h4>🧬 Applications</h4>
        <ul>
            <li><b>Cross-Cell Type Gene Expression Prediction:</b> Inferring gene expression in cell types where direct measurements are not available.</li>
            <li><b>Understanding Gene Regulation:</b> Identifying key transcription factors and regulatory regions influencing gene expression.</li>
            <li><b>Epigenomic Studies:</b> Exploring the relationship between chromatin accessibility and gene activity across different cell types.</li>
        </ul>
        <h4>⚠️ Challenges</h4>
        <ul>
            <li><b>Data Availability:</b> The accuracy of predictions depends on the quality and comprehensiveness of chromatin accessibility and transcription factor expression data.</li>
            <li><b>Model Generalization:</b> Ensuring the model generalizes well to unseen cell types requires diverse and representative training data.</li>
            <li><b>Interpretability:</b> Understanding the specific contributions of different features to predictions remains a complex task.</li>
        </ul>
        </div>
        '''
        st.markdown(project5_desc, unsafe_allow_html=True)


st.write("---")



# --- SKILLS ---

st.subheader("Technical Skills")
skills_html = '''
<div class="skills-box">
    <ul>
        <li><b>Python</b> (Pandas, TensorFlow, Streamlit & Bioinformatics libraries)</li>
        <li><b>R</b> (tidyverse, ggplot2, Shiny)</li>
        <li><b>Bash</b> and <b>SLURM</b> for high-performance computing</li>
        <li><b>AWS</b> and <b>DNA-Nexus</b> for cloud computing</li>
        <li><b>SQL</b> for database management</li>
        <li><b>Data visualization and reporting</b> (Seaborn, Matplotlib, Plotly)</li>
        <li><b>Machine learning and statistical modeling</b> (Gaussian Processes, Random Forests, Neural Networks, Regression Models)</li>
        <li> Currently training myself in Agentic AI applications and LLM deployment</li>
    </ul>
</div>
'''
st.markdown(skills_html, unsafe_allow_html=True)




# * NGS or other data experience and expertise: Bulk / sc-RNA-seq, CITE-seq, bulk/sc-ATAC-seq, VDJ-seq, spectral-flow cytometry data, Flurospot, DNA-methylation, multi-modal integrative analysis. 
# * Programming expertise: Python (Pandas, TensorFlow), R, Bash, SLURM, AWS, DNA-Nexus, SQL

st.write("---")
st.subheader("Contact")
st.write("Email: dinesh.mdh01@gmail.com | Phone: +1 (571) 337-8235")

st.write("---")
st.html("<i>I have used free lottie animations, ChatGPT5 summarization and image creation to help me build this portfolio.</i>")