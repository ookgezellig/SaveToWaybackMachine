/*!
 * Javascript code based on the original toc.js library.
 * Original code has been heavily modified and refactored.
 *
 * toc - jQuery Table of Contents Plugin
 * http://projects.jga.me/toc/
 * copyright Greg Allen 2014
 * MIT License
 */
(($) => {
  const PADDING_TOP_UPDATE_EVENT = 'toc_js-padding-top-update';
  const TOC_UPDATE_EVENT = 'toc_js-toc-update';
  const DATA_FOCUSED_ELEMENT_ID = 'focusedElementId';

  /**
   * The TocObject struct definition.
   * @typedef {Object} TocObject
   * @property {Object} opts - TODO.
   * @property {Node} element - TODO.
   * @property {Object} $element - TODO.
   * @property {Node} tocContainer - TODO.
   * @property {Object} $tocContainer - TODO.
   * @property {NodeList} containers - TODO.
   * @property {Object} $headings - TODO.
   * @property {number} bodyPaddingTop - TODO.
   * @property {number|null} highlightTimeout - Highlight on scroll timeout
   * @property {number|null} scrollToTimeout - TODO.
   * @property {function} highlightOnScroll - TODO.
   * @property {function} scrollTo - TODO.
   * @property {function|undefined} scrollListener - TODO.
   * @property {boolean} updating - TODO.
   * @property {Node} observableContainer - TODO.
   */

  /**
   * Get the new body padding-top and update the sticky positioning.
   *
   * @param {TocObject} tocObj - The tocObj object.
   */
  function refreshBodyPaddingTop(tocObj) {
    const bodyCompStyle = window.getComputedStyle(document.body);
    tocObj.bodyPaddingTop = parseInt(
      bodyCompStyle.getPropertyValue('padding-top'),
      10,
    );
    document.dispatchEvent(new Event(PADDING_TOP_UPDATE_EVENT));
  }

  /**
   * Handle body padding-top changes for correct sticky positioning.
   *
   * The Drupal admin toolbar adds a padding-top to the page body.
   * We try to handle it as properly as possible.
   *
   * @param {TocObject} tocObj - The tocObj object.
   */
  function initBodyPaddingTopObserver(tocObj) {
    const mutObserver = new MutationObserver((mutations) => {
      mutations.forEach((mutationRecord) => {
        if (
          mutationRecord.type === 'attributes' &&
          mutationRecord.attributeName === 'style' &&
          mutationRecord.target === document.body
        ) {
          refreshBodyPaddingTop(tocObj);
        }
      });
    });
    mutObserver.observe(document.body, {
      attributes: true,
      attributeFilter: ['style'],
    });
  }

  /**
   * Creates a Range from a NodeList.
   *
   * It will be used to get the common ancestor of several containers.
   *
   * @param {NodeList} nodeList - The node list to use to create the range.
   * @return {Range} - The corresponding range.
   */
  function createRangeFromNodeList(nodeList) {
    if (nodeList.length === 0) return null;
    const range = document.createRange();
    range.setStartBefore(nodeList[0]);
    range.setEndAfter(nodeList[nodeList.length - 1]);
    return range;
  }

  /**
   * Starts observing the specified container for mutations.
   *
   * @param {MutationObserver} mutObserver - The Ajax MutationObserver.
   * @param {Node} container - The Node to observer for mutation.
   */
  function mutationObserve(mutObserver, container) {
    mutObserver.observe(container, {
      childList: true,
      subtree: true,
    });
  }

  /**
   * @param {TocObject} tocObj - The tocObj object.
   */
  function initContainerObserver(tocObj) {
    const mutObserver = new MutationObserver((mutations) => {
      let updateNeeded = false;
      for (let k = 0; k < mutations.length; k++) {
        if (updateNeeded) {
          break;
        }
        const mutation = mutations[k];
        if (mutation.type === 'childList') {
          const { addedNodes, removedNodes } = mutation;
          if (addedNodes.length > 0) {
            let containerUpdated = false;
            for (let i = 0; i < addedNodes.length; i++) {
              if (containerUpdated) {
                break;
              }
              const addedNode = addedNodes[i];
              if (
                addedNode.nodeType === Node.ELEMENT_NODE &&
                (addedNode.querySelectorAll(tocObj.opts.selectors).length > 0 ||
                  addedNode.closest(tocObj.opts.selectors))
              ) {
                for (let j = 0; j < tocObj.containers.length; j++) {
                  if (containerUpdated) {
                    break;
                  }
                  const container = tocObj.containers[j];
                  if (container.contains(addedNode)) {
                    containerUpdated = true;
                  }
                }
              }
            }
            updateNeeded = updateNeeded || containerUpdated;
          }
          if (updateNeeded) {
            break;
          }
          if (removedNodes.length > 0) {
            let containerUpdated = false;
            for (let i = 0; i < removedNodes.length; i++) {
              if (containerUpdated) {
                break;
              }
              const removedNode = removedNodes[i];
              if (removedNode.nodeType === Node.ELEMENT_NODE) {
                for (let j = 0; j < tocObj.containers.length; j++) {
                  if (containerUpdated) {
                    break;
                  }
                  const container = tocObj.containers[j];
                  if (removedNode.contains(container)) {
                    containerUpdated = true;
                  } else if (container.contains(mutation.target)) {
                    containerUpdated =
                      removedNode.querySelectorAll(tocObj.opts.selectors)
                        .length > 0;
                  }
                }
              }
            }
            updateNeeded = updateNeeded || containerUpdated;
          }
        }
      }
      if (updateNeeded) {
        document.dispatchEvent(new Event(TOC_UPDATE_EVENT));
      }
    });
    if (tocObj.observableContainer) {
      mutationObserve(mutObserver, tocObj.observableContainer);
    } else if (tocObj.containers.length === 1) {
      mutationObserve(mutObserver, tocObj.containers[0]);
    } else {
      const containersRange = createRangeFromNodeList(tocObj.containers);
      if (containersRange) {
        mutationObserve(mutObserver, containersRange.commonAncestorContainer);
      } else {
        // Could be problematic performance wise, but should not happen.
        mutationObserve(mutObserver, document);
      }
    }
  }

  /**
   * @param {TocObject} tocObj - The tocObj object.
   */
  function removeActiveStatus(tocObj) {
    const { element, opts } = tocObj;
    element.querySelectorAll(`li.${opts.activeClass}`).forEach((li) => {
      li.classList.remove(opts.activeClass);
      li.querySelector('a[aria-current="true"]').removeAttribute(
        'aria-current',
      );
    });
  }

  /**
   * Add class and aria-current to the active link.
   *
   * @param {TocObject} tocObj - The tocObj object.
   * @param {Element} activeLink - The link to set active.
   */
  function setActiveStatus(tocObj, activeLink) {
    const { opts } = tocObj;
    activeLink.closest('li').classList.add(opts.activeClass);
    activeLink.setAttribute('aria-current', 'true');
  }

  /**
   * @param {TocObject} tocObj - The tocObj object.
   */
  function refreshHighlight(tocObj) {
    const scrollHeight = window.innerHeight - tocObj.bodyPaddingTop;
    let closest = Number.MAX_VALUE;
    let index = -1;
    let prevIndex = -1;
    for (let i = 0; i < tocObj.$headings.length; i += 1) {
      const headingRect = tocObj.$headings[i].getBoundingClientRect();
      // Process visible headings only.
      if (headingRect.height > 0) {
        prevIndex = index;
        const headingScrollTop = headingRect.top - tocObj.bodyPaddingTop;
        const currentClosest = Math.abs(headingScrollTop);
        if (currentClosest < closest) {
          closest = currentClosest;
          index = i;
          if (headingScrollTop > scrollHeight / 2 && prevIndex !== -1) {
            // Go back to the previous index if not high enough on screen.
            index = prevIndex;
          }
        } else {
          break;
        }
      }
    }
    if (index >= 0) {
      removeActiveStatus(tocObj);
      const headingId = tocObj.$headings[index].id;
      const highlighted = tocObj.element.querySelector(
        `li a[href="#${headingId}"]`,
      );
      setActiveStatus(tocObj, highlighted);
      tocObj.opts.onHighlight($(highlighted).closest('li'));
    }
  }

  function highlightOnScroll() {
    /** @type {TocObject} */
    const tocObj = this;
    if (tocObj.highlightTimeout) {
      clearTimeout(tocObj.highlightTimeout);
    }
    tocObj.highlightTimeout = setTimeout(() => {
      refreshHighlight(tocObj);
    }, 50);
  }

  /**
   * @param {TocObject} tocObj - The tocObj object.
   */
  function addHighlightScrollListener(tocObj) {
    $(window).on(
      'scroll',
      ((to) => {
        to.scrollListener = () => {
          to.highlightOnScroll();
        };
        return to.scrollListener;
      })(tocObj),
    );
  }

  function scrollTo(e, anchor) {
    /** @type {TocObject} */
    const tocObj = this;
    if (tocObj.opts.smoothScrolling) {
      e.preventDefault();
      if (tocObj.opts.highlightOnScroll) {
        // If currently waiting for highlight re-enabling... Check below.
        if (tocObj.scrollToTimeout) {
          clearTimeout(tocObj.scrollToTimeout);
        }
        // Disable highlight before using scrollIntoView for performance reason.
        $(window).off('scroll', tocObj.scrollListener);
      }
      anchor.scrollIntoView({ behavior: 'smooth' });
      window.history.replaceState(undefined, undefined, `#${anchor.id}`);
      if (tocObj.opts.highlightOnScroll) {
        // Re-enable highlight after waiting for one second.
        tocObj.scrollToTimeout = setTimeout(() => {
          addHighlightScrollListener(tocObj);
        }, 1000);
      }
    }
  }

  /**
   * Get the heading level from the related DOM element.
   *
   * @param {Object} heading - The heading element object.
   * @return {number} - The heading level if the element is an HTML heading,
   * 1 otherwise.
   */
  function getHeadingLevel(heading) {
    if (/^H[1-6]$/.test(heading.tagName)) {
      return parseInt(heading.tagName[1], 10);
    }
    return 1;
  }

  /**
   * Returns a cleaned copy of the heading element, removing unwanted child elements.
   *
   * @param {Element} heading - The heading DOM element to clean.
   * @param {Object} opts - The configuration options object.
   * @return {Element} - The cleaned heading element.
   */
  function cleanupHeading(heading, opts) {
    let headingElt = heading;
    if (opts.headingCleanupSelector > '') {
      headingElt = heading.cloneNode(true);
      headingElt.querySelectorAll(opts.headingCleanupSelector).forEach((el) => {
        el.remove();
      });
    }
    return headingElt;
  }

  /**
   * @param {TocObject} tocObj - The tocObj object.
   */
  function processHeadings(tocObj) {
    const $tocEl = tocObj.$element;
    const { $headings, element, opts } = tocObj;

    let currentLevel = 0;
    let currentList;
    const $tocNav = $tocEl.find('nav');
    $tocNav.find('ul').remove();
    let lastLi = $tocNav[0];

    $headings.each((i, heading) => {
      // Skip invisible headings if specified in configuration.
      if (opts.skipInvisibleHeadings) {
        if (!heading.checkVisibility()) {
          return;
        }
      }

      // Cleanup heading content.
      const cleanHeading = cleanupHeading(heading, opts);

      // Generate heading ID from the clean heading content for anchor use.
      heading.id = opts.generateHeadingId(cleanHeading, opts.prefix);

      // If specified, allow heading to take focus.
      if (opts.headingFocus) {
        heading.tabIndex = -1;
      }

      // Apply scroll offset.
      if (opts.scrollToOffset) {
        heading.style.scrollMarginTop = opts.scrollToOffset;
      }

      // build TOC item
      const a = document.createElement('a');
      if (opts.useHeadingHtml) {
        a.innerHTML = opts.headingHtml(cleanHeading);
      } else {
        a.textContent = opts.headingText(cleanHeading);
      }
      a.href = `#${heading.id}`;
      a.addEventListener('click', (event) => {
        if (opts.collapsibleItems) {
          event.stopPropagation(); // To prevent toggling of subitems.
        }
        tocObj.scrollTo(event, heading);
        if (opts.headingFocus) {
          heading.focus({ preventScroll: true });
        }
        removeActiveStatus(tocObj);
        setActiveStatus(tocObj, event.target);
        $tocEl.trigger('selected', event.target.href);
      });
      if (opts.collapsibleItems) {
        a.addEventListener('keydown', function noToggleCollapse(e) {
          if (e.key === 'Enter' || e.key === ' ') {
            e.stopPropagation(); // To prevent toggling of subitems.
          }
        });
      }

      const li = document.createElement('li');
      li.classList.add(opts.itemClass(heading, opts.prefix));
      $(li).addClass(opts.liClasses);
      if (opts.inheritableClasses.length > 0) {
        heading.classList.forEach((className) => {
          if (opts.inheritableClasses.includes(className)) {
            li.classList.add(className);
          }
        });
      }
      li.append(a);

      // Add custom classes to heading after adding inheritable classes to toc.
      $(heading).addClass(opts.headingClasses);

      const level = getHeadingLevel(heading);

      if (level === currentLevel) {
        currentList.appendChild(li);
        lastLi = li;
      } else if (level > currentLevel) {
        const ul = document.createElement(opts.listType);
        if (opts.listClasses.length > 0) {
          ul.classList.add(...opts.listClasses);
        }
        if (currentLevel > 0 && opts.collapsibleItems) {
          ul.classList.add('collapsible');
          const expanded = opts.collapsibleExpanded;
          lastLi.role = 'button';
          lastLi.tabIndex = 0;
          lastLi.setAttribute('aria-label', expanded ? 'Collapse' : 'Expand');
          lastLi.setAttribute('aria-expanded', expanded ? 'true' : 'false');
          lastLi.addEventListener('click', function toggleCollapse(e) {
            if (e.target === this) {
              const isExpanded = this.getAttribute('aria-expanded') === 'true';
              this.setAttribute('aria-expanded', !isExpanded);
            }
          });
          lastLi.addEventListener('keydown', function toggleCollapse(e) {
            if (e.key === 'Enter' || e.key === ' ') {
              e.preventDefault(); // Prevent space from scrolling the page
              this.click();
            }
          });
        }
        currentLevel = level;
        ul.level = level;
        ul.appendChild(li);
        lastLi.appendChild(ul);
        currentList = ul;
        lastLi = li;
      } else if (level < currentLevel) {
        while (level < currentLevel) {
          // Special case where the parent element is the root nav element.
          // Can occur when the first heading is not of the highest level.
          // See: https://www.drupal.org/project/toc_js/issues/3474535
          if (currentList.parentNode.nodeName === 'NAV') {
            if (level < currentList.level) {
              currentList.level = level;
            }
            break;
          } else {
            currentList = currentList.parentNode.parentNode;
            currentLevel = currentList.level;
          }
        }
        currentList.appendChild(li);
        lastLi = li;
        currentLevel = level;
      }
    });
  }

  /**
   * Build "back to top" and "back to toc" links.
   *
   * @param {TocObject} tocObj - The tocObj object.
   */
  function buildTocAndTopLinks(tocObj) {
    const { element, $element, $headings, opts } = tocObj;
    const tocId = element.id;
    const firstHeadingId = $headings[0].id;
    const firstLinkSelector = `a[href="#${firstHeadingId}"]`;
    const firstLink = element.querySelector(firstLinkSelector);
    let currentLinkIndex = 0;
    $element.find('a').each(function updateTocLinks() {
      const link = this;
      const linkHash = link.hash;
      const anchor = linkHash.replace(/^#/, '');
      const heading = document.getElementById(anchor);
      if (!heading) {
        // Can happen when the "Use heading HTML" option is activated.
        // Some headings can have links in their HTML.
        // These are not valid toc links, obviously.
        return;
      }
      if (
        opts.backToTop &&
        currentLinkIndex > 0 &&
        (opts.backToTopSelector === '' ||
          heading.matches(opts.backToTopSelector))
      ) {
        const a = document.createElement('a');
        a.innerHTML = opts.backToTopLabel;
        a.href = `#${firstHeadingId}`;
        a.dataset.tocId = tocId;
        a.addEventListener('click', (e) => {
          const firstHeading = document.getElementById(firstHeadingId);
          tocObj.scrollTo(e, firstHeading);
          if (opts.headingFocus) {
            firstHeading.focus({ preventScroll: true });
          }
          removeActiveStatus(tocObj);
          setActiveStatus(tocObj, firstLink);
          $element.trigger('selected', linkHash);
        });
        const $a = $(a);
        $a.addClass(opts.backToTopClass);
        heading.parentNode.insertBefore(a, heading);
      }
      if (opts.backToToc) {
        const anchorNameToToc = `${tocId}-${anchor}-to-toc`;
        $(link).attr('id', anchorNameToToc);
        const a = document.createElement('a');
        a.innerHTML = opts.backToTocLabel;
        a.href = `#${anchorNameToToc}`;
        a.dataset.tocId = tocId;
        a.addEventListener('click', (e) => {
          tocObj.scrollTo(e, link);
          link.focus({ preventScroll: true });
          removeActiveStatus(tocObj);
          setActiveStatus(tocObj, link);
          $element.trigger('selected', linkHash);
        });
        const $a = $(a);
        $a.addClass(opts.backToTocClass);
        $a.addClass(opts.backToTocClasses);
        heading.parentNode.insertBefore(a, heading);
      }
      currentLinkIndex += 1;
    });
  }

  /**
   * @param {TocObject} tocObj - The tocObj object.
   * @return {string} - The focused element id.
   */
  function getFocusedElementId(tocObj) {
    return tocObj.$element.data(DATA_FOCUSED_ELEMENT_ID);
  }

  /**
   * @param {TocObject} tocObj - The tocObj object.
   * @param {string} id - The focused element id.
   */
  function setFocusedElementId(tocObj, id) {
    tocObj.$element.data(DATA_FOCUSED_ELEMENT_ID, id);
  }

  /**
   * @param {TocObject} tocObj - The tocObj object.
   */
  function unsetFocusedElementId(tocObj) {
    tocObj.$element.data(DATA_FOCUSED_ELEMENT_ID, null);
  }

  /**
   * @param {TocObject} tocObj - The tocObj object.
   * @return {Object} - The focusable element if found.
   */
  function getFirstFocusableElement(tocObj) {
    return tocObj.$element.find('button, a').first();
  }

  /**
   * Restore focus on previously focused element when toc is updated.
   *
   * @param {TocObject} tocObj - The tocObj object.
   */
  function restoreFocus(tocObj) {
    setTimeout(() => {
      // Get the ID of the previously focused element.
      const focusedElementId = getFocusedElementId(tocObj);
      if (focusedElementId) {
        // Unset the previously focused element.
        unsetFocusedElementId(tocObj);
        // Get element to focus using the stored focused element id.
        let focusedElement = tocObj.$element.find(`#${focusedElementId}`);
        if (focusedElement.length === 0) {
          // Use first focusable element if stored focused element not found.
          focusedElement = getFirstFocusableElement(tocObj);
        }
        if (focusedElement) {
          focusedElement.focus();
        }
      }
    }, 0);
  }

  function isFocusingOut(event, element) {
    return (
      event.relatedTarget === null || !element.contains(event.relatedTarget)
    );
  }

  /**
   * @param {TocObject} tocObj - The tocObj object.
   */
  function manageFocus(tocObj) {
    // A11y: store the currently focused toc element to be able to restore the
    // focus on this element after a toc refresh caused by an Ajax page update.
    tocObj.$element
      .on('focusin', function focusIn(event) {
        // We store the currently focused element id in the toc.
        setFocusedElementId(tocObj, event.target.id);
      })
      .on('focusout', function focusOut(event) {
        if (!tocObj.updating && isFocusingOut(event, this)) {
          // Delete the stored focused element id when focus leaves the toc.
          unsetFocusedElementId(tocObj);
        }
      });
  }

  /**
   * Stick the toc.
   *
   * @param {TocObject} tocObj - The tocObj object.
   */
  function stickTheToc(tocObj) {
    const topArray = [
      tocObj.bodyPaddingTop > 0 ? `${tocObj.bodyPaddingTop}px` : null,
      tocObj.opts.stickyOffset,
    ].filter(Boolean);
    tocObj.tocContainer.style.top =
      topArray.length === 2
        ? `calc(${topArray.join(' + ')})`
        : topArray[0] || '0';
  }

  /**
   * Remove eventual existing back to top links.
   *
   * @param {TocObject} tocObj - The tocObj object.
   */
  function cleanupBackToTopAndTocLinks(tocObj) {
    const tocId = tocObj.element.id;
    const topClass = tocObj.opts.backToTopClass;
    const tocClass = tocObj.opts.backToTocClass;
    const selector = `a.${topClass}[data-toc-id="${tocId}"], a.${tocClass}[data-toc-id="${tocId}"]`;
    tocObj.containers.forEach((container) => {
      container.querySelectorAll(selector).forEach((el) => {
        el.remove();
      });
    });
  }

  /**
   * Adds the is-visible class to back to top links.
   *
   * @param {TocObject} tocObj - The tocObj object.
   */
  function showBackToTopLinks(tocObj) {
    const tocId = tocObj.element.id;
    const selector = `a.${tocObj.opts.backToTopClass}[data-toc-id="${tocId}"]`;
    tocObj.containers.forEach((container) => {
      container.querySelectorAll(selector).forEach((el) => {
        el.classList.add('is-visible');
      });
    });
  }

  /**
   * Build ToC.
   *
   * @param {TocObject} tocObj - The tocObj object.
   */
  function buildToc(tocObj) {
    tocObj.updating = true;
    tocObj.$tocContainer.addClass('toc-js-container');
    processHeadings(tocObj);
    const tocLength = tocObj.$element.find('li').length;
    const minimum = tocObj.opts.selectorsMinimum;
    if (tocLength >= minimum) {
      if (
        (tocObj.opts.backToTop || tocObj.opts.backToToc) &&
        tocObj.$headings.length > 1
      ) {
        buildTocAndTopLinks(tocObj);
      }

      if (tocObj.opts.sticky) {
        tocObj.$tocContainer.addClass('sticky');
        document.addEventListener(PADDING_TOP_UPDATE_EVENT, () => {
          stickTheToc(tocObj);
        });
        refreshBodyPaddingTop(tocObj);
      }

      tocObj.$tocContainer.addClass('is-visible');
      tocObj.$tocContainer.removeClass('is-hidden');
      showBackToTopLinks(tocObj);
    } else {
      tocObj.$tocContainer.removeClass('is-visible');
      tocObj.$tocContainer.addClass('is-hidden');
    }
    tocObj.updating = false;
  }

  /**
   * Build a TocObject instance for a specific ToC.
   *
   * @param {Object} element - TODO.
   * @param {Object} opts - TODO.
   * @return {TocObject} - The TocObject instance.
   */
  function initTocObject(element, opts) {
    const tocContainer = opts.getTocContainer(element);
    return {
      opts,
      element,
      $element: $(element),
      tocContainer,
      $tocContainer: $(tocContainer),
      containers: opts.getContainers(),
      $headings: $(opts.getHeadings()),
      highlightTimeout: null,
      scrollToTimeout: null,
      bodyPaddingTop: 0,
      highlightOnScroll,
      scrollTo,
      scrollListener: undefined,
      updating: false,
      observableContainer: opts.getObservableContainer(),
    };
  }

  /**
   * @param {TocObject} tocObj - The tocObj object.
   */
  function updateTocObject(tocObj) {
    tocObj.containers = tocObj.opts.getContainers();
    tocObj.$headings = $(tocObj.opts.getHeadings());
  }

  /**
   * @param {TocObject} tocObj - The tocObj object.
   */
  function addTocUpdateListener(tocObj) {
    document.addEventListener(TOC_UPDATE_EVENT, () => {
      updateTocObject(tocObj);
      cleanupBackToTopAndTocLinks(tocObj);
      buildToc(tocObj);
      restoreFocus(tocObj);
      if (tocObj.opts.highlightOnScroll) {
        refreshHighlight(tocObj);
      }
    });
  }

  $.fn.toc_js = function fnTocJS(options) {
    const opts = $.extend({}, jQuery.fn.toc_js.defaults, options);
    return this.each(function eachToc() {
      const tocObj = initTocObject(this, opts);
      initBodyPaddingTopObserver(tocObj);
      buildToc(tocObj);
      if (tocObj.opts.highlightOnScroll) {
        addHighlightScrollListener(tocObj);
        refreshHighlight(tocObj);
      }
      if (tocObj.opts.ajaxPageUpdates) {
        manageFocus(tocObj);
        initContainerObserver(tocObj);
        addTocUpdateListener(tocObj);
      }
    });
  };

  jQuery.fn.toc_js.defaults = {
    container: 'body',
    selectorsMinimum: 0,
    listType: 'ul',
    selectors: 'h1,h2,h3',
    smoothScrolling: true,
    scrollToOffset: null,
    sticky: false,
    stickyOffset: null,
    prefix: 'toc',
    activeClass: 'toc-active',
    onHighlight() {},
    highlightOnScroll: true,
    highlightOffset: 0,
    skipInvisibleHeadings: false,
    useHeadingHtml: false,
    collapsibleItems: false,
    collapsibleExpanded: true,
    backToTop: false,
    backToTopLabel: 'Back to top',
    headingFocus: false,
    backToToc: false,
    tocContainer: '',
    ajaxPageUpdates: false,
    observableSelector: '',
    generateHeadingId(heading, prefix) {
      if (heading.id.length) {
        // Use existing id if not empty.
        return heading.id;
      }
      // Source: https://www.30secondsofcode.org/js/s/remove-accents/
      let headingId = heading.textContent
        .toLowerCase()
        .normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '')
        .replace(/[^a-z0-9]/gi, ' ')
        .replace(/\s+/g, '-')
        .replace(/^-+|-+$/g, '');
      headingId = prefix ? `${prefix}-${headingId}` : headingId;
      // Handle potential headingId collision.
      if (document.getElementById(headingId)) {
        let newHeadingId;
        let j = 2;
        do {
          newHeadingId = `${headingId}-${j}`;
          j += 1;
        } while (document.getElementById(newHeadingId));
        headingId = newHeadingId;
      }
      return headingId;
    },
    headingHtml(heading) {
      return heading.innerHTML;
    },
    headingText(heading) {
      return heading.textContent;
    },
    itemClass(heading, prefix) {
      const tagName = heading.tagName.toLowerCase();
      return prefix ? `${prefix}-${tagName}` : tagName;
    },
    getContainers() {
      return document.querySelectorAll(this.container || 'body');
    },
    getHeadings() {
      const containers = this.getContainers();
      const headings = [];
      containers.forEach((container) => {
        headings.push(
          ...Array.from(container.querySelectorAll(this.selectors)),
        );
      });
      return headings;
    },
    getTocContainer(element) {
      if (this.tocContainer > '') {
        return element.closest(this.tocContainer) || element;
      }
      return element;
    },
    getObservableContainer() {
      if (this.observableSelector > '') {
        return document.querySelector(this.observableSelector);
      }
      return null;
    },
  };
})(jQuery);
