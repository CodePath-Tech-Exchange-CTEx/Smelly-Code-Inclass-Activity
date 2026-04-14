import streamlit as st

if st.session_state.get("logged_in") is None:
    st.session_state["logged_in"] = False


def login():
    st.session_state.logged_in = True


def logout():
    st.session_state.logged_in = False


COMPANY_ADDRESS = "1600 Amphitheatre Parkway Mountain View, CA 94043"
COPYRIGHT_TEXT = "This site is copyright Fake Company LLC Inc., 2024"


def render_sidebar():
    if st.session_state.logged_in:
        st.sidebar.success("Logged in")
        st.sidebar.button("Log out", key="logout", on_click=logout)
    else:
        st.sidebar.warning("Not logged in")
        st.sidebar.button("Log in", key="login", on_click=login)

    st.sidebar.write(COPYRIGHT_TEXT)


def render_company_info():
    st.write(f"Fake Company LLC Inc. is located at {COMPANY_ADDRESS}")


def render_links():
    st.markdown(
        """
        [Google](https://google.com)

        [Gemini](https://gemini.google.com)

        [Streamlit Docs](https://docs.streamlit.io/)
        """
    )


st.set_page_config(page_title="Overview")

st.markdown("# Overview")
render_sidebar()

st.write(
    """Here is a page with a site overview.

    This site has one main page (app) and three pages (about, overview, and report).

    All of them have some redundant code that can be abstracted out to make changes easier in the future.
    """
)

with st.expander("Company Info"):
    render_company_info()

with st.expander("Links"):
    render_links()