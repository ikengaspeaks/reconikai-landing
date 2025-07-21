import streamlit as st

# Page config
st.set_page_config(page_title="reconik.ai - Financial Processing Solutions",
                   page_icon="🏦",
                   layout="centered")

# Professional Monochrome Design System
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Global Styles */
    .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        background-color: #F8F9FA;
        color: #1F2937;
    }

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .main-header {
        color: #1F2937;
        font-size: 3rem;
        font-weight: 600;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -0.025em;
    }
    
    .subtitle {
        color: #6B7280;
        font-size: 1.3rem;
        font-weight: 400;
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .app-container {
        padding: 1.5rem;
        background-color: white;
        border-radius: 8px;
        margin-bottom: 1rem;
        border: 1px solid #E5E7EB;
        transition: all 0.15s ease;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    }
    
    .app-container:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .app-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1F2937;
        margin-bottom: 0.3rem;
    }
    
    .app-description {
        color: #6B7280;
        margin-bottom: 1rem;
        font-size: 0.875rem;
    }
    
    .disabled-container {
        opacity: 0.6;
        position: relative;
    }
    
    .coming-soon {
        position: absolute;
        top: 1rem;
        right: 1rem;
        background-color: #6B7280;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 500;
    }
    
    .launch-button {
        background-color: #4B5563;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 6px;
        text-decoration: none;
        display: inline-block;
        font-weight: 500;
        font-size: 0.875rem;
        letter-spacing: 0.025em;
        transition: all 0.15s ease;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
        border: none;
    }
    
    .launch-button:hover {
        background-color: #374151;
        color: white;
        text-decoration: none;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transform: translateY(-1px);
    }
    
    .footer {
        text-align: center;
        color: #6B7280;
        margin-top: 3rem;
        font-size: 0.875rem;
    }
</style>
""",
            unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">reconik.ai</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Financial Processing Solutions</p>',
            unsafe_allow_html=True)

# NIBSS Settlement - Active
with st.container():
    st.markdown("""
    <div class="app-container">
        <h3 class="app-title">NIBSS Settlement</h3>
        <p class="app-description">Process NIBSS transaction files and generate settlement reports for accounting system integration.</p>
        <a href="https://nibss.reconik.ai" class="launch-button" target="_self">Launch Application →</a>
    </div>
    """,
                unsafe_allow_html=True)

# File Processing - Coming Soon
with st.container():
    st.markdown("""
    <div class="app-container disabled-container">
        <span class="coming-soon">Coming Soon</span>
        <h3 class="app-title">File Processing</h3>
        <p class="app-description">Advanced file processing and transformation tools for various financial data formats.</p>
        <button class="launch-button" disabled style="opacity: 0.5; cursor: not-allowed; background-color: #6B7280;">Coming Soon</button>
    </div>
    """,
                unsafe_allow_html=True)

# NIBSS Reconciliation - Coming Soon
with st.container():
    st.markdown("""
    <div class="app-container disabled-container">
        <span class="coming-soon">Coming Soon</span>
        <h3 class="app-title">NIBSS Reconciliation</h3>
        <p class="app-description">Automated reconciliation and dispute management for NIBSS transactions.</p>
        <button class="launch-button" disabled style="opacity: 0.5; cursor: not-allowed; background-color: #6B7280;">Coming Soon</button>
    </div>
    """,
                unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2024 Reconikai. All rights reserved.</div>',
            unsafe_allow_html=True)
