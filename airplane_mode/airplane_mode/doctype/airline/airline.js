// Copyright (c) 2024, Yim Sovandara and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
  refresh: function (frm) {
    var website = frm.doc.website;

    if (website) {
      var link =
        '<div class="website-link"><a href="' +
        website +
        '" target="_blank">Official Website</a></div>';

      // frm.sidebar.add_user_action("Visit Website", function () {
      //   window.open(website, "_blank");
      // });
      frm.add_web_link("link", link, false, "Visit Website");
    }
  },
});
