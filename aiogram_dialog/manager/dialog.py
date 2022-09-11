from typing import Any, Optional

from aiogram.filters.state import State

from aiogram_dialog.api.protocols import ManagedDialogProtocol
from aiogram_dialog.manager.protocols import (
    DialogManager,
    ManagedDialogProto,
)


class ManagedDialogAdapter(ManagedDialogProtocol):
    def __init__(self, dialog: ManagedDialogProto, manager: DialogManager):
        self.dialog = dialog
        self.manager = manager

    async def show(self):
        return await self.dialog.show(self.manager)

    async def next(self):
        return await self.dialog.next(self.manager)

    async def back(self):
        return await self.dialog.back(self.manager)

    async def switch_to(self, state: State):
        return await self.dialog.switch_to(state, self.manager)

    def find(self, widget_id) -> Optional[Any]:
        widget = self.dialog.find(widget_id)
        if widget is None:
            return None
        return widget.managed(self.manager)
