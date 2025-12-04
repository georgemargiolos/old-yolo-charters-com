# YOLO Charters - Detailed Style Guide

**Generated:** December 4, 2025  
**Purpose:** Complete style specifications for replicating yolo-charters.com design

---

## Color Palette

The website uses a cohesive color scheme centered around blues and neutrals, creating a nautical and professional appearance.

### Primary Colors

| Color Name | Hex Code | RGB | Usage |
|---|---|---|---|
| **Primary Blue (Dark)** | `#001c3d` | rgb(0, 28, 61) | Primary brand color, headers, navigation |
| **Primary Blue (Medium)** | `#003066` | rgb(0, 48, 102) | Secondary brand color, accents |
| **Accent Blue (Bright)** | `#0076FA` | rgb(0, 118, 250) | Call-to-action buttons, links, highlights |
| **Navy Blue** | `#142942` | rgb(20, 41, 66) | Text headings, dark sections |
| **Sky Blue** | `#87C4FF` | rgb(135, 196, 255) | Light accents, hover states |

### Neutral Colors

| Color Name | Hex Code | RGB | Usage |
|---|---|---|---|
| **White** | `#fff` | rgb(255, 255, 255) | Backgrounds, text on dark backgrounds |
| **Light Gray** | `#F1F5F9` | rgb(241, 245, 249) | Section backgrounds, borders |
| **Beige/Sand** | `#EDE1D2` | rgb(237, 225, 210) | Warm accent backgrounds |

### Utility Colors

| Color Name | Hex Code | Usage |
|---|---|---|---|
| **Success Green** | `#160` | Success messages, availability indicators |
| **Error Red** | `red` (inline) | Error messages, validation |

---

## Typography

### Font Stack

Based on the analysis, the website appears to use a **system font stack** or a custom font loaded via the main stylesheet (`dist/css/style.min.css`). No Google Fonts or external font services were detected in the HTML.

**Recommended Modern Font Stack:**
```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

### Heading Specifications

#### H1 - Main Page Title
- **Context:** Hero section, main page headings
- **Example:** "Sailing in Ionian Sea"
- **Estimated Specifications:**
  - Font Size: `48px - 64px` (responsive)
  - Font Weight: `700` (Bold)
  - Color: `#fff` (on hero) or `#001c3d` (on white background)
  - Line Height: `1.2`
  - Text Transform: None

#### H2 - Section Headings
- **Context:** Major section titles
- **Estimated Specifications:**
  - Font Size: `36px - 48px` (responsive)
  - Font Weight: `700` (Bold)
  - Color: `#001c3d` or `#142942`
  - Line Height: `1.3`
  - Margin Bottom: `24px`

#### H3 - Subsection Headings
- **Context:** Card titles, subsections
- **Example:** "Follow us", "Our Yachts"
- **Estimated Specifications:**
  - Font Size: `24px - 32px` (responsive)
  - Font Weight: `600` (Semi-bold)
  - Color: `#142942`
  - Line Height: `1.4`

#### H4 - Component Headings
- **Estimated Specifications:**
  - Font Size: `20px - 24px`
  - Font Weight: `600`
  - Color: `#001c3d`

### Body Text
- **Font Size:** `16px` (base)
- **Line Height:** `1.6`
- **Color:** `#333` or similar dark gray

### Links
- **Color:** `#0076FA`
- **Hover Color:** `#003066` or darker blue
- **Text Decoration:** None (underline on hover)

---

## Component Specifications

### Hero Section

**Class:** `.hero`

**Specifications:**
- **Background:** Full-width image with overlay
- **Height:** `500px - 700px` (responsive)
- **Text Color:** `#fff`
- **Overlay:** Dark gradient or semi-transparent overlay for text readability

**Hero Title (`.hero-title`):**
- **H1 Styling:**
  - Font Size: `48px - 64px`
  - Font Weight: `700`
  - Color: `#fff`
  - Text Shadow: Optional for readability

**Hero Subtitle (`.hero-title-subtitle`):**
- **Font Size:** `18px - 24px`
- **Font Weight:** `400`
- **Color:** `#fff` or `rgba(255, 255, 255, 0.9)`
- **Margin Top:** `16px`

---

### Search Form / Search Widget

**Class:** `.small-search`, `.small-search-wrapper`, `.small-search__form`

**Container Specifications:**
- **Background:** `#fff` or `rgba(255, 255, 255, 0.95)`
- **Border Radius:** `8px` or `12px`
- **Box Shadow:** `0 4px 20px rgba(0, 0, 0, 0.1)`
- **Padding:** `24px - 32px`
- **Max Width:** `900px - 1200px`

**Form Fields:**
- **Input Height:** `48px - 56px`
- **Border:** `1px solid #ddd` or `#e5e7eb`
- **Border Radius:** `4px - 8px`
- **Font Size:** `16px`
- **Padding:** `12px 16px`

**Select Dropdowns (Select2):**
- **Library:** Select2
- **Styling:** Custom themed to match brand colors
- **Height:** `48px - 56px`
- **Border:** `1px solid #ddd`

