import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.title("Keluarga Davin Wedding Invitation")

# Google Sheet CSV URL (replace gid if needed)
sheet_url = "https://docs.google.com/spreadsheets/d/1p7Xl_4KIONLbLHAAYtcayhYCWtLJhIztRM9MUYadDdU/export?format=csv&gid=152989060"

try:
    df = pd.read_csv(sheet_url)

    st.markdown("### Pilih Salah Satu Undangan untuk Disalin")

    selected_name = st.selectbox("Pilih nama:", df["Nama"])
    selected_row = df[df["Nama"] == selected_name].iloc[0]
    undangan_text = selected_row["Template WA"]

    # Escape for JavaScript
    escaped_text = (
        undangan_text.replace("\\", "\\\\")
        .replace("`", "\\`")
        .replace('"', '\\"')
        .replace("\n", "\\n")
    )

    # ✅ Button and delay logic all inside components.html
    components.html(
        f"""
        <div>
            <button id="copyButton" onclick="copyText()" style="display:none;margin-bottom:10px;">
                📋 Copy Undangan
            </button>
            <script>
                // Delay display for 1 second
                setTimeout(() => {{
                    document.getElementById("copyButton").style.display = "inline-block";
                }}, 1000);

                function copyText() {{
                    navigator.clipboard.writeText("{escaped_text}").then(function() {{
                        alert("✅ Teks berhasil di copy!");
                    }}, function(err) {{
                        alert("❌ Gagal meng-copy teks.");
                    }});
                }}
            </script>
        </div>
        """,
        height=60,
    )

    # Show message below
    # st.code(undangan_text, language="markdown")

except Exception as e:
    st.error(f"Error loading data from Google Sheets: {e}")
