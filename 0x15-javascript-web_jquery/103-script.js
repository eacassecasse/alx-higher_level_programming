$('document').ready(() => {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(() => {
    $(this).keydown((ev) => {
      if (ev.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const uri = 'https://www.fourtonfish.com/hellosalut/hello/?';
  $.get(uri + $.param({ lang: $('INPUT#language_code').val() }), (data) => {
    $('DIV#hello').html(data.hello);
  });
}
