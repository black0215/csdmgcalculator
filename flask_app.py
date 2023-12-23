import math

def calculate(data:dict):
    # 변수 값 설정
    스킬데미지증가량 = data.get("skill_damage_increase",0) # 캐릭터 스킬 레벨에 표기된거 참고(총 증가량이 20%면 1.2)
    기본스킬계수 = data.get("base_skill_multiplier",0) # 기본 스킬계수(10000은 1, 22000은 2.2임)
    공격력 = data.get("attack_power",0) # 버프를 받았다면 그것 까지 포함한 공격력
    체력비례증가공격력 = data.get("attack_power_by_hp",0) #체력비례증가 공격력이 없는 유닛이면 1로 설정
    공격자체력 = data.get("attacker_hp",0) # 위와 동일
    방어율 = data.get("defense_ratio",0)  # (예시값, 실제로는 필요에 따라 조절)
    _1군능력치 = data.get("team1_ability_power",0)  # 1군 능력치 (2군,3군을 제외한 나머지 능력)
    _2군능력치 = data.get("team2_ability_power",0)  # 2군 능력치 (피해증폭 / 피해감쇄, 특수기 증폭 / 감쇄, 궁극기 증폭 / 감쇄)
    상성피해량 = data.get("compatibility_damage",0)  # 상성 피해량 (유리 상성이면 1.3, 불리 상성이면 0.7, 3군능력치는 상성피해량 밖에 없음)
    타격판정 = data.get("strike_judgement",1)  # 타격 판정 (이거 뭐임? 걍 1로 냅두셈)
    엑스트라스탯 = data.get("extra_stat",0)  # 엑스트라 스탯 (PVE 등에서 사용되는 특이 능력치)
    최대피해제한 = data.get("max_damage_limit",0)  # 최대 피해 제한 (최피제 10%면 0.1)

    # 데미지 계산
    데미지 = (1 + 스킬데미지증가량) * 기본스킬계수 * (공격력 + (공격력 * 체력비례증가공격력 * (1.0 - 공격자체력)))

    # 1군 최종계산을 첫 번째로 계산하고 최대값 80%로 제한
    _1군최종계산 = min((1 - 방어율) * _1군능력치, 3)

    # 2군 최종계산을 두 번째로 계산하고 최대값을 50%로 제한
    _2군최종계산 = min(_2군능력치, 3)


    # 최종 피해량 보정치 계산
    최종피해량보정치 = _1군최종계산 * _2군최종계산 * 상성피해량 * 타격판정 * 엑스트라스탯 * 최대피해제한

    # 최종 데미지 계산
    final_damage = 데미지 * 최종피해량보정치


    # 결과 출력
    return final_damage

if __name__ == "__main__":
    calculate({})
