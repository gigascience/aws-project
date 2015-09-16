var app = app || {};

app.TabView = Backbone.View.extend({
    initialize: function () {
        console.log('Tab View initialized!');
        this.render();
        var galaxy_wf_id = $("#tab_container").attr("data-galaxy_wf_id");
        var galaxy_history_id = $("#tab_container").attr("data-galaxy_history_id");
        console.log("Galaxy workflow id:", galaxy_wf_id);
        console.log("Galaxy history id:", galaxy_history_id);
    },
    events: {
        'click #toolsTab': 'renderInfoTab',
    },
    render: function () {
        this.renderInfoTab();
    },
    renderInfoTab: function() {
        // Compile the template using underscore
        var template = _.template($("#info_tab_template").html(), {});
        // Load the compiled HTML into the Backbone "el"
        this.$el.html(template);
    },
    renderToolsTab: function() {
        // Compile the template using underscore
        var template = _.template($("#tools_tab_template").html(), {});
        // Load the compiled HTML into the Backbone "el"
        this.$el.html(template);
    }

});
