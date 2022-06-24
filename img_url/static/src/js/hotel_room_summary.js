    odoo.define("img_url.hotel_room_summary", function (require) {
    "use strict";

    var core = require("web.core");
    var registry = require("web.field_registry");
    var basicFields = require("web.basic_fields");
    var FieldText = basicFields.FieldText;
    var FieldChar = basicFields.FieldChar;
    var QWeb = core.qweb;
    var FormView = require("web.FormView");
    const rpc = require('web.rpc');
//    var TreeView = require("web.TreeView");
    var py = window.py;

    var MyWidget = FieldChar.extend({
        events: _.extend({}, FieldChar.prototype.events, {
            change: "_onFieldChanged",
        }),
        init: function () {
            this._super.apply(this, arguments);
            if (this.mode === "edit") {
                this.tagName = "span";
            }
        },
        start: function () {
            var self = this;
            console.log(self.setting);
            if (self.setting) {
                return;
            }
//            if (!this.get("summary_header") || !this.get("room_summary")) {
//                return;
//            }
            this.renderElement();
            this.view_loading();
        },
        /* 初始化小部件时调用的函数。 */
        initialize_field: function () {

            FormView.ReinitializeWidgetMixin.initialize_field.call(this);
            var self = this;
        },
        view_loading: function (r) {
            return this.load_form(r);
        },


        load_form: function () {
            var self = this;
            const link = this.recordData.link;
            this.$el.find(".table_header").bind("click", function () {
                const input = document.createElement('input');
                document.body.appendChild(input);
                input.setAttribute('value', link);
                input.select();
                if (document.execCommand('copy')) {
                    document.execCommand('copy');
                    rpc.query({
                            model: 'img.url',
                            method: 'notification',
                            args: ['复制成功']
                        }, {shadow: true})
                }
             document.body.removeChild(input);
            });
        },
        renderElement: function () {
            this._super();
            this.$el.html(
                QWeb.render("img_url.copy", {
                    widget: this,
                })
            );
        },
        _onFieldChanged: function (event) {
            console.log(this.recordData);
            this._super();
            this.lastChangeEvent = event;
            this.set({
                summary_header: py.eval(this.recordData.summary_header),
            });
            this.set({
                room_summary: py.eval(this.recordData.room_summary),
            });
            this.renderElement();
            this.view_loading();
        },
    });

    registry.add("copy", MyWidget);
    return MyWidget;
});