**Date Picker (Litepicker):**
- **Library:** Litepicker
- **Primary Color:** `#0076FA`
- **Selected Date Background:** `#0076FA`
- **Selected Date Text:** `#fff`

---

### Buttons

#### Primary Button (`.btn-primary`)
- **Background Color:** `#0076FA`
- **Text Color:** `#fff`
- **Font Size:** `16px`
- **Font Weight:** `600`
- **Padding:** `12px 32px`
- **Border Radius:** `4px - 8px`
- **Border:** None
- **Hover Background:** `#003066` or darker blue
- **Transition:** `all 0.3s ease`

#### Secondary Button (`.btn-secondary`)
- **Background Color:** `#142942` or `#003066`
- **Text Color:** `#fff`
- **Font Size:** `16px`
- **Font Weight:** `600`
- **Padding:** `12px 32px`
- **Border Radius:** `4px - 8px`
- **Hover Background:** Lighter shade

#### Search Button (`.btn-search`)
- **Background Color:** `#0076FA`
- **Text Color:** `#fff`
- **Font Size:** `16px - 18px`
- **Font Weight:** `700`
- **Padding:** `14px 40px`
- **Border Radius:** `8px`
- **Text Transform:** `uppercase`
- **Width:** `100%` (on mobile)

---

### Navigation / Header

**Class:** `.header`, `.header-wrapper`

**Specifications:**
- **Background Color:** `#fff` or transparent (on hero)
- **Height:** `70px - 90px`
- **Box Shadow:** `0 2px 8px rgba(0, 0, 0, 0.05)` (when scrolled)
- **Position:** `fixed` or `sticky`

**Logo (`.nav-logo`):**
- **Max Height:** `50px - 60px`

**Navigation Links (`.nav-link`):**
- **Font Size:** `16px`
- **Font Weight:** `500`
- **Color:** `#001c3d` or `#142942`
- **Padding:** `8px 16px`
- **Hover Color:** `#0076FA`
- **Active Color:** `#0076FA`

**Mobile Menu (`.hamburger`):**
- **Icon Color:** `#001c3d`
- **Size:** `24px x 24px`

---

### Cards / Yacht Cards

**Class:** `.card`, `.card-grid`

**Card Container:**
- **Background:** `#fff`
- **Border:** `1px solid #e5e7eb` or none
- **Border Radius:** `12px`
- **Box Shadow:** `0 2px 12px rgba(0, 0, 0, 0.08)`
- **Overflow:** `hidden`
- **Transition:** `transform 0.3s ease, box-shadow 0.3s ease`
- **Hover Transform:** `translateY(-4px)`
- **Hover Shadow:** `0 8px 24px rgba(0, 0, 0, 0.12)`

**Card Image (`.card-img`):**
- **Aspect Ratio:** `16:9` or `4:3`
- **Object Fit:** `cover`
- **Width:** `100%`

**Card Title (`.card-text-yacht-name`):**
- **Font Size:** `20px - 24px`
- **Font Weight:** `700`
- **Color:** `#001c3d`
- **Margin:** `12px 0 8px`

**Card Text (`.card-text`):**
- **Font Size:** `14px - 16px`
- **Color:** `#666` or `#6b7280`
- **Line Height:** `1.5`

---

### Footer

**Class:** `.footer`

**Specifications:**
- **Background Color:** `#001c3d` or `#142942`
- **Text Color:** `#fff` or `rgba(255, 255, 255, 0.8)`
- **Padding:** `60px 0 30px`

**Footer Headings:**
- **Font Size:** `18px - 20px`
- **Font Weight:** `700`
- **Color:** `#fff`
- **Margin Bottom:** `16px`

**Footer Links:**
- **Font Size:** `14px - 16px`
- **Color:** `rgba(255, 255, 255, 0.8)`
- **Hover Color:** `#fff` or `#87C4FF`

**Copyright (`.copyright`):**
- **Font Size:** `14px`
- **Color:** `rgba(255, 255, 255, 0.6)`
- **Border Top:** `1px solid rgba(255, 255, 255, 0.1)`
- **Padding Top:** `20px`
- **Margin Top:** `40px`

---

### Modal / Popup (Wishlist/Quote)

**Class:** `.custom-modal`, `.custom-modal-quote`

**Modal Container:**
- **Background:** `rgba(0, 0, 0, 0.5)` (overlay)
- **Z-Index:** `1000`

**Modal Content:**
- **Background:** `#fff`
- **Border Radius:** `12px`
- **Max Width:** `600px - 800px`
- **Box Shadow:** `0 10px 40px rgba(0, 0, 0, 0.2)`

**Modal Header (`.modal-header`):**
- **Background:** `#f8f9fa` or `#F1F5F9`
- **Padding:** `20px 24px`
- **Border Bottom:** `1px solid #e5e7eb`

**Modal Title (`.modal-title`):**
- **Font Size:** `24px`
- **Font Weight:** `700`
- **Color:** `#001c3d`

