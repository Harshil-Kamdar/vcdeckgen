import os

def export_to_reveal(slides):
    html = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>VCDeckGen Reveal.js</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reveal.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reveal.min.js"></script>
</head>
<body>
<div class="reveal"><div class="slides">
"""
    for slide in slides:
        html += f"<section><h2>{slide['title']}</h2><p>{slide['content'].replace('\n', '<br>')}</p></section>"

    html += """
</div></div>
<script>
  Reveal.initialize();
</script>
</body>
</html>
"""
    with open("output/deck_reveal.html", "w", encoding="utf-8") as f:
        f.write(html)
