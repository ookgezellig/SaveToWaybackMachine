(function ($, Drupal, once) {
  Drupal.behaviors.updateImageSizeFields = {
    attach: function (context, settings) {

      // Handle changes in the image size selector and update the height and
      // width input fields
      $(once('updateImageSizeFields', '#edit-image-size')).each(function () {
        $(this).on('change', function () {

          let imageSize = $(this).val();

          let constrain = $('#edit-constrain-proportions').is(":checked");
          let ratio = $('#image-ratio').val();

          updateImageSize(imageSize, constrain, ratio);
        });
      });

      // Handle changes in the image size selector and update the proportions
      // and input error handling
      $(once('updateImageSizeRatioError', '#edit-image-size')).each(function () {
        $(this).on('input change paste keyup select', function () {

          let constrain = $('#edit-constrain-proportions').is(":checked");
          let ratio = $('#image-ratio').val();

          if (constrain) {
            let currentWidth = $('#image-width').val();

            $('#image-height').val(parseInt(currentWidth/ratio));
          }

          errorHandling(constrain, ratio);
        });
      });

      // Handle changes in the image width and update the proportions and
      // input error handling
      $(once('updateImageWidth', '#image-width')).each(function () {
        $(this).on('input change paste keyup select', function () {

          let constrain = $('#edit-constrain-proportions').is(":checked");
          let ratio = $('#image-ratio').val();

          if (constrain) {
            let currentWidth = $(this).val();

            $('#image-height').val(parseInt(currentWidth/ratio));
          }

          errorHandling(constrain, ratio);
        });
      });

      // Handle changes in the image height and update the proportions and
      // input error handling
      $(once('updateImageSizeFields', '#image-height')).each(function () {
        $(this).on('input change paste keyup select', function () {

          let constrain = $('#edit-constrain-proportions').is(":checked");
          let ratio = $('#image-ratio').val();

          if (constrain) {
            let currentHeight = $(this).val();

            $('#image-width').val(parseInt(currentHeight * ratio));
          }

          errorHandling(constrain, ratio);
        });
      });

      // Handle changes in the image proportions and update the proportions and
      // input error handling
      $(once('updateImageSizeRatio', '#edit-constrain-proportions')).each(function () {
        $(this).change(function () {
          let constrain = $('#edit-constrain-proportions').is(":checked");

          let currentWidth = $('#image-width').val();
          let ratio = $('#image-ratio').val();

          if (constrain) {
            $('#image-height').val(parseInt(currentWidth/ratio));
          }

          updateImageSizeOptions(constrain, ratio);

          errorHandling(constrain, ratio);
        });
      });

      function errorHandling(constrain, ratio) {
        let width = $('#image-width').val();
        let height = $('#image-height').val();

        let nativeWidth = parseInt($('#image-native-width').val());
        let nativeHeight = parseInt($('#image-native-height').val());

        let maxWidth = 3840;
        let maxHeight = 2160;

        if (constrain) {
          maxHeight = parseInt(3840/ratio);
        }

        if (nativeWidth > maxWidth) {
          maxWidth = nativeWidth;
        }

        if (nativeHeight > maxHeight) {
          maxHeight = nativeHeight;
        }

        if ((!isNaN(width) && width >= 1) && (!isNaN(height) && height >= 1)) {
          $("#size-error").removeClass('alert alert-danger').text('');

          if ((width > maxWidth) || (height > maxHeight)) {
            $("#size-error").addClass('alert alert-danger').text(Drupal.t('Please enter a width smaller than ' + maxWidth + ' and a height smaller than ' + maxHeight));
          } else {
            $("#size-error").removeClass('alert alert-danger').text('');
          }
        } else {
          $("#size-error").addClass('alert alert-danger').text(Drupal.t('Please enter a valid number greater than or equal to 1'));
        }
      }

      function updateImageSizeOptions(constrain, ratio) {

        let nativeWidth = parseInt($('#image-native-width').val());
        let nativeHeight = parseInt($('#image-native-height').val());

        let imageSize = $('#edit-image-size');
        let imageSizeSelected = imageSize.val();

        let originalText = 'original - ' + nativeWidth + ' x ' + nativeHeight;

        let updatedOptions = {[originalText]: nativeWidth + ' x ' + nativeHeight + ' (original)',
          'small': '1024 x 768 (small)',
          'HD': '1920 x 1080 (HD)',
          '4K': '3840 x 2160 (4K)',
          'custom': Drupal.t('Custom Size')
        }

        if (constrain) {
          updatedOptions = {[originalText]: nativeWidth + ' x ' + nativeHeight + ' (original)',
            'small': '1024 x ' + parseInt(1024/ratio) + ' (small)',
            'HD': '1920 x ' + parseInt(1920/ratio) + ' (HD)',
            '4K': '3840 x ' + parseInt(3840/ratio) + ' (4K)',
            'custom': Drupal.t('Custom Size')
          }
        }

        imageSize.empty();

        $.each(updatedOptions, function(index, option) {
          imageSize.append($("<option></option>")
            .attr("value", index)
            .text(option));
        });

        imageSize.val(imageSizeSelected);
        updateImageSize(imageSizeSelected, constrain, ratio);
      }

      function updateImageSize(imageSize, constrain, ratio) {
        let imageWidth = '';
        let imageHeight = '';
        let imageWidthElement = $('#image-width');
        let imageHeightElement = $('#image-height');

        let imageInputDiv = $('.image-dimensions-input');
        imageInputDiv.removeClass('show');
        imageInputDiv.addClass('hide');

        switch (imageSize) {
          case 'small':
            imageWidth = '1024';
            imageHeight = constrain ? parseInt(1024/ratio) : '768';
            break;
          case 'HD':
            imageWidth = '1920';
            imageHeight = constrain ? parseInt(1920/ratio) : '1080';
            break;
          case '4K':
            imageWidth = '3840';
            imageHeight = constrain ? parseInt(3840/ratio) : '2160';
            break;
          case 'custom':
            imageInputDiv.removeClass('hide');
            imageInputDiv.addClass('show');

            imageWidth = '10';
            imageHeight = '10';
            break;
          default:
            let imageSizeClean = imageSize.replace(/^original\s-\s/, '');
            let dimensions = imageSizeClean.split(' x ');

            imageWidth = parseInt(dimensions[0]);
            imageHeight = parseInt(dimensions[1]);
            break;
        }

        imageWidthElement.val(imageWidth);
        imageHeightElement.val(imageHeight);
      }
    }
  };
})(jQuery, Drupal, once);
