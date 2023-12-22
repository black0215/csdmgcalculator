function calculate() {
    // Get the form input values
    const skillDamageIncrease = document.getElementById('skillDamageIncrease').value;
    const baseSkillMultiplier = document.getElementById('baseSkillMultiplier').value;
    const attackPower = document.getElementById('attackPower').value;
    const attackPowerByHp = document.getElementById('attackPowerByHp').value;
    const attackerHp = document.getElementById('attackerHp').value;
    const defenseRatio = document.getElementById('defenseRatio').value;
    const team1AbilityPower = document.getElementById('team1AbilityPower').value;
    const team2AbilityPower = document.getElementById('team2AbilityPower').value;
    const compatibilityDamage = document.getElementById('compatibilityDamage').value;
    const strikeJudgement = document.getElementById('strikeJudgement').value;
    const extraStat = document.getElementById('extraStat').value;
    const maxDamageLimit = document.getElementById('maxDamageLimit').value;

    // Organize the values into an object
    const formData = {
        skill_damage_increase: skillDamageIncrease,
        base_skill_multiplier: baseSkillMultiplier,
        attack_power: attackPower,
        attack_power_by_hp: attackPowerByHp,
        attacker_hp: attackerHp,
        defense_ratio: defenseRatio,
        team1_ability_power: team1AbilityPower,
        team2_ability_power: team2AbilityPower,
        compatibility_damage: compatibilityDamage,
        strike_judgement: strikeJudgement,
        extra_stat: extraStat,
        max_damage_limit: maxDamageLimit
    };

    // Send the data to the server
    const result = fetch('/api/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            // Display the result
            document.getElementById('result').innerHTML = data.result;
        })
}