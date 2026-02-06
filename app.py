import streamlit as st
from vxp.ui import init_state, route
from vxp.styles import XP_CSS

def main():
    st.set_page_config(page_title="VXP Simulator – BO105", layout="centered")
    init_state()

    # Layout general (toolbar a la izquierda, ventana a la derecha)
    st.markdown(XP_CSS, unsafe_allow_html=True)
    left, right = st.columns([0.20, 0.80], gap="small")

    with left:
        st.markdown("<div class='vxp-toolbar'>", unsafe_allow_html=True)
        st.markdown("<div class='vxp-label'>Toolbar</div>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:11px;'>Aquí puedes meter los botones laterales con icons.</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        route()

if __name__ == "__main__":
    main()
