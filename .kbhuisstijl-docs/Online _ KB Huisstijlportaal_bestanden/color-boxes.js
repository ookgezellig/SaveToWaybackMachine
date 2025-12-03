(function ($, once, Drupal) {
  Drupal.behaviors.copyColor = {
    attach: function (context, settings) {
      $(".copy-color").click(function(event) {
          var text = $(this).attr('colorvalue');
          navigator.clipboard.writeText(text);

          // Get the snackbar DIV
          var toast = document.getElementById("color-notification");

          // Add the "show" class to DIV
          toast.className = "show";

          // After 3 seconds, remove the show class from DIV
          setTimeout(function(){ toast.className = toast.className.replace("show", ""); }, 3000);
        });
      $(once('copyColor', '.color-box')).each(function (e) {
        let color = getRGB($(this).css('background-color'));
        let textColor = getContrast(color['r'], color['g'], color['b']);

        $(this).css('color', textColor);
        $(this).find('.copy-color').css('background', textColor);
      });
    }
  }

  function getLuminance(r, g, b) {
    const a = [r, g, b].map(function (v) {
      v = v / 255;
      return (v <= 0.03928) ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722;
  }

  function getContrastRatio(rgb1, rgb2) {
    const luminance1 = getLuminance(rgb1[0], rgb1[1], rgb1[2]);
    const luminance2 = getLuminance(rgb2[0], rgb2[1], rgb2[2]);
    const brightest = Math.max(luminance1, luminance2);
    const darkest = Math.min(luminance1, luminance2);
    return (brightest + 0.05) / (darkest + 0.05);
  }

  // https://www.w3.org/TR/AERT#color-contrast
  // https://www.w3.org/TR/WCAG20-TECHS/G18.html#G18-procedure
  function getContrast(r, g, b) {
    const black = [0, 0, 0];
    const color = [parseInt(r), parseInt(g), parseInt(b)];

    // Measure contrast with black to see if a black text color fits.
    // If it doesn't, change the text color to white to meet WCAG standards.
    const contrastWithBlack = getContrastRatio(color, black);

    return (contrastWithBlack >= 4.5) ? 'black' : 'white';
  }

  function getRGB(str){
    var match = str.match(/rgba?\((\d{1,3}), ?(\d{1,3}), ?(\d{1,3})\)?(?:, ?(\d(?:\.\d?))\))?/);
    return match ? {
      r: match[1],
      g: match[2],
      b: match[3]
    } : {};
  }
})(jQuery, once, Drupal);
