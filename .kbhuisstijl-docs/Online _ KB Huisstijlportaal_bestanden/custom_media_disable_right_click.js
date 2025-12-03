(function ($, Drupal, once) {
  Drupal.behaviors.customMediaDisableRightClick = {
    attach: function (context, settings) {
      $(once('custom-media-disable-right-click', '.media-item img', context)).on('contextmenu', function (e) {
        e.preventDefault();
        showMessage();
      });

      function showMessage() {
        alert(Drupal.t('Please navigate to the "Downloads" tab on the right to download images.'));
      }
    }
  };
})(jQuery, Drupal, once);
