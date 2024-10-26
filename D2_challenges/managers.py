import random
from challenges_loader import Loader
from challenge import Challenge
from d2_classes import D2Class
from utils import PollPresets, ChallengeCategories, Errors, D2Builds
from utils import D2Classes, PRESET_SETTINGS, roll_int


def result_to_json(result) -> dict:
    challenges, builds, classes = result
    result_json = {
        'challenges': [c.dump() for c in challenges],
        'builds': builds,
        'classes': [c.dump() for c in classes]
    }

    return result_json


class D2BuildsManager:
    def get_random_build() -> str:
        return D2Builds.ALL[roll_int(0, len(D2Builds.ALL) - 1)]


class D2ClassManager:
    AMA = D2Class(D2Classes.AMA, [D2Builds.MELEE, D2Builds.RANGE, D2Builds.SUM])
    ASA = D2Class(D2Classes.ASA, [D2Builds.MELEE, D2Builds.RANGE, D2Builds.CAS])
    NEC = D2Class(D2Classes.NEC, [D2Builds.MELEE, D2Builds.CAS, D2Builds.SUM])
    BAR = D2Class(D2Classes.BAR, [D2Builds.MELEE, D2Builds.RANGE, D2Builds.CAS])
    PAL = D2Class(D2Classes.PAL, [D2Builds.MELEE, D2Builds.CAS])
    SOR = D2Class(D2Classes.SOR, [D2Builds.MELEE, D2Builds.RANGE, D2Builds.CAS])
    DRU = D2Class(D2Classes.DRU, [D2Builds.MELEE, D2Builds.CAS, D2Builds.SUM])

    ALL = [AMA, ASA, NEC, BAR, PAL, SOR, DRU]

    def get_random_class():
        return D2ClassManager.ALL[roll_int(0, len(D2ClassManager.ALL) - 1)]

    def get_random_class_for_build(build: str) -> D2Class:
        if build not in D2Builds.ALL:
            raise RuntimeError(Errors.INVALID_BUILD)

        cls = D2ClassManager.get_random_class()
        while build not in cls.builds:
            cls = D2ClassManager.get_random_class()

        return cls

    def get_allowed_classes_for_build(build: str | list[D2Class]) -> list[D2Class]:
        '''Get all available classes for the specified build'''
        if build == D2Builds.ALL:
            return D2ClassManager.ALL

        if build not in D2Builds.ALL:
            raise RuntimeError(Errors.INVALID_BUILD)

        result = []

        for cls in D2ClassManager.ALL:
            if build in cls.builds:
                result.append(cls)

        return result

    def get_allowed_classes_with_x_restricted(build: str, restricted_ct: int) -> list[D2Class]:
        result = []

        allowed = D2ClassManager.get_allowed_classes_for_build(build)
        allowed_ct = len(allowed)

        if restricted_ct < allowed_ct:
            allowed_ct -= restricted_ct
        else:
            allowed_ct = 1

        while len(result) != allowed_ct:
            cls = D2ClassManager.get_random_class_for_build(build)

            if cls not in result:
                result.append(cls)

        return result


