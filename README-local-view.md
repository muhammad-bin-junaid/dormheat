# Quick instructions to view your Dormheat store locally

## Option 1: Python simple server (recommended)

1. Open a terminal/command prompt in the folder containing these files
2. Run:
   ```bash
   python3 -m http.server 8000
   ```
   (or `python -m http.server 8000` on Windows)
3. Open your browser to: http://localhost:8000

## Option 2: Open directly in browser

Some browsers block local file access for security. If `file://` doesn't work, use Option 1.

## What to expect

The theme was designed for Shopify and tries to load some assets from Shopify's CDN. Even with local paths fixed, some JavaScript may fail (that's OK - the visible content should still render).

If you see a blank orange screen:
- The orange is the theme's default background color
- The content may not be rendering due to JavaScript errors
- Check the browser console (F12) for errors

## Files modified for local viewing

- index.html - main homepage
- cart.html - shopping cart
- collections.1.html - product collections
- blogs/news.html - blog listing
- Blog post files in blogs/news/

Image/font URLs have been changed from `dormheat.myshopify.com/cdn/` to `/cdn/` to use local files.

## To change more text

Edit the HTML files directly. Look for:
- `<h1`, `<h2`, `<h3` tags - headings
- `<p>` tags - paragraphs
- `<span>` with menu text - navigation items
- `<title>` - page title

The text has already been changed to sound like a dorm room seller.
