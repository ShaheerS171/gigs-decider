import pandas as pd
import numpy as np

files = [
    "/home/shaheer/python/machine-learning/projects/statement-decider/api.csv",
    "/home/shaheer/python/machine-learning/projects/statement-decider/chatbot.csv",
    "/home/shaheer/python/machine-learning/projects/statement-decider/web.csv",
    "/home/shaheer/python/machine-learning/projects/statement-decider/webapp.csv",
    "/home/shaheer/python/machine-learning/projects/statement-decider/golang.csv"
]

merged_df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

merged_df.to_csv("/home/shaheer/python/machine-learning/projects/statement-decider/merged.csv", index=False)

print("✅ All files merged into merged.csv")