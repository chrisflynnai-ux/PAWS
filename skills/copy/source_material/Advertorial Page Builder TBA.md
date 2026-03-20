# Simple Lander Builder — Agent Playbook

> **For the AI agent:** This is your complete operating guide. You have everything you need to build the landing page yourself — no CLI tools, no external scripts. Use whatever browser, fetch, screenshot, and file-writing capabilities your tool provides.

---

## What You're Building

A polished advertorial landing page that:
- Mirrors the layout and style of a **reference advertorial** the user provides
- Uses brand data (colors, fonts, images, ingredients, testimonials, pricing) scraped from a **brand website**
- Is formatted for either **Replo** or **Shopify Custom Liquid** — ready to paste and publish

---

## Your Role

You do everything. You are the scraper, the copywriter, and the builder. No terminal commands, no npm, no external tools. Fetch both URLs using whatever web access your tool supports, take screenshots if you can to understand the visual layout, extract what you need, generate the copy, and write the HTML files directly.

Be conversational and low-jargon. The user has managed to get their AI tool set up — that's all you can assume. Keep instructions simple. Confirm each step before moving to the next.

---

## Phase 1: Gather Inputs

Ask everything at once to avoid back-and-forth.

**Say to the user:**
> "Let's build your landing page. I need a few things from you:
>
> 1. **Reference advertorial URL** — a link to an advertorial whose layout and style you want to model (the look, not the content)
> 2. **Brand website URL** — the homepage or product page of the brand you're writing about
> 3. **CTA URL** — where all the buttons should link to (product page, cart link, etc. — leave blank to use the brand URL)
> 4. **Article length** — relative to the reference: `shorter`, `same`, or `longer`
> 5. **Publishing platform** — **Replo** (Replo page builder) or **Shopify** (Shopify's built-in Custom Liquid section)?
>
> Paste all five answers and I'll get started."

Confirm inputs back to the user before proceeding.

---

## Phase 2: Scrape the Reference Advertorial

Fetch the reference URL and analyze its structure. This gives you the layout blueprint. If your tool supports screenshots, take one of the full page — it's the fastest way to understand the visual layout before digging into the HTML.

**What to extract:**

- **Layout type:** Is it two-column (article + sidebar) or single column?
- **Section order:** List every section from top to bottom (top bar, header, breadcrumbs, headline, subtitle, meta line, author line, social share, hero image, warning box, body sections, stat callouts, ingredient grid, timeline, testimonials, CTA box, footer, etc.)
- **Color palette:** Background colors, heading colors, accent/button colors, text colors — pull from CSS custom properties (`--color-*`, `var(--*)`), inline styles, and `background-color` / `color` values in stylesheets
- **Typography:** Font family and weights from `font-family`, `font-weight` declarations on headings and body text
- **CSS patterns:** Border radius, box shadows, card styles, button shapes, spacing
- **Trust signals used:** View counts, social share buttons, star ratings, "Verified Buyer" labels, medical reviewer credits, warning boxes
- **CTA pattern:** How many CTAs, button text style, urgency language used

Store everything you find as working notes. You'll apply this blueprint to the brand data in Phase 5.

---

## Phase 3: Scrape the Brand Website

Fetch the brand URL and extract all usable data. This is your raw material. Take a screenshot if you can — it helps identify the hero image, product shots, and color palette at a glance.

**Colors**
Look for CSS custom properties (`--color-*`, `--primary-*`, `--accent-*`), computed styles on major elements (hero sections, buttons, headers, footers). Identify:
- Primary dark color (backgrounds, headings)
- Accent color 1 (buttons, highlights, links)
- Accent color 2 (secondary callouts, numbers)
- Background light color (cards, article background)

**Fonts**
Look for `font-family` declarations on headings and body text. Check if the font is a Google Font — if so, construct the Google Fonts URL. If self-hosted, note the font name.

**Images — Find Every One You Can**

Images are critical to the finished page. Be thorough. Check all of these sources:

1. `<img>` tags — collect every `src` attribute
2. `<picture>` and `<source>` tags — collect `srcset` values (use the largest resolution)
3. CSS `background-image: url(...)` — extract the URL from any hero, banner, or section with a background image
4. `<meta property="og:image">` — the Open Graph image is almost always the hero/product image and a reliable fallback
5. Inline `style="background-image: url(...)"` attributes on div elements

**Handle framework-specific URL formats:**
- **Next.js:** Images appear as `/_next/image?url=%2Fsome%2Fpath.jpg&w=1920&q=75` — decode the `url` parameter and prepend the domain: `https://brand.com/some/path.jpg`
- **Shopify CDN:** URLs like `cdn.shopify.com/s/files/...` — use as-is
- **imgix / Cloudflare Images:** Strip query parameters to get the base image URL, or use as-is if the URL resolves

**Classify every image you find** — label each one so you know where to use it:

| Label | What to look for |
|-------|-----------------|
| `hero` | Large lifestyle or product-in-use image, usually above the fold |
| `product` | Clean product shot (bottle, bag, box) on white or minimal background |
| `graph` | A chart, graph, or infographic showing data or results |
| `ingredients` | Ingredient panel or supplement facts image |
| `headshot` | Expert or doctor photo |
| `logo` | Brand logo (don't use as publication logo — create a text-based fictional publication name instead) |

**You must identify at minimum:**
- ✅ 1 hero image (goes at the top of the article)
- ✅ 1 product image (goes in the CTA box and sidebar)

If you cannot find a hero image, use the product image in both places. If you cannot find any usable images from the HTML, tell the user:

> "I wasn't able to pull images automatically from this site — it may load them via JavaScript. Can you paste 1–2 image URLs directly? Right-click any image on the brand site → 'Copy image address' and paste it here."

**Product data**
Scrape visible text for: product name, current price, original price, quantity/count, flavor, guarantee (money-back policy), shipping info, company name and address.

**Ingredients**
Find any ingredient list — name, dose/amount, benefit. These go in the ingredient grid section.

**Testimonials**
Find customer reviews — quote text, reviewer name, star rating. Use real quotes only. Do not fabricate.

**Experts / Medical reviewers**
Find any named experts, doctors, or advisors with credentials — name, title, institution. Used for credibility stack and medical reviewer byline.

**Unique brand elements**
Results timelines, progress trackers, milestone names, any distinctive marketing copy or gamification.

Once scraped, summarize what you found — **always list the image URLs explicitly** so the user can verify them:

**Say to the user:**
> "Here's what I pulled from the brand site:
>
> **Images found:**
> - Hero: [full URL or 'not found']
> - Product: [full URL or 'not found']
> - Graph: [full URL or 'not found']
> - Other: [any additional URLs]
>
> **Brand data:**
> - Colors: [primary], [accent1], [accent2]
> - Font: [font name]
> - Ingredients: [N] found
> - Testimonials: [N] found
> - Experts: [names if any]
> - Price: [price], Guarantee: [guarantee]
>
> Do the image URLs look right? If any are missing or wrong, paste the correct ones now. Otherwise I'll move on to the copy."

Wait for the user to confirm images before proceeding. This is the easiest point for them to fix any gaps.

---

## Phase 4: Copy — Two Paths

**Say to the user:**
> "Now for the words. Two options:
>
> **Option A — You have copy:** Paste in your headline, subheadline, or as much of the article as you've written. Even just a headline and a rough angle is enough — I'll build the rest around it.
>
> **Option B — AI writes it:** I'll write the full advertorial from the brand data. You can review and change anything before I build.
>
> Which would you prefer?"

---

### Path A: User-Provided Copy

**Say to the user:**
> "Paste whatever you have. At minimum give me:
> - **Headline** (the big H1)
> - **Subheadline** (the italic line underneath)
>
> Optional extras:
> - Publication name (the fictional editorial brand — e.g. 'Men's Vitality Reset')
> - Warning box text
> - Body copy, section headings, key points, angle
> - CTA button text"

Use their exact wording for fields they provide. Generate everything else from the scraped brand data. Follow the narrative arc below for any sections they haven't provided.

---

### Path B: AI-Generated Copy

Using the scraped brand data, write the full advertorial following the **13-beat narrative arc**:

| Beat | Name | What to Write |
|------|------|---------------|
| 1 | Hook | Personal, conversational opening. "I'm going to be honest with you." |
| 2 | Skeptic Setup | Writer was skeptical about this product category. |
| 3 | The Data | A shocking statistic with a source citation. |
| 4 | Stat Callout | Visual callout with the big number. |
| 5 | Problem Expansion | Why this matters beyond the obvious. |
| 6 | Emotional Hook | Relatable, personal — make the reader feel it. |
| 7 | Product Introduction | Transition from problem to solution. Name the product. |
| 8 | Credibility Stack | Medical experts, credentials, formulation details from scraped expert data. |
| 9 | Ingredient Breakdown | Use scraped ingredients — name, dose, benefit for each. |
| 10 | Timeline / Results | Scraped milestones, or plausible ones if none found. |
| 11 | Social Proof | Real scraped testimonials only. Do not fabricate. |
| 12 | Bottom Line | Acknowledge any quirks, reaffirm the science. |
| 13 | CTA | Scraped price, guarantee, urgency, button. |

**Copy rules:**
- `publicationName`: Fictional editorial name matching the niche — never the brand name
- `authorName`: Fictional journalist matching the niche
- `medicalReviewer`: Real expert from scraped data, or omit
- `viewCount`: A number like "184,291" — in the 100k–500k range
- Paragraphs: 1–3 sentences max, short and punchy
- Tone: Conversational, first-person, authoritative but not clinical
- Never fabricate testimonials, ingredients, prices, or credentials

---

### Review Step (Both Paths)

Before building, show the user a plain-English summary:

**Say to the user:**
> "Here's what I have for the page:
> - **Headline:** [headline]
> - **Subheadline:** [subtitle]
> - **Publication name:** [name]
> - **Author:** [name][, reviewed by [expert]]
> - **Sections:** [N] body sections
> - **Ingredients:** [N]
> - **Testimonials:** [N]
> - **CTA button:** "[text]" → [CTA URL]
>
> Want to change anything before I build? Or does this look good?"

Wait for sign-off.

---

## Phase 5: Build the HTML

Write a complete, self-contained HTML advertorial using:
- The **layout blueprint** from the reference (section order, two-column vs single column, CSS patterns)
- The **brand colors and fonts** from the brand scrape
- The **copy** from Phase 4
- The **confirmed image URLs** from Phase 3

### Image Placement — Required

Every image you confirmed in Phase 3 must appear in the HTML. Do not skip images. Place them as follows:

| Image | Where it goes |
|-------|--------------|
| `hero` | Full-width `<img>` at the top of the article body, before the warning box |
| `product` | Inside the CTA box (alongside price and button), AND in the sidebar product card if two-column |
| `graph` | Inline in the article body, placed after the stat callout or in the problem expansion section |
| `ingredients` | Inline in the article body, placed near or before the ingredient grid |
| `headshot` | Next to the expert's name in the credibility stack section |

Every image tag must use:
- The **full absolute URL** (e.g. `https://brand.com/Hero.png`) — never a relative path
- `loading="eager"` on the hero image, `loading="lazy"` on all others
- `style="max-width:100%; height:auto; display:block;"` if inline styles are being used

If an image URL was confirmed by the user but returns a 404, note it in a comment and leave a placeholder `<div>` with the same dimensions rather than a broken `<img>`.

### Layout Rules

Follow the reference advertorial's section order exactly. Common structure (adjust to match what you found in Phase 2):

```
Top navigation bar (dark background, uppercase category links)
Site header (fictional publication name + date + subscribe link)
Breadcrumbs (category badge + breadcrumb trail)
H1 headline (large, bold, with one phrase highlighted in accent color)
Subtitle (italic, below headline)
Meta line (date, read time, view count)
Author byline (written by + medically reviewed by)
Social share buttons (Facebook, X, Pinterest, WhatsApp, Email)
Hero image ← REQUIRED
Warning box (colored left-border callout)
Body copy (narrative arc, H2 section breaks)
Stat callout (large number on dark background)
Inline images (graph, ingredients) ← include if found
Ingredient grid (cards: name, dose, description)
Timeline (visual milestone progression)
Inline testimonials (star ratings + quotes)
Bottom line section
CTA box (dark gradient, product image ← REQUIRED, price, button, guarantee)
FDA disclaimer
[Sidebar if two-column: product card with product image ← REQUIRED, stat box, benefits list, testimonials, offer card]
Footer
```

### CSS Rules

- Use the reference advertorial's exact color values, border-radius, box-shadow, and spacing patterns as your baseline
- Replace only the brand-specific values: font family, accent colors, primary colors
- Keep the reference's card treatment, button shape, and layout proportions
- Build for responsive: single column below 900px

---

## Phase 6: Convert for Publishing Platform

Based on the platform chosen in Phase 1:

---

### If Replo — Apply All Conversion Rules

Transform the HTML into a Replo-compatible fragment:

**Rule 1 — Remove all document-level tags:**
Delete entirely: `<!DOCTYPE html>`, `<html>`, `</html>`, `<head>...</head>` (entire head block), `<body>`, `</body>`

**Rule 2 — Replace semantic structural tags with `<div>`:**
`<header>` → `<div>`, `<article>` → `<div>`, `<aside>` → `<div>`, `<footer>` → `<div>`, `<section>` → `<div>`, `<nav>` → `<div>`, `<main>` → `<div>`
Keep content tags as-is: `<h1>–<h6>`, `<p>`, `<a>`, `<img>`, `<ul>`, `<ol>`, `<li>`, `<span>`, `<em>`, `<strong>`, `<blockquote>`

**Rule 3 — Wrap everything in a single root `<div>`:**
```html
<div id="{cssPrefix}-advertorial">
  <style>...</style>
  <!-- all content -->
</div>
```
The root `<div>` must be the **very first element** in the file — no comments, no whitespace before it.

**Rule 4 — Nest `<style>` inside the root `<div>`:**
The `<style>` block is the first child inside the root div — not a sibling before it.

**Rule 5 — Load fonts via `@import` inside `<style>`:**
Replace any `<link href="fonts.googleapis.com...">` with:
```css
@import url('https://fonts.googleapis.com/css2?family=...');
```

**Rule 6 — Prefix all CSS class names:**
Every class gets a 2–4 character brand prefix derived from the brand name (e.g. `sw-` for Sperm Worms):
`.article` → `.sw-article`, `.sidebar` → `.sw-sidebar`, `.cta-btn` → `.sw-cta-btn`, etc.

**Rule 7 — Scope all CSS selectors with the root ID:**
```css
/* Wrong: */
.sw-article { }

/* Correct: */
#sw-advertorial .sw-article { }
#sw-advertorial .sw-article h1 { }
```
The root element's own styles use just the ID: `#sw-advertorial { font-family: ...; }`

**Rule 8 — Add a scoped CSS reset:**
```css
#sw-advertorial *,
#sw-advertorial *::before,
#sw-advertorial *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
#sw-advertorial img { max-width: 100%; height: auto; display: block; }
#sw-advertorial a { color: inherit; text-decoration: none; }
```

**Rule 9 — Convert emojis to HTML entities:**
Replace raw emoji with entities: ⭐ → `&#x2B50;`, ✅ → `&#x2705;`, → → `&#x2192;`, ★ → `&#x2605;`, © → `&#169;`

**Rule 10 — Add loading attributes to images:**
Hero image: `loading="eager"` — all others: `loading="lazy"`

**Rule 11 — Remove large HTML comments:**
Remove any comment blocks. Small inline comments like `<!-- CTA -->` are fine.

**Rule 12 — Verify tag balance:**
Count every `<div>` and `</div>` — they must match exactly. Fix any mismatch before delivering.

**Final validation checklist:**
- [ ] Zero forbidden tags: `<html>`, `<head>`, `<body>`, `<!DOCTYPE>`
- [ ] Root `<div>` is the first element in the file
- [ ] `<style>` is nested inside the root `<div>`
- [ ] Opening `<div>` count = closing `</div>` count
- [ ] File size under 256 KB
- [ ] All CSS selectors start with `#[rootId]`
- [ ] All CSS classes prefixed with `[cssPrefix]-`
- [ ] Google Fonts via `@import`, not `<link>`
- [ ] No semantic structural tags (`<header>`, `<article>`, `<aside>`, `<footer>`, etc.)
- [ ] All images use absolute URLs and appear in the HTML
- [ ] Hero image is present, product image is present

---

### If Shopify — Same Format, Different Instructions

Apply all the same Replo conversion rules above. The output format is identical — Shopify Custom Liquid accepts the same self-contained `<div>` fragment.

---

## Phase 7: Write the Output Files and Deliver

Create an `output/` folder if it doesn't exist. Save files using the brand name.

Write:
- `output/[brandname]-advertorial.html` — the full standalone HTML (for preview in a browser)
- `output/[brandname]-replo.html` — the converted fragment (for Replo or Shopify paste)

---

### If Replo:

**Say to the user:**
> "Done. Here's how to publish it in Replo:
>
> 1. Open your page in the Replo editor
> 2. Add a new element → **Custom HTML**
> 3. Open the file `output/[brandname]-replo.html`, select all, copy
> 4. Click into the Replo code editor → **Cmd+A** → **Cmd+V**
> 5. Save and preview
>
> If Replo shows a warning about 'Incorrect HTML tags', let me know and I'll fix it."

---

### If Shopify:

**Say to the user:**
> "Done. Here's how to publish it in Shopify:
>
> 1. Go to Shopify Admin → Online Store → Themes → click **Customize**
> 2. Navigate to the page you want the advertorial on (or create a new Page first under Shopify Admin → Pages)
> 3. In the left sidebar click **Add section** → search for **Custom Liquid** → select it
> 4. Open `output/[brandname]-replo.html`, select all, copy
> 5. Paste into the Custom Liquid code box
> 6. Click **Save** and preview"

---

## Troubleshooting

**Images didn't pull from the site**
Many modern brand sites load images via JavaScript (React, Next.js) so a standard fetch won't see them. If your tool has a browser/headless mode use that instead. Otherwise ask the user:
> "I wasn't able to grab images automatically. Can you right-click each image on the brand site, choose 'Copy image address', and paste the URLs here?"
Then embed those URLs directly in the HTML.

**Next.js image URLs returning broken images**
The raw `/_next/image?url=...` URL requires the right domain origin to resolve. Always decode the `url` parameter and reconstruct the full direct URL: `https://domain.com` + decoded path.

**Replo shows "Incorrect HTML tags detected"**
Search the Replo file for `<html`, `<head`, `<body`, `<!DOCTYPE`. Remove any matches. Also check that no HTML comments contain these words. Re-validate tag balance.

**Shopify Custom Liquid section not showing on page**
In the Theme Editor left sidebar, confirm the Custom Liquid section toggle is switched on. If the section was added to the wrong page template, navigate to the correct page and add it there.

**Images loading correctly in standalone but broken in Replo/Shopify**
The images are hotlinked to the brand's domain. If the brand site is on a different CDN or blocks hotlinking, images will fail. Fix: ask the user to download the images and upload them to Shopify Admin → Content → Files, then swap in the Shopify CDN URLs.

**File is over 256 KB**
Remove any base64-encoded images (replace with absolute URLs), tighten whitespace, and trim duplicate CSS. A well-built advertorial should be well under 50 KB.
