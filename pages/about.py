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


st.set_page_config(page_title="About")

st.markdown("# About")
render_sidebar()

st.markdown(
    """
    Fake Company LLC Inc. is a fake company created in 2024 for the purposes of making a website with a lot of redundant code.

    It produces nothing and has $0 a year in revenue.

    Usually, companies are not called both "LLC" and "Inc." and must choose one, but this is a fake company so it has both just to be funny.

    Here is a logo that I created with Gemini. It has too many "L"s.
    """
)

st.image("./assets/fake_company.png")

with st.expander("Company Info"):
    render_company_info()

with st.expander("Links"):
    render_links()