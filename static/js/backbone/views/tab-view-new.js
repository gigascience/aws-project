var app = app || {};

app.TabViewNew = Backbone.View.extend({
    el: "#tabs",
    $label: $("#tabs").find("ul"),
    $content: $("#tabs").find("div"),
    template: _.template('<p>New stuff!</p>'),
    infoContentTmpl: _.template('<div id="pane1" class="tab-pane active"><div class="panel panel-success"><div class="panel-heading"><h3 class="panel-title"><%= title %></h3> </div><div id="wf_description" class="panel-body"><p><%= description %></p></div></div></div>'),
    toolContentTmpl: _.template('<div id="pane2" class="tab-pane"><div class="panel panel-default panel-info"><div class="panel-heading"><h3 class="panel-title"><%= tool_id %></h3></div><div class="panel-body"><%= tool_name %></div></div></div>'),
    wf: [
        {
            title: $("#wf_info").attr("data-wf_title"),
            description: $("#wf_info").attr("data-wf_description")
        }
    ],
    tools: [
        {tool_id: "tool1", tool_name: "getEMBL"},
        {tool_id: "tool2", tool_name: "getUniprot"}
    ],
    galaxy_wf_id: $("#wf_info").attr("data-galaxy_wf_id"),
    galaxy_history_id: $("#wf_info").attr("data-galaxy_history_id"),
    initialize: function () {
        console.log('Tab View New initialized!');
        console.log("Galaxy workflow id:", this.galaxy_wf_id);
        console.log("Galaxy history id:", this.galaxy_history_id);
        this.render();
    },
    events: {
        'click #toolsTab': 'renderInfoTab'
    },
    render: function () {
        //this.$el.html(this.template());
        var labelHtml = "<li class='active'><a id='tab1' href='#pane1' data-toggle='tab'>Info</a></li><li><a id='tab2' href='#pane2' data-toggle='tab'>Tools</a></li><li><a id='tab3' href='#pane3' data-toggle='tab'>AWS</a></li>";
        var infoContentHtml = "";
        _.each(this.wf, function (info) {
            infoContentHtml += this.infoContentTmpl(info).trim();
        }, this);
        var toolContentHtml = "";
        _.each(this.tools, function (tool_info) {
            toolContentHtml += this.toolContentTmpl(tool_info).trim();
        }, this);
        this.$label.html(labelHtml);
        this.$content.html(infoContentHtml);
        //this.$content.html(toolContentHtml);
    },
    setState: function () {
        var Events = {
            bind: function () {
                if (!this.o) this.o = $({});
                this.o.on.apply(this.o, arguments);
            },
            trigger: function () {
                if (!this.o) this.o = $({});
                this.o.trigger.apply(this.o, arguments);
            }
        };
        //StateMachine
        var SM = function () {
        };
        SM.fn = SM.prototype;
        $.extend(SM.fn, Events);
        SM.fn.add = function (tab) {
            this.bind("change", function (e, current) {
                if (tab === current) {
                    tab.activate();
                } else {
                    tab.deactivate();
                }
            });
            tab.changeState = $.proxy(function () {
                this.trigger("change", tab);
            }, this);
        };
        var sm = new SM;
        this.$label.find("li").each(function () {
            $(this).click(function () {
                if (!$(this).hasClass("active")) {
                    this.changeState();
                }
            });
            this.activate = function () {
                var self = this;
                $(self).addClass("active");
                $("#content-" + $(self).data("label")).removeClass("deactive");
            };
            this.deactivate = function () {
                var self = this;
                $(self).removeClass("active");
                $("#content-" + $(self).data("label")).addClass("deactive");
            };

            sm.add(this);
        });
    }
});
