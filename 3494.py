def minTime(skill: list[int], mana: list[int]) -> int:
    answer = 0
    num_wizard = len(skill)
    num_potions = len(mana)
    wizard_avail = [0 for _ in range(num_wizard)]

    time = 0  ## current time
    for i in range(num_potions):
        for j in range(num_wizard):
            time = time + (mana[i] * skill[j])
            wizard_avail[j] = time
    return time
