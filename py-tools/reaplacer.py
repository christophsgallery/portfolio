# Read the image URLs from a text file
with open('image_urls.txt', 'r') as file:
    image_urls = [line.strip() for line in file.readlines()]

# HTML template
html_template = '''
<!-- Begin album single item -->
<div class="album-single-item">
    <img class="asi-img" src="{masonry_url}" alt="image">
    <!-- Begin item cover -->
    <div class="asi-cover">
        <a class="asi-link lg-trigger"
            href="{big_url}"
            data-exthumbnail="{thumb_url}">
        </a>
    </div>
    <!-- End item cover -->
</div>
<!-- End album single item -->
'''

# Generate HTML snippets for each image URL
snippets = []
for url in image_urls:
    snippet = html_template.format(masonry_url=url, big_url=url, thumb_url=url)
    snippets.append(snippet)

# Save the snippets to a text file
with open('divs.txt', 'w') as file:
    file.write('\n'.join(snippets))