class ChallengesManager:
    def __init__(self) -> None:
        self.loader = Loader()
        self._categories: list[str] = []
        self._challenges: list[Challenge] = []

    def _create_challenges_objects(self) -> None:
        if not self.loader.raw_challenges_data:
            return

        for category in self.loader.raw_challenges_data:
            if category not in ChallengeCategories.ALL:
                msg = f'{Errors.INVALID_CHALLENGE_CATEGORY}\n- {category}'
                raise RuntimeError(msg)

            for challenge in self.loader.raw_challenges_data[category]:
                if category not in self._categories:
                    self._categories.append(category)

                name, tier, description = challenge['Name'], challenge['Tier'], challenge['Description']
                self._challenges.append(Challenge(category, name, tier, description))

    def load_challenges(self) -> None:
        self.loader.load()
        self._create_challenges_objects()

    @property
    def challenges(self) -> list[Challenge]:
        '''Return all challenges'''
        return self._challenges

    @property
    def categories(self) -> list[str]:
        '''Return all categories'''
        return self._categories

    def get_challenges_by_category(self, category: str) -> list[Challenge]:
        '''Get all challenges from specific category'''
        if category not in self.categories:
            return

        result = []

        for challenge in self.challenges:
            if challenge.category == category:
                result.append(challenge)

        return result

    def get_challenges_by_name(self, name: str) -> list[Challenge]:
        '''Get all challenges with specific name'''
        if not name:
            return

        result = []

        for challenge in self.challenges:
            if challenge.name == name:
                result.append(challenge)

        return result

    def pick_random_challenge_from_category(self, category: str) -> Challenge | None:
        '''Pick random challenge from the given category'''
        if category not in self.categories:
            msg = f'{Errors.INVALID_CHALLENGE_CATEGORY}\n- {category}'
            raise RuntimeError(msg)

        challenges_found = self.get_challenges_by_category(category)
        roll_dice = roll_int(0, len(challenges_found) - 1)

        return challenges_found[roll_dice] if challenges_found else None

    def pick_tier_for_challenge(self, challenge_name: str) -> Challenge | None:
        '''Pick random tier for the given challenge [if there are any]'''
        if not challenge_name:
            return

        challenges_found = self.get_challenges_by_name(challenge_name)
        roll_dice = roll_int(0, len(challenges_found) - 1)

        return challenges_found[roll_dice] if challenges_found else None


class ChallengePollSystem:
    def __init__(self) -> None:
        self.qol_ct = 0
        self.consumables_ct = 0
        self.item_ct = 0
        self.allowed_build = D2Builds.ALL
        self.allowed_classes = D2ClassManager.ALL

    def _reset_restrictions_ct(self):
        '''Reset the restrictions count to 0'''
        self.qol_ct = 0
        self.consumables_ct = 0
        self.item_ct = 0
        self.allowed_build = D2Builds.ALL
        self.allowed_classes = D2ClassManager.ALL

    def poll(self, preset=PollPresets.EASY) -> list[list[Challenge], str, list[D2Class]]:
        '''Poll challenges set based on the chosen preset [defaults to EASY]'''
        if preset not in PollPresets.ALL:
            raise RuntimeError(Errors.INVALID_POLL_PRESET)

        self._reset_restrictions_ct()

        self.qol_ct = PRESET_SETTINGS[preset]['qol']
        self.consumables_ct = PRESET_SETTINGS[preset]['consumables']
        self.item_ct = PRESET_SETTINGS[preset]['item']
        if not PRESET_SETTINGS[preset]['random_build']:
            self.allowed_build = D2Builds.ALL
        else:
            self.allowed_build = D2BuildsManager.get_random_build()
        if self.allowed_build != D2Builds.ALL:
            self.allowed_classes = D2ClassManager.get_allowed_classes_with_x_restricted(
                self.allowed_build,
                restricted_ct=PRESET_SETTINGS[preset]['cls_restricted']
                )
        else:
            D2ClassManager.ALL

        self.allowed_build = (
            [self.allowed_build]
            if not isinstance(self.allowed_build, list)
            else self.allowed_build
            )

        return self._poll(), self.allowed_build, self.allowed_classes

    def _poll(self) -> list[Challenge]:
        '''Poll challenges'''
        qol_challenges = self._poll_challenges(ChallengeCategories.QOL, self.qol_ct)
        consumables_challenges = self._poll_challenges(ChallengeCategories.CONSUMABLES, self.consumables_ct)
        item_challenges = self._poll_challenges(ChallengeCategories.ITEM, self.item_ct)

        return [*qol_challenges, *consumables_challenges,
                *item_challenges]

    def _poll_custom(self) -> list[Challenge]:
        '''Poll from custom preset'''
        # TODO - to be implemented

    def _poll_challenges(self, category, challenges_ct):
        result = []

        # ! Prevent infinity loop by requiring more challenges than are available
        max_challenges = CHALLENGES_MGR.get_challenges_by_category(category)
        if challenges_ct > len(max_challenges):
            challenges_ct = len(max_challenges)

        while len(result) != challenges_ct:
            challenge = CHALLENGES_MGR.pick_random_challenge_from_category(category)
            challenge = CHALLENGES_MGR.pick_tier_for_challenge(challenge_name=challenge.name)
            if challenge not in result:
                result.append(challenge)

        return result


CHALLENGES_MGR = ChallengesManager()
CHALLENGES_POLL = ChallengePollSystem()