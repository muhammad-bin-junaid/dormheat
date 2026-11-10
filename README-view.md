# How to View Your Dormheat Store Locally

## Quick Start

1. Open terminal/command prompt in this folder
2. Run: `python3 serve.py` (or `python serve.py` on Windows)
3. Open browser to: http://localhost:8000

**Note:** Use `serve.py` instead of `python3 -m http.server` because it handles links like `/collections/all` that don't have `.html` extensions. The standard Python server would return 404 for those.

## What Works Locally

✅ **Images** - All product images from `/cdn/shop/files/` load locally
✅ **Fonts** - Roboto, Oswald, Instrument Sans fonts load locally  
✅ **Theme CSS/JS** - The theme's styles and web components load from local `/cdn/shop/t/11/assets/`
✅ **Text content** - All the rewritten text (headings, descriptions) is in the HTML

## What Won't Work Locally

❌ **Shopify features** - Cart, checkout, search, customer accounts need Shopify's servers
❌ **Some JavaScript** - External scripts from `cdn.shopify.com` won't load (cart sync, analytics, etc.)

## Troubleshooting

### If links show 404

Make sure you're using `python3 serve.py`, not `python3 -m http.server`. The custom server rewrites URLs like `/collections/all` to `/collections/all.html` automatically.

### If you see a blank orange screen

The orange background is the theme's default color. If content doesn't appear:

1. **Check browser console** (F12 → Console tab) for JavaScript errors
2. **The theme uses Shopify web components** - some may fail without Shopify's servers
3. **Content is built dynamically** by JavaScript that expects Shopify's API

## Alternative: Simplified View

The orange background is the theme's default color. If content doesn't appear:

1. **Check browser console** (F12 → Console tab) for JavaScript errors
2. **The theme uses Shopify web components** - some may fail without Shopify's servers
3. **Content is built dynamically** by JavaScript that expects Shopify's API

## Alternative: Simplified View

If the full theme doesn't render, you can still see the text content by viewing the HTML source or using a simpler HTML file.

## To Make It Fully Work

To see the complete store with all features working, you would need to:
1. Upload these files to a Shopify store (Online Store → Themes → Edit code)
2. Or use Shopify's theme preview feature

The files are ready for upload to Shopify - they've been rebranded to "Dormheat" and all text has been changed to sound like a dorm room seller.
