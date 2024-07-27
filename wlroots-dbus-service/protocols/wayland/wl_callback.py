# This file has been autogenerated by the pywayland scanner

# Copyright © 2008-2011 Kristian Høgsberg
# Copyright © 2010-2011 Intel Corporation
# Copyright © 2012-2013 Collabora, Ltd.
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice (including the
# next paragraph) shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT.  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

from pywayland.protocol_core import (
    Argument,
    ArgumentType,
    Global,
    Interface,
    Proxy,
    Resource,
)


class WlCallback(Interface):
    """Callback object

    Clients can handle the 'done' event to get notified when the related
    request is done.

    Note, because :class:`WlCallback` objects are created from multiple
    independent factory interfaces, the :class:`WlCallback` interface is frozen
    at version 1.
    """

    name = "wl_callback"
    version = 1


class WlCallbackProxy(Proxy[WlCallback]):
    interface = WlCallback


class WlCallbackResource(Resource):
    interface = WlCallback

    @WlCallback.event(
        Argument(ArgumentType.Uint),
    )
    def done(self, callback_data: int) -> None:
        """Done event

        Notify the client when the related request is done.

        :param callback_data:
            request-specific data for the callback
        :type callback_data:
            `ArgumentType.Uint`
        """
        self._post_event(0, callback_data)


class WlCallbackGlobal(Global):
    interface = WlCallback


WlCallback._gen_c()
WlCallback.proxy_class = WlCallbackProxy
WlCallback.resource_class = WlCallbackResource
WlCallback.global_class = WlCallbackGlobal
