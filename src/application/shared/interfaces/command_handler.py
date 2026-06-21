from typing import Protocol


class ICommandHandler[TCommand, TResult](Protocol):
    async def execute(self, command: TCommand) -> TResult: ...
