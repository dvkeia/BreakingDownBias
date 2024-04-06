from taipy.gui import Markdown

text = "Welcome to our dashboard!"

home_md = Markdown("""
# Home

<|{text}|>
""")