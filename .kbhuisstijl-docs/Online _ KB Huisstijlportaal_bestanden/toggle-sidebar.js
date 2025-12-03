(function (Drupal, $) {
  Drupal.behaviors.toggleSidebar = {
    attach: function (context, settings) {
      const sidebar = $('.sidebar', context);

      $(window).resize(function() {
        if (window.innerWidth >= 767) {
          sidebar.show();
        } else {
          sidebar.hide();
        }
      });

      $(once('toggleSidebar', '.filter-icon', context)).each(function () {
        $(this).on('click', function() {
          $('.sidebar').slideToggle();
          $(this).toggleClass('open');
        });
      });
    }
  };
})(Drupal, jQuery);
