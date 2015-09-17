var app = app || {};

app.TabView = Backbone.View.extend({
    template2: _.template('<div id="pane1" class="tab-pane active"><div class="panel panel-success"><div class="panel-heading"><h3 class="panel-title">Workflow Title</h3></div><div id="wf_description" class="panel-body"><p>Workflow description</p></div></div></div>'),
    initialize: function () {
        console.log('Tab View initialized!');
        this.render();
        var galaxy_wf_id = $("#tab_container").attr("data-galaxy_wf_id");
        var galaxy_history_id = $("#tab_container").attr("data-galaxy_history_id");
        console.log("Galaxy workflow id:", galaxy_wf_id);
        console.log("Galaxy history id:", galaxy_history_id);
    },
    events: {
        'click #toolsTab': 'renderInfoTab'
    },
    render: function () {
        this.renderInfoTab();
    },
    renderInfoTab: function () {
        //this.$el.html(this.template2());
        // Compile the template using underscore
        //var template = _.template($("#info_tab_template").html(), {});
        // Load the compiled HTML into the Backbone "el"
        //this.$el.html(template);
    },
    renderToolsTab: function () {
        // Compile the template using underscore
        var template = _.template($("#tools_tab_template").html(), {});
        // Load the compiled HTML into the Backbone "el"
        this.$el.html(template);
    }

});
