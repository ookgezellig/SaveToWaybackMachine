(function ($, Drupal, once, window, document, undefined) {
  Drupal.behaviors.main_menu = {
    attach: function (context, settings) {
      let behavior = this;

      // All menu items with the class expanded on the first level (no submenus)
      $('#main-menu.js-nav-hook', context).find('> .menu > .menu-item.expanded').each(function () {
        $(once('main_menu', this)).find('> a, > span').on('click keydown', function (e) {
          if (e.type === 'click' || (e.type === 'keydown' && e.keyCode === 13)) {
            let $this = $(this).parent();

            if (!$this.hasClass('submenu-open')) {
              // Remove all submenu-open classes from menu.
              $this.parent().find('.submenu-open').removeClass('submenu-open').find(' > .menu').slideToggle();

              // Add submenu-open class to this item and open submenu by setting display mode.
              $this.toggleClass('submenu-open').find('> .menu').slideToggle({
                start: function () {
                  if ($(window).width() < 1207.5) {
                    $(this).css({
                      display: "block"
                    })
                  } else {
                    $(this).css({
                      display: "grid"
                    })
                  }
                }
              });
            } else {
              $this.removeClass('submenu-open').find('> .menu').slideToggle({
                complete: function () {
                  $(this).css({
                    display: "none"
                  })
                }
              });
              $this.find('a.dropdown-toggle').attr('aria-label', 'Open dropdown');
            }
            $this.find('a.dropdown-toggle').attr('aria-expanded', $this.hasClass('submenu-open'));
            $this.find('span.caret').attr('aria-expanded', $this.hasClass('submenu-open'));

            if ($this.hasClass('submenu-open')) {
              let link = $this.find('a.dropdown-toggle');
              let label = link.first().text();
              link.attr('aria-label', Drupal.t('Close dropdown and open @label page', { '@label': label }));
            }

            // Prevents link to be fired.
            e.preventDefault();
          }
        });
      });

      $(document).on('keydown', function(event) {
        if (event.key === "Escape") {
          let menu = $(document).find('.submenu-open');
          menu.removeClass("submenu-open").find('> .menu').slideUp();
          menu.find('a.dropdown-toggle').attr('aria-expanded', false).attr('aria-label', 'Open dropdown');
          menu.find('> span').attr('aria-expanded', false);
        }
      });

    },
  };

  $(document).on("click", function (event) {
    var $trigger = $(".dropdown");
    if (!$trigger.is(event.target) && !$trigger.has(event.target).length) {
      let menu_item = $('.submenu-open');
      menu_item.removeClass('submenu-open').find('> .menu').slideUp();
      menu_item.find('a.dropdown-toggle').attr('aria-expanded', false).attr('aria-label', 'Open dropdown');
      menu_item.find('> span').attr('aria-expanded', false);
    }
  });

  document.addEventListener('keyup', function (event) {
    if (event.key === 'Tab') {
      var $trigger = $(".dropdown.submenu-open");
      if (!$trigger.is(event.target) && !$trigger.has(event.target).length) {
        let menu_item = $('.submenu-open');
        menu_item.removeClass('submenu-open').find('> .menu').slideUp();
        menu_item.find('a.dropdown-toggle').attr('aria-expanded', false).attr('aria-label', 'Open dropdown');
        menu_item.find('> span').attr('aria-expanded', false);
      }
    }
  });

})(jQuery, Drupal, once, this, this.document);
