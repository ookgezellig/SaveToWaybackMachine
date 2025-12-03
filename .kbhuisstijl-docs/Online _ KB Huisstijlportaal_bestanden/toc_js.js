/**
 * @file
 * Toc.js.
 */
(($, once) => {
  /**
   * Decode an HTML-encoded string.
   *
   * @param {string} html - The HTML-encoded string to decode.
   * @return {string} - The decoded string.
   */
  function decodeHtml(html) {
    const textarea = document.createElement('textarea');
    textarea.innerHTML = html;
    return textarea.value;
  }
  /**
   * Retrieves the value of a CSS property from a CSS variable.
   *
   * If the CSS variable contains a fallback value, it will be used
   * if the CSS variable is not defined.
   *
   * @param {string} styleValueSetting - The value of the CSS variable or a string containing `var(--variable, fallback)`.
   * @param {string} [containerSelector='body'] - The selector for the container element to retrieve the CSS variable from.
   * @return {string} - The value of the CSS property or the fallback value if defined.
   */
  function getStyleValueFromCssProperty(
    styleValueSetting,
    containerSelector = 'body',
  ) {
    let styleValue = styleValueSetting;
    if (styleValueSetting) {
      // Check if it's a CSS variable reference with optional fallback.
      const variableMatch = styleValueSetting.match(
        /^var\((--[a-zA-Z0-9-_]+)(?:,\s*([^)]+))?\)$/,
      );
      if (variableMatch) {
        const propertyName = variableMatch[1];
        const fallback = variableMatch[2]?.trim();
        const container =
          document.querySelector(containerSelector) || document.body;
        styleValue = getComputedStyle(container)
          .getPropertyValue(propertyName)
          .trim();
        if (!styleValue && fallback) {
          styleValue = fallback;
        }
      }
    }
    return styleValue;
  }
  /**
   * Converts an integer or a numeric string to a pixel value.
   *
   * @param {number|string} value - The value to convert. Can be an integer or a numeric string.
   * @return {string} - The value converted to a pixel string (e.g., "10px").
   */
  function convertIntToPx(value) {
    if (Number.isInteger(value)) {
      return `${value}px`;
    }
    if (typeof value === 'string') {
      const trimmedValue = value.trim();
      if (/^-?[0-9]+$/.test(trimmedValue)) {
        return `${trimmedValue}px`;
      }
    }
    return value;
  }
  /**
   * Checks if a given CSS property and value are supported by the browser.
   *
   * @param {string} property - The CSS property to check (e.g., "display").
   * @param {string} value - The value of the CSS property to check (e.g., "grid").
   * @return {string|null} - The value if supported, otherwise `null`.
   */
  function checkCss(property, value) {
    return CSS.supports(property, value) ? value : null;
  }
  /**
   * Converts a string into an array based on a separator.
   *
   * @param {string} value - The string to convert into an array.
   * @param {RegExp|string} [separator=/[,\s]+/] - The separator used to split the string. Defaults to comma and whitespace.
   * @param {Array} [dflt=[]] - The default value to return if the input string is empty or invalid.
   * @return {Array} - The resulting array after splitting the string, or the default value if the input is invalid.
   */
  function stringToArray(value, separator = /[,\s]+/, dflt = []) {
    if (typeof value === 'string' && value !== '') {
      // We split the string value using the provided separator.
      // If no separator is provided, comma and spaces are used as separators.
      // We finally filter out empty strings.
      return value.split(separator).filter((v) => v !== '');
    }
    return dflt;
  }
  Drupal.behaviors.toc_js = {
    attach(context, settings) {
      once('toc_js', '.toc-js', context).forEach((elt) => {
        const $tocEl = $(elt);
        const tocJsSettings = settings.toc_js[elt.id];
        const options = {
          listType: $tocEl.data('list-type') === 'ol' ? 'ol' : 'ul',
          listClasses: stringToArray($tocEl.data('list-classes')),
          selectors: decodeHtml($tocEl.data('selectors')) || 'h2, h3',
          container: decodeHtml($tocEl.data('container')) || 'body',
          selectorsMinimum: $tocEl.data('selectors-minimum') || 0,
          sticky: !!$tocEl.data('sticky'),
          stickyOffset: checkCss(
            'top',
            convertIntToPx($tocEl.data('sticky-offset')),
          ),
          prefix: $tocEl.data('prefix') || '',
          liClasses: $tocEl.data('li-classes') || '',
          inheritableClasses: stringToArray($tocEl.data('inheritable-classes')),
          headingClasses: $tocEl.data('heading-classes') || '',
          skipInvisibleHeadings: !!$tocEl.data('skip-invisible-headings'),
          useHeadingHtml: !!$tocEl.data('use-heading-html'),
          headingCleanupSelector:
            decodeHtml(elt.dataset.headingCleanupSelector) || '',
          collapsibleItems: elt.dataset.collapsibleItems === '1',
          collapsibleExpanded: elt.dataset.collapsibleExpanded === '1',
          backToTop: !!$tocEl.data('back-to-top'),
          backToTopLabel: tocJsSettings.back_to_top_label || 'Back to top',
          backToTopClass: 'back-to-top',
          backToTopSelector: decodeHtml(elt.dataset.backToTopSelector) || '',
          headingFocus: !!$tocEl.data('heading-focus'),
          backToToc: !!$tocEl.data('back-to-toc'),
          backToTocLabel:
            tocJsSettings.back_to_toc_label || 'Back to table of contents',
          backToTocClass: 'back-to-toc',
          backToTocClasses:
            $tocEl.data('back-to-toc-classes') || 'visually-hidden-focusable',
          highlightOnScroll: !!$tocEl.data('highlight-on-scroll'),
          highlightOffset: $tocEl.data('highlight-offset') || 0,
          smoothScrolling: !!$tocEl.data('smooth-scrolling'),
          scrollToOffset: checkCss(
            'scroll-margin-top',
            convertIntToPx($tocEl.data('scroll-to-offset')),
          ),
          tocContainer: decodeHtml($tocEl.data('toc-container')) || '',
          ajaxPageUpdates: !!$tocEl.data('ajax-page-updates'),
          observableSelector:
            decodeHtml($tocEl.data('observable-selector')) || '',
        };
        options.scrollToOffset = getStyleValueFromCssProperty(
          options.scrollToOffset,
          options.container || 'body',
        );
        options.stickyOffset = getStyleValueFromCssProperty(
          options.stickyOffset,
          options.container || 'body',
        );
        $tocEl.toc_js(options);
      });
    },
  };
})(jQuery, once);
