# YOLO Charters Website Analysis

This document provides a comprehensive analysis of the front-end resources used by the `yolo-charters.com` website, based on the provided page source files. The goal is to identify all key technologies, libraries, scripts, and stylesheets to aid in replicating the site's styles and functionality.

## Summary of Detected Technologies

The website is built on a foundation of standard web technologies, including HTML, CSS, and JavaScript. It leverages several popular open-source libraries to provide interactive features such as date pickers, image galleries, and dynamic content loading.

## CSS Analysis

The site's styling is managed through a combination of a main compiled stylesheet and several individual library-specific stylesheets.

### Local CSS Files

These files are hosted directly within the website's directory structure.

| File Path | Purpose |
|---|---|
| `dist/css/style.min.css` | The primary, minified stylesheet for the website. This file likely contains all the custom styles for the site's layout, components, and overall appearance. |
| `src/css/jquery-ui.min.css` | Stylesheet for the jQuery UI library, providing UI components like sliders, dialogs, and more. |
| `src/css/magnific-popup.min.css` | Stylesheet for the Magnific Popup library, a responsive lightbox and dialog script. |
| `src/css/photo-swipe.min.css` | Stylesheet for the PhotoSwipe library, an image gallery and lightbox. |
| `src/css/select2.min.css` | Stylesheet for the Select2 library, which replaces standard select boxes with a more powerful and customizable version. |

## JavaScript Analysis

The website's interactivity is powered by jQuery and a collection of plugins and libraries.

### Local JavaScript Files

| File Path | Purpose |
|---|---|
| `dist/js/custom.min.js` | A minified file containing custom JavaScript code for the website. This likely includes initialization scripts for the various libraries and any unique site-specific functionality. |
| `dist/js/plugins.min.js` | A minified file that likely bundles several of the smaller JavaScript plugins used on the site into a single file for performance. |
| `src/js/jquery.min.js` | The core jQuery library. |
| `src/js/litepicker.js` | A lightweight, dependency-free date range picker. |
| `src/js/mobilefriendly.js` | A plugin for Litepicker to improve its usability on mobile devices. |

### CDN-Hosted JavaScript Files

| URL | Library/Purpose |
|---|---|
| `https://cdn.jsdelivr.net/npm/litepicker/dist/plugins/mobilefriendly.js` | Mobile-friendly plugin for Litepicker. |
| `https://cdnjs.cloudflare.com/ajax/libs/jquery-bootpag/1.0.4/jquery.bootpag.min.js` | A jQuery plugin for dynamic pagination. |
| `https://www.google.com/recaptcha/api.js?hl=` | Google's reCAPTCHA library for spam protection. |

### Identified JavaScript Libraries

| Library | Purpose |
|---|---|
| **jQuery** | The foundational library for most of the site's JavaScript functionality. |
| **jQuery UI** | Provides a suite of UI interactions, effects, widgets, and themes. |
| **Litepicker** | Used for selecting date ranges in the booking/search forms. |
| **Select2** | Enhances standard HTML `<select>` elements with features like searching, tagging, and remote data loading. |
| **PhotoSwipe** | Powers the image galleries, providing a responsive and touch-friendly lightbox experience. |
| **Magnific Popup** | Used for creating responsive lightboxes and modal dialogs. |
| **jQuery Bootpag** | Handles the pagination of search results or other lists of content. |
| **Google reCAPTCHA** | Protects forms from spam and abuse. |

## Font Analysis

No explicit font-family declarations or links to external font services like Google Fonts were found in the provided HTML source files. The fonts are likely defined within the `dist/css/style.min.css` file. To identify the specific fonts used, this file would need to be retrieved and analyzed.

## Conclusion

The `yolo-charters.com` website is built with a robust set of well-established front-end libraries. To replicate its look and feel, you will need to incorporate these same libraries and then recreate the custom styles found in `dist/css/style.min.css` and the custom functionality from `dist/js/custom.min.js`.
