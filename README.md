# Google News Headline Analysis
Final project for UCSD's COGS 18 class, Introduction to Python.

This project analyzes of Google News headlines of the day. It collects headlines using the `requests` library and utilizes `BeautifulSoup` (from the `bs4` library) to parse HTML. Finally, it visualizes the most commonly occurring words using a bar graph (via the `matplotlib.pyplot` library) and wordclouds (via the `wordcloud` library).

Data visualization is done in the Jupyter Notebook, `ProjectNotebook.ipynb`, which uses functions in `my_module/functions.py` to parse and preprocess the headlines. You can view an example (using headlines from June 12, 2019) on the current notebook. Clone this repo and re-run the notebook to try out the data visualizations with the headlines of the day!
