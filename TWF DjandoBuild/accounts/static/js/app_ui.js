(function appUI () {
    "use strict";
    $("input[type=file]").change(function () {
        var file = $("input[type=file]")[0].files[0];
        alert(file.name + "\n" +
            file.type + "\n" +
            file.size + "\n" +
            file.lastModifiedDate);
    });
})();
