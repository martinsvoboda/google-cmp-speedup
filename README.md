# Google Consent Management Platform Speedup

This package optimize loading and rendering Google Consent tool. Standard implementation provided by Google has several flaws affecting
website speed. This simple CSS file fixes following issues:

- [x] Prevent Cumulative Layout Shift by font/icons swap
- [x] Use default website font. Don't download Open Sans font (saves 43 kB)
- [x] Use only subset of Material icons. Include icons inside CSS in order to fast loading (saves 129 kB)
- [ ] Don't download font specification (saves 4 kB)

## Usage

Just copy simple override `./dist/cmp.dist.css` to your project CSS:

```css
/* Prevent font swap use default website font */
body div.fc-consent-root {
    font-family: inherit !important;
}

body .fc-consent-root .fc-faq-header .fc-faq-label {
    font-family: inherit !important;
}

/* Override Material Icons with defined subset */
body .fc-consent-root i.material-icons {
    font-family: "Material Icons Subset" !important;
    overflow: hidden !important;
}

/* Load only subset of Material icons */
@font-face {
  font-family: 'Material Icons Subset';
  font-style: normal;
  font-weight: 400;
  font-display: block;
  src: url(data:font/woff2;base64,d09GMgABAAAAAAOsAA8AAAAACcgAAANYAAEEWgAAAAAAAAAAAAAAAAAAAAAAAAAAGhwbEByBdAZgAHQIBBEICod8hEUBNgIkA1oLWgAEIAWCegcgG7IGoB6DbXvpfJwkSZLa9peOeP5jv3bu23VEp5PFQ6F5tUiHRCgsWTw0qIHG0CyTvw+fZ72f/CJpPSiAFZmBmO66s1eQJ/gG8iz0v0D/4L8/NdkP8AdsA0YwQjkPSHbnAprrfHIxRtVYxwKdXIKCctFrWOHqnCqLusynF6xU4kcjYBxAYRA+hF8Eg4AhJTWAgCG7KHIhVJVAjgINBOSyKD8XchAQFAUhRxwgpRfV32wN1iGoIJ6NjZmbgoqSWjqCCpDRckmlpmVHUCEKHhZKJhoKRmY2WgQVoaRlYKFg5uRgkMqU5MJUyMboIkHTwcQh1TK86bqflLYcuEBFSilyU/pRbGiBPEICOSQ5gB33H/hnsgiKpAUAMg0AACPtv/8GoAACABZEQIEWmMciYB41H8zTYlE9zNPwNevV0XeX3934uOvjX8C6eQTyPf/fcuD/fvsVe405yzzTsMgQB4FflJkMBqSBAiwDTsEWeAN/gD6AjAhrLu1aQyYo1ao4KS+Hm7rmcOLSTCVRZRIe025WAqNXnk+uIiSxWpEBBWUUEb9foUJu51Fw6rTQ5FxbPzUy5UHbvWswnsSNb9Nb4s3k7cS95F2YSOJ+co+4t21/4gntYnRgeH149/4X9rmISvfaHqSTd8XUF3JPvJu8n5hCFAB6/Q1vgbuvq6asKjjHneLucac5kbvqJq5waeEv9/tHdtgX3XKdGMG++TCtqX22z9xnVoWw+6wVWz4TBLz47T9K98ncf2p/86fht4bqh+qeUPHk9ClOpYEalCUv/Wv9a1oRT6/4Iz2WH4awoX1LF7VujXuNLuxR/1iRlbWVieYjTU2qcw8i4Qjg+gFpz2y8PGDyPE3vr3KOAfDxvrUbwOfircv//3mEYQF9DCBQgJIEASBg+BQwg3zuOTgimiKCgOVshhFQIAjYFgfQMxOLtDnAGYQKYTVfYag1KayJkstUokiYPX0VqbBvBilVpl6FfLnyVHHqqL0OunMaplSpXEWyRTmNUCJTnNMARYo4TTwWqfxxs90eslWokS1L3BiCKqKeT1BUoj9TqRKV4lKuarIuqDCUjFS5eoVc2Rfx4gs59Zy+kCkY7iKmk9j1Kz1MFVcq5YsqTh2KBXfQbTpzhdilKljQa4aOAA==) format('woff2');
}

```

## Regenerate dist files

Dist files can be generated by python script generate.py:

    poetry run python ./generate.py
