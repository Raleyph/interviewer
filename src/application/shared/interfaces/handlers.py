from typing import Protocol


class ICommandHandler[TCommand, TResult](Protocol):
    async def handle(self, command: TCommand) -> TResult: ...


class IQueryHandler[TQuery, TResult](Protocol):
    async def handle(self, query: TQuery) -> TResult | None: ...
