import streamlit as st

# Page config
st.set_page_config(
    page_title="Reconikai - Financial Processing Solutions",
    page_icon="🏦",
    layout="centered"
)

# Custom CSS to match the app style
st.markdown("""
<style>
    .stApp {
        background-color: #FFFFFF;
    }
    
    .main-header {
        color: #FF6B35;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        color: #666666;
        font-size: 1.3rem;
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .app-container {
        padding: 1.5rem;
        background-color: #F8F9FA;
        border-radius: 8px;
        margin-bottom: 1rem;
        border: 1px solid #E5E7EB;
        transition: all 0.3s ease;
    }
    
    .app-container:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    .app-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #333333;
        margin-bottom: 0.3rem;
    }
    
    .app-description {
        color: #666666;
        margin-bottom: 1rem;
    }
    
    .disabled-container {
        opacity: 0.6;
        position: relative;
    }
    
    .coming-soon {
        position: absolute;
        top: 1rem;
        right: 1rem;
        background-color: #666666;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 4px;
        font-size: 0.8rem;
    }
    
    .launch-button {
        background-color: #FF6B35;
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 5px;
        text-decoration: none;
        display: inline-block;
        transition: background-color 0.3s;
    }
    
    .launch-button:hover {
        background-color: #E55A2B;
        color: white;
        text-decoration: none;
    }
    
    .footer {
        text-align: center;
        color: #999999;
        margin-top: 3rem;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">Reconikai</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Financial Processing Solutions</p>', unsafe_allow_html=True)

# NIBSS Settlement - Active
with st.container():
    st.markdown("""
    <div class="app-container">
        <h3 class="app-title">NIBSS Settlement</h3>
        <p class="app-description">Process NIBSS transaction files and generate settlement reports for accounting system integration.</p>
        <a href="https://nibss.reconik.ai" class="launch-button" target="_self">Launch Application →</a>
    </div>
    """, unsafe_allow_html=True)

# File Processing - Coming Soon
with st.container():
    st.markdown("""
    <div class="app-container disabled-container">
        <span class="coming-soon">Coming Soon</span>
        <h3 class="app-title">File Processing</h3>
        <p class="app-description">Advanced file processing and transformation tools for various financial data formats.</p>
        <button class="launch-button" disabled style="opacity: 0.5; cursor: not-allowed;">Coming Soon</button>
    </div>
    """, unsafe_allow_html=True)

# NIBSS Reconciliation - Coming Soon
with st.container():
    st.markdown("""
    <div class="app-container disabled-container">
        <span class="coming-soon">Coming Soon</span>
        <h3 class="app-title">NIBSS Reconciliation</h3>
        <p class="app-description">Automated reconciliation and dispute management for NIBSS transactions.</p>
        <button class="launch-button" disabled style="opacity: 0.5; cursor: not-allowed;">Coming Soon</button>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2024 Reconikai. All rights reserved.</div>', unsafe_allow_html=True)