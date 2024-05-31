import os
import pandas as pd
import difflib
from datetime import datetime, timedelta
import re

def calculate_text_diff(text1, text2):
    d = difflib.Differ()
    diff = list(d.compare(text1.splitlines(), text2.splitlines()))
    added = [line[2:] for line in diff if line.startswith('+ ')]
    removed = [line[2:] for line in diff if line.startswith('- ')]
    abs_diff = len(added) + len(removed)
    rel_diff = abs_diff / (len(text1.splitlines()) + len(text2.splitlines())) * 2
    return abs_diff, rel_diff, '\n'.join(removed), '\n'.join(added)

def get_time_interval(date1, date2, interval):
    delta = date2 - date1
    if interval == "day":
        return "day"
    elif interval == "week":
        return "week"
    elif interval == "month":
        return "month"
    elif interval == "year":
        return "year"
    else:
        if delta.days < 7:
            return "day"
        elif delta.days < 30:
            return "week"
        elif delta.days < 365:
            return "month"
        else:
            return "year"

def process_csv(input_file, date_column, text_column, time_interval):
    df = pd.read_csv(input_file)
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.sort_values(by=date_column)

    results = []

    for i in range(len(df) - 1):
        text1 = df.iloc[i]["Text"]
        text2 = df.iloc[i + 1]["Text"]
        abs_diff, rel_diff, removed, added = calculate_text_diff(text1, text2)

        results.append({
            **df.iloc[i + 1].drop("Text").to_dict(),
            "Textdiff absolute value": abs_diff,
            "Textdiff relative value": rel_diff,
            "Time interval": time_interval,
            "Text removed": removed,
            "Text added": added
        })

    result_df = pd.DataFrame(results)
    output_file = f"output_{os.path.basename(input_file)}"
    result_df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

def process_markdown_files(base_path, time_interval):
    results = []

    for root, _, files in os.walk(base_path):
        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r') as file:
                    text = file.read()
                date_str = re.search(r'\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}Z', filename).group()
                date_formatted = datetime.strptime(date_str, "%Y-%m-%dT%H-%M-%SZ").strftime("%Y-%m-%d %H:%M:%S")

                # Extract platform, policy type, and policy name from the directory structure
                parts = root.split(os.sep)
                platform = parts[-3] if len(parts) >= 3 else 'n.a'
                policy_type = parts[-2] if len(parts) >= 2 else 'n.a'
                policy_name = parts[-1] if len(parts) >= 1 else 'n.a'

                results.append({
                    "Platform": platform,
                    "Policy type": policy_type,
                    "Policy name": policy_name,
                    "Date": date_formatted,
                    "Content": text
                })

    df = pd.DataFrame(results)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by="Date")

    output_results = []

    for i in range(len(df) - 1):
        text1 = df.iloc[i]["Content"]
        text2 = df.iloc[i + 1]["Content"]
        abs_diff, rel_diff, removed, added = calculate_text_diff(text1, text2)

        # Ensure the specified time interval is used
        time_diff = get_time_interval(df.iloc[i]['Date'], df.iloc[i + 1]['Date'], time_interval)

        output_results.append({
            **df.iloc[i + 1].drop("Content").to_dict(),
            "Textdiff absolute value": abs_diff,
            "Textdiff relative value": rel_diff,
            "Time interval": time_diff,
            "Text removed": removed,
            "Text added": added
        })

    result_df = pd.DataFrame(output_results)
    output_file = "output_markdown_files.csv"
    result_df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    # Directly specify your input CSV or markdown directory and parameters here
    input_type = "markdown"  # choose "markdown" or "csv" depending on what kind of policy files you want to process
    input_path = "path/to/your/file/or/folder/with/files"  # or "/path/to/your/Markdown_format"

    if input_type == "csv":
        date_column = "Date"  # Specify what the column with dates is called. 
        text_column = "Text"  # Specify what the column with text is called. 
        time_interval = "week"  # Choose if you're like the script to count text differences per day, week, month or year. 
        process_csv(input_path, date_column, text_column, time_interval)
    elif input_type == "markdown":
        time_interval = "week"  # Ensure the time interval is consistent
        process_markdown_files(input_path, time_interval)