**Close Button (`.close-quote`):**
- **Color:** `#666`
- **Hover Color:** `#000`
- **Size:** `32px x 32px`

---

### Accordion (FAQ/Details)

**Class:** `.accordion`, `.accordion-item`

**Accordion Item:**
- **Border:** `1px solid #e5e7eb`
- **Border Radius:** `8px`
- **Margin Bottom:** `12px`

**Accordion Button (`.accordion-button`):**
- **Background:** `#f8f9fa`
- **Font Size:** `16px - 18px`
- **Font Weight:** `600`
- **Color:** `#001c3d`
- **Padding:** `16px 20px`
- **Hover Background:** `#e9ecef`

**Accordion Body (`.accordion-body`):**
- **Background:** `#fff`
- **Padding:** `20px`
- **Font Size:** `15px - 16px`
- **Color:** `#666`

---

## Layout & Grid

### Container

**Class:** `.custom-container`, `.container`

**Specifications:**
- **Max Width:** `1200px - 1400px`
- **Padding:** `0 15px` (mobile), `0 30px` (desktop)
- **Margin:** `0 auto`

### Grid System

The website uses a **Bootstrap-like grid system** with responsive columns:
- `.col-12` - Full width
- `.col-md-6` - Half width on medium screens
- `.col-lg-4` - One-third width on large screens
- `.col-xl-3` - One-quarter width on extra-large screens

---

## Responsive Breakpoints

Based on the CSS classes detected:

| Breakpoint | Size | Classes |
|---|---|---|
| **Small (sm)** | `576px` | `.col-sm-*`, `.d-sm-*` |
| **Medium (md)** | `768px` | `.col-md-*`, `.d-md-*` |
| **Large (lg)** | `992px` | `.col-lg-*`, `.d-lg-*` |
| **Extra Large (xl)** | `1200px` | `.col-xl-*`, `.d-xl-*` |

---

## Animations & Transitions

### Standard Transitions
```css
transition: all 0.3s ease;
```

### Hover Effects
- **Cards:** `transform: translateY(-4px)`
- **Buttons:** Background color change
- **Links:** Color change

### Scroll Progress Indicator

**Class:** `.scroll-progress`

- **Position:** `fixed`, bottom right
- **Background:** Circular with SVG arrow
- **Color:** `#0076FA`

---

## Image Specifications

### Hero Images
- **Format:** JPEG or WebP
- **Dimensions:** `1920px x 1080px` (minimum)
- **Optimization:** Compressed for web
- **Mobile Version:** Separate smaller image (`hero_home_mobile.jpeg`)

### Yacht Images
- **Aspect Ratio:** `16:9` or `4:3`
- **Dimensions:** `800px x 600px` (minimum)
- **Format:** JPEG or WebP

### Favicon
- **Sizes:** `16x16`, `32x32`, `192x192`
- **Format:** PNG

---

## Key CSS Classes Reference

### Utility Classes

| Class | Purpose |
|---|---|
| `.d-flex` | Display flex |
| `.d-none` | Display none |
| `.d-md-flex` | Display flex on medium screens |
| `.align-items-center` | Align items center |
| `.w-100` | Width 100% |
| `.color-light` | Light text color |
| `.color-primary` | Primary brand color |
| `.color-secondary` | Secondary brand color |

### Component Classes

| Class | Component |
|---|---|
| `.hero` | Hero section |
| `.small-search` | Search form container |
| `.card` | Card component |
| `.btn-primary` | Primary button |
| `.btn-secondary` | Secondary button |
| `.nav-link` | Navigation link |
| `.footer` | Footer section |

---

## Implementation Notes

### Required Libraries

To replicate the exact functionality, you must include:

1. **jQuery** - Core JavaScript library
2. **Litepicker** - Date range picker
3. **Select2** - Enhanced select dropdowns
4. **PhotoSwipe** - Image gallery/lightbox
5. **Magnific Popup** - Modal/popup dialogs
6. **jQuery UI** - UI components
7. **jQuery Bootpag** - Pagination

### CSS Files to Reference

1. `dist/css/style.min.css` - Main stylesheet (needs to be downloaded from live site)
2. `src/css/jquery-ui.min.css`
3. `src/css/select2.min.css`
4. `src/css/photo-swipe.min.css`
5. `src/css/magnific-popup.min.css`

### JavaScript Files to Reference

1. `src/js/jquery.min.js`
2. `src/js/litepicker.js`
3. `src/js/mobilefriendly.js`
4. `dist/js/plugins.min.js`
5. `dist/js/custom.min.js`

---

## Next Steps for Replication

1. **Download the main stylesheet** (`dist/css/style.min.css`) from the live website to get exact font specifications and additional styling details
2. **Download custom JavaScript** (`dist/js/custom.min.js`) to understand initialization and custom functionality
3. **Set up the same library versions** as documented in this guide
4. **Implement the color palette** exactly as specified
5. **Use the component specifications** as a reference for building each section
6. **Test responsive behavior** at all breakpoints

---

**Document Version:** 1.0  
**Last Updated:** December 4, 2025  
**Author:** Manus AI
