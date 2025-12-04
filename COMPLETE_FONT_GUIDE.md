# YOLO Charters - Complete Font Usage Guide

**Generated:** December 4, 2025  
**Source:** Extracted from `dist/css/style.min.css`

---

## Font Summary

The YOLO Charters website uses **two primary font families**:

1. **Inter** (Light & Medium weights) - Primary font for body text
2. **Poppins** (Regular & Medium weights) - Secondary font for headings and emphasis

---

## Font Declarations (@font-face)

### 1. Poppins Regular (Weight: 400)
```css
@font-face {
    font-family: Poppins;
    font-style: normal;
    font-weight: 400;
    src: url(../../fonts/Poppins-Regular.ttf) format("truetype");
}
```
**File:** `fonts/Poppins-Regular.ttf`

### 2. Poppins Medium (Weight: 500)
```css
@font-face {
    font-family: Poppins;
    font-style: normal;
    font-weight: 500;
    src: url(../../fonts/Poppins-Medium.ttf) format("truetype");
}
```
**File:** `fonts/Poppins-Medium.ttf`

### 3. Inter Light (Weight: 300)
```css
@font-face {
    font-family: Inter Light;
    font-style: normal;
    font-weight: 300;
    src: url(../../fonts/InterLight.ttf) format("truetype");
}
```
**File:** `fonts/InterLight.ttf`

### 4. Inter Medium (Weight: 500)
```css
@font-face {
    font-family: Inter Medium;
    font-style: normal;
    font-weight: 500;
    src: url(../../fonts/InterMedium.ttf) format("truetype");
}
```
**File:** `fonts/InterMedium.ttf`

---

## CSS Custom Properties (Variables)

The website defines font stacks using CSS custom properties:

```css
:root {
    --font-primary: "Inter Light";
    --font-secondary: "Poppins";
    
    --bs-font-sans-serif: system-ui, -apple-system, "Segoe UI", Roboto, 
                          "Helvetica Neue", Arial, "Noto Sans", 
                          "Liberation Sans", sans-serif, "Apple Color Emoji", 
                          "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
    
    --bs-font-monospace: SFMono-Regular, Menlo, Monaco, Consolas, 
                         "Liberation Mono", "Courier New", monospace;
}
```

---

## Font Usage by Component

### Primary Font (Inter Light)
**CSS Variable:** `var(--font-primary)`  
**Font Family:** `"Inter Light"`  
**Weight:** 300

**Used for:**
- Body text
- Paragraphs
- General content
- Light-weight text elements

### Secondary Font (Poppins)
**CSS Variable:** `var(--font-secondary)`  
**Font Family:** `"Poppins"`  
**Weights:** 400 (Regular), 500 (Medium)

**Used for:**
- Headings (H1-H6)
- Buttons
- Navigation links
- Emphasis text
- Call-to-action elements

### Inter Medium
**Font Family:** `"Inter Medium"`  
**Weight:** 500

**Used for:**
- Medium-weight body text
- Subheadings
- Important text that needs more weight than Inter Light

---

## How to Implement

### Option 1: Use Google Fonts (Recommended for ease)

Add to your HTML `<head>`:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;500&family=Poppins:wght@400;500&display=swap" rel="stylesheet">
```

Then in your CSS:
```css
:root {
    --font-primary: "Inter", sans-serif;
    --font-secondary: "Poppins", sans-serif;
}

body {
    font-family: var(--font-primary);
    font-weight: 300;
}

h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-secondary);
    font-weight: 500;
}
```

### Option 2: Self-Host the Fonts

1. **Download the font files:**
   - Poppins: https://fonts.google.com/specimen/Poppins
   - Inter: https://fonts.google.com/specimen/Inter

2. **Place them in your project:**
   ```
   your-project/
   └── fonts/
       ├── Poppins-Regular.ttf
       ├── Poppins-Medium.ttf
       ├── InterLight.ttf
       └── InterMedium.ttf
   ```

3. **Add the @font-face declarations to your CSS:**
   ```css
   @font-face {
       font-family: 'Poppins';
       font-style: normal;
       font-weight: 400;
       src: url('../fonts/Poppins-Regular.ttf') format('truetype');
   }

   @font-face {
       font-family: 'Poppins';
       font-style: normal;
       font-weight: 500;
       src: url('../fonts/Poppins-Medium.ttf') format('truetype');
   }

   @font-face {
       font-family: 'Inter';
       font-style: normal;
       font-weight: 300;
       src: url('../fonts/InterLight.ttf') format('truetype');
   }

   @font-face {
       font-family: 'Inter';
       font-style: normal;
       font-weight: 500;
       src: url('../fonts/InterMedium.ttf') format('truetype');
   }
   ```

4. **Define CSS variables:**
   ```css
   :root {
       --font-primary: 'Inter', -apple-system, BlinkMacSystemFont, 
                       'Segoe UI', Roboto, sans-serif;
       --font-secondary: 'Poppins', -apple-system, BlinkMacSystemFont, 
                         'Segoe UI', Roboto, sans-serif;
   }
   ```

---

## WordPress Plugin Implementation

For your YOLO Yacht Search WordPress plugin, add this to your enqueue function:

```php
// In your class-yolo-ys-public.php or similar file

public function enqueue_styles() {
    // Google Fonts
    wp_enqueue_style(
        'yolo-google-fonts',
        'https://fonts.googleapis.com/css2?family=Inter:wght@300;500&family=Poppins:wght@400;500&display=swap',
        array(),
        null
    );
    
    // Your plugin CSS
    wp_enqueue_style(
        $this->plugin_name,
        YOLO_YS_PLUGIN_URL . 'public/css/yolo-yacht-search-public.css',
        array('yolo-google-fonts'),
        $this->version
    );
}
```

Then in your main CSS file:
```css
:root {
    --font-primary: 'Inter', sans-serif;
    --font-secondary: 'Poppins', sans-serif;
}

body,
.yolo-yacht-search-widget,
.yolo-search-results {
    font-family: var(--font-primary);
    font-weight: 300;
}

h1, h2, h3, h4, h5, h6,
.yacht-card-title,
.btn,
.nav-link {
    font-family: var(--font-secondary);
}
```

---

## Font Weights Reference

| Font | Weight | CSS Value | Usage |
|---|---|---|---|
| **Inter Light** | Light | 300 | Body text, paragraphs |
| **Inter Medium** | Medium | 500 | Emphasized body text |
| **Poppins Regular** | Regular | 400 | Standard headings, buttons |
| **Poppins Medium** | Medium | 500 | Bold headings, important CTAs |

---

## Fallback Font Stacks

The website includes comprehensive fallback stacks:

### Sans-Serif Stack (Bootstrap Default)
```css
system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", 
Arial, "Noto Sans", "Liberation Sans", sans-serif, 
"Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"
```

### Monospace Stack
```css
SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", 
"Courier New", monospace
```

---

## Download Links

### Google Fonts
- **Inter:** https://fonts.google.com/specimen/Inter
- **Poppins:** https://fonts.google.com/specimen/Poppins

### Direct Download (TTF files)
You'll need to download these from Google Fonts or use a font service.

---

## Summary

**Primary Font:** Inter (Light 300, Medium 500)  
**Secondary Font:** Poppins (Regular 400, Medium 500)  
**Font Files Needed:** 4 TTF files total  
**Implementation:** Use Google Fonts CDN or self-host

This matches the exact font setup from the original yolo-charters.com website.

---

**Document Version:** 1.0  
**Last Updated:** December 4, 2025  
**Author:** Manus AI
