# recipe_formatter.py

def format_recipe_html(recipe_content):
    # HTML template with styling
    full_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Generated Recipe</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }}
            h2 {{
                color: #2c3e50;
                border-bottom: 2px solid #3498db;
                padding-bottom: 10px;
            }}
            h3 {{
                color: #e74c3c;
            }}
            ul, ol {{
                padding-left: 20px;
            }}
            li {{
                margin-bottom: 10px;
            }}
            strong {{
                color: #2980b9;
            }}
        </style>
    </head>
    <body>
        {0}
    </body>
    </html>
    """
    return full_html.format(recipe_content)