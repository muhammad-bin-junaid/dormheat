# Dormheat Store - Local Viewing Ready

## To View Locally

1. Start the server:
   ```bash
   ./start-server.sh
   ```
   Or: `python3 -m http.server 8000`

2. Open browser to: **http://localhost:8000**

## What's Fixed

✅ **Images** - All 18 product/can images load from local `/cdn/shop/files/`
- product-01.jpg through product-16.jpg
- can_1.png, can-2_1.png, can-3_1.png, can-4_1.png
- GENPOP.svg (logo), GENPOP.png (banner)
- about-img.webp, banner images

✅ **Fonts** - 20 font files (Roboto, Oswald, Instrument Sans) load locally

✅ **CSS/JS** - Theme assets load from local `/cdn/shop/t/11/assets/`
- styles.css, xo-webcomponents.min.css
- main.js, xo-critical.min.js, xo-webcomponents.min.js

✅ **Text Content** - Rewritten to sound like a dorm room seller:
- "What I've Got" (Home products)
- "My Collection" (Collection)
- "About Me" (About)
- "My Posts" (Blog list)
- "My Favorite" (Featured product)
- "Item" (Product)
- Blog titles: "Why I'm Obsessed With Canned Food", etc.

✅ **Branding** - "XO Foodtech" → "Dormheat" everywhere

✅ **Languages** - Removed Vietnamese (vi) and Korean (ko), English only

## What Won't Work Locally

- Shopping cart functionality (needs Shopify servers)
- Checkout (needs Shopify)
- Search (needs Shopify)
- Customer accounts (needs Shopify)

These show as blank/errors but the visual storefront should render.

## Files Modified

- index.html - main homepage
- cart.html - shopping cart page  
- collections.1.html - all products collection
- blogs/news.html - blog listing
- blogs/news/*.html - individual blog posts
- All image/font paths cleaned of query parameters
