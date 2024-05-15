from utils.db_keys import DB_Keys
import services
import datetime
from enum import Enum


class User:
    def __init__(
        self,
        id: str,
        profile: dict,
        calendar: dict,
        finances: dict,
        social: dict,
        settings: dict,
    ):
        self.id = id
        self.profile = profile
        self.calendar = calendar
        self.finances = finances
        self.social = social
        self.settings = settings

        # settings = Settings(language=Langs.PL)

    def serialize(self):
        """
        Serializes the user data into a dictionary format.

        Returns:
            dict: The serialized user data.
        """
        return {
            DB_Keys.PROFILE.value: self.profile,
            DB_Keys.CALENDAR.value: self.calendar,
            DB_Keys.FINANCES.value: self.finances,
            DB_Keys.SOCIAL.value: self.social,
            DB_Keys.SETTINGS.value: self.settings,
        }

    # Calendar view
    def from_savings_datarow(
        self, date: datetime.datetime, goal: str, amount: str, currency: str
    ) -> None:
        keys = [int(key) for key in self.calendar["savings_rows"].keys()]
        next_key = max(keys) + 1
        self.calendar["savings_rows"][str(next_key)] = {
            "savings_deadline": date,
            "savings_goal": goal,
            "savings_amount": amount,
            "savings_currency": currency,
        }

    def does_savings_goal_exist(self, goal: str) -> bool:
        """
        Check if a savings goal exists in the user's calendar.

        Args:
            goal (str): The savings goal to check for.

        Returns:
            bool: True if the savings goal exists in the user's calendar, False otherwise.
        """
        return any(
            value.get("savings_goal") == goal
            for _, value in self.calendar["savings_rows"].items()
        )

    def __repr__(self):
        return f"User(id = {self.id}, first_name = {self.profile[DB_Keys.FIRST_NAME.value]}, last_name = {self.profile[DB_Keys.LAST_NAME.value]}, email = {self.profile[DB_Keys.EMAIL.value]})"


class Statistics: ...


class Langs(Enum):
    PL = 0
    EN = 1
    DE = 2
    NL = 3
