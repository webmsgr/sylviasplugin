# -*- coding: utf-8 -*-
"""
    slyv.views
    ~~~~~~~~~~

    This module contains the views for the
    slyv Plugin.

    :copyright: (c) 2018 by Zachary.
    :license: Not open source, see LICENSE for more details.
"""
from flask import Blueprint, flash
from flask_babelplus import gettext as _

from flaskbb.utils.helpers import render_template
from flaskbb.plugins.models import PluginRegistry


slyv_bp = Blueprint("slyv_bp", __name__, template_folder="templates")


@slyv_bp.route("/")
def index():
    plugin = PluginRegistry.query.filter_by(name="slyv").first()
    if plugin and not plugin.is_installed:
        flash(_("Plugin is not installed."), "warning")

    return render_template("index.html", plugin=plugin)
