import streamlit as st
import pandas as pd

st.title("Mission Pharmacy Stock Search")

uploaded_file = st.file_uploader("Upload stock Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Read Excel (headers are in row 8)
    df = pd.read_excel(uploaded_file, header=7)

    st.success("File uploaded successfully")

    # -------------------------
    # Project selection
    # -------------------------
    project_options = ["Damazin", "Khartoum", "Port Sudan"]

    selected_project = st.selectbox(
        "Select project",
        project_options
    )

    # -------------------------
    # Search logic (Code + Description only)
    # -------------------------
    search = st.text_input("Search by Code or Description")

    if search:
        search = search.lower()
        filtered_df = df[
            df["Code"].astype(str).str.lower().str.contains(search)
            |
            df["Description"].astype(str).str.lower().str.contains(search)
        ]
    else:
        filtered_df = df

    # -------------------------
    # Display logic per project
    # -------------------------
    if selected_project == "Damazin":
        display_df = filtered_df.copy()

        display_df["Damazin - Project"] = display_df["Damazin.1"]
        display_df["Damazin - PZU"] = display_df["DMZ in PZU"]

        display_df["Damazin - TOTAL"] = (
            display_df["Damazin.1"].fillna(0)
            + display_df["DMZ in PZU"].fillna(0)
        )

        display_df["Damazin - Exp < 6m"] = display_df["DMZ EXP<6months"]

        display_columns = [
            "Code",
            "Description",
            "Damazin - Project",
            "Dama
