import os


def Print(value):
    print(f"{__file__} --- {value}")

os.system("python -m streamlit run website.py --server.port 7777")
Print("test")