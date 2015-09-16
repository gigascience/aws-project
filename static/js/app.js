// Used for instantiating app-view.js on loading index.html
// This is done using jQuery's ready()

var app = app || {};
//var ENTER_KEY = 13;

$(function () {
    // Kick things off by creating the **App**
    //new app.AppView();
    // We create a CytoscapeWorkflow model here which is used for the whole
    // web application
    //var cy_wf = new app.CytoscapeWorkflow();
    // How do we pass the CytoscapeWorkflow model onto the views?

    //new app.WorkflowView({el: $("#cy")});
    new app.TabView({el: $("#tab_container")});
});