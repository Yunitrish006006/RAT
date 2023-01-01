import discord
from discord.ui import Select
from discord import SelectOption
class slection(Select):
    def __init__(self, *, custom_id: str = "job_selection", placeholder:str = "select your job", min_values: int = 1, max_values: int = 1, options: list[SelectOption] = ..., disabled: bool = False, row: int = None) -> None:
        super().__init__(custom_id=custom_id, placeholder=placeholder, min_values=min_values, max_values=max_values,options=options, disabled=disabled, row=row)
     