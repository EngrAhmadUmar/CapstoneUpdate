import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, upload  # import your app modules here

st.set_page_config(page_title="Cardiovascular Disease Prediction System", layout="wide")

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = [
    {"func": home.app, "title": "Home", "icon": "house"},
#     {"func": heatmap.app, "title": "Heatmap", "icon": "map"},
    {"func": upload.app, "title": "Upload for Prediction", "icon": "cloud-upload"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This web app is maintained by Ahmad Ahmed. You can follow me on social media:
            [GitHub](https://github.com/EngrAhmadUmar) | [Twitter](https://twitter.com/ahmadumar.66) | [LinkedIn](http://linkedin.com/in/ahmad-ahmed-a9a461175/).
        
        Source code: <https://github.com/EngrAhmadUmar/CapstoneUpdate>
    """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
